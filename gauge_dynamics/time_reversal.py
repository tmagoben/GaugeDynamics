import numpy as np
def kramers_J(n_pairs):
 J2=np.array([[0.,1.],[-1.,0.]],complex); return np.kron(np.eye(n_pairs),J2)
def project_time_reversal(H):
 H=np.asarray(H,complex)
 if H.shape[0]%2: raise ValueError('Kramers spinor space must have even dimension')
 H=(H+H.conj().T)/2;J=kramers_J(H.shape[0]//2); return 0.5*(H+J@H.conj()@J.conj().T)
def time_reversal_residual(H):
 H=np.asarray(H,complex);J=kramers_J(H.shape[0]//2); return float(np.linalg.norm(H-J@H.conj()@J.conj().T))
