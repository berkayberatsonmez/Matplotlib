import numpy as np
import matplotlib.pyplot as plt

numpy_str = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
print(numpy_str)
numpy_str1 = numpy_str ** 3

my_figure = plt.figure()
figureAxes = my_figure.add_axes([0.2,0.2,0.4,0.4]) #ilk iki değer x ekseni ve y ekseninin etkiliyor, son iki değer ise büyüklüğünü etkiliyor

figureAxes.plot(numpy_str,numpy_str1,"g")
figureAxes.set_xlabel("X ekseni")
figureAxes.set_ylabel("Y ekseni")
figureAxes.set_title("Graph")

plt.show()