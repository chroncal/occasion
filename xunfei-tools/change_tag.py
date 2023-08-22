'''
批量修改xml文件中的缺陷类别名称
当有多个物体时，多个物体的名称均能被修改
'''
from lxml.etree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
# 修改自己的路径
template_file = r'D:\nanodet-0.2.0\nanodet-0.2.0\val\label'  #这里是存放xml文件的文件夹
xmllist = os.listdir(template_file)
for xml in xmllist:
    #print(xml)
    tree = ET.parse(os.path.join(template_file,xml))
    root = tree.getroot() # 获取根节点
    for child in root:
        print(child.tag,child.attrib)
        if child.tag == 'object':
            name=child.find('name').text
            # print(name)
            if name == 'cucumber2':
                child.find('name').text='cucumber2a'
                tree=ET.ElementTree(root)

    tree.write(os.path.join(template_file,xml))


