import numpy as np
import matplotlib.pyplot as plt

numpy_str1 = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
numpy_str2 = numpy_str1 ** 2

(my_figure, my_axis) = plt.subplots()

my_axis.plot(numpy_str1,numpy_str2, color = "#3A95A8") #RGB kodlar kullanılarak renkler belirlene bilir
my_axis.plot(numpy_str2,numpy_str1, color = "#C96F23", alpha = 0.3) #alpha rengin saydamlığını belirler


(new_figure, new_axis) = plt.subplots()

new_axis.plot(numpy_str1,numpy_str1 + 1, "p") 
new_axis.plot(numpy_str1,numpy_str1 + 2, color = "blue", linewidth = 5.0) #linewidth çizginin kalınlığını belirler
new_axis.plot(numpy_str1,numpy_str1 + 3, color = "red", linestyle= "-.") #linestlye çizginin nasıl görünüceğini belirler
new_axis.plot(numpy_str1,numpy_str1 + 4, color = "red", linestyle= ":")  
new_axis.plot(numpy_str1,numpy_str1 + 5, color = "red", linestyle= "--") 
new_axis.plot(numpy_str1,numpy_str1 + 6, color = "black") 
new_axis.plot(numpy_str1,numpy_str1 + 7, color = "green",linestyle="--", marker = "+", markersize = 10) 
new_axis.plot(numpy_str1,numpy_str1 + 8, color = "green",linestyle="--", marker = "o", markersize = 5, markerfacecolor="red") #marker çizgi üzerine çift tırnak içindekileri ekliyor, marker size büyüklüğün belirliyor, markerface rengini belirliyor 

plt.show()