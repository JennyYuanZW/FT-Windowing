import numpy as np
import matplotlib.pyplot as plt

class DiscreteFourierTransform:
    def __init__(self, data, samplerate):
        self.data = data
        self.samplerate = samplerate

    def DFT(self):
        N = len(self.data)
        X = np.fft.fft(self.data ) # Compute the DFT using numpy's fft function
        return X
    
    def DFTplot(self):
        N = len(self.data)
        freq = np.fft.fftfreq(N, d=1/self.samplerate)  # Compute the frequency axis
        plt.figure(figsize=(16, 8))
        plt.stem(freq, abs(self.DFT()))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('DFT Amplitude')
        plt.title('Magnitude Spectrum')
        plt.show()
    def apply_window(self, windowfunction, sampling_range):
        windowed = np.transpose(self.data[0:sampling_range])[0] * windowfunction
        X = np.fft.fft(windowed)
        print(len(X))
        print(X)
        N = len(windowed)
        freq = np.fft.fftfreq(N, d=1/self.samplerate)
        print(len(freq))
        print(freq)
        plt.figure(figsize=(16, 8))
        plt.stem(freq, abs(X))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('DFT Amplitude')
        plt.title('Magnitude Spectrum')
        plt.show()




