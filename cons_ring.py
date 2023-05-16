import sys
import numpy as np
import os
sys.path.append(os.path.abspath("C:/Users/zzlli/Anaconda3/envs/forQPSI_deUn/Lib/site-packages/deUn"))
from cons_GC_ring_GC import GC_ring_GC


ring1 = GC_ring_GC('yourName', 1.55, np.array([25, 50, 75, 125, 150]), 0.800, 0.800, np.array([.700, .800, .900, 1, 1.2]), 'positive')
ring1.deUn_ring()
