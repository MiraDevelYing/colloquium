#З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
#що протягом цього часу температура знижувалася. Визначте, о котрій годині було
#вперше зафіксовано від'ємну температуру.
#Дудук Вадим
import numpy as np
import random
while True:
    a=np.array(range(8,21))
    b=np.zeros(len(a),dtype=int)
    print(a)
    for i in range(len(a)):
      b[i] = random.randint(-20,10)
    print(b)
    u=[]
    for k in range(len(a)):
       if b[k]<0: 
           print('Температура менше нуля була в ',k+8,'годин')
           break
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
