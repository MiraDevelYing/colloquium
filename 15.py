#Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
#20. Заповнення масиву здійснити випадковими числами від 100 до 200.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(20,dtype=int)
    count=0
    for i in range(20):
      b[i] = random.randint(100,201)
    print(b)
    for k in range(20):
      l=b[k]
      if l%2==0:
         count+=l
    print('Сума парних елементів',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
