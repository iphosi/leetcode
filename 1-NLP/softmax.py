import torch


def softmax(x):
    x_exp = torch.exp(x - x.max(dim=-1, keepdim=True).values)
    partition = x_exp.sum(dim=-1, keepdim=True)

    return x_exp / partition


t = torch.tensor([[1,2,3,2,1], [5,5,5,5,5]])

print(softmax(t))

pass