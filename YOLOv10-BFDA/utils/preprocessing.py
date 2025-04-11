# utils/preprocessing.py
import cv2
import numpy as np

def preprocess_image(image_path, img_size=640):
    """
    读取图像、调整尺寸（img_size x img_size）、归一化、调整为 (C, H, W) 格式。
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"读取图像失败，请检查路径: {image_path}")
    # 调整图像尺寸
    image = cv2.resize(image, (img_size, img_size))
    # BGR 转 RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 转为 float 并归一化
    image = image.astype("float32") / 255.0
    # 转换为 CHW 格式
    image = np.transpose(image, (2, 0, 1))
    return image
