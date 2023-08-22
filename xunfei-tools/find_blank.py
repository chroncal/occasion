import os
import shutil
import xml.etree.ElementTree as ET


# 定义XML文件夹和JPG文件夹路径
xml_folder = "C:\\Users\\Meow_Sakura\\Desktop\\dataset_2\\wheat\\label_wheat"
jpg_folder = "C:\\Users\\Meow_Sakura\\Desktop\\dataset_2\\wheat\\pic_wheat"
target_folder = "C:\\Users\\Meow_Sakura\\Desktop\\trash"

for root, dirs, files in os.walk(xml_folder):
    for file in files:
        if file.endswith(".xml"):  # 检查文件是否为XML文件
            xml_path = os.path.join(root, file)  # XML文件路径

            # 构建对应的JPG文件路径
            jpg_file = file.replace(".xml", ".jpg")
            jpg_path = os.path.join(jpg_folder, jpg_file)

            # 解析XML文件
            tree = ET.parse(xml_path)
            xml_root = tree.getroot()

            if xml_root.find("object") is None:
                # 将XML文件和对应的JPG文件转移到目标文件夹中
                shutil.move(str(xml_path), target_folder)
                shutil.move(str(jpg_path), target_folder)