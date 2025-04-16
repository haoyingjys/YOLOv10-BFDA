Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection | Published in The Visual Computer
# YOLOv10-BFDA 模型架构说明

**Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection | Published in The Visual Computer**

本项目基于 YOLOv10 框架，针对手术器械检测任务提出了一系列改进创新。我们的工作主要包括以下三个方面：

- **双向特征融合**  
  在模型的 Neck 部分采用了改进的 Dual-Path Feature Pyramid Network (DP-FPN) 模块，通过上采样与下采样路径的交互实现多尺度特征的高效融合，从而提升了对不同尺度目标的检测能力。

- **双重注意力机制**  
  在 Backbone 中引入了 ATT 模块和 C2fATT 模块，这些模块结合了通道注意力和空间（像素）注意力，能够动态调整特征权重，突出关键信息，改善模型在复杂场景下的表现。

- **核心代码隐藏**  
  为保护关键算法细节，项目中部分核心实现（例如 ATT 模块内部计算）已通过 Cython 编译为二进制模块（如 `ATT/_hidden_impl.pyx` 编译后的 .so 或 .pyd 文件），对外只提供封装好的 API 接口，从而兼顾代码复现性和知识产权保护。

## 模块说明

- **ATT 模块**  
  该模块对输入特征执行通道和空间注意力计算，并对特征进行加权。它在保证模型准确性的同时，通过二进制文件形式保护实现细节。

- **C2fATT 模块**  
  该模块是在 CSP Bottleneck 结构上融合注意力机制的改进版，用于进一步强化特征提取的能力，从而提升整体检测效果。

- **YOLOv10-BFDA 主模型**  
  本模型将上述各模块整合于一起，在检测头部分采用轻量化卷积实现目标检测。最终输出包括目标的边界框和类别概率，经由后处理（如非最大抑制，NMS）来获得最终检测结果。

---

**总结：**  
通过上述改进，本项目实现了对手术器械的精确检测，具有高鲁棒性和实时性。请参考我们的详细文档以获得完整的 API 使用说明和模型架构信息，确保实验的透明性和复现性。

---




