from PIL import ImageEnhance,Image
import os

# 输入图像文件夹路径
input_folder = "C:\\Users\\Meow_Sakura\\Desktop\\全版本数据集\\dataset_5\\addition_2\\cucumber2b\\pic_cucumber2b"

# 输出图像文件夹路径
output_folder = "C:\\Users\\Meow_Sakura\\Desktop\\全版本数据集\\dataset_5\\addition_2\\cucumber2b\\pic_cucumber2b"

# 提高亮度的因子（0为完全黑暗，1为原始亮度，大于1为增加亮度）
brightness_factor = 2

# 创建输出图像文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历输入图像文件夹中的图像
for filename in os.listdir(input_folder):
    # 读取图像
    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path)

    # 提高图像亮度
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(brightness_factor)

    # 保存输出图像
    output_path = os.path.join(output_folder, filename)
    enhanced_image.save(output_path)

    print(f"Processed image: {filename}")

print("Image brightness enhancement complete.")