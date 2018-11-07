import os
import shutil
import argparse

usr_dir = os.path.expanduser('~')
data_dir = 'datasets/Cityscapes/temp_seg/'
in_dir = 'raw_segmentation_results/'
out_dir = 'datasets/Cityscapes/video_mask/train/'

parser = argparse.ArgumentParser()
parser.add_argument("--seq_idx", type=int, default=0)
args = parser.parse_args()

in_folder = os.path.join(usr_dir, data_dir, in_dir)
out_folder = os.path.join(usr_dir, out_dir, 'seq%04d' % args.seq_idx)
frame_list = os.listdir(in_folder)
#os.makedirs(out_folder)
for frame in frame_list:
    img_name = frame.replace('.', '_leftImg8bit.')
    print os.path.join(out_folder, img_name)
    shutil.copyfile(os.path.join(in_folder, frame), os.path.join(out_folder, img_name))

data_fake = 'datasets/Cityscapes/video_mask_fake/train/'
shutil.rmtree(os.path.join(usr_dir, data_fake))
os.mkdir(os.path.join(usr_dir, data_fake))
tf_file = 'datasets/Cityscapes/tfrecord/seq-00000-of-00001.tfrecord'
os.remove(os.path.join(usr_dir, tf_file))
temp_seg = 'datasets/Cityscapes/temp_seg/'
shutil.rmtree(os.path.join(usr_dir, temp_seg))
