import numpy as np

batch_size_0 = 50
batch_size_1 = 1
rnn_size = 128

c0 = np.zeros(batch_size_0, rnn_size)
h0 = np.zeros(batch_size_0, rnn_size)
c1 = np.zeros(batch_size_1, rnn_size)
h1 = np.zeros(batch_size_1, rnn_size)

np.savetxt('c0.csv', c0, delimiter=',', newline='\n')
np.savetxt('h0.csv', h0, delimiter=',', newline='\n')
np.savetxt('c1.csv', c1, delimiter=',', newline='\n')
np.savetxt('h1.csv', h1, delimiter=',', newline='\n')
