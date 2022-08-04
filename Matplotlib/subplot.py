import numpy as np
import matplotlib.pyplot as plt

numpy_str = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
print(numpy_str)
numpy_str1 = numpy_str ** 3

#2 tane grafiği yan yana gösterme
plt.subplot(1,2,1) #1 sıra olucak 2 kolon olucak 1. grafik
plt.plot(numpy_str,numpy_str1,"g*-") #kesikli çizgi yapmak için 'g--'
plt.subplot(1,2,2) #1 sıra olucak 2 kolon olucak 2. grafik
plt.plot(numpy_str1,numpy_str,"r--")

plt.show()