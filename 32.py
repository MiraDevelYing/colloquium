#Змінній t привласнити значення істина, якщо в одновимірному масиві є
#хоча б одне від’ємне і парне число.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    t=False 
    for i in range(10):
      b[i] = random.randint(-10,10)
    print(b)
    for k in range(10):
       if b[k]%2==0 and b[k]<0: 
           t=True
    print(t)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
