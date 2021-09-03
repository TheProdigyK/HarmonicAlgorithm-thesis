import numpy as np
import librosa
import matplotlib.pyplot as plt

# matplotlib options
from matplotlib import rcParams
rcParams['savefig.transparent'] = True
rcParams['text.usetex'] = False

class OnsetGenerate(object):
    def __init__(self, x, fs, h, uc):
        self.x = x
        self.fs = fs
        
        self.onsets = []
        self.onset_times_f = []
        self.onset_envelope = []
        self.tempo = 120
  
        self.heuristica = 3 if h == 0 else h
        
        self.umbral_compensation = 0.5 if uc == 0 else uc/100
        

    
    def __call__(self):
        self.onsets, self.onset_envelope, self.tempo = self.second_onset_detect(self.x, self.fs)
        self.onset_times_f = librosa.frames_to_time(self.onsets)
        
        peaks = librosa.util.peak_pick(self.onset_envelope, self.heuristica, self.heuristica, self.heuristica
                                       , 50, self.umbral_compensation, 10)
        #peaks = librosa.util.peak_pick(self.onset_envelope, 3, 3, 3, 5, 0.5, 10)
        times = librosa.frames_to_time(np.arange(len(self.onset_envelope)),
                               sr=self.fs, hop_length=512)
        '''
        peaks = []
        for i in range(len(self.onset_envelope)):
            if self.onset_envelope[i] >= 2:
                peaks.append(i)
        '''        

        #self.graphic(self.onsets, self.onset_envelope)
        self.graphic2(self.onset_envelope, self.fs, peaks, times)
        

    
        return np.multiply(times[peaks],2), self.tempo
        #return self.onset_times_f, self.tempo
    
    def graphic(self, onsets, onset_envelope):
        fig2, ax2 = plt.subplots(figsize=(25,10))
        ax2.plot(onset_envelope, label='onset strength')
        ax2.vlines(onsets, 0, onset_envelope.max(), color = 'r', alpha=0.25)
        ax2.set_xticks([]), ax2.set_yticks([])
        
        fig2.show()
    
    def graphic2(self, onset_envelope, sr, peaks, times):
        '''
        peaks = librosa.util.peak_pick(onset_envelope, 3, 3, 3, 5, 0.5, 10)
        times = librosa.frames_to_time(np.arange(len(onset_envelope)),
                               sr=sr, hop_length=512)
        '''
        fig2, ax2 = plt.subplots(figsize=(25,10))
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('ONSET STRENGTH')
        
        ax2.plot(times, onset_envelope, label='onset strength')
        ax2.vlines(times[peaks], 0, onset_envelope.max(), color = 'r', alpha=0.25)
        #ax2.set_xticks([]), ax2.set_yticks([])
        
        fig2.show()
    
    def first_onset_detect(self, onset_times, pitch, time):
    
        onsetReplace = []
        onsetValue = 0
        
        onsetFinal = []
        
        
        for i in range(len(pitch)):
            if(onsetValue != pitch[i]):
                onsetValue = pitch[i]
                onsetReplace.append(time[i])
        #print(onsetReplace)    
        onsetFinal.append(onsetReplace[0])
        verify = False
        '''
        for i in range(len(onset_times)):
            onset_sample = onset_times[i]
            for j in range(len(onsetReplace)):
                if(abs(onset_sample-onsetReplace[j]) < 0.12):
                    onsetFinal.append(onsetReplace[j])
                    verify = True
                    break
                else:
                    verify = False
            if(not verify):
                onsetFinal.append(onset_sample)
        #print('onset azul: ', onsetFinal)
        '''
        return onsetFinal
    
    def second_onset_detect(self, x, fs):
        onset_envelope = librosa.onset.onset_strength(x, sr=fs)
        
        
        #onsets = librosa.onset.onset_detect(onset_envelope = onset_envelope, hop_length=512,
        #                                    wait=35, pre_avg=100, post_avg=30, pre_max=30, post_max=30) #35 #100 30 30 70
                
        onsets = librosa.onset.onset_detect(onset_envelope = onset_envelope, hop_length=18, wait = 10)
        
        tempo, beats = librosa.beat.beat_track(onset_envelope = onset_envelope)
        
        return onsets, onset_envelope, tempo
    

        
