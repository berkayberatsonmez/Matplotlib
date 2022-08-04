import numpy as np
import matplotlib.pyplot as plt

age_list = [10,20,30,30,30,40,50,60,70,75]
weight_list = [20,60,80,85,86,87,70,90,95,90]

np_age_list = np.array(age_list)
np_weight_list =  np.array(weight_list)

plt.plot(np_age_list,np_weight_list,"g") #x ekseni yaş, y ekseni ağırlık, sondaki parantez renk için
plt.xlabel("Age") #x ekseninin etiketi
plt.ylabel("Weight") #y ekseniin etiketi,
plt.title("Age/Weight") #grafiğin etiketi

plt.show()