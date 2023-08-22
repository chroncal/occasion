import os
import xml.etree.ElementTree as ET

# 指定需要修改的文件夹路径
folder_path = "D:\\nanodet-0.2.0\\nanodet-0.2.0\\backup-dataset\\全版本数据集\\dataset_5\\addition_6\\watermelon_c\\label_watermelon_c"

# 遍历文件夹中的所有xml文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
        xml_path = os.path.join(folder_path, filename)
        
        # 解析xml文件
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # 获取XML文件名（不含扩展名）
        xml_name = os.path.splitext(filename)[0]
        
        # 修改filename属性
        for elem in root.iter("filename"):
            elem.text = xml_name + ".jpg"
        
        # 保存修改后的xml文件
        tree.write(xml_path)