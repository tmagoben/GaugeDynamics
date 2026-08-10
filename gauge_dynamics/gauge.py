import numpy as np
def _hermitian_eigh(K):
 K=np.asarray(K,complex)
 if not np.allclose(K,K.conj().T): raise ValueError('generator must be Hermitian')
 return np.linalg.eigh(K)
def unitary_path(K,x):
 e,U=_hermitian_eigh(K); x=np.asarray(x,float); return np.stack([U@np.diag(np.exp(1j*e*t))@U.conj().T for t in x])
def unitary_path_derivative(K,x):
 G=unitary_path(K,x); return np.einsum('ab,xbc->xac',1j*np.asarray(K,complex),G)
def transform_hamiltonian(H,G): return G.conj().T@H@G
def transform_connection(A,G,dG): return G.conj().T@A@G+1j*G.conj().T@dG
def central_derivative(values,x):
 values=np.asarray(values);x=np.asarray(x,float); out=np.empty_like(values,dtype=complex); out[1:-1]=(values[2:]-values[:-2])/(x[2:,None]-x[:-2,None]); out[0]=(values[1]-values[0])/(x[1]-x[0]); out[-1]=(values[-1]-values[-2])/(x[-1]-x[-2]); return out
def covariant_derivative(psi,x,A): return central_derivative(psi,x)-1j*np.einsum('xij,xj->xi',A,psi)
