#Дані про температуру води на Чорноморському узбережжі за декаду
#вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
#купання.
#Дудук Вадим 
import numpy as np
import random

while True:
    b=np.zeros(10,dtype=int)
    for i in range(10):
      b[i] = random.randint(10,25)
    print(b)
    count=0
    for k in range(10):
       if b[k]>=18: 
           count+=1
    print('Днів для купання:',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
