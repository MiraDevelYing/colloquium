#Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
#спаданню.
#Дудук Вадим
import numpy as np
while True:
    b=np.zeros(5,dtype=int)
    u=[]
    for i in range(5):
      b[i] = int(input(''))
      u.append(b[i])   
      u.sort(reverse=True)
    print(b)
    print('Відсортований по зменшенню масив',u)
    t=False
    for k in range(5):
        if u[k]!=b[k]:           
          t=False  
          break
        else:
          t=True
    print(t) 
         
    result = input('Продовжити? Так - 1,Ні - інше: ')
    if result == '1':
        continue
    else:
        break
