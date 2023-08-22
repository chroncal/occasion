import os
import xml.etree.ElementTree as ET

# 指定XML文件所在的目录
xml_dir = 'D:\\nanodet-0.2.0\\nanodet-0.2.0\\backup-dataset\\二队数据集\\label'

# 遍历目录中的所有文件
for filename in os.listdir(xml_dir):
    if filename.endswith('.xml'):
        # 解析XML文件
        xml_path = os.path.join(xml_dir, filename)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 查找path属性的元素
        path_element = root.find('path')

        if path_element is not None:  # 确保path属性存在
            # 获取filename属性的值
            filename_element = root.find('filename')
            filename_attr = filename_element.text

            if filename_attr:  # 确保filename属性不为空
                # 构建新的路径
                new_path = os.path.join('D:\\nanodet-0.2.0\\nanodet-0.2.0\\dataset\\img\\', filename_attr)

                # 更新路径属性
                path_element.text = new_path

                # 保存修改后的XML文件
                tree.write(xml_path)

                print(f'{filename}修改完成')
            else:
                print(f'{filename}的filename属性为空')
        else:
            print(f'{filename}没有path属性')