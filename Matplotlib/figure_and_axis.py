import numpy as np
import matplotlib.pyplot as plt

numpy_str = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
print(numpy_str)
numpy_str1 = numpy_str ** 3

#nrows,ncols değerleri girilmezse program 'AxesSubplot' hatası döndürür
(my_figure, my_axis) = plt.subplots(nrows=1,ncols=2) # bu şekilde boş eksen ve boş figure oluşturabiliriz

for axis in my_axis:
    axis.plot(numpy_str,numpy_str1,"b")
    axis.set_xlabel("X axis")
plt.tight_layout() #iki grafik arasındaki mesafeyi açarak düzgün bir görüntü elde etmemizi sağlar
plt.show()