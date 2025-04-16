Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection | Published in The Visual Computer
# YOLOv10-BFDA 模型架构说明

**Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection | Published in The Visual Computer**

本项目基于 YOLOv10 框架，针对手术器械检测任务提出了一系列改进创新。

- **双向特征融合**  
  在模型的 Neck 部分采用了改进的 Dual-Path Feature Pyramid Network (DP-FPN) 模块，通过上采样与下采样路径的交互实现多尺度特征的高效融合，从而提升了对不同尺度目标的检测能力。

- **双重注意力机制**  
  在 Backbone 中引入了 ATT 模块和 C2fATT 模块，这些模块结合了通道注意力和空间（像素）注意力，能够动态调整特征权重，突出关键信息，改善模型在复杂场景下的表现。






