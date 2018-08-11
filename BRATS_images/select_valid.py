from PIL import Image
import numpy as np
import os
import shutil

path_root = "Synthetic_Data"

for mode in ["Flair", "T1", "T2"]:
    out_folder = "Synthetic_" + mode
    os.makedirs(out_folder)
    count = 0
    print out_folder
    for grid in ["HG", "LG"]:
        file_root = os.path.join(path_root, grid, mode)
        file_list = os.listdir(file_root)
        print len(file_list)
        for fn in file_list:
            img = Image.open(os.path.join(file_root, fn))
            img_mat = np.array(img)
            valid = img_mat >0
            valid_num = valid.sum() 
            if np.float(valid_num) / (img_mat.shape[0]*img_mat.shape[1]) > 0.1:
                shutil.copy(os.path.join(file_root, fn), os.path.join(out_folder, grid+'_'+fn))
                count += 1
        print count
