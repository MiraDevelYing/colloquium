#Створіть масив А [1..7] за допомогою генератора випадкових чисел і
#виведіть його на екран. Збільште всі його елементи в 2 рази.
#Дудук Вадим 122-Г
import numpy as np 
import random
while True:
    b=np.zeros(7,dtype=int) 
    u=[] 
    for i in range(7): 
      b[i] = random.randint(0,100)
    print(b)
    for k in range(7): 
      l=b[k]*2 
      u.append(l) 
    print(u)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
