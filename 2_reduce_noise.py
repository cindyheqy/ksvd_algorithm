# denoise, 根据k的不同取值denoise出不同的图片，都存起来？，计算和真实图片的误差，输出到table folder下面的对应文件名
# 写一个denoise的function，最后输出就是存在

# 一些规范： function括号里的input是path，而不是直接文件名，方便作为中间过程调用
# 几个img path的格式统一一下，并且写在最上面

import os
import numpy as np
from skimage import io, util
from sklearn.feature_extraction import image
import ksvd

image_dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm/image'
noised_dir = os.path.join(image_dir, 'noised')
denoised_dir = os.path.join(image_dir, 'denoised')


#test on noised image
def clip(img):
    img = np.minimum(np.ones(img.shape), img)
    img = np.maximum(np.zeros(img.shape), img)
    return img

def denoise(noised_img_path, k): 
    img_noised = util.img_as_float(io.imread(noised_img_path))
    patch_size = (5, 5)
    patches = image.extract_patches_2d(img_noised, patch_size)
    signals = patches.reshape(patches.shape[0], -1)
    mean = np.mean(signals, axis=1)[:, np.newaxis]
    signals -= mean
    aksvd = ksvd.ApproximateKSVD(n_components=k)
    dictionary = aksvd.fit(signals[:10000]).components_
    gamma = aksvd.transform(signals)
    reduced = gamma.dot(dictionary) + mean
    reduced_img = image.reconstruct_from_patches_2d(
        reduced.reshape(patches.shape), img_noised.shape)
    return clip(reduced_img)

def create_dir(img_path): 
    img_name = img_path.split('.')[0]
    dir = os.path.join(denoised_dir, img_name)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

def save_denoiced_img(img_path, start=10, end=130, step=10): # change k
    for k in range(start, end, step): 
        print(k)
        noised_img_path = os.path.join(noised_dir, img_path)
        dir = create_dir(img_path)
        output_path = os.path.join(dir, f'{k}.png')
        io.imsave(output_path, denoise(noised_img_path, k))

def reduce_noise(update_all=False, path=noised_dir):  
    if update_all: 
        for fname in os.listdir(path): 
            save_denoiced_img(fname)
    else: 
        save_denoiced_img(path)

reduce_noise(update_all=True)
# reduce_noise(path='coffee_draw.png')