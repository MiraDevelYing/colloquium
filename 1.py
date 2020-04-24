#Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
#один рядок через кому. Отримайте для масиву середнє арифметичне.
#Дудук Вадим 122-Г
import numpy as np  
while True:
    b=np.zeros(5,dtype=int) 
    u=[] 
    for i in range(5): 
      b[i] = int(input('Введіть елементи: ')) 
    for k in range(5): 
      l=b[k] 
      u.append(l) 
    print(u)
    g=sum(u)/5 
    print('Середнє Арифметичне',g)
    result = input(' продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
