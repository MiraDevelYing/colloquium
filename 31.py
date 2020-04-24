#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які потрапляють в інтервал від -2 до 10.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    sered=0
    count=0
    for i in range(10):
      b[i] = random.randint(-10,10)
      if -2<b[i]<10: 
          count+=1
    print(b)
    for k in range(10):
       if -2<b[k]<10: 
           sered+=b[k]/count
    print(count)
    print('Средне значення',sered)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
