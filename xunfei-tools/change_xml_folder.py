import os
import xml.etree.ElementTree as ET

# 指定需要修改的文件夹路径
folder_path = "C:\\Users\\Meow_Sakura\\Desktop\\7.23add\\label"

# 新的folder属性值
new_folder = "img"

# 遍历文件夹中的所有xml文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xml"):
        xml_path = os.path.join(folder_path, filename)
        
        # 解析xml文件
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # 修改folder属性
        for elem in root.iter("folder"):
            elem.text = new_folder
        
        # 保存修改后的xml文件
        tree.write(xml_path)
