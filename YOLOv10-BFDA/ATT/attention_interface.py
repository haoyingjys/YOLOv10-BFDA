# ATT/attention_interface.py
import torch
import torch.nn as nn
from ._hidden_impl import _HiddenAttention

class ATTModule(nn.Module):
  

    def __init__(self, channels, kernel_size=7):
        super().__init__()
        self._att = _HiddenAttention(channels, kernel_size)

    def forward(self, x):
        return self._att(x)
