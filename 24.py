#Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
#одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
#числами від 500 до 1000.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(30,dtype=int)
    count=0
    for i in range(30):
      b[i] = random.randint(500,1000)
    print(b)
    for k in range(30):
      l=b[k]
      if l%5==0 and l%8==0: 
         count+=l
    if count==0:
        print('Таких чисел немає')
    else:
       print('Cума чисел кратних 5 и 8',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
