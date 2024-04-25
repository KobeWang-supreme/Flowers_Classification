import os
import random
from PIL import Image


def augment_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                image_path = os.path.join(root, file)
                image = Image.open(image_path)

                # 随机翻转
                if random.random() < 0.5:
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)

                # 随机裁剪
                width, height = image.size
                min_dim = min(width, height)
                crop_size = random.randint(min_dim // 2, min_dim)
                left = random.randint(0, width - crop_size)
                top = random.randint(0, height - crop_size)
                right = left + crop_size
                bottom = top + crop_size
                image = image.crop((left, top, right, bottom))

                # 保存增强后的图像
                augmented_path = os.path.join(root, f'augmented_{file}')
                image.save(augmented_path)


# 执行图像增强
augment_images("C:\\data\\flower_photos")