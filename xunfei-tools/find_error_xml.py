import os
import xml.etree.ElementTree as ET

folder_path = 'C:\\Users\\Meow_Sakura\\Desktop\\全版本数据集\\dataset_2\\wheat\\label_wheat'

def check_xml_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file = os.path.join(folder_path, filename)
            tree = ET.parse(xml_file)
            root = tree.getroot()
            # 查找"name"属性
            name_element = root.find('object/name')
            if name_element is not None and name_element.text != 'wheat':
                print(filename)

# 调用函数进行检查
check_xml_files(folder_path)