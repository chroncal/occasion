from PIL import Image
import os

def adjust_tint(image_path, tint_color, output_folder):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    img = Image.open(image_path)
    img = img.convert("RGB")

    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # 调整红色和绿色通道的值，增加黄色的成分
            r = int(r + (tint_color[0] - r) * 0.5)
            g = int(g + (tint_color[1] - g) * 0.5)
            pixels[i, j] = (r, g, b)
    
    # 构造输出路径
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    
    # 保存修改后的图片到输出路径
    img.save(output_path)

def adjust_tint_for_folder(input_folder, output_folder, tint_color):
    # 获取输入文件夹中所有的文件名
    file_names = os.listdir(input_folder)
    
    # 遍历文件夹中的文件
    for file_name in file_names:
        # 检查文件是否为图片（可根据实际需求调整条件）
        if file_name.endswith(".png") or file_name.endswith(".jpg"):
            # 构造输入和输出图片路径
            input_path = os.path.join(input_folder, file_name)
            # 调用调整色调的函数，并传入输出文件夹路径
            adjust_tint(input_path, tint_color, output_folder)

# 调用函数来调整指定文件夹下的所有图片的色调为偏黄色，并保存到另一个文件夹中
input_folder = "C:\\Users\\Meow_Sakura\\Desktop\\全版本数据集\\dataset_1\\corn1a\\pic_corn1a"  # 替换为你的输入文件夹路径
output_folder = "C:\\Users\\Meow_Sakura\\Desktop\\222"  # 替换为你的输出文件夹路径
tint_color = (255, 255, 0)  # 偏黄色的 RGB 值

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

adjust_tint_for_folder(input_folder, output_folder, tint_color)