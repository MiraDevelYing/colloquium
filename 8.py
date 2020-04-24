#Створіть цілочисельний масив А [1..15] за допомогою генератора
#випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
#найбільший елемент масиву і його індекс.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(15,dtype=int)
    for i in range(15):
      b[i] = random.randint(-15,30)
    print(b)
    count=0
    a=0
    for k in range(15):
        if b[k]>a: 
            a=b[k]
            count=k
    print('Індекс',count)
    print('Число',a)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
