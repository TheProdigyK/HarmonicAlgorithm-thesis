from abc import ABC, abstractmethod
from itertools import zip_longest
import numpy as np


from harmonic_algorithm.pitch_onset.kl import PitchGenerate

class Pitch(ABC):
    def __init__(self, signal, sampleRate, frameSize=2048, fftBins=4096):
        self.signal = signal
        self.sampleRate = sampleRate
        self.frameSize = frameSize
        self.fftSize = fftBins

    def __call__(self, signal=None):
        if signal is not None:
            return self._func(signal)
        pitch = []
        start, stop = 0, self.frameSize
        while stop <= self.signal.size:
            f0 = self._func(self.signal[start:stop])
            pitch.append(f0)
            start, stop = stop, stop + self.frameSize
        return np.array(pitch)

    @abstractmethod
    def _func(self, signal):
        return 0




class MonoPitch(Pitch):
    def __init__(self, signal, sampleRate, frameSize=2048, fftBins=4096, **kwargs):
        super().__init__(signal, sampleRate, frameSize, fftBins)
        self.estimate_f0 = None
        
        poly = kwargs.pop('max_polyphony', 1)
        self.estimate_f0 = PitchGenerate(max_poly=poly)


    def __call__(self, signal=None):
        f0 = self.estimate_f0(self.signal, self.sampleRate)
        return np.array(list(zip_longest(*f0, fillvalue=np.nan)))

    def _func(self, signal):
        return []




    
        
        
        
