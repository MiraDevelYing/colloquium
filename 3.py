#Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
#починаючи з останнього.
#Дудук Вадим 122-Г 
import numpy as np 
while True:
    b=np.array([input('Введіть фамілію: ') for i in range(5)]) 
    for k in range(5):  
      l=b[5-1-k] 
      print(l)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
