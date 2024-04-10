import numpy as np
import math as m

#Matriz M 
M=np.array([[1,2,3,6,7,8,1],[0,2,4,6,2,4,2],[0,0,4,8,1,3,3],[0,0,0,2.3,7,8,4],[0,0,0,0,1,6,5],[0,0,0,0,0,2,6],[0,0,0,0,0,0,7]])
#Vetor B representa o lado direito do sistema linear
B=np.array([7,3,7,6,8,9,6])

#Alternativamente, pode-se obter a matriz M e o vetor B através do bloco abaixo, que está como comentado:
# n=int(input('Digite o tamanho da matriz '))
# print('A matriz tem tamanho ',n)
# M=np.identity(n)
# B=np.ones(n)
# for linha in range(n):
      
#       for coluna in range(n):
         
#          print(f'Digite o valor de M',linha,coluna)
#          M[linha][coluna]=float(input())

# for contador in range(n):
#      print(f'Digite o valor de B',contador)
#      B[contador]=float(input())
# print(f'M=',M)
# print(f'B=',B)

#Após a definição de M e B, é criado um vetor X, conforme abaixo:
#Criação de um vetor X, inicialmente com elementos iguais a 1, mas que será a solução do problema
X=np.ones(len(M))



#Lista criada para analisar-se a diagonal principal, em busca de zeros
Lista_diag=[]

#Montagem da lista contendo os valores da diagonal principal
for i in range(len(M)):
    
    Lista_diag.append(M[i][i])



#Verificação de zeros na diagonal principal de M e aplicação do método de substituição regressiva
if 0 not in Lista_diag:
    X[len(M)-1]=B[len(M)-1]/M[len(M)-1][len(M)-1]
    
    for j in range(len(M)-1,0,-1):
        ksum=0
        for k in range(j,len(M)):
            ksum=ksum+X[k]*M[j-1][k]
        X[j-1]=((B[j-1]-ksum)/M[j-1][j-1])
    #Vetor X é a solução
    print(f'O valor de X é: ',X)
else:
    print('Há pelo menos um valor igual a zero na diagonal principal')

