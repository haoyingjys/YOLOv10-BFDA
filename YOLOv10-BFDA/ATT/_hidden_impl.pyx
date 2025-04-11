# ATT/_hidden_impl.pyx

# 导入必要的模块
import torch
import torch.nn as nn

cdef class _HiddenAttention(nn.Module):
    """
    核心注意力模块的内部实现，经过 Cython 编译生成二进制文件以隐藏源代码。
    这里只是一个示例实现，实际中请根据算法要求更改。
    """
    def __init__(self, int channels, int kernel_size=7):
        super(_HiddenAttention, self).__init__()
        self.channels = channels
        self.kernel_size = kernel_size
        # 创建卷积层，注意这里用的是 PyTorch 的 nn.Conv2d
        self.conv = nn.Conv2d(channels, channels, kernel_size=kernel_size, padding=kernel_size // 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # 获取注意力映射
        att_map = self.sigmoid(self.conv(x))
        # 返回加权后的结果
        return x * att_map
