# ksvd_algorithm

Image denoising has been a classic problem for a long time. A great number of algorithms have been crafted and refined to solve this problem. Of all types of solutions, the use of sparse and redundant representations over trained dictionaries, namely, K-SVD algorithm, has been proven to be highly effective and promising. In this project, we focus on K-SVD with Batch-OMP algorithm, try to understand both its mathematics and implementations. Specifically, we wish to understand the algorithm from its optimal range of applications and the impact of its key parameters on the quality of image reconstruction. 

In our **'final_paper'** , we first reviewed image denoising algorithms and the specific kind of K-SVD algorithm using Batch-OMP that attracts us in Part 1. Then we walked through the kernel mathematics for both Batch-OMP and the K-SVD algorithms in Part 2. Finally, in Part 3, we reproduced this algorithm and tested its performance on 6 different images and observed the relationship between K – the target sparsity in K-SVD, and the reconstruction quality.

