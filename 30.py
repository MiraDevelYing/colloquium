#Обчислити середнє арифметичне значення тих елементів одновимірного
#масиву, які розташовані за першим по порядку мінімальним елементом.
#Дудук Вадим
import numpy as np
while True:
    i, num, summa = 0, 0, 0 
    n = int(input('Введіть кількість елементів = '))
    A = np.zeros(n, dtype = int)
    for i in range(n):
        A[i] = input()
    minim = A[0]
    for i in range(n):
        if(A[i] < minim):
            minim = A[i]        
    for i in range(n):
        if(A[i] == minim):
            i = num      
    for i in range(num, n, 1):
        summa += A[i]
    print(summa/(n-num))        
        
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
