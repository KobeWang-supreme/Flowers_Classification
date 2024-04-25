import os
import shutil

# flower_photos 文件夹路径
flower_photos_folder = "flower_photos"

# 获取 flower_photos 文件夹内的所有图片文件
images = [f for f in os.listdir(flower_photos_folder) if
          f.startswith('image_') and os.path.isfile(os.path.join(flower_photos_folder, f))]

# 对图片文件进行排序
images.sort()

# 创建17个文件夹，并将图片每80张放入一个文件夹
num_images = len(images)
images_per_folder = 80

for i in range(17):
    # 计算每个文件夹的图片范围
    start_index = i * images_per_folder
    end_index = min((i + 1) * images_per_folder, num_images)
    folder_name = f"category_{i + 1:02d}"

    # 创建文件夹
    os.makedirs(os.path.join(flower_photos_folder, folder_name), exist_ok=True)

    # 移动图片到新文件夹
    for j in range(start_index, end_index):
        if j < num_images:  # 确保不会超出图片列表的范围
            src = os.path.join(flower_photos_folder, images[j])
            dst = os.path.join(flower_photos_folder, folder_name, images[j])
            shutil.move(src, dst)

print("图片已分配到新文件夹中。")