import os
import shutil

# 定义源文件夹、目标JPG文件夹和目标XML文件夹路径
source_folder = "D:\\nanodet-0.2.0\\nanodet-0.2.0\\backup-dataset\\全版本数据集\\dataset_5\\addition_7"
target_jpg_folder = "C:\\Users\\Meow_Sakura\\Desktop\\img"
target_xml_folder = "C:\\Users\\Meow_Sakura\\Desktop\\label"

# 创建目标文件夹（如果不存在）
os.makedirs(target_jpg_folder, exist_ok=True)
os.makedirs(target_xml_folder, exist_ok=True)

# 遍历源文件夹中的所有文件（包括子文件夹）
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 复制JPG文件到目标JPG文件夹
        if file.endswith(".jpg"):
            source_file = os.path.join(root, file)
            shutil.copy2(source_file, target_jpg_folder)

        # 复制XML文件到目标XML文件夹
        if file.endswith(".xml"):
            source_file = os.path.join(root, file)
            shutil.copy2(source_file, target_xml_folder)