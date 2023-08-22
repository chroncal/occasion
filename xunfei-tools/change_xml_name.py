import os
from natsort import natsorted

folder_path = "C:\\Users\\Meow_Sakura\\Desktop\\1234"# 根据实际路径修改
start_number = 0  # 起始数字

# 获取文件夹中的所有XML文件，并按文件名排序
#xml_files = natsorted([f for f in os.listdir(folder_path) if f.endswith(".xml")])
jpg_files=natsorted([f for f in os.listdir(folder_path) if f.endswith(".jpg")])

for index, xml_file in enumerate(jpg_files):
    xml_path = os.path.join(folder_path, xml_file)

    # 构建新的文件名
    #new_file_name = f"{start_number + index:05}.jpg"
    new_file_name = f"interrupt1_{start_number + index:05}.jpg"
    new_xml_path = os.path.join(folder_path, new_file_name)

    # 重命名XML文件
    os.rename(xml_path, new_xml_path)

    # 输出修改的文件名
    print(f"{xml_file}  -->  {new_file_name}")

print("文件名修改完成！")