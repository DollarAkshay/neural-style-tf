import os
import sys


files = reversed(os.listdir("styles"))

for img in files:
    try:
        folder_name = img.split('.')[0]
        command = "python neural_style.py --content_img lion.png --style_imgs {} --img_name {}_results --max_size 1400 --verbose".format(img, folder_name)
        os.system(command)
    except Exception as e:
        print(str(e))
