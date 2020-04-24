#Знайти суму всіх елементів масиву цілих чисел, які менше середнього
#арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
#здійснити випадковими числами від 150 до 300.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(20,dtype=int)
    u=[]
    count=0
    for i in range(20):
      b[i] = random.randint(150,300)
    print(b)
    srednee=np.mean(b) 
    for k in range(20):
      l=b[k]
      if l<srednee:
          count+=l
    print('Середнє арифметичне',srednee)
    print('Сума всіх елементів',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
