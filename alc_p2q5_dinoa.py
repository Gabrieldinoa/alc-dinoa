import numpy as np

def alc_cholesky(a):
    print(f'A matriz fornecida é: {a}')
    
    at=a.transpose()
    
    n=len(a)
    r=np.zeros([n,n])
    

    for i in range(n):
        
        rt=r.transpose()
        tmp=a[i][i]-sum(rt[i,0:i]**2)
        
        if tmp<0:
            print()
            print('Não foi possível fazer a decomposição de Cholesky, pois a matriz não é PD')
            print()
            return
        r[i][i]=tmp**0.5
        
        for j in range(i+1,n):
            
            
            r[i][j]=(1/r[i][i])*(a[i][j]-sum(rt[i,0:i]*rt[j,0:i]))
            
    print(f'A matriz R é: {r}')
    return r

print()
print('Teste do código com uma matriz PD')
print()
a=np.array([[1,1,4,-1],[1,5,0,-1],[4,0,21,-4],[-1,-1,-4,10]])
R1=alc_cholesky(a)

print(f'RTR é: {R1.transpose()@R1}')

print('Teste do código com uma matriz não PD')
print()
b=np.array([[1,5,6],[-7,12,5],[2,1,10]])
R2=alc_cholesky(b)
