import numpy as np
from numpy.linalg import norm

def modqrgrsch(a):

    import numpy as np
    from numpy.linalg import norm

    
    m=len(a) #colunas de a
    n=len(a[0]) #colunas de a
    r=np.zeros((n,n))
    print(a)
    u=np.zeros((m,n))
    e=np.zeros((m,n))
    u[0:n,0]=a[0:n,0]
    e[0:n,0]=u[0:n,0]/norm(a[0:n,0])
    for i in range(1,n):
        tmp=a[0:n,i]
    
        for j in range(i):
            tmp=tmp-np.inner(a[0:n,i],e[0:n,j])*e[0:n,j]            
            
            
        u[0:n,i]=tmp
        e[0:n,i]=u[0:n,i]/norm(u[0:n,i])
        
    for i in range(n):
        for j in range(i,n):
            if i==j:
                r[i][j]=norm(u[0:n,i])
            else:
                r[i][j]=np.inner(a[0:n,j],e[0:n,i])

    np.set_printoptions(precision=3)
    print(e)
    print(r)
    
    return e,r

a=np.array([[1,9,0,5,3,2],[-6,3,8,2,-8,0],[3,15,23,2,1,7],[3,57,35,1,7,9],[3,5,6,15,55,2],[33,7,5,3,5,7]])
modqrgrsch(a)

print('Usando a função do numpy, temos:')
Q,R1=np.linalg.qr(a)
print(Q)
print(R1)


