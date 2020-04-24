#Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
#масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(15,dtype=int)
    count=1
    for i in range(15):
      b[i] = random.randint(10,51)
    print(b)
    for k in range(15):
      l=b[k]
      if l%7==0:
         count*=l
    if count==1:
        print('Елементів кратних 7 немає')
    else:
     print('Кратних 7 ',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
