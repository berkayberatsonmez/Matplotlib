#The "load_digits" dataset contains approximately 1800 images of handwritten digits 0 through 9.
# Each image is 8x8 which translates to 64 attributes per image.

from sklearn import datasets
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import pandas as pd

digits1 = datasets.load_digits(n_class=8,as_frame=True)
print(digits1.data.shape)

plt.figure(1, figsize=(5,5), facecolor=('red'), edgecolor=('blue'))
plt.imshow(digits1.images[5], cmap=plt.cm.gray_r, interpolation="bicubic")


digits2 = load_digits()
print(digits2.data.shape)

plt.gray()
plt.matshow(digits2.images[0])

plt.show()