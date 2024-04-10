import numpy as np


def posicao(theta1,theta2):
        
    L1=20
    L2=15
    Xu=L1*np.cos(np.radians(theta1))+L2*np.cos(np.radians(theta1+theta2))
    Yu=L1*np.sin(np.radians(theta1))+L2*np.sin(np.radians(theta1+theta2))
    vetor=[round(Xu,1),round(Yu,1)]
    
    return vetor

v1=float(input('Digite o valor de theta1 em graus '))
print(v1)
v2=float(input('Digite o valor de theta2 em graus '))
print(v2)
saida=posicao(v1,v2)
print('A posição do efetuador é dada por: ')
print(f'Xu=',saida[0],'cm')
print(f'Yu=',saida[1],'cm')
