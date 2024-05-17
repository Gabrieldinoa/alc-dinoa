import numpy as np
import math as m

def inversa_eliminacao(matriz):


    
    tam=len(matriz)
    #print(tam)
    print('A matriz inicial é:')
    print(matriz)

    avaliador=1
    for cont in range(0,tam):
        avaliador=matriz[cont][cont]*avaliador
    if avaliador==0:
        print('Zero na diagonal principal: Sugere-se o uso de uma função alternativa para o cálculo da inversa')
    else:
        matriz_inversa=np.linalg.inv(matriz)
        identidade=np.eye(tam)
        
        
        aumentada=np.concatenate((np.transpose(matriz),identidade))
        aT=np.transpose(aumentada)
        matriz=aT
        print('A matriz aumentada é:')
        print(matriz)
        
        for k in range(0,tam-1):
            
            if matriz[k][k]==0:
                print('Surgiu um zero na diagonal principal')
           
            matriz[k]=matriz[k]/matriz[k][k]
            
            
            
            for n in range(k+1,tam):
                
                        
                matriz[n]=matriz[k][k]*matriz[n]-matriz[n][k]*matriz[k]
                
                
            
        for t in range(1,tam):
            
            for n in range(0,t):
                        
                matriz[n]=matriz[t][t]*matriz[n]-matriz[n][t]*matriz[t]
                
            
        matriz=(1/matriz[0][0])*matriz
        print(f' A matriz aumentada após as operações é:')
        print(np.round(matriz,3))
        
        matrizinvertida=matriz
        for contador in range(0,tam):
            matrizinvertida=np.delete(matrizinvertida,0,axis=1)
            
        
      
        print('Extraindo o lado direito da matriz aumentada, temos:')
        print(matrizinvertida)
        print(f'Comparando com a inversa da matriz pela função inv do numpy: ')
        print(matriz_inversa)
matriz=np.array([[2,3,1.4,3,4],[3,2,5,5,2.3],[1,3,2,2,1.2],[2,4.5,6,2,3.4],[1,2,3,4,5]])

inversa_eliminacao(matriz)
