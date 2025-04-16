# yolov10_bfda/model.py
import torch
import torch.nn as nn
from ATT.attention_interface import ATTModule

class YOLOv10_BFDA(nn.Module):
    """
    示例 YOLOv10-BFDA 主模型。
    该模型使用了基础卷积、ATT 模块进行特征加权，以及简单的下采样和检测头。
    实际项目中可在此基础上扩展 C2fATT、DP-FPN 等模块，部分核心细节在内部隐藏。
    """
    def __init__(self, num_classes=80):
        super().__init__()
        # 基础卷积层（示例）
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.act1 = nn.ReLU(inplace=True)
        
        # 使用 ATT 模块（内部实现已隐藏）
        self.att_module = ATTModule(channels=32, kernel_size=7)
        
        # 模拟后续特征提取层（下采样等）
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.act2 = nn.ReLU(inplace=True)
        
        # 检测头（输出类别数）
        self.head = nn.Conv2d(64, num_classes, kernel_size=1)

    def forward(self, x):
        x = self.act1(self.bn1(self.conv1(x)))
        # 调用 ATT 模块处理
        x = self.att_module(x)
        x = self.act2(self.bn2(self.conv2(x)))
        x = self.head(x)
        return x
