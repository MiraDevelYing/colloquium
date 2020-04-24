#Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
#пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с.
#Дудук Вадим
import numpy as np
while True:
    b=np.array(range(1,11))
    for k in range(10):
      l=b[k]**2*10/2 
      print(f'Відстань за {k+1} сек',l)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
