import torch
from torch.nn.utils.rnn import pad_sequence


def get_batch_loss_and_ppl(
    model,
    tokenizer,
    formatted_text_batch,
    target_text_batch,
    max_length,
    device,
):
    batch_input_ids = []
    batch_attention_mask = []
    batch_labels = []

    for i in range(len(formatted_text_batch)):
        input_ids = tokenizer.encode(
            formatted_text_batch[i],
            return_tensors='pt',
            truncation=True,
            max_length=max_length,
        )[0].to(device)

        start_index = formatted_text_batch[i].rfind(target_text_batch[i])
        start_token = len(tokenizer.encode(formatted_text_batch[i][:start_index]))
        end_token = start_token + len(tokenizer.encode(target_text_batch[i]))

        labels = input_ids.clone()
        labels[:start_token] = -100
        labels[end_token:] = -100

        batch_input_ids.append(input_ids)
        batch_attention_mask.append(torch.ones(input_ids.shape).to(device))
        batch_labels.append(labels)

    batch_input_ids = pad_sequence(
        batch_input_ids,
        batch_first=True,
        padding_value=tokenizer.pad_token_id,
    )
    batch_attention_mask = pad_sequence(
        batch_attention_mask,
        batch_first=True,
        padding_value=0,
    )
    batch_labels = pad_sequence(
        batch_labels,
        batch_first=True,
        padding_value=-100,
    )

    model.eval()

    loss_function = torch.nn.CrossEntropyLoss(reduction='none', ignore_index=-100)

    with torch.no_grad():
        batch_logits = model(
            input_ids=batch_input_ids,
            attention_mask=batch_attention_mask,
        ).logits

    batch_loss = loss_function(
        batch_logits[:, :-1, :].permute(0, 2, 1).contiguous(),
        batch_labels[:, 1:].contiguous(),
    )
    batch_loss = batch_loss.sum(dim=1) / (batch_loss > 0).sum(dim=1)
    batch_ppl = torch.exp(batch_loss)

    return batch_loss, batch_ppl


def get_ifd_and_rifd(
    model,
    tokenizer,
    orig_prompt_batch,
    orig_response_batch,
    prompt_template,
    response_template,
    reverse_template,
    max_length,
    device,
):
    prompt_batch = [
        prompt_template.format(orig_prompt)
        for orig_prompt in orig_prompt_batch
    ]
    response_batch = [
        response_template.format(orig_response)
        for orig_response in orig_response_batch
    ]
    chat_batch = [
        f'{prompt}\n{response}'
        for prompt, response in zip(prompt_batch, response_batch)
    ]
    reverse_chat_batch = [
        reverse_template.format(orig_response, orig_prompt)
        for orig_prompt, orig_response in zip(orig_prompt_batch, orig_response_batch)
    ]

    batch_response_loss_alone, batch_response_ppl_alone = get_batch_loss_and_ppl(
        model,
        tokenizer,
        response_batch,
        orig_response_batch,
        max_length,
        device,
    )
    batch_response_loss_condition, batch_response_ppl_condition = get_batch_loss_and_ppl(
        model,
        tokenizer,
        chat_batch,
        orig_response_batch,
        max_length,
        device,
    )
    batch_prompt_loss_alone, batch_prompt_ppl_alone = get_batch_loss_and_ppl(
        model,
        tokenizer,
        prompt_batch,
        orig_prompt_batch,
        max_length,
        device,
    )
    batch_prompt_loss_condition, batch_prompt_ppl_condition = get_batch_loss_and_ppl(
        model,
        tokenizer,
        reverse_chat_batch,
        orig_prompt_batch,
        max_length,
        device,
    )

    batch_ifd = batch_response_loss_condition / batch_response_loss_alone
    batch_rifd = batch_prompt_loss_condition / batch_prompt_loss_alone

    return (
        batch_ifd.tolist(),
        batch_rifd.tolist(),
        batch_response_ppl_alone.tolist(),
        batch_response_ppl_condition.tolist(),
        batch_prompt_ppl_alone.tolist(),
        batch_prompt_ppl_condition.tolist(),
    )