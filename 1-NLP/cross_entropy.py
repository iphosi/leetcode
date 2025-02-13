import torch
import torch.nn.functional as F


def cross_entropy(logits, labels, reduction="none"):
    # logits: [batch_size, vocab_size, seq_len - 1]
    # labels: [batch_size, seq_len - 1]
    probs = F.softmax(logits, dim=1)
    loss = - torch.log(
        probs.gather(dim=1, index=labels.unsqueeze(1)).squeeze()
    )

    if reduction == "mean":
        return loss.mean()
    elif reduction == "none":
        return loss
    else:
        return loss.sum()


i = torch.randn((2, 5, 3), requires_grad=True)
t = torch.randint(5, (2, 3), dtype=torch.int64)

loss1_none = F.cross_entropy(i, t, reduction="none")
loss2_none = cross_entropy(i, t, reduction="none")

loss1_mean = F.cross_entropy(i, t, reduction="mean")
loss2_mean = cross_entropy(i, t, reduction="mean")

loss1_sum = F.cross_entropy(i, t, reduction="sum")
loss2_sum = cross_entropy(i, t, reduction="sum")

pass
