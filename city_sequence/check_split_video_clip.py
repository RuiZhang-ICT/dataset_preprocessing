import os

usr_dir = os.path.expanduser('~')
data_dir = 'datasets/Cityscapes/video_clip'
data_set = 'val'

log_dir = 'val.txt'

log = open(os.path.join(usr_dir, data_dir, log_dir))
for line in log:
    info = line.split()
    count = int(info[0])
    name, start, end, frames = info[1:]
    img_list = os.listdir(os.path.join(usr_dir, data_dir, data_set, 'seq%04d'%count))
    img_list.sort()
    assert img_list[0].split('_')[0] == name
    assert img_list[0].split('_')[1] + '_' + img_list[0].split('_')[2] == start
    assert img_list[-1].split('_')[1] + '_' + img_list[-1].split('_')[2] == end
    assert len(img_list) == 30
    print count

