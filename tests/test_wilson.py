import numpy as np
from gauge_dynamics.gauge import unitary_path
from gauge_dynamics.wilson import transform_links,wilson_loop
def test_wilson_trace_invariant():
 K=np.array([[.2,.1,0.],[.1,-.3,.05],[0.,.05,.15]],complex); links=unitary_path(K,np.array([.03,.07,-.02,.05]));G=unitary_path(np.diag([.1,-.2,.3]),np.arange(4)*.11);Wt=wilson_loop(transform_links(links,G));W=wilson_loop(links); assert abs(np.trace(Wt)-np.trace(W))<1e-12
