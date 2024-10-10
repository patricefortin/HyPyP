import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import chirp

class SynteticSignal:
    def __init__(self, tmax: int, n_points: int = 10000):
        self.n_points = n_points
        self.times_vec = np.linspace(0, tmax, n_points)
        self.sample_rate = n_points / tmax
        self.period = 1.0 / self.sample_rate
        self.y = np.zeros_like(self.times_vec)
    
    @property
    def x(self):
        return self.times_vec

    def add_chirp(self, f0, f1):
        self.y += chirp(self.times_vec, f0=f0, f1=f1, t1=np.max(self.times_vec), method='linear')
        return self
    
    def add_sin(self, freq):
        self.y += np.sin(self.times_vec * 2 * np.pi * freq)
        return self
    
    def add_noise(self, level=0.1):
        self.y += level * np.random.normal(0, 1, self.n_points)
        return self
    
    def add_custom(self, y):
        self.y += y
        return self
    
    def plot(self):
        plt.plot(self.times_vec, self.y)
        plt.xlabel('Time (s)')
    
    def plot_fft(self):
        xf = fftfreq(self.n_points, self.period)[:self.n_points//2]
        yf = fft(self.y)

        #plt.plot(xf, 2.0/self.n_points * np.imag(yf[0:self.n_points//2]))
        #plt.plot(xf, 2.0/self.n_points * np.imag(yf[0:self.n_points//2]))
        plt.plot(xf, 2.0/self.n_points * np.abs(yf[0:self.n_points//2]))
        plt.xscale('log')
        plt.xlabel('Freq (Hz)')
        
        
        
