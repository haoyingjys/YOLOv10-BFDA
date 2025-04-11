# YOLOv10-BFDA 项目

这是一个基于 YOLOv10 框架改进的手术器械检测模型项目。项目结合了双向特征融合与注意力机制，旨在提升多尺度目标检测的准确性和鲁棒性。

## 项目特点

- **双向特征融合**：在 Neck 部分采用改进的 DP-FPN 模块，充分利用上采样与下采样特征进行多尺度信息融合。
- **注意力机制**：在 Backbone 中引入 ATT 模块以及 C2fATT 模块，通过通道和空间注意力机制强化关键特征。
- **核心代码隐藏**：部分核心实现经过 Cython 编译为二进制文件，保护关键算法细节，同时对外公开 API 接口。

## 项目结构

YOLOv10-BFDA/
├── ATT/ # 注意力模块 ├── yolov10_bfda/ # YOLOv10-BFDA 主模型及配置 ├── utils/ # 数据预处理、训练和推理脚本 ├── docs/ # 项目架构说明及 API 使用文档 ├── LICENSE # 开源许可证：GNU AGPL v3 ├── README.md # 项目说明文件 ├── .gitignore # Git 忽略文件 └── requirements.txt # 项目依赖文件

less
复制

## 安装依赖

确保你已安装 [Python 3.x](https://www.python.org/)。然后在项目根目录下运行：

```bash
pip install -r requirements.txt
训练和推理
请参阅以下命令示例：

训练模型：
在项目根目录下运行：

bash
复制
python utils/train.py
模型推理：
在项目根目录下运行：

bash
复制
python utils/infer.py --image_path path/to/your/image.jpg
License
本项目采用 GNU Affero General Public License Version 3 开源许可证，详情请参见 LICENSE 文件。


