import numpy as np
import math as m

def is_ortogonal_by_definition(A):
    P1_inv=np.linalg.inv(A)
    P1_transposto=np.matrix.transpose(A)
    if (P1_inv==P1_transposto).all:
        return True
    else:
        return False

def is_ortogonal_by_vectors(A):
    u1=np.array([A[0,0],A[1,0],A[2,0]])
    u1=u1.reshape(-1,1)
    #print(u1)
    u2=np.array([A[0,1],A[1,1],A[2,1]])
    u2=u2.reshape(-1,1)
    #print(u2)
    u3=np.array([A[0,2],A[1,2],A[2,2]])
    u3=u3.reshape(-1,1)
    #print(u3)
    if -0.1<(u1.T@u2)and(u2.T@u3)and(u3.T@u1)<0.1:
        if 0.9<(u1.T@u1)and(u2.T@u2)and(u3.T@u3)<1.1:
            return True
        else:
            print('norma diferente de 1')
            return False
        
    else:
        return False
       

P1=np.array([[-0.40825,0.43644,0.80178],[-0.8165,0.21822,-0.53452],[-0.40825,-0.87287,0.26726]])
print(P1)
resultado=is_ortogonal_by_definition(P1)
print(f'A matriz é ortogonal pela definição? {resultado}')

resultado_vetores=is_ortogonal_by_vectors(P1)
print(f'A matriz é ortogonal pela verificação da base? {resultado_vetores}')