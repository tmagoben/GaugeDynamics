import numpy as np
from gauge_dynamics.time_reversal import project_time_reversal,time_reversal_residual
r=np.random.default_rng(7);A=r.normal(size=(4,4))+1j*r.normal(size=(4,4));H=project_time_reversal((A+A.conj().T)/2);print('TR residual',time_reversal_residual(H));print('eigenvalues',np.linalg.eigvalsh(H))
