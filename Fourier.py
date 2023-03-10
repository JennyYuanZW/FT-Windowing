import numpy as np
import matplotlib.pyplot as plt

class DiscreteFourierTransform:
    def __init__(self, data, samplerate):
        self.data = data
        self.samplerate = samplerate

    def DFT(self):
        N = len(self.data)
        n = np.arange(N)
        k = n.reshape((N,1))
        # we first create a N*N matrix, n is a matrix of size (1, N), is a matrix (N, 1)
        e = np.exp(-2j * np.pi * k * n / N)
        # next we used e to dot with data to get a N*1 matrix, which represents X at different k
        X = np.dot(e, self.data)

        return X
    
    def DFTplot(self):
        X = self.DFT()
        T = len(self.data)/self.samplerate
        frequency = np.arange(len(self.data))/ T
        plt.stem(frequency, abs(X))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('DFT Amplitude')
        plt.show()
# recetangular window

#sin window

#hanning window




