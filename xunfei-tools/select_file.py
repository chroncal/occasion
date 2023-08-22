import os
import random
import shutil

# 设置训练集和验证集的路径
train_img_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\img'
train_label_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\label'
val_img_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\img_random'
val_label_dir = 'C:\\Users\\Meow_Sakura\\Desktop\\trash'

# 设置验证集的比例（例如，20%的样本作为验证集）
validation_ratio = 0.01

# 创建验证集文件夹
if not os.path.exists(val_img_dir):
    os.makedirs(val_img_dir)
if not os.path.exists(val_label_dir):
    os.makedirs(val_label_dir)

# 获取训练集中的img文件列表
train_img_files = os.listdir(train_img_dir)

# 计算需要移动到验证集的样本数量
num_validation_samples = int(len(train_img_files) * validation_ratio)

# 随机选择需要移动的样本并移动到验证集文件夹
random.shuffle(train_img_files)
selected_samples = train_img_files[:num_validation_samples]
for sample in selected_samples:
    img_src = os.path.join(train_img_dir, sample)
    label_src = os.path.join(train_label_dir, sample.replace('.jpg', '.xml'))
    img_dst = os.path.join(val_img_dir, sample)
    label_dst = os.path.join(val_label_dir, sample.replace('.jpg', '.xml'))
    shutil.move(img_src, img_dst)
    shutil.move(label_src, label_dst)