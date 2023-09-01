import numpy as np


# Matriz bidimensional

mt7 = np.array([[7,2,23],[12,27,4],[5,34,23]])
print(mt7)

print ('                                ')
print ('--------------------------------')
print ('                                ')


# Calcular múltimas matrizes

A = np.array([[3,5,7], [4,4,2], [2,9,1], [1,2,3]])
Z = np.array([[2,2,2], [3,5,1], [4,1,2], [7,7,7]])

R = A*Z 

print(R)

print ('                                ')
print ('--------------------------------')
print ('                                ')


# Gerador de números aleatórios
# obs. Se vc colocar 1 no default_rng(), vai gerar números aleatórios uma única vez, porém se você põe 2,
#       sempre que você compilar, ele vai gerar números aleatórios diferentes de cada compilação sua

gerador = np.random.default_rng(2)
ale5 = gerador.random(3)
print (ale5)