import numpy as np
import math as m

matriz=np.array([[1,2,3,2],[2,3,4,7],[1,3,2,2],[3,4,6,10]])
print(matriz)

#identidade=np.eye(2)
#print(identidade)

#zerar a primeira coluna
for n in range(1,4):
    print(n)
    matriz[n]=matriz[0][0]*matriz[n]-matriz[n][0]*matriz[0]

print(matriz)

#zerar a segunda coluna

for n in range(2,4):
    print(n)
    matriz[n]=matriz[1][1]*matriz[n]-matriz[n][1]*matriz[1]

print(matriz)

#zerar a terceira coluna

for n in range(3,4):
    print(n)
    matriz[n]=matriz[2][2]*matriz[n]-matriz[n][2]*matriz[2]

print(matriz)

#zerar a parte superior

#zerar a segunda coluna
for n in range(0,1):
    print(n)
    matriz[n]=matriz[1][1]*matriz[n]-matriz[n][1]*matriz[1]

print(matriz)



#zerar a terceira coluna

for n in range(0,2):
    print(n)
    matriz[n]=matriz[2][2]*matriz[n]-matriz[n][2]*matriz[2]

print(matriz)


#zerar a quarta coluna

for n in range(0,3):
    print(n)
    matriz[n]=matriz[3][3]*matriz[n]-matriz[n][3]*matriz[3]

print(matriz)

