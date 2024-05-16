import numpy as np
import math as m

matriz=np.array([[10,1,1,2],[1,3,4,1],[1,2,2,2],[3,4,1,0]])
tam=len(matriz)
print(tam)
print(matriz)

identidade=np.eye(tam)
print(identidade)

#zerar a primeira coluna
for k in range(0,tam-1):
    print(k)
    for n in range(k+1,tam):
        print(n)
        matriz[n]=matriz[k][k]*matriz[n]-matriz[n][k]*matriz[k]
        identidade[n]=matriz[k][k]*identidade[n]-matriz[n][k]*identidade[k]
        

    
print(matriz)

#zerar a parte superior

#zerar a segunda coluna
for t in range(1,tam):
    print(t)
    for n in range(0,t):
        print(t)
        matriz[n]=matriz[t][t]*matriz[n]-matriz[n][t]*matriz[t]
        identidade[n]=matriz[t][t]*identidade[n]-matriz[n][t]*identidade[t]

print(matriz)

# for n in range(0,1):
#     print(n)
#     matriz[n]=matriz[1][1]*matriz[n]-matriz[n][1]*matriz[1]

# print(matriz)

# #zerar a terceira coluna

# for n in range(0,2):
#     print(n)
#     matriz[n]=matriz[2][2]*matriz[n]-matriz[n][2]*matriz[2]

# print(matriz)

# #zerar a quarta coluna

# for n in range(0,3):
#     print(n)
#     matriz[n]=matriz[3][3]*matriz[n]-matriz[n][3]*matriz[3]

# print(matriz)
