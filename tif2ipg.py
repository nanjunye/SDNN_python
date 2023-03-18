from PIL import Image
from natsort import ns, natsorted
import os

tif_path = '/Users/yenanjun/PycharmProjects/SDNN/SDNN_python/stimuli'
tif_list = os.listdir(tif_path)
tif_list = natsorted(tif_list, alg=ns.PATH)
temp = 1
for tif_img in tif_list:
    tif_name = tif_path + '/' + tif_img
    im = Image.open(tif_name)
    tif_name_jpg = tif_path + '_jpg/stimuli' + f"{temp}" + '.jpg'
    im.save(tif_name_jpg)
    temp += 1
