import os

jpg_dir = 'D:\\nanodet-0.2.0\\nanodet-0.2.0\\dataset\\img'
xml_dir = 'D:\\nanodet-0.2.0\\nanodet-0.2.0\\dataset\\label'

jpg_files = set([os.path.splitext(file)[0] for file in os.listdir(jpg_dir) if file.endswith('.jpg')])
xml_files = set([os.path.splitext(file)[0] for file in os.listdir(xml_dir) if file.endswith('.xml')])

unmatched_files = jpg_files.symmetric_difference(xml_files)

print("无法对应的文件:")
for file in unmatched_files:
    print(file)