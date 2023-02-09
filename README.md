# K-SVD Algorithm Using Batch-OMP in Image Denoising

In this project, we focus on K-SVD with Batch-OMP algorithm, try to understand both its mathematics and implementations. Specifically, we wish to understand the algorithm from its optimal range of applications and the impact of its key parameters on the quality of image reconstruction. 

In our **'final_paper'** , we first reviewed image denoising algorithms and the specific kind of K-SVD algorithm using Batch-OMP that attracts us in Part 1. Then we walked through the kernel mathematics for both Batch-OMP and the K-SVD algorithms in Part 2. Finally, in Part 3, we reproduced this algorithm and tested its performance on 6 different images and observed the relationship between K – the target sparsity in K-SVD, and the reconstruction quality.

_Data source:_ 
After rewriting Python syntax by referring to the algorithm in **'ksvd.py'**, we choose 6 different types of images to test its performance. There are black and white, colored, 3-d, informative CT photo, black and white mosaic and colored mosaic images. The goal is to test the performance of K-SVD using Batch-OMP on as much types of signals as possible to find its optimal applications.
Initial images can be found under **'image/initial'** folder. 

_Pre-Processing:_
We first tried to uniform the pixel sizes of those images by setting them all to be 600x400 after we read them into the environment. Resizing process is conducted with **'0_resize.py'**. Risized images can be found under **'image/resized'** folder. 

And next, we manually added Gaussian noise with fixed seed = 1 to make sure choices of noise type and standard deviations won’t affect test results. Adding noise was conducted with **'1_add_noise.py'**. Noised images can be found under **'image/noised'** folder. 

_Denoising:_
We wrote the K-SVD algorithm with **'2_reduce_noise.py'** and it turns out to work on all types of images we chose. The denoised images are stored in **'image/denoised'** folder. 

_Observe the impact of different K(s) on reconstruction quality measured by PSNR"_
We used Peak signal-to-noise ratio (PSNR) to examine the impact of K on the reconstruction quality. With higher scores, the reconstruction quality of the noised image will be better. To observe the change, we varied K from 10 to 120 in steps of 10 units at a time, and we expected to see a close-to-linear relationship between the choice of K and the reconstruction accuracy. We calculated PSNR with different K values for all 6 pictures with **'3_psnr_table'** and visualize the data with **'4_draw_plot.py'**. And the output can be found at **'final_output.png'**. 

_Results:_ 
With higher K, the reconstruction accuracy tends to drop eventually for 3 out of 6 images we chose. And for those images, K = 10 or 20 turned out to be the most accurate condition for image reconstruction. It would be helpful for us to focus on K smaller than 20 to dive deeper into this topic. 

However, there are indeed three exceptions, which are the black and white coffee, 3-d and the colored mosaic image, where accuracy surprisingly increased as K grew. Also, the reconstruction errors vary greatly across these 6 images, with that of the black and white coffee image surprisingly being the lowest, namely, the worst of all experiments. Our guess at the moment for the unexpectedness is mainly from the perspective of color scales and numbers of pixels with related to each large color category. More experiments that better control over factors other than color, for instance, noise type and level, number of iterations, and number of training signals would be necessary to make more responsible assumptions regarding which types of images might be the most suitable for K-SVD denoising algorithm.
