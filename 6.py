#Створіть масив А [1..8] за допомогою генератора випадкових чисел з
#елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
#елементів масиву.
#Дудук Вадим 
import numpy as np
import random
while True:
    b=np.zeros(8,dtype=int)
    count=0
    for i in range(8):
      b[i] = random.randint(-10,10)
    print(b)
    for k in range(8):
       if b[k]<0: 
           count+=1
    print('Кількість від`ємних елементів',count)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
