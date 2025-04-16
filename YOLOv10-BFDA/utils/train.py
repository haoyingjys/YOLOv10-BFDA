# utils/train.py
import torch
import torch.nn as nn
import torch.optim as optim
from yolov10_bfda.model import YOLOv10_BFDA
from utils.preprocessing import preprocess_image

def dummy_data_loader(batch_size=4, img_size=640, num_batches=10):
    """
    生成假数据进行演示：返回随机图像张量和随机标签。
    """
    for _ in range(num_batches):
        # 随机生成图像数据 (batch, 3, img_size, img_size)
        images = torch.randn(batch_size, 3, img_size, img_size)
        # 随机生成标签（假设每个像素的类别，示例用整数表示）
        labels = torch.randint(0, 80, (batch_size, img_size, img_size))
        yield images, labels

def train():
    model = YOLOv10_BFDA(num_classes=80)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    criterion = nn.CrossEntropyLoss()
    num_epochs = 5

    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for images, labels in dummy_data_loader():
            images = images.to(device)
            labels = labels.to(device).long()

            optimizer.zero_grad()
            outputs = model(images)
            # 输出尺寸可能为 (batch, num_classes, H, W)，将其变换为 (batch, num_classes, -1)
            outputs = outputs.view(outputs.size(0), outputs.size(1), -1)
            labels = labels.view(labels.size(0), -1)

            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss:.4f}")

    # 保存模型权重
    torch.save(model.state_dict(), "yolov10_bfda.pth")
    print("训练完成，模型权重已保存为 yolov10_bfda.pth")

if __name__ == "__main__":
    train()
