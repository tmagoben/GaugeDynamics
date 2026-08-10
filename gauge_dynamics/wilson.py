import numpy as np
def transform_links(links,gauges):
 links=np.asarray(links,complex);gauges=np.asarray(gauges,complex);N=len(links); return np.stack([gauges[k].conj().T@links[k]@gauges[(k+1)%N] for k in range(N)])
def wilson_loop(links):
 W=np.eye(links.shape[1],dtype=complex)
 for L in links: W=W@L
 return W
