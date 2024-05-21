import time

#A mayor N elementos -> El tiempo aumenta 
arreglo = [1, 5, 8, 9, 15, 879, 354, 6787, 6786, 78, 735, 4, 343] #O(1)

inicio = time.time() #O(1)
for i in arreglo: #O(N)
  print(i) #O(1)
fin = time.time() #O(1)
print(fin - inicio) #O(1)

#Formula de complejidad:
#1+1+N*1 + 1 + 1 = 4 + N <- Complejidad O(N) Lineal
