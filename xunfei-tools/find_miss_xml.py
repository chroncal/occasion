import os
import xml.etree.ElementTree as ET
from collections import OrderedDict
from xml.dom import minidom

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_xml_file(filename, width, height, depth, xml_directory):
    annotation = ET.Element('annotation')
    
    elements = OrderedDict()
    elements['folder'] = 'img'
    elements['filename'] = filename
    elements['path'] = f'/home/ros/nanodet-0.2.0/img/{filename}'

    source = OrderedDict()
    source['database'] = 'Unknown'
    
    size = OrderedDict()
    size['width'] = str(width)
    size['height'] = str(height)
    size['depth'] = str(depth)

    segmented = "0"

    elements['source'] = source
    elements['size'] = size
    elements['segmented'] = segmented

    for key, value in elements.items():
        if isinstance(value, dict):
            sub_element = ET.SubElement(annotation, key)
            for sub_key, sub_value in value.items():
                child = ET.SubElement(sub_element, sub_key)
                child.text = sub_value
        else:
            child = ET.SubElement(annotation, key)
            child.text = value

    xml_string = prettify(annotation)
    xml_string = '\n'.join(xml_string.split('\n')[1:])  # 剔除第一行的 <?xml version='1.0' encoding='utf-8'?>
    with open(os.path.join(xml_directory, filename[:-4] + ".xml"), 'w') as f:
        f.write(xml_string)


def check_jpg_xml_pairs(jpg_directory, xml_directory):
    jpg_files = os.listdir(jpg_directory)
    xml_files = os.listdir(xml_directory)

    for jpg_file in jpg_files:
        jpg_name, jpg_extension = os.path.splitext(jpg_file)
        #jpg_name = jpg_name.lstrip("0")  # 去除前导零
        xml_file = jpg_name + '.xml'

        if xml_file not in xml_files:
            print(f"Missing XML file for {jpg_file}")
            # 创建新的XML文件
            create_xml_file(jpg_file, 640, 480, 3, xml_directory)
        else:
            print(f"No missing XML file for {jpg_file}")


jpg_directory = 'C:\\Users\\Meow_Sakura\\Desktop\\1234'
xml_directory = 'C:\\Users\\Meow_Sakura\\Desktop\\1235'

check_jpg_xml_pairs(jpg_directory, xml_directory)