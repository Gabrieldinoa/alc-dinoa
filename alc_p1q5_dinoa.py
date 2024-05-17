import numpy as np
import math as m

matriz=np.array([[2,1,1,5],[3,3,3,1],[1,3,2,7],[2.4,6,1,8]])
tam=len(matriz)
#print(tam)
print('a matriz eh:')
print(matriz)
matriz_inversa=np.linalg.inv(matriz)
identidade=np.eye(tam)

aumentada=np.concatenate((np.transpose(matriz),identidade))
#print(aumentada)
#print(identidade)
aT=np.transpose(aumentada)
print(aT)
matriz=aT
#zerar a primeira coluna
for k in range(0,tam-1):
    
    matriz[k]=matriz[k]/matriz[k][k]
    #identidade[k]=identidade[k]/matriz[k][k]
    for n in range(k+1,tam):
        print(f'k eh {k} e n eh {n}')
        
        
        matriz[n]=matriz[k][k]*matriz[n]-matriz[n][k]*matriz[k]
        #identidade[n]=matriz[k][k]*identidade[n]-matriz[n][k]*identidade[k]
        print(matriz)

    
print(f'matriz superior eh')
print(matriz)


#zerar a parte superior

#zerar a segunda coluna
for t in range(1,tam):
    
    for n in range(0,t):
        print(f't eh {t} n eh {n}')
        
        matriz[n]=matriz[t][t]*matriz[n]-matriz[n][t]*matriz[t]
        #identidade[n]=matriz[t][t]*identidade[n]-matriz[n][t]*identidade[t]
        print(matriz)



print('A  matriz final eh')
matriz=(-1/matriz[0][0])*matriz
print(f' A matriz eh: {matriz}')
print(f'a matriz inversa eh {matriz_inversa}')

