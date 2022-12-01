# 从initial文件夹下面的图片创建noised图片，添加到noised文件夹

import os
from skimage import io, util

path = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm/image'
initial_path = os.path.join(path, 'initial')
noised_path = os.path.join(path, 'noised')
for fname in os.listdir(initial_path): 
    img_path = os.path.join(initial_path, fname)
    # img_name = fname.split('.')[0]
    img_data = util.img_as_float(io.imread(img_path))
    img_with_noise = util.random_noise(img_data, seed=1)
    output_path = os.path.join(noised_path, fname)
    io.imsave(output_path, img_with_noise)
