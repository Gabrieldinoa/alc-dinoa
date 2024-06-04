import numpy as np

def dotProduct(u, v):
    product = 0
    n=len(u)
    
    for i in range(0, n):
        product = product + u[i] * v[i]
 
    return product
 
def crossProduct(u, v):
     
    a=u[1] * v[2] - u[2] * v[1]
    b=u[2] * v[0] - u[0] * v[2]
    c=u[0] * v[1] - u[1] * v[0]
    
    vetor_resultado=[a,b,c]

    return vetor_resultado
 
u = [3,1,2]
v = [1,4,2]
    
uxv=crossProduct(u,v)
vxu=crossProduct(v,u)
uxvu=dotProduct(uxv,u)
vxuv=dotProduct(vxu,v)

print(f"u x v:", uxv)
print(f"v x u:", vxu)
print(f"<u x v,u>:", uxvu)
print(f"<v x u,v>:", vxuv)