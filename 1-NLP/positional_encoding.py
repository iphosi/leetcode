import numpy as np


def sinusoidal_positional_encoding(seq_len, d_model):
    position = np.arange(seq_len)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(position * div_term)
    pe[:, 1::2] = np.cos(position * div_term)

    return pe


# 示例使用
seq_len = 50  # 序列长度
d_model = 512  # 模型维度
positional_encoding = sinusoidal_positional_encoding(seq_len, d_model)
print(positional_encoding.shape)  # 输出: (50, 512)