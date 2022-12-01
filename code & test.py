#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:59:23 2022
"""

# coding:utf-8
import numpy as np
import scipy as sp
from sklearn.linear_model import orthogonal_mp_gram
import scipy.misc
from skimage import data, io, util
from skimage.metrics import peak_signal_noise_ratio
from sklearn.feature_extraction import image



class ApproximateKSVD(object):
    def __init__(self, n_components, max_iter=10, tol=1e-6,
                 transform_n_nonzero_coefs=None):
        """
        Parameters
        ----------
        n_components:
            Number of dictionary elements

        max_iter:
            Maximum number of iterations

        tol:
            tolerance for error

        transform_n_nonzero_coefs:
            Number of nonzero coefficients to target
        """
        self.components_ = None
        self.max_iter = max_iter
        self.tol = tol
        self.n_components = n_components
        self.transform_n_nonzero_coefs = transform_n_nonzero_coefs

    def _update_dict(self, X, D, gamma):
        for j in range(self.n_components):
            I = gamma[:, j] > 0
            if np.sum(I) == 0:
                continue

            D[j, :] = 0
            g = gamma[I, j].T
            r = X[I, :] - gamma[I, :].dot(D)
            d = r.T.dot(g)
            d /= np.linalg.norm(d)
            g = r.dot(d)
            D[j, :] = d
            gamma[I, j] = g.T
        return D, gamma

    def _initialize(self, X):
        if min(X.shape) < self.n_components:
            D = np.random.randn(self.n_components, X.shape[1])
        else:
            u, s, vt = sp.sparse.linalg.svds(X, k=self.n_components)
            D = np.dot(np.diag(s), vt)
        D /= np.linalg.norm(D, axis=1)[:, np.newaxis]
        return D

    def _transform(self, D, X):
        gram = D.dot(D.T)
        Xy = D.dot(X.T)

        n_nonzero_coefs = self.transform_n_nonzero_coefs
        if n_nonzero_coefs is None:
            n_nonzero_coefs = int(0.1 * X.shape[1])

        return orthogonal_mp_gram(
            gram, Xy, n_nonzero_coefs=n_nonzero_coefs).T

    def fit(self, X):
        """
        Parameters
        ----------
        X: shape = [n_samples, n_features]
        """
        D = self._initialize(X)
        for i in range(self.max_iter):
            gamma = self._transform(D, X)
            e = np.linalg.norm(X - gamma.dot(D))
            if e < self.tol:
                break
            D, gamma = self._update_dict(X, D, gamma)

        self.components_ = D
        return self

    def transform(self, X):
        return self._transform(self.components_, X)


#the original image used in the sample project
coffee = data.coffee()
io.imsave('coffee.png', coffee)


#add noise and save the image
coffee_data = util.img_as_float(io.imread('coffee.png'))
img_with_noise = util.random_noise(coffee_data, seed=1)
io.imsave('noise_coffee.png', img_with_noise)


#test on noised image
def clip(img):
    img = np.minimum(np.ones(img.shape), img)
    img = np.maximum(np.zeros(img.shape), img)
    return img

img_noised = util.img_as_float(io.imread('noise_coffee.png'))
patch_size = (5, 5)
patches = image.extract_patches_2d(img_noised, patch_size)
signals = patches.reshape(patches.shape[0], -1)
mean = np.mean(signals, axis=1)[:, np.newaxis]
signals -= mean
aksvd = ApproximateKSVD(n_components=70)
dictionary = aksvd.fit(signals[:10000]).components_
gamma = aksvd.transform(signals)
reduced = gamma.dot(dictionary) + mean
reduced_img = image.reconstruct_from_patches_2d(
    reduced.reshape(patches.shape), img_noised.shape)
io.imsave('denoised_70.png', clip(reduced_img))


#compare images measuring by psnr: greater results means better quality
true = io.imread('coffee.png')
noise = io.imread('noise_coffee.png')
reduced_32 = io.imread('denoised_32.png')
reduced_50 = io.imread('denoised_50.png')
reduced_70 = io.imread('denoised_70.png')

print('noise: %.3f' % (peak_signal_noise_ratio(true, noise)))
print('reduced: %.3f' % (peak_signal_noise_ratio(true, reduced_32)))
print('reduced: %.3f' % (peak_signal_noise_ratio(true, reduced_50)))
print('reduced: %.3f' % (peak_signal_noise_ratio(true, reduced_70)))

