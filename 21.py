#Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
#числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
#від 50 до 100.
#Дудук Вадим
import numpy as np
import random
while True:
    x=int(input('Введіть число для порівняння:'))
    b=np.zeros(10,dtype=float)
    count=1
    for i in range(10):
      b[i] = random.uniform(50,100)
    print(b)
    for k in range(10):
      l=b[k]
      if l<x: 
         count*=l
    if count==1:
         print('Таких чисел не існує')
    else:
         print('Произведение елементов',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
