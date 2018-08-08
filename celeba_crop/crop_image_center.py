import os
from PIL import Image

in_root = '../celeba/img_align_celeba/'
out_root = './img_align_celeba/'

img_list = os.listdir(in_root)
for img_name in img_list:
    img = Image.open(in_root + img_name)
    img_crop = img.crop([0,20,178,178+20])
    img_crop.save(out_root + img_name)
