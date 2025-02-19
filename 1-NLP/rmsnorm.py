import torch
import torch.nn as nn

class RMSNorm(nn.Module):
    def __init__(self, d_model, eps=1e-6):
        """
        初始化 RMSNorm 模块。

        参数:
        d_model: 输入张量的最后一个维度的大小。
        eps: 防止除零错误的一个小常数。
        """
        super(RMSNorm, self).__init__()
        self.gamma = nn.Parameter(torch.ones(d_model))  # 缩放参数
        self.eps = eps

    def forward(self, x):
        """
        前向传播函数。

        参数:
        x: 输入张量，形状为 [batch_size, seq_len, d_model]。

        返回:
        归一化后的张量，形状同输入张量。
        """
        rms = torch.sqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)  # 计算均方根
        x_norm = x / rms  # 标准化
        return self.gamma * x_norm  # 缩放
