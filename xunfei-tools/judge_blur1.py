import os
import shutil
import cv2
import xml.etree.ElementTree as ET

# 解析XML文件，提取标注信息
def extract_annotations(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    annotations = []

    for obj in root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        label = obj.find('name').text

        annotations.append((xmin, ymin, xmax, ymax, label))

    return annotations

# 计算图像清晰度评分
def compute_image_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradient = cv2.Laplacian(gray, cv2.CV_64F).var()
    return gradient

# 设置JPEG图像文件和XML文件所在的文件夹路径
jpg_folder_path = 'C:\\Users\\Meow_Sakura\\Desktop\\dataset_2\\wheat\\pic_wheat'  # 替换为实际的JPEG图像文件所在的文件夹路径
xml_folder_path = 'C:\\Users\\Meow_Sakura\\Desktop\\dataset_2\\wheat\\label_wheat'  # 替换为实际的XML文件所在的文件夹路径

# 设置保存模糊图像和XML文件的目标文件夹路径
output_folder_path = 'C:\\Users\\Meow_Sakura\\Desktop\\trash'  # 替换为实际用于保存模糊图像和XML文件的目标文件夹路径
os.makedirs(output_folder_path, exist_ok=True)

# 统计模糊图片的数量
num_blurry_images = 0

# 遍历JPEG图像文件夹中的图像文件
for jpg_file_name in os.listdir(jpg_folder_path):
    if jpg_file_name.endswith('.jpg'):
        jpg_file_path = os.path.join(jpg_folder_path, jpg_file_name)

        # 检查对应的XML文件是否存在
        xml_file_name = jpg_file_name[:-4] + '.xml'
        xml_file_path = os.path.join(xml_folder_path, xml_file_name)
        if not os.path.exists(xml_file_path):
            print("未找到图像（{}）对应的XML文件".format(jpg_file_name))
            continue

        # 加载图像
        image = cv2.imread(jpg_file_path)

        # 解析XML文件，提取标注信息
        annotations = extract_annotations(xml_file_path)

        # 遍历每个框体并分析物体是否模糊
        threshold = 100 # 设置判断模糊的阈值(果实基本75 cucumber需要很高 蔬菜100-110即可)
        is_blurry = False
        for xmin, ymin, xmax, ymax, label in annotations:
            roi = image[ymin:ymax, xmin:xmax]
            sharpness = compute_image_sharpness(roi)
            if sharpness < threshold:
                is_blurry = True
                print("图像（{}）中的框中的物体（{}）模糊".format(jpg_file_name, label))
                break

        if is_blurry:
            # 将模糊的图像文件和对应的XML文件移动到目标文件夹中
            shutil.move(jpg_file_path, os.path.join(output_folder_path, jpg_file_name))
            shutil.move(xml_file_path, os.path.join(output_folder_path, xml_file_name))
            num_blurry_images += 1

# 打印模糊图片的数量
print("模糊图片的数量：{}".format(num_blurry_images))