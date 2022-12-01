import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import data, io, util
from skimage.metrics import peak_signal_noise_ratio
from sklearn.feature_extraction import image
import ksvd

dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm'
# image_dir = os.path.join(dir, 'image')
# initial_dir = os.path.join(image_dir, 'initial')
# noised_dir = os.path.join(image_dir, 'noised')
# denoised_dir = os.path.join(image_dir, 'denoised')
table_dir = os.path.join(dir, 'table')

def draw_change(df): 
    f = plt.figure()
    f.set_figwidth(20)
    f.set_figheight(10)
    plt.plot( 'k', 'psnr', data=df, marker='.', markerfacecolor='blue')
    plt.legend()

for fname in os.listdir(table_dir): 
    img_name = fname.split('.')[0]
    df = pd.read_csv(os.path.join(table_dir, fname))
    draw_change(df)
    plt.savefig(os.path.join(dir, 'output.png'))