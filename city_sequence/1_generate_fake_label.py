import os
from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--data_dir", type=str, default="datasets/Cityscapes/video_clip")
parser.add_argument("--out_dir", type=str, default="datasets/Cityscapes/video_mask_fake")
parser.add_argument("--data_set", type=str, default="train")
parser.add_argument("--seq_idx", type=int, default=0)

args = parser.parse_args()

usr_dir = os.path.expanduser('~')
frame_list = os.listdir(os.path.join(usr_dir, args.data_dir, args.data_set, 'seq%04d'%args.seq_idx))
os.makedirs(os.path.join(usr_dir, args.out_dir, args.data_set, 'seq%04d'%args.seq_idx))
for img in frame_list:
    img_name = img.replace('leftImg8bit', 'gtFine_labelTrainIds')
    mat = np.zeros((1024, 2048))
    mask = Image.fromarray(np.uint8(mat))
    mask.save(os.path.join(usr_dir, args.out_dir, args.data_set, 'seq%04d'%args.seq_idx, img_name))
