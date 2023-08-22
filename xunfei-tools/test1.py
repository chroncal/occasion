import os
import xml.etree.ElementTree as ET

def extract_filename(xml_content, target_name):
    root = ET.fromstring(xml_content)
    filename = root.find('filename').text
    object_name = root.find('object/name').text

    if object_name == target_name:
        return filename
    else:
        return None

def traverse_folder(folder_path, target_name):
    filenames = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.endswith('.xml') and os.path.isfile(file_path):
            with open(file_path, 'r') as xml_file:
                xml_content = xml_file.read()
                filename = extract_filename(xml_content, target_name)
                if filename:
                    filenames.append(filename)

    return filenames

# 示例使用：
folder_path = 'D:\\nanodet-0.2.0\\nanodet-0.2.0\\val\\label'
target_name = 'cucumber2'

filenames = traverse_folder(folder_path, target_name)

print(f"Target name: {target_name}")
if filenames:
    print("Matched filenames:")
    for filename in filenames:
        print(filename)
else:
    print("No matching filenames found")