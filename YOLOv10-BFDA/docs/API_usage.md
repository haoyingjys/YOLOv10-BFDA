# API Usage

This document provides an overview of how to use the main components of the **YOLOv10-BFDA** model.

## 1. Importing the Model

You can import the model from the `yolov10_bfda` module as follows:

```python
from yolov10_bfda import YOLOv10_BFDA

model = YOLOv10_BFDA.load_model('path/to/model.pth')

from utils.preprocessing import preprocess_image

image = preprocess_image('path/to/image.jpg')
output = model(image)
print(output)
python eval.py --config config.yaml --model_path path/to/saved_model.pth



