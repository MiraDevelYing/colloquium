#Створіть масив з 15 цілочисельних елементів і визначте серед них
#мінімальне значення.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(15,dtype=int)
    for i in range(15):
      b[i] = random.randint(10,25)
    print(b)
    a=min(b)
    print('Мінімальне значення',a)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
