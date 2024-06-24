import numpy as np
from scipy.linalg import lu

def LUDECOMP(A):
    import numpy as np    
    print('A Matriz de entrada é:')
    print(A)
    A_original=A.copy()
    n=len(A)
    L=np.identity(n)
    P=np.identity(n)
    for i in range(n-1):        
        idx=max(A[i:n,i])      
        k=np.argmax(abs(A[i:n,i]))       
        pivotindex=i+k
        
        if pivotindex != i:
            A[[i,pivotindex]] = A[[pivotindex,i]]               
            L[[i,pivotindex]] = L[[pivotindex,i]]                                
            P[[i,pivotindex]] = P[[pivotindex,i]]
               
        
             
        for j in range(i,n-1):           
            L[j+1][i]=float(A[j+1][i]/A[i][i])
            A[j+1,0:n]=A[j+1,0:n]-(A[j+1][i]/A[i][i])*A[i,0:n]    
                                    
              
    for i in range(n):
        L[i][i]=1
        for j in range(i+1,n):
            L[i][j]=0
    U=A.copy()
    
    print('P :')
    print(P)
    print('L :')
    print(L)
    print('U :')
    print(U)
    A=A_original.copy()
    return P,L,U

A=np.array([[3.0,8,1],[5,2,0],[6,1,12]])
A_original=A.copy()
[x,y,z]=LUDECOMP(A)
A=A_original 

print('Resultados com o scipy:')
a,b,c=lu(A)
print(a)
print(b)
print(c)


