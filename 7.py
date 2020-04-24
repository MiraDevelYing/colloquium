#Створіть масив А [1..12] за допомогою генератора випадкових чисел з
#елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
#масиву числом 0.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(12,dtype=int)
    for i in range(12):
      b[i] = random.randint(-20,10)
    print(b)
    u=[]
    for k in range(12):
       if b[k]<0: 
           b[k]=0
    print(b)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
