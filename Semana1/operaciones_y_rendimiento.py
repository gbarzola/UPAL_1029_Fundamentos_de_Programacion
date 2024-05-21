import time
import random

arreglo_resultados = []

#10 vueltas
for i in range(0, 100):
  inicio = time.time()
  #Proceso: agregar valores aleatorios a un arreglo vacio
  arreglo = []
  numero_aleatorio = random.randint(1, 1000)

  for i in range(numero_aleatorio):
    arreglo.append(i)

  fin = time.time()
  #(longitud arreglo, duracion (sec))
  resultado = (numero_aleatorio, fin - inicio)
  arreglo_resultados.append(resultado)

resultados_ordenados = sorted(arreglo_resultados)
print(resultados_ordenados)
