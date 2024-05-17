import numpy as np
import math as m

def inversa_eliminacao(matriz):


    #Calcula o tamanho da matriz
    tam=len(matriz)
    #Plota a matriz de entrada
    print('A matriz inicial é:')
    print(matriz)

    #Verifica a existência de zeros na diagonal principal

    avaliador=1
    for cont in range(0,tam):
        avaliador=matriz[cont][cont]*avaliador
    if avaliador==0:
        print('Zero na diagonal principal: Sugere-se o uso de uma função alternativa para o cálculo da inversa')
    else:
        #Cálculo da inversa pela função inv do numpy, para comparação
        

        #Criação da matriz aumentada
        identidade=np.eye(tam)
        aumentada=np.concatenate((np.transpose(matriz),identidade))
        aT=np.transpose(aumentada)
        matriz=aT
        print('A matriz aumentada é:')
        print(matriz)
        
        #Laços das operações de diagonalização na matriz aumentada

        #Zerando os elementos abaixo da diagonal principal da matriz original
        for k in range(0,tam-1):
            
            if matriz[k][k]==0:
                print('Surgiu um zero na diagonal principal')
           
            matriz[k]=matriz[k]/matriz[k][k]
            
            
            
            for n in range(k+1,tam):
                
                        
                matriz[n]=matriz[k][k]*matriz[n]-matriz[n][k]*matriz[k]
                
                
        #Zerando os elementos acima da diagonal principal da matriz original    
        for t in range(1,tam):
            
            for n in range(0,t):
                        
                matriz[n]=matriz[t][t]*matriz[n]-matriz[n][t]*matriz[t]
                
            
        matriz=(1/matriz[0][0])*matriz

        #Plotando a matriz aumentada
        print(f' A matriz aumentada após as operações é:')
        #A matriz aumentada é apresentada arredondada para se facilitar a visualização
        print(np.round(matriz,3))
        
        #Extração do bloco da direita da matriz aumentada, excluindo-se as colunas da esquerda
        matrizinvertida=matriz
        for contador in range(0,tam):
            matrizinvertida=np.delete(matrizinvertida,0,axis=1)
            
        #Plotagem da matriz inversa
      
        print('Extraindo o lado direito da matriz aumentada, temos a inversa pedida:')
        print(matrizinvertida)

        

#Declaração da matriz da qual se quer tirar a inversa
matriz=np.array([[2,3,1.4,3,4],[3,2,5,5,2.3],[1,3,2,2,1.2],[2,4.5,6,2,3.4],[1,2,3,4,5]])

#Chamada da função que inverte a matriz
inversa_eliminacao(matriz)
