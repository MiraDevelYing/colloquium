#Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
#починаються з певної букви, яка вводиться з клавіатури.
#Дудук Вадим 
import numpy as np 
while True:
    x=input('Введіть букву')
    b=np.array([input('Введіть фамілію: ') for i in range(5)]) 
    for k in b: 
     if k[0]==x:
         print(k)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
