import torch
from torch import nn


class LayerNorm(nn.Module):
    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.gamma = nn.Parameter(torch.ones(features))
        self.beta = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        # x: [batch_size, seq_len, d_model]
        mean = x.mean(-1, keepdim=True)  # mean: [batch_size, seq_len, 1]
        std = x.std(-1, keepdim=True)  # std: [batch_size, seq_len, 1]

        return self.gamma * (x - mean) / (std + self.eps) + self.beta