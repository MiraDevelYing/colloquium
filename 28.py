#Знайти кількість парних елементів одновимірного масиву.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    count=0
    for i in range(10):
      b[i] = random.randint(-10,10)
    print(b)
    for k in range(10):
       if b[k]%2==0: 
           count+=1
    print('Кількість парних елементів',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
