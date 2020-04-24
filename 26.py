#Напишіть програму аналізу значень температури хворого за добу:
#визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
#температури виробляються шість раз на добу і результати вводяться з клавіатури у
#масив T.
#Дудук Вадим
import numpy as np
while True:
    T=np.array(range(1,25,4))
    sered=0
    for i in range(len(T)):
      T[i] = float(input('Введіть температуру'))
      sered+=T[i]/len(T)
    print(T)
    print('Средня температура',sered)
    minim=min(T)
    maxim=max(T)
    print('Мінімальна',minim,'Максимальна',maxim)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
