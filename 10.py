#Дані про температуру повітря за декаду листопада зберігаються в масиві.
#Визначити, скільки разів температура опускалася нижче -10 градусів.
#Дудук Вадим
import numpy as np
import random
while True:
    b=np.zeros(10,dtype=int)
    for i in range(10):
      b[i] = random.randint(-20,10)
    print(b)
    count=0
    for k in range(10):
       if b[k]<-10: 
           count+=1
    if count==2 or count==3 or count==4:
      print('Опускалась',count,'разів')
    else:
        print('Опускалась',count,'раз')
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
