#Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(20,dtype=int)
    for i in range(20):
      b[i] = random.randint(-2,1)
    print(b)
    dobutok=1
    for k in range(20):
       if b[k]!=0:
           dobutok*=b[k]
    print(dobutok)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
