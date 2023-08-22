# 代码功能为 判断模糊图片
# coding=utf-8
from imutils import paths
import cv2
import os
import shutil

def variance_of_laplacian(image):
    '''
    计算图像的laplacian响应的方差值
    '''
    return cv2.Laplacian(image, cv2.CV_64F).var()

if __name__ == '__main__':
    # 设置输入和输出路径
    input_path = "C:\\Users\\Meow_Sakura\\Desktop\\dataset_version3\\corn1a\\pic_corn1a"
    xml_path = "C:\\Users\\Meow_Sakura\\Desktop\\dataset_version3\\corn1a\\label_corn1a"
    output_path = "C:\\Users\\Meow_Sakura\\Desktop\\trash"

    # 创建输出文件夹
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 遍历每一张图片
    for imagePath in paths.list_images(input_path):
        # 读取图片
        image = cv2.imread(imagePath)
        # 将图片转换为灰度图片
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 计算灰度图片的方差
        fm = variance_of_laplacian(gray)
        text = "Not Blurry"

        # 设置输出的文字
        if fm < 200.0:
            text = "Blurry"
            # 获取文件名
            filename = os.path.basename(imagePath)
            # 根据图片文件名找到对应的XML文件路径
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            xml_filepath = os.path.join(xml_path, xml_filename)
            # 将模糊图片转移到输出文件夹中
            shutil.move(imagePath, os.path.join(output_path, filename))
            # 将对应的XML文件一起转移
            shutil.move(xml_filepath, os.path.join(output_path, xml_filename))