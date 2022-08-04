import numpy as np
import matplotlib.pyplot as plt

numpy_str = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
print(numpy_str)
numpy_str1 = numpy_str ** 3

figure = plt.figure()

eksen1 = figure.add_axes([0.1,0.1,0.8,0.8]) #ilk iki değer x ekseni ve y ekseninin etkiliyor
eksen2 = figure.add_axes([0.3,0.5,0.3,0.3]) #son iki değer ise büyüklüğünü etkiliyor

eksen1.plot(numpy_str,numpy_str1,"g")
eksen1.set_xlabel("X ekseni 1.grafik")
eksen1.set_ylabel("Y ekseni 1.grafik")
eksen1.set_title("1.Graph")

eksen2.plot(numpy_str1,numpy_str,"b")
eksen2.set_xlabel("X ekseni 2.grafik")
eksen2.set_ylabel("Y ekseni 2.grafik")
eksen2.set_title("2.Graph")

plt.show()