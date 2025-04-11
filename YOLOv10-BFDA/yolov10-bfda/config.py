# yolov10_bfda/config.py
import yaml

def load_config(config_path="yolov10nImprove.yaml"):
    """
    读取 YAML 格式的模型配置文件，并返回配置字典。
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config

# 如果配置文件不存在，可以使用下面默认配置：
CONFIG = {
    "nc": 80,
    "scales": {
        "n": [0.33, 0.25, 1024]
    },
    "backbone": [
        [-1, 1, "Conv", [64, 3, 2]],
        [-1, 1, "Conv", [128, 3, 2]],
        [-1, 3, "C2fATT", [128, True]],
        [-1, 1, "Conv", [256, 3, 2]],
        [-1, 6, "C2fATT", [256, True]],
        [-1, 1, "SCDown", [512, 3, 2]],
        [-1, 6, "C2fATT", [512, True]],
        [-1, 1, "SCDown", [1024, 3, 2]],
        [-1, 3, "C2fATT", [1024, True]],
        [-1, 1, "SPPF", [1024, 5]],
        [-1, 1, "PSA", [1024]]
    ],
    "head": [
        [4, 1, "Conv", [256]],
        [6, 1, "Conv", [256]],
        [9, 1, "Conv", [256]],
        [-1, 1, "nn.Upsample", [None, 2, "nearest"]],
        [[-1, 12], 1, "Concat", [1]],
        [-1, 3, "C2f", [256]],
        [-1, 1, "nn.Upsample", [None, 2, "nearest"]],
        [[-1, 11], 1, "Concat", [1]],
        [-1, 3, "C2f", [256]],
        [1, 1, "Conv", [256, 3, 2]],
        [[-1, 11, 19], 1, "Concat", [1]],
        [-1, 3, "C2f", [256]],
        [-1, 1, "Conv", [256, 3, 2]],
        [[-1, 12, 16], 1, "Concat", [1]],
        [-1, 3, "C2f", [512]],
        [-1, 1, "SCDown", [256, 3, 2]],
        [[-1, 13], 1, "Concat", [1]],
        [-1, 3, "C2fCIB", [1024, True, True]],
        [[22, 25, 28], 1, "Detect", ["nc"]]
    ]
}
