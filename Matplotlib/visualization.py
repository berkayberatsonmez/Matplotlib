import numpy as np
import matplotlib.pyplot as plt

numpy_str1 = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
print(numpy_str1)
numpy_str2 = numpy_str1 ** 2
numpy_str3 = numpy_str1 ** 3


new_figure = plt.figure(figsize=(8,6), dpi=100) #figsize ekrana çıkan grafiğin büyüklüğünü ayarlıyor,dpi kaç piksel olucağını belirliyor ne kadar büyük olursa o kadar kaliteli olur

new_axis = new_figure.add_axes([0.1,0.1,0.9,0.9])

new_axis.plot(numpy_str1,numpy_str2, label = "numpy_str ** 2")
new_axis.plot(numpy_str1,numpy_str3, label = "numpy_str ** 3") #grafiğin sol üstünde çizginin anlamı yazar
new_axis.legend(loc = 2) #içine değer girerek yerini değiştirebiliyoruz default: loc=2

new_figure.savefig("new_figure.png", dpi=200) #grafiği resim olarak kaydeder

plt.show()