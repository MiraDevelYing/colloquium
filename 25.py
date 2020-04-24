#Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
#Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
#100.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    count=1
    for i in range(10):
      b[i] = random.randint(10,100)
    print(b)
    for k in range(10):
      l=b[k]
      if l%5==0:
         count*=l
    if count==1:
        print('Таких чисел немає')
    else:
       print('Произведение чисел кратних 5',count)
    result = input('Продовжити? Так- 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
