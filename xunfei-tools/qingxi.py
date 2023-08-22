import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.utils import save_image
from PIL import Image

# 超分辨率模型定义
class SuperResolutionModel(nn.Module):
    def __init__(self):
        super(SuperResolutionModel, self).__init__()
        # 定义模型结构，可以根据具体需求选择合适的模型

    def forward(self, x):
        # 模型前向传播

# 超分辨率模型路径
model_path = "path/to/model.pth"

# 输入图像文件夹路径
input_folder = "path/to/input/images"

# 输出图像文件夹路径
output_folder = "path/to/output/images"

# 加载超分辨率模型
model = SuperResolutionModel()
model.load_state_dict(torch.load(model_path))
model.eval()

# 图像预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 批量处理图像
for filename in os.listdir(input_folder):
    # 读取图像
    input_image = Image.open(os.path.join(input_folder, filename)).convert("RGB")
    input_tensor = transform(input_image).unsqueeze(0)

    # 使用超分辨率模型提高图像清晰度
    with torch.no_grad():
        output_tensor = model(input_tensor)

    # 保存输出图像
    output_image = transforms.ToPILImage()(output_tensor.squeeze(0))
    output_image.save(os.path.join(output_folder, filename))