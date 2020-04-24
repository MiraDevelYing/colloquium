#Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
#екран значення коріння і квадратів кожного з елементів масиву.
#Дудук Вадим 122-Г
import numpy as np 
while True:
    b=np.zeros(5,dtype=int) 
    u=[] 
    u1=[]
    for i in range(5): 
      b[i] = int(input('Введіть елементи: ')) 
    for k in range(5):
      l=b[k]**2  
      l1=b[k]**0.5  
      u.append(l)
      u1.append(l1)
    print('Значення в квадраті',u)
    print('Корінь',u1)
    result = input('продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
