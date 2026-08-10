import numpy as np
from gauge_dynamics.time_reversal import project_time_reversal,time_reversal_residual,kramers_J
def test_kramers_projection_and_pairs():
 r=np.random.default_rng(3);A=r.normal(size=(4,4))+1j*r.normal(size=(4,4));H=project_time_reversal((A+A.conj().T)/2); assert time_reversal_residual(H)<1e-12; e=np.linalg.eigvalsh(H); assert abs(e[0]-e[1])<1e-10 and abs(e[2]-e[3])<1e-10;J=kramers_J(2);assert np.allclose(J@J.conj(),-np.eye(4))
