#Дані про температуру повітря за декаду грудня зберігаються в масиві.
#Визначити, скільки раз температура була вище середньої за цю декаду.
#Дудук Вадим
import numpy as np
import random

while True:
    b=np.zeros(10,dtype=int)
    for i in range(10):
      b[i] = random.randint(-3,3)
    print(b)
    sered=0
    count=0
    for k in range(10):
        sered+=b[k]/10
    for o in range(10):
        if b[o]>sered: 
           count+=1
    print('Середня температура',sered)
    if count==2 or count==3 or count==4:
      print('Вище була',count,'раза')
    else:
        print('Вище була',count,'раз')
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
