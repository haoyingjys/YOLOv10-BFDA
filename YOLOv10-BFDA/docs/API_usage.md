# API Usage Documentation

This document provides a comprehensive guide on how to utilize the main components of the **YOLOv10-BFDA** model. It includes instructions for importing the model, loading pretrained weights, preprocessing images, performing inference, training the model, compiling Cython modules, and (optionally) evaluation. Follow these steps to reproduce our experimental results.

---

## 1. Importing the Model

Import the main model class from the `yolov10_bfda` module:

```python
from yolov10_bfda import YOLOv10_BFDA



##  2. Loading a Pretrained Model
To load a pretrained model from saved weights, use the following code:

python
import torch
from yolov10_bfda import YOLOv10_BFDA

# Initialize the model with the correct number of classes (e.g., 80)
model = YOLOv10_BFDA(num_classes=80)

# Load the pretrained weights (update the file path as necessary)
model.load_state_dict(torch.load("path/to/model.pth", map_location="cpu"))
model.eval()

##3. Preprocessing Images
Use the provided function in utils/preprocessing.py to preprocess your input image. This function resizes the image to 640×640, converts it from BGR (as read by OpenCV) to RGB, normalizes the pixel values, and rearranges the image dimensions to (C, H, W).

python
from utils.preprocessing import preprocess_image
import torch

# Preprocess the image
image = preprocess_image("path/to/your/image.jpg")

# Convert the preprocessed image to a tensor and add a batch dimension if necessary
image_tensor = torch.from_numpy(image).unsqueeze(0)

##4. Performing Inference
Run inference on the preprocessed image with the loaded model:

python
# Perform inference
output = model(image_tensor)
print("Inference Output:", output)
Alternatively, you can use the provided inference script by running:

bash
python utils/infer.py --image_path path/to/your/image.jpg

##5. Training the Model
To train the model, execute the training script. Note that the current training script uses dummy data for demonstration purposes. You may need to modify the data loader in utils/train.py for your custom dataset.

bash
python utils/train.py


##6. Compiling Cython Modules
Certain key modules, such as the core implementation of the ATT module, are written in Cython. To compile these modules into binary form (e.g., _hidden_impl.so on Linux/Mac or _hidden_impl.pyd on Windows), run the following command in the project root:

bash
python setup.py build_ext --inplace
This command compiles the file ATT/_hidden_impl.pyx and generates the binary module in the ATT folder.

##7. Evaluation (Optional)
If an evaluation script is provided, you can evaluate the model performance using the following command (update the command based on your actual implementation):

bash
python utils/eval.py --config config.yaml --model_path path/to/saved_model.pth
By following the instructions above, you will be able to import the model, load pretrained weights, preprocess images, perform inference, train the model, and compile the core Cython modules. For further details, please refer to the source code comments in the respective modules.


---
