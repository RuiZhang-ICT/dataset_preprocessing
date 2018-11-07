import os
import shutil

usr_dir = os.path.expanduser('~')
data_dir = 'datasets/Cityscapes/leftImg8bit_sequence/'
data_set = 'train/'

out_dir = 'datasets/Cityscapes/video_clip/'

def get_seq_img_num(img_name):
    img_name_list = img_name.split('_')
    num1 = int(img_name_list[1])
    num2 = int(img_name_list[2])
    return num1, num2

if not os.path.exists(os.path.join(usr_dir, out_dir, data_set)):
    os.makedirs(os.path.join(usr_dir, out_dir, data_set))

folder_list = os.listdir(os.path.join(usr_dir, data_dir, data_set))
folder_list.sort()
seq_count = 0
for folder in folder_list:
    img_list = os.listdir(os.path.join(usr_dir, data_dir, data_set, folder))
    img_list.sort()
    pre1, pre2 = get_seq_img_num(img_list[0])
    start1, start2 = pre1, pre2
    os.mkdir(os.path.join(usr_dir, out_dir, data_set, 'seq%04d'%seq_count))
    src_dir = os.path.join(usr_dir, data_dir, data_set, folder, img_list[0])
    dst_dir = os.path.join(usr_dir, out_dir, data_set, 'seq%04d'%seq_count, img_list[0])
    shutil.copyfile(src_dir, dst_dir)
    frame_count = 1
    for idx in xrange(1, len(img_list)):
        num1, num2 = get_seq_img_num(img_list[idx])
        src_dir = os.path.join(usr_dir, data_dir, data_set, folder, img_list[idx])
        if num1==pre1 and num2-pre2==1:
            dst_dir = os.path.join(usr_dir, out_dir, data_set, 'seq%04d'%seq_count, img_list[idx])
            shutil.copyfile(src_dir, dst_dir)
            frame_count += 1
            pre1, pre2 = num1, num2
        else:
            print seq_count, folder, '%06d_%06d'%(start1, start2), '%06d_%06d'%(pre1, pre2), frame_count
            start1, start2 = num1, num2
            pre1, pre2 = num1, num2
            seq_count += 1
            os.mkdir(os.path.join(usr_dir, out_dir, data_set, 'seq%04d'%seq_count))
            dst_dir = os.path.join(usr_dir, out_dir, data_set, 'seq%04d'%seq_count, img_list[idx])
            shutil.copyfile(src_dir, dst_dir)
            frame_count = 1
    print seq_count, folder, '%06d_%06d'%(start1, start2), '%06d_%06d'%(pre1, pre2), frame_count
    seq_count += 1        

