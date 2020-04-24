#Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
#Заповнення масиву здійснити випадковими числами від 5 до 500.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    count=1
    for i in range(10):
      b[i] = random.randint(5,500)
    print(b)
    for k in range(10):
      l=b[k]
      if l%3==0 and l%9==0: 
         count*=l
    if count==1:
        print('Таких чисел немає')
    else:
       print('Произведение чисел кратних 3 и 9',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
