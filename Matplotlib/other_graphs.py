import numpy as np
import matplotlib.pyplot as plt

numpy_str1 = np.linspace(0,10,20) #random 20 tane float sayı oluştur 0 dan 10 a kadar
numpy_str2 = numpy_str1 ** 2

#scatter
plt.scatter(numpy_str1,numpy_str2)

#histogram
new_str = np.random.randint(0,100,150)
plt.hist(new_str)

#boxplot
plt.boxplot(numpy_str2)


plt.show()