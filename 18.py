#Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
#масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
#Дудук Вадим
from random import randint
import numpy as np
while True:
    i, dob = 0, 1  
    A = np.zeros(10, dtype = int)
    for i in range(10):
        A[i] = input()
        if(A[i] < 0):
            dob *= A[i]
    print(dob)        
     result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    break
