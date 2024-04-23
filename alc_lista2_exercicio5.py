import numpy as np
import math as m

def is_ortogonal_by_definition(A):
    P_inv=np.linalg.inv(A)
    P_transposto=np.matrix.transpose(A)
    
    if np.allclose(P_inv,P_transposto,0.1):
        return True
    else:
        return False

def is_ortogonal_by_vectors(A):
    u1=np.array([A[0,0],A[1,0],A[2,0]])
    u1=u1.reshape(-1,1)
    
    u2=np.array([A[0,1],A[1,1],A[2,1]])
    u2=u2.reshape(-1,1)
    
    u3=np.array([A[0,2],A[1,2],A[2,2]])
    u3=u3.reshape(-1,1)
    
    if (-0.1<(u1.T@u2)<0.1)and(-0.1<(u2.T@u3)<0.1)and(-0.1<(u3.T@u1)<0.1):
       
        if (0.9<(u1.T@u1)<1.1)and(0.9<(u2.T@u2)<1.1)and(0.9<(u3.T@u3)<1.1):
            
           
            return True
        else:
            print('norma diferente de 1')
            return False
        
    else:
       
        return False
       

P1_6_38=np.array([[-0.40825,0.43644,0.80178],[-0.8165,0.21822,-0.53452],[-0.40825,-0.87287,0.26726]])
print(f'P1_6_38 é: {P1_6_38}')
resultado=is_ortogonal_by_definition(P1_6_38)
print(f'A matriz P1_6_38 é ortogonal pela definição? {resultado}')

resultado_vetores=is_ortogonal_by_vectors(P1_6_38)
print(f'A matriz P1_6_38 é ortogonal pela verificação da base? {resultado_vetores}')

P2_6_38=np.array([[-0.51450,0.48507,0.70711],[-0.68599,-0.72761,0.0000],[0.51450,-0.48507,0.70711]])
print(f'P2_6_38 é: {P2_6_38}')
resultado=is_ortogonal_by_definition(P2_6_38)
print(f'A matriz P2_6_38 é ortogonal pela definição? {resultado}')

resultado_vetores=is_ortogonal_by_vectors(P2_6_38)
print(f'A matriz P2_6_38 é ortogonal pela verificação da base? {resultado_vetores}')

P1_6_39=np.array([[-0.58835,0.70206,0.40119],[-0.78446,-0.37524,-0.49377],[-0.19612,-0.60523,0.77152]])
print(f'P1_6_39 é: {P1_6_39}')
resultado=is_ortogonal_by_definition(P1_6_39)
print(f'A matriz P1_6_39 é ortogonal pela definição? {resultado}')

resultado_vetores=is_ortogonal_by_vectors(P1_6_39)
print(f'A matriz é P1_6_39 ortogonal pela verificação da base? {resultado_vetores}')

P2_6_39=np.array([[-0.47624,-0.4264,0.30151],[0.087932,0.86603,-0.40825],[-0.87491,-0.26112,0.86164]])
print(f'P2_6_39 é: {P2_6_39}')
resultado=is_ortogonal_by_definition(P2_6_39)
print(f'A matriz P2_6_39 é ortogonal pela definição? {resultado}')

resultado_vetores=is_ortogonal_by_vectors(P2_6_39)
print(f'A matriz é P2_6_39 ortogonal pela verificação da base? {resultado_vetores}')
