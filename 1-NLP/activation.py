import torch
import torch.nn as nn

# Sigmoid
class Sigmoid(nn.Module):
    def forward(self, x):
        return 1 / (1 + torch.exp(-x))

# ReLU
class ReLU(nn.Module):
    def forward(self, x):
        return torch.max(torch.zeros_like(x), x)

# Leaky ReLU
class LeakyReLU(nn.Module):
    def forward(self, x, alpha=0.01):
        return torch.where(x > 0, x, alpha * x)

# Parametric ReLU
class PReLU(nn.Module):
    def __init__(self, num_parameters=1, init=0.25):
        super(PReLU, self).__init__()
        self.weight = nn.Parameter(torch.full((num_parameters,), init))

    def forward(self, x):
        return torch.where(x > 0, x, self.weight * x)

# GELU
class GELU(nn.Module):
    def forward(self, x):
        return 0.5 * x * (1 + torch.tanh(torch.sqrt(torch.tensor(2.0 / torch.pi)) * (x + 0.044715 * x ** 3)))

# SwiGLU
class SwiGLU(nn.Module):
    def __init__(self, dim, hidden_dim=None):
        super().__init__()
        hidden_dim = hidden_dim if hidden_dim is not None else dim * 2
        self.w1 = nn.Linear(dim, hidden_dim, bias=False)  # W 权重
        self.w2 = nn.Linear(dim, hidden_dim, bias=False)  # V 权重

    def forward(self, x):
        gate = torch.sigmoid(self.w1(x)) * self.w1(x)  # Swish 激活
        value = self.w2(x)  # 线性变换
        return gate * value  # 逐元素乘法

# Learnable Swish
class LearnableSwish(nn.Module):
    def __init__(self):
        super(LearnableSwish, self).__init__()
        self.beta = nn.Parameter(torch.tensor(1.0))  # 可学习参数

    def forward(self, x):
        return x * torch.sigmoid(self.beta * x)