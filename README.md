# ksvd_algorithm

In this project, we focus on K-SVD with Batch-OMP algorithm, try to understand both its mathematics and implementations. Specifically, we wish to understand the algorithm from its optimal range of applications and the impact of its key parameters on the quality of image reconstruction. 

In our **'final_paper'** , we first reviewed image denoising algorithms and the specific kind of K-SVD algorithm using Batch-OMP that attracts us in Part 1. Then we walked through the kernel mathematics for both Batch-OMP and the K-SVD algorithms in Part 2. Finally, in Part 3, we reproduced this algorithm and tested its performance on 6 different images and observed the relationship between K – the target sparsity in K-SVD, and the reconstruction quality.

3 K-SVD Application and Test Results 

3.1 Test on different types of images

_Data source:_ 
After rewriting Python syntax by referring to the algorithm in **'ksvd.py'**, we choose 6 different types of images to test its performance. There are black and white, colored, 3-d, informative CT photo, black and white mosaic and colored mosaic images. The goal is to test the performance of K-SVD using Batch-OMP on as much types of signals as possible to find its optimal applications.
Initial images can be found under **'image/initial'** folder. 

* Pre-Processing: We first tried to uniform the pixel sizes of those images by setting them all to be 600x400 after we read them into the environment. Pre-Processing process is conducted with **'0_resize.py'**. Pre-Processed images can be found under **'image/resized'** folder. 

And next, we manually added Gaussian noise with fixed seed = 1 to make sure choices of noise type and standard deviations won’t affect test results.


Denoising and observations: This K-SVD algorithm turns out to work on all types of images we chose. And the performance can be (though vaguely) seen from below. Also, with larger pixel sizes, the cost of running the algorithm can be considerably higher. We tried one black and white image with pixel size 2800 x 2800, it cost us roughly an hour to denoise. How will other variations of K-SVD perform on such large images would be another interesting experiment for us to carry out in the future.

3.2 Observe the impact of different K(s) on reconstruction quality measured by PSNR
PSNR Peak signal-to-noise ratio (PSNR) stands for the ratio between the maximum representative power of the signal matrix and the power of noise that affects the accuracy of representation by the signal matrix. It is one of the most widely used metrics to quantify the reconstruction quality for degraded images. With higher scores, the reconstruction quality of the noised image will be better. This is the central measurement we used to examine the impact of K on the reconstruction quality6.
Experiments and findings To observe the change, we varied K from 10 to 120 in steps of 10 units at a time, and we expected to see a close-to-linear relationship between the choice of K and the reconstruction accuracy. And the result can be seen from the graph below. With higher K, the reconstruction accuracy tends to drop eventually for 3 out of 6 images we chose. And for those images, K = 10 or 20 turned out to be the most accurate condition for image reconstruction. It would be helpful for us to focus on K smaller than 20 to dive deeper into this topic.
However, there are indeed three exceptions, which are the black and white coffee, 3-d and the colored mosaic image, where accuracy surprisingly increased as K grew. Also, the reconstruction errors vary greatly across these 6 images, with that of the black and white coffee image surprisingly being the lowest, namely, the worst of all experiments. Our guess at the moment for the unexpectedness is mainly from the perspective of color scales and numbers of pixels with related to each large color category. More experiments that better control over factors other than color, for instance, noise type and level, number of iterations, and number of training signals would be necessary to make more responsible assumptions regarding which types of images might be the most suitable for K-SVD denoising algorithm.
