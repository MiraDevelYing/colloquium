#Дано два лінійних масиву однакової розмірності. Скласти третій масив з
#добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(5,dtype=int)
    a=np.zeros(5,dtype=int)
    for i in range(5):
      b[i] = random.randint(-5,5)
      a[i]=random.randint(-5,5)
    print(b)
    print(a)
    ab=np.zeros(5,dtype=int)
    for k in range(5):
        ab[k]=b[k]*a[k] 
    print('Третій масив',ab)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
