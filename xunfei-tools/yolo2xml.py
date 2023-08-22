import os

def convert_yolo_to_xml(yolo_file, xml_file):
    class_name = "watermelon_d"  # 填写类别名称
    img_width = 640  # 填写图片宽度
    img_height = 480  # 填写图片高度

    with open(yolo_file, 'r') as yolo:
        text = yolo.readline().strip()
        if text:
            values = text.split(' ')
            confidence = float(values[0])
            x_center = float(values[1])
            y_center = float(values[2])
            width = float(values[3])
            height = float(values[4])

            xmin = int((x_center - width / 2) * img_width)
            ymin = int((y_center - height / 2) * img_height)
            xmax = int((x_center + width / 2) * img_width)
            ymax = int((y_center + height / 2) * img_height)

            with open(xml_file, 'w') as xml:
                xml.write('<annotation>\n')
                
                # 替换原始文件夹名称为目标文件夹名称
                target_folder = "img"
                xml.write('\t<folder>{}</folder>\n'.format(target_folder))
                
                #批量修改filename
                xml.write('\t<filename>{}.jpg</filename>\n'.format(os.path.splitext(os.path.basename(yolo_file))[0]))

                #批量修改path
                target_path = "C:\\path\\to\\image"
                xml.write('\t<path>{}</path>\n'.format(os.path.join(target_path, '{}.jpg'.format(os.path.splitext(os.path.basename(yolo_file))[0]))))

                xml.write('\t<source>\n')
                xml.write('\t\t<database>Unknown</database>\n')
                xml.write('\t</source>\n')
                xml.write('\t<size>\n')
                xml.write('\t\t<width>{}</width>\n'.format(img_width))
                xml.write('\t\t<height>{}</height>\n'.format(img_height))
                xml.write('\t\t<depth>3</depth>\n')
                xml.write('\t</size>\n')
                xml.write('\t<segmented>0</segmented>\n')
                xml.write('\t<object>\n')
                xml.write('\t\t<name>{}</name>\n'.format(class_name))
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>0</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>{}</xmin>\n'.format(xmin))
                xml.write('\t\t\t<ymin>{}</ymin>\n'.format(ymin))
                xml.write('\t\t\t<xmax>{}</xmax>\n'.format(xmax))
                xml.write('\t\t\t<ymax>{}</ymax>\n'.format(ymax))
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
                xml.write('</annotation>')

# 需要转换的 YOLO txt 文件所在目录
yolo_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\pic\\pic_watermelon_d\\pic_watermelon_d\\label'

# 生成的 XML 文件保存目录
xml_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\picture\\picture\\watermelon_d\\label_watermelon_d'

# 遍历指定目录下的所有文件
for filename in os.listdir(yolo_dir):
    if filename.endswith('.txt'):
        yolo_file = os.path.join(yolo_dir, filename)

        # 构建对应的 XML 文件路径
        base_filename = os.path.splitext(filename)[0]
        xml_file = os.path.join(xml_dir, '{}.xml'.format(base_filename))

        convert_yolo_to_xml(yolo_file, xml_file)
        print("Converted: {}".format(filename))