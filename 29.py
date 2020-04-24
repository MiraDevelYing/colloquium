#Знайти кількість парних елементів одновимірного масиву до першого
#зустрінутого числа рівного наперед заданому числу а.
#Дудук Вадим
import numpy as np
while True:
    b=np.zeros(5,dtype=int)
    count=0
    a=int(input('Введіть число: '))
    for i in range(5):
      b[i] = int(input('Введіть елементи масива:'))
    print(b)
    for k in range(5):
       if b[k]%2==0: 
           if b[k]==a:
               break
           else:
               count+=1
    print(f'Кількість парних елементів до числa {a}',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
