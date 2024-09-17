import torch
from torch.nn import LogSigmoid
from transformers import Trainer


class BradleyTerryTrainer(Trainer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logsigmoid = LogSigmoid()

    def compute_loss(self, model, inputs, return_outputs=False):
        chosen_inputs = inputs.get("chosen")
        rejected_inputs = inputs.get("rejected")

        chosen_outputs = model(**chosen_inputs)
        rejected_outputs = model(**rejected_inputs)
        outputs = {"chosen": chosen_outputs, "rejected": rejected_outputs}

        chosen_logits = chosen_outputs.logits.view(-1)
        rejected_logits = rejected_outputs.logits.view(-1)

        loss = - self.logsigmoid(chosen_logits - rejected_logits).mean(dim=0)

        return (loss, outputs) if return_outputs else loss

    def prediction_step(
        self,
        model,
        inputs,
        prediction_loss_only,
        ignore_keys=None,
    ):
        with torch.no_grad():
            loss, outputs = self.compute_loss(model, inputs, return_outputs=True)

        logits = outputs["chosen"].logits.view(-1) - outputs["rejected"].logits.view(-1)
        labels = torch.ones(logits.size(0))

        if prediction_loss_only:
            return loss, None, None
        else:
            return loss, logits, labels
