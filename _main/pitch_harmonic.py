import sys
from os import path
project_root = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
sys.path.append(project_root)
    
from harmonic_algorithm.io import AudioLoader
from harmonic_algorithm.pitch_onset import MonoPitch, OnsetGenerate
from harmonic_algorithm.transcription.score import MiditoScore
from harmonic_algorithm.util.units import Hz_to_MIDI2

from harmonic_algorithm.eval import transcription_eval, midi_to_score

import numpy as np
import matplotlib.pyplot as plt

# matplotlib options
from matplotlib import rcParams
rcParams['savefig.transparent'] = True
rcParams['text.usetex'] = False


    

def demo(audio, name, h, uc):
    
    print(sys.path[-1])
    #Obtener señales musicales
    fs = audio.sampleRate
    x = audio.signal
    audio_duration = audio.duration
    
    #Tamaño de ventana
    isset = 1
    frameSize = 2048*isset

    #Aplicar algoritmo harmonic
    kl = MonoPitch(x, fs, frameSize=frameSize)

    pitch = np.around(Hz_to_MIDI2(kl()),0)
    time = np.arange(pitch.shape[1]) * (frameSize / fs)*4/isset
    
    #Obtener onsets y graficarlo
    onset_times = OnsetGenerate(x, fs, h, uc)
    onset_times_f, tempo = onset_times()
    
    #Generar Partitura
    score = MiditoScore(pitch, time, onset_times_f, tempo, audio_duration, name)
    score()
    
    #Graficar piano roll
    graphic_piano_roll(time, pitch, onset_times_f)
    
    '''
    #MIR EVAL
    midi_to_score.main_converter(name)
    
    output = sys.path[-1] + "/mir_eval/clarinete/"
    output = output.replace("\\","/")
    reference_file = output + name + ".txt"
    estimated_file = output + name + "_estimated" + ".txt"
    output_file = output + name + "_results" + ".txt"
    transcription_eval.__eval(reference_file, estimated_file, output_file)
    '''

def graphic_piano_roll(time, pitch, onset_times_f):
    fig, ax = plt.subplots(figsize=(25,10)) #25 10
    fig.suptitle("PITCH ESTIMATION: HARMONIC ALGORITHM", fontsize=16)
    #ax.set_title("Piano roll of Beethoven's \"Für Elise\"")
    ax.set_title("Piano Roll")
    #pitch.shape[0]
    for m in range(pitch.shape[0]):
        ax.scatter(time, pitch[m])
        #print('Midi: ', pitch[m])
        
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Pitch (MIDI)')
    #ax.set_ylim(20, 109)
    ax.set_ylim(30, 100)
    ax.set_yticks(np.arange(30,100,10))
    
    #plt.show()
    ax.vlines(onset_times_f, 30, 100, color='r')

def initInterface(filepath, audio, h, uc):
    audio_file = filepath
    name = audio_file.split("/")
    name = name[-1].split(".")
    name = name[0]
    demo(audio, name, h, uc)
    

if __name__ == '__main__':
    
    songs = ["", 
             "1 violin-twinkle", 
             "2 Lightly_Row", 
             "4 Go_Tell_Aunt_Rhody", 
             "5 O_Come_Little_Children", 
             "7 1 Long_Long_Ago", 
             "9 Perpetual Motion", 
             "11 1 Nocturne-Andantino_voor_piano_en_viool_2013-Viool", 
             "13_Minuet_1", 
             "14 Minuet_2", 
             "15 Minuet_3",
             "16_The_Happy_Farmer2"] 
    h = 3
    uc = 57
    
    if len(sys.argv) > 3:
        print("Wrong number of arguments", file=sys.stderr)
        print("Usage: python %s [filename] [duration_in_seconds]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv) > 1:
        audio_file = sys.argv[1]
        audio = AudioLoader(audio_file)
        if len(sys.argv) == 3:
            audio.cut(stop=sys.argv[2])
    else:
        audio_file = "../samples/polyphonic/Clair_de_Lune_by_Claude_Debussy.wav"
        
        audio_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/input/violin/13_Minuet_1.wav"
        #audio_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/input/piano/17_Gavotte2.wav"
        #audio_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/input/clarinete/17_Gavotte2.wav"
        
        audio_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/input/violin/" + songs[1] + ".wav"
        name = audio_file.split("/")
        name = name[-1].split(".")
        name = name[0]
        
        audio = AudioLoader(audio_file)
        audio.cut(stop=5)
        print("Using first ", 10, " seconds of ", audio_file)
    
    demo(audio, name, h, uc)
