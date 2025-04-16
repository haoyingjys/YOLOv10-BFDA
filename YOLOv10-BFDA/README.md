# YOLOv10-BFDA

**Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection**

This repository contains the source code for the YOLOv10-BFDA model – an enhanced version of the YOLOv10 object detection framework specially designed for precise surgical instrument detection. By integrating bidirectional feature fusion (via an improved DP-FPN module) and dual attention mechanisms (channel and spatial attention), our model achieves high detection accuracy and robustness across multiple scales in challenging surgical scenarios.

---

## Permanent Link & Citation

- **Permanent Repository Link:**  
  [https://github.com/haoyingjys/YOLOv10-BFDA](https://github.com/haoyingjys/YOLOv10-BFDA)  


- **Citation Format:**  
[1] Enhanced YOLOv10 with Bidirectional Feature Fusion and Dual Attention for Precise Surgical Instrument Detection, The Visual Computer.

---

## Project Features

- **Bidirectional Feature Fusion:**  
The model employs a DP-FPN module to effectively fuse features from both upsampling and downsampling paths, ensuring comprehensive multi-scale information capture.

- **Dual Attention Mechanism:**  
Integration of channel and spatial attention modules allows the network to dynamically focus on critical parts of the image, suppressing irrelevant background noise.

- **Protected Core Code:**  
Key algorithm implementations (e.g., in the ATT module) are compiled using Cython into binary modules, protecting proprietary details while providing well-documented APIs.

---

## Dependencies & Requirements

This project requires the following dependencies:
- **Python 3.x** (preferably 3.8+)
- **PyTorch** and **torchvision**
- **PyYAML**
- **opencv-python**
- **numpy**
- **Cython** (required for compiling core modules)

Install the dependencies with:
```bash
pip install -r requirements.txt

##Usage Guide
###1. Preprocessing
###Load and preprocess an image using:
from utils.preprocessing import preprocess_image
image = preprocess_image("path/to/your/image.jpg")
###The preprocessing script resizes the image to 640×640, converts it from BGR to RGB, normalizes the pixel values, and converts the image layout to (C, H, W).

###2. Training
###Train the model by executing:
python utils/train.py
###Note: The provided training script currently uses dummy data for demonstration. Modify the data loader in utils/train.py to incorporate your own dataset if required

###3. Inference
###Perform inference on an image using:
python utils/infer.py --image_path path/to/your/image.jpg
###This script loads the pretrained model, preprocesses the input image, and outputs the model’s prediction (bounding boxes and class scores).

###4. Compiling Cython Modules
###To compile the core Cython modules (for example, ATT/_hidden_impl.pyx), run the following command in the project root:
python setup.py build_ext --inplace
###This will compile the Cython source file and generate the binary module (e.g., _hidden_impl.so) in the ATT folder.

###Project Structure
###The repository follows the structure below:
YOLOv10-BFDA/
├── ATT/                   # Attention module (core algorithms compiled via Cython)
│   ├── __init__.py
│   ├── attention_interface.py
│   └── _hidden_impl.pyx   # Core implementation source (compiled into binary)
├── yolov10_bfda/          # Main model implementation and configuration
│   ├── __init__.py
│   ├── config.py
│   └── model.py
├── utils/                 # Utilities for data preprocessing, training, and inference
│   ├── preprocessing.py
│   ├── train.py
│   └── infer.py
├── docs/                  # Detailed documentation (API usage and architecture)
│   ├── API_usage.md
│   └── architecture.md
├── LICENSE                # GNU AGPL v3 License
├── README.md              # Project overview and usage documentation (this file)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependency list
└── setup.py               # Cython build configuration

##License
##This project is licensed under the GNU Affero General Public License (AGPL) Version 3. See the LICENSE file for full details.

---

## 修改说明

- **项目简介和标题**：在文件开头增加了项目英文标题和简要描述，以便国际读者理解项目的主要创新点。
- **永久链接与引用格式**：添加了用于引用的永久链接和推荐的引用格式，方便读者引用你的工作。
- **依赖和要求**：详细列出了项目所需的依赖项，并给出了安装命令，确保用户能够快速搭建运行环境。
- **使用指南**：增加了对图像预处理、训练、推理和 Cython 模块编译的详细示例，帮助用户复现实验。
- **项目结构说明**：详细描述了项目各个目录的作用，方便用户定位源代码及文档。
- **License 部分**：明确项目采用 AGPL v3 许可，提示读者查阅 LICENSE 文件中的完整内容。


