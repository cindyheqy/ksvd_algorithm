# 定义一个函数用来计算psnr
# 把数值存到一个表格里并输出到table文件夹下面

import os
import pandas as pd
from skimage import io
from skimage.metrics import peak_signal_noise_ratio

dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm'
image_dir = os.path.join(dir, 'image')
resized_dir = os.path.join(image_dir, 'resized')
noised_dir = os.path.join(image_dir, 'noised')
denoised_dir = os.path.join(image_dir, 'denoised')
table_dir = os.path.join(dir, 'table')

def get_psnr(img_path, k): 
    img_name = img_path.split('.')[0]
    true = io.imread(os.path.join(resized_dir, img_path))
    reduced = io.imread(os.path.join(denoised_dir, img_name, f'{k}.png'))
    psnr = peak_signal_noise_ratio(true, reduced)
    psnr = round(psnr, 3)
    return psnr

def get_psnr_table(img_path):
    img_name = img_path.split('.')[0]
    k_list = []
    psnr_list = []
    for fname in os.listdir(os.path.join(denoised_dir, img_name)):
        k = int(fname.split('.')[0])
        k_list.append(k)
        psnr = get_psnr(img_path, k)
        psnr_list.append(psnr)
    data = {'k': k_list, 'psnr': psnr_list}
    k_psnr_change = pd.DataFrame(data)
    k_psnr_change = k_psnr_change.sort_values(by='k')
    k_psnr_change.reset_index(drop=True, inplace=True)
    return k_psnr_change

def write_psnr_table(img_path): 
    img_name = img_path.split('.')[0]
    k_psnr_change = get_psnr_table(img_path)
    k_psnr_change.to_csv(os.path.join(table_dir, f'{img_name}.csv'))

def psnr_table(path=resized_dir, update_all=True):  
    if update_all: 
        for fname in os.listdir(path): 
            write_psnr_table(fname)
    else: 
        write_psnr_table(path)

psnr_table(path=resized_dir, update_all=True)
# psnr_table('mosaic_color.png', update_all=False)