import os
from skimage import io, util
import cv2

dir = '/Users/qingyi/Documents/uchicago/courses/machine_learning/project/ksvd_algorithm'
image_dir = os.path.join(dir, 'image')
initial_dir = os.path.join(image_dir, 'initial')
resized_dir = os.path.join(image_dir, 'resized')
noised_dir = os.path.join(image_dir, 'noised')

def img_resize(img_path): 
    img = cv2.imread(img_path)
    # print('Original Dimensions : ', img_path, img.shape)
    width = 600
    height = 400
    dim = (width, height)
    resized_img = cv2.resize(img, dim)
    # print('Resized Dimensions : ', img_path, resized_img.shape)
    output_path = os.path.join(resized_dir, fname)
    io.imsave(output_path, resized_img)
    return resized_img

for fname in os.listdir(initial_dir): 
    img_path = os.path.join(initial_dir, fname)
    img = img_resize(img_path)


