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
        dft=abs(self.DFT())
        #getting rid of negative freq
        dft_short=[]
        freq_short=[]
        for i in range(0,round(N/2)):
            dft_short.append(dft[i])
            freq_short.append(freq[i])
        plt.figure(figsize=(16, 8))
        plt.stem(freq_short,dft_short )
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('DFT Amplitude')
        plt.title('Magnitude Spectrum')
        plt.show()
    
    def apply_window(self, windowfunction, sampling_range):
        windowed = np.transpose(self.data[0:sampling_range])[0] * windowfunction
        X = np.fft.fft(windowed)
        N = len(windowed)
        freq = np.fft.fftfreq(N, d=1/self.samplerate)
        #getting rid of negative freq
        X_short=[]
        freq_short=[]
        for i in range(0,round(N/2)):
            X_short.append(abs(X[i]))
            freq_short.append(freq[i])
        print(len(X))
        print(X)
        
        
        print(len(freq))
        print(freq)
        plt.figure(figsize=(16, 8))
        plt.stem(freq_short, X_short)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('DFT Amplitude')
        plt.title('Magnitude Spectrum')
        plt.show()




