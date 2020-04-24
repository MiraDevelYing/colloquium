#Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
#остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
#здійснити випадковими числами від 200 до 300.
#Дудук Вадим
import numpy as np
import random
while True:
    b = np.array([random.randint(200,300) for i in range(20)])
    s = 0
    print(b)
    for i in range(len(b)): 
        if b[i] % 2 == 3:
             s += b[i]
    print("Cума: ",s)
    result = input('Продовжити? Так - 1, Ні - інше: ')
    if result == '1':
        continue
    else:
        break
