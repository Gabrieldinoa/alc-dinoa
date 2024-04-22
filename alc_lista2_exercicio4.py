import numpy as np
import math as m
n=3
print(f'Para n = {n}')
u=np.random.rand(n)
u=u.reshape(-1,1)
print(f'O valor de u é: {u}')
v=np.random.rand(n)
v=v.reshape(-1,1)
vT=np.transpose(v)

A=u@vT
print(f'A matriz A é: {A}')
print(f'O posto de A é: {np.linalg.matrix_rank(A)}')
print(f'A norma de A é: {np.linalg.norm(A)}')
print(f'A nomra de A pode ser calculada a partir de At*A: {(np.linalg.eig(A.T@A))}')
print(f'A norma de |u||v| é: {(np.linalg.norm(u))*np.linalg.norm(v)}')

n=15
print(f'Para n = {n}')
u=np.random.rand(n)
u=u.reshape(-1,1)
v=np.random.rand(n)
v=v.reshape(-1,1)
vT=np.transpose(v)

A=u@vT
print(f'O posto de A é: {np.linalg.matrix_rank(A)}')
print(f'A norma de A é: {np.linalg.norm(A)}')
print(f'A norma de |u||v| é: {(np.linalg.norm(u))*np.linalg.norm(v)}')

n=25
print(f'Para n = {n}')
u=np.random.rand(n)
u=u.reshape(-1,1)
v=np.random.rand(n)
v=v.reshape(-1,1)
vT=np.transpose(v)

A=u@vT
print(f'O posto de A é: {np.linalg.matrix_rank(A)}')
print(f'A norma de A é: {np.linalg.norm(A)}')
print(f'A norma de |u||v| é: {(np.linalg.norm(u))*np.linalg.norm(v)}')