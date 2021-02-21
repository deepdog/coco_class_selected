import os
import re
import shutil


# 给定文件夹，返回存在指定类别的文件名
def get_class_exist_path(l_path, c):
    result = []
    for root, dirs, files in os.walk(l_path):
        total = len(files)
        for i, file in enumerate(files):
            f_path = os.path.join(root, file)
            with open(f_path) as f:
                for line in f.readlines():
                    items = re.split(r"[ ]+", line)
                    if items[0] == c:
                        result.append(file)
                        break
            print("check class: %d/%d" % (i + 1, total))
        return result


def move_txt_files(l_path, e_fs, dst_d_path):
    total = len(e_fs)
    for i, e_f in enumerate(e_fs):
        src = os.path.join(l_path, e_f)
        dst = os.path.join(dst_d_path, e_f)
        shutil.move(src, dst)
        print("move txt: %d/%d" % (i+1, total))


def delete_other_class(dist_l_path, c):
    for root, dirs, files in os.walk(dist_l_path):
        total = len(files)
        for i, file in enumerate(files):
            f_path = os.path.join(dist_l_path, file)
            with open(f_path, 'r') as f:
                lines = f.readlines()
            with open(f_path, 'w') as f_w:
                for line in lines:
                    items = re.split(r"[ ]+", line)
                    if items[0] == c:
                        f_w.write(line)
            print("delete other class: %d/%d" % (i + 1, total))


def move_images(img_dir, dist_img_dir, dist_l_path):
    for root, dirs, files in os.walk(dist_l_path):
        total = len(files)
        for i, file in enumerate(files):
            image_file = os.path.splitext(file)[0] + ".jpg"  # txt后缀替换为jpg
            src = os.path.join(img_dir, image_file)
            dst = os.path.join(dist_img_dir, image_file)
            shutil.move(src, dst)
            print("move images: %d/%d" % (i+1, total))


labels_path = "labels/train2017"
dist_labels_path = "labels/train"
dist_class = '0'

# 第一步：将含有指定class的txt文件移动到指定目录
e_files = get_class_exist_path(labels_path, dist_class)
move_txt_files(labels_path, e_files, dist_labels_path)

# 第二步：删除移动后的txt中，不需要的class
delete_other_class(dist_labels_path, dist_class)

# 第三步：将含有指定class的images移动到指定目录
images_dir = "images/train2017"
dist_images_dir = "images/train"
move_images(images_dir, dist_images_dir, dist_labels_path)
