# utils/infer.py
import torch
from yolov10_bfda.model import YOLOv10_BFDA
from utils.preprocessing import preprocess_image
import argparse
import cv2
import numpy as np

def run_inference(image_path):
    # 加载模型（此处默认加载 CPU 权重，可根据需要设置 device）
    model = YOLOv10_BFDA(num_classes=80)
    state_dict = torch.load("yolov10_bfda.pth", map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()

    # 预处理图像
    image = preprocess_image(image_path, img_size=640)
    image_tensor = torch.from_numpy(image).unsqueeze(0)  # 添加 batch 维度

    # 推理
    with torch.no_grad():
        output = model(image_tensor)
    output = output.squeeze(0).numpy()
    return output

def main():
    parser = argparse.ArgumentParser(description="YOLOv10-BFDA 推理示例")
    parser.add_argument("--image_path", type=str, required=True, help="输入图像路径")
    args = parser.parse_args()

    output = run_inference(args.image_path)
    print("推理输出形状：", output.shape)
    # 可在此处添加进一步的后处理，如解码检测框、绘制结果等

if __name__ == "__main__":
    main()
