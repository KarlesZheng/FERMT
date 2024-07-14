import os
import shutil

# 定义文件夹A的路径
folder_a = '/data/data-user-njf87/tnl2k/TNL2K_test_subset_p7'

# 获取文件夹A的同级目录路径
folder_a_parent = os.path.dirname(folder_a)

# 遍历文件夹A下的所有子文件夹
for root, dirs, files in os.walk(folder_a):
    for dir_name in dirs:
        # 构建子文件夹的完整路径
        folder_path = os.path.join(root, dir_name)
        # 提取子文件夹到同级目录下
        shutil.move(folder_path, folder_a_parent)

print('所有子文件夹已提取到同级目录下')