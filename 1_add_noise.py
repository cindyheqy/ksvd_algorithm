# 从initial文件夹下面的图片创建noised图片，添加到noised文件夹

import os
from skimage import io, util

dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm'
image_dir = os.path.join(dir, 'image')
initial_dir = os.path.join(image_dir, 'initial')
resized_dir = os.path.join(image_dir, 'resized')
noised_dir = os.path.join(image_dir, 'noised')

for fname in os.listdir(resized_dir): 
    img_path = os.path.join(resized_dir, fname)
    img_data = util.img_as_float(io.imread(img_path))
    img_with_noise = util.random_noise(img_data, seed=1)
    output_path = os.path.join(noised_dir, fname)
    io.imsave(output_path, img_with_noise)
