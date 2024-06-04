import numpy as np
import matplotlib.pyplot as plt

#Letra a) Criação das matriz de Wilkinson
def matriz_Wilkinson(n):
    M=np.zeros((n,n))
    for cont in range(n):
        M[cont][cont]=n-cont
        if cont<n-1:
            M[cont][cont+1]=n


    return M

#Letra b) Plotar os números de condição das matrizes de Wilkinson
n=15
num_cond=np.linalg.cond(matriz_Wilkinson(n))

vetor_cond=np.zeros(n)
vetor_ordem=np.zeros(n)
for cont in range(n):
    vetor_cond[cont]=np.linalg.cond(matriz_Wilkinson(cont+1))
    vetor_ordem[cont]=cont+1

print(matriz_Wilkinson(n))

plt.plot(vetor_ordem,vetor_cond, marker='o')
plt.xlabel('Número de ordem da matriz')
plt.ylabel('Número de condicionamento da matriz')
plt.grid(True)
plt.show()

#Letra c) Calcular os autovalores de A(20x20) e de A_pertubada(20x20)
A=matriz_Wilkinson(20)

auto_valores, auto_vetores=np.linalg.eig(A)
print(f'Autovalores da matriz de Wilkinson:',auto_valores)

A_perturb=A
A_perturb[19][0]=1e-10


auto_valores, auto_vetores=np.linalg.eig(A_perturb)
print(f'Autovalores da matriz de Wilkinson perturbada:',auto_valores)