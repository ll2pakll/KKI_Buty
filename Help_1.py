import os
import shutil

dst_dir = 'f:\Work area\Buty NN\Buty_frames\DataFaces'

os.chdir('d:\DeepFaceLab\workspace\data_dst\\aligned')

listdir = os.listdir(path='d:\DeepFaceLab\workspace\data_dst\\aligned')


for i in range(len(listdir)):
    if not i % 50:
        shutil.copyfile(listdir[i], os.path.join(dst_dir, listdir[i]))