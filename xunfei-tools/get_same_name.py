import os
import shutil
import xml.etree.ElementTree as ET

def move_files(xml_source_folder, jpg_source_folder, xml_target_folder, jpg_target_folder):
    # 遍历XML文件夹中的所有XML文件，包括子文件夹
    for root, dirs, files in os.walk(xml_source_folder):
        for xml_filename in files:
            if not xml_filename.endswith(".xml"):
                continue
            
            xml_path = os.path.join(root, xml_filename)
            
            # 获取对应的JPG文件名
            rel_path = os.path.relpath(xml_path, xml_source_folder)
            jpg_filename = os.path.splitext(rel_path)[0] + ".jpg"
            jpg_path = os.path.join(jpg_source_folder, jpg_filename)
            
            if os.path.exists(jpg_path):
                # 获取XML文件的name属性值
                tree = ET.parse(xml_path)
                xml_root = tree.getroot()
                name = None
                for obj in xml_root.iter('object'):
                    name = obj.find('name').text
                    break

                if name:
                    # 创建对应的目标文件夹
                    jpg_target_path = os.path.join(jpg_target_folder, name)
                    os.makedirs(jpg_target_path, exist_ok=True)
                    xml_target_path = os.path.join(xml_target_folder, name)
                    os.makedirs(xml_target_path, exist_ok=True)

                    # 将JPG文件移动到对应的目标文件夹
                    shutil.move(jpg_path, os.path.join(jpg_target_path, jpg_filename))

                    # 将XML文件移动到对应的目标文件夹
                    shutil.move(xml_path, os.path.join(xml_target_path, xml_filename))

xml_source_folder = "C:\\Users\\Meow_Sakura\\Desktop\\label"
jpg_source_folder = "C:\\Users\\Meow_Sakura\\Desktop\\img"
xml_target_folder = "C:\\Users\\Meow_Sakura\\Desktop\\test\\label"
jpg_target_folder = "C:\\Users\\Meow_Sakura\\Desktop\\test\\img"

move_files(xml_source_folder, jpg_source_folder, xml_target_folder, jpg_target_folder)
