import numpy as np
import sys
import code

name = sys.argv[1]

target = np.genfromtxt(name+'.csv', delimiter=',')
np.savetxt(name+'_t.csv', target.T, delimiter=',', newline='\n')
