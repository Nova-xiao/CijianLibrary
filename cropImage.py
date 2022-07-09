import os
import pwd
from turtle import right, width
from PIL import Image
import pathlib

pwd_path = pathlib.Path().resolve()
folder_path = os.path.join(pwd_path, "images/2019fall_raw")
new_folder_path = os.path.join(pwd_path, "images/2019fall")

if __name__ == "__main__":
    images = os.listdir(folder_path)
    images.sort()
    counter = 0
    for img in images:
        if not img.endswith(".jpg"):
            continue
        print(img)
        original_img = Image.open(os.path.join(folder_path, img))
        width, height = original_img.size
        counter = counter + 1
        left_img = original_img.crop((0, 0, width/2, height))
        left_img.save(os.path.join(new_folder_path, "2019fall_{0:03}.jpg".format(counter)), quality=95)
        counter = counter + 1
        right_img = original_img.crop((width/2, 0, width, height))
        right_img.save(os.path.join(new_folder_path, "2019fall_{0:03}.jpg".format(counter)), quality=95)

