# https://pypi.org/project/MedPy/
# https://github.com/loli/medpy/wiki/IO-basics
# https://github.com/K10shah/GAN-on-BRATS/blob/master/DCGAN-2.ipynb
# https://github.com/pzaffino/python-mha/blob/master/mha.py

from medpy.io import load
import numpy as np
import os
from PIL import Image

#file_path = "../BRATS-2/Synthetic_Data/HG/0001/VSD.Gray_matter_of_neuraxis_5more.XX.O.OT/VSD.Gray_matter_of_neuraxis_5more.XX.O.OT.870.mha"
#file_path = "../BRATS-2/Synthetic_Data/HG/0001/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.866.mha"
#file_path = "../BRATS-2/Synthetic_Data/HG/0001/VSD.Brain.XX.O.MR_Flair/VSD.Brain.XX.O.MR_Flair.865.mha"
#out_path = "Flair/"

def preprocessing(file_path, out_path):

  image_data, image_header = load(file_path)
  print image_data.shape

  img_mat = np.array(image_data, dtype=np.float)
  img_mat = (img_mat - img_mat.min()) / (img_mat.max() - img_mat.min()) * 255
  for idx in range(img_mat.shape[2]):
    img = img_mat[:,:,idx]
    img = Image.fromarray(np.uint8(img.transpose()))
    img.save(out_path + "%03d.png" %idx)

def processing_folder(data_type, grid_type, mode_type):
  #data_type = "Synthetic_Data"
  #grid_type = "HG"
  #mode_type = "Flair" # mode = ["Flair", "T1", "T1c", "T2", "OT"]
  brats_root = "../BRATS-2"

  folder_path = os.path.join(brats_root, data_type, grid_type)
  for folder in os.listdir(folder_path):
    for mode in os.listdir(os.path.join(folder_path, folder)):
      if not mode.endswith(mode_type):
        continue
      if mode_type == "OT" and ("Gray" not in mode):
        continue
      for fn in os.listdir(os.path.join(folder_path, folder, mode)):
        if fn.endswith(".mha"):
          fn_path = os.path.join(folder_path, folder, mode, fn)
          out_root = os.path.join(data_type, grid_type, mode_type)
          if not os.path.exists(out_root):
            os.makedirs(out_root)
          out_path = out_root + '/' + folder + '_'
          preprocessing(fn_path, out_path)

for set_data_type in ["Synthetic_Data", "Image_Data"]:
  for set_grid_type in ["HG", "LG"]:
    for set_mode_type in ["Flair", "T1", "T1c", "T2", "OT"]:
      processing_folder(set_data_type, set_grid_type, set_mode_type)
#processing_folder("Synthetic_Data", "HG", "OT")
