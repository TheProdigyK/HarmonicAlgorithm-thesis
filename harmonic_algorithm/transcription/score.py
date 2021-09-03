import numpy as np
import music21
import sys

class MiditoScore(object):
    def __init__(self, midi_note, midi_time, onset_times, tempo, audio_duration, name):
        self.midi_note = midi_note
        self.midi_time = midi_time
        self.onset_times = onset_times
        self.tempo = tempo
        self.audio_duration = audio_duration
        self.name = name
        
        self.base_note = 125 # 4/4 con 120 bpm default
        self.midiN = []
        self.duration = []
        
        #Creacion de una nueva partitura
        self.s = music21.stream.Stream()
    
    def __call__(self):
        self.base_note = self.tempoToMilliSeconds(self.tempo)
        self.midiN, self.duration = self.onsetFilter(self.midi_note, self.midi_time, self.onset_times, self.audio_duration)
        self.generateScore(self.midiN, self.duration, self.base_note)
        return self.midiN
        
    
    def tempoToMilliSeconds(self, tempo):
        onefour_note = tempo/60
        base_note = onefour_note/4
        return base_note # nota base: doble corchea
    
    def onsetFilter(self, midi_note, midi_time, onset_times, last_duration):
        midiN =[]
        duration = []
        midi_note = midi_note[0]

        
        if(abs(0-onset_times[0]) < 0.5):
            onset_times = onset_times[1:]
            midiN.append(midi_note[0])
            
        else:
            midiN.append(midi_note[0])
            
       
        duration_ant = 0
                
        for i in range(len(onset_times)):
            time = onset_times[i]
            
            for j in range(len(midi_note)):
                aprox_time = midi_time[j]
                if(time <= aprox_time and (j+1)<len(midi_note)):
                    '''
                    if(midi_note[j] != midi_note[j+1] and midi_note[j] == midi_note[j-2]):
                        midiN.append(midi_note[j+1])
                    else:
                        midiN.append(midi_note[j])
                    '''
                    midiN.append(midi_note[j])
                        
                    duration.append(time-duration_ant)
                    duration_ant = time
                    break
                else:
                    if(j+1 >= len(midi_note)):
                        midiN.append(midi_note[j])
                        duration.append(time-duration_ant)
                        duration_ant = time
                    

        duration.append(duration[-1])
        
        
        #print('notas finales: ', midiN)
        #print('notas finales duracion: ', duration)
        
        return midiN, duration

        
    def QuarterLengthAprox(self, time):
        #quarterlength
        qls = [1/4, 1/2, 1, 1*2, 1*4]
        ql = [1*4, 1*2, 1, 1/2, 1/4]
        
        for data in ql:
            if(abs(data-time) < 0.25):
                return data
            elif(abs((data+data/2) - time) < 0.25):
                return data+(data/2)
           
        return 0
        
    
    def generateScore(self, midi_note, onset_times, base_note):
        onset_times = np.around(onset_times,2)
        qls = [1/4, 1/2, 1, 1*2, 1*4]

        
        
        #Creacion de una nueva partitura
        self.s = music21.stream.Stream()
        
        #Asignación del tempo
        mm1 = music21.tempo.MetronomeMark(int(base_note*(4*60)))
        self.s.append(mm1)
        
        #compas 4/4
        ts = music21.meter.TimeSignature('4/4')
        self.s.append(ts)
        
        s_array = []
        pitch = 0
    
        Violin = music21.instrument.Violin()
        Violin.midiChannel=0
        self.s.append(Violin)
        
        print(len(midi_note),len(onset_times))
        #print('onset_time ant: ', onset_times)
        for i in range(len(midi_note)-1):
            silence = 0

            time= self.QuarterLengthAprox(onset_times[i])
            
            if(time==0):
                j = 0
                while(time == 0 and j < len(qls)):
                    silence = qls[j]
                    time = self.QuarterLengthAprox(onset_times[i]-silence)
                    j+=1

                s_array.append(music21.note.Note(midi_note[i], quarterLength = time))
                s_array.append(music21.note.Rest(quarterLength = silence))

            else:
                s_array.append(music21.note.Note(midi_note[i], quarterLength = time))
        
            
        s_array.append(music21.note.Note(midi_note[-1]))
                  
        
        #print(s_array)
        self.s.append(s_array)
        
        
        for n in self.s.notes:
            if n.pitch.accidental.name == "natural":
                n.pitch.accidental.name = "none"
        
        key=self.s.analyze('key')
        self.s.finalBarline = 'final'
    
        self.s.insert(0, music21.metadata.Metadata())        
        self.s.metadata.title = self.name
        self.s.metadata.composer = ''
        
        #s.append(music21.key.KeySignature(3))
        output = sys.path[-1] + "/samples/output/"
     
        output = output.replace("\\","/")
        self.s.write(fp = output + self.name+'.png', fmt = 'musicxml.png')
        self.s.write(fp = output + 'PDFcreate.pdf', fmt = 'musicxml.pdf')
        #self.s.write(fp = output + 'outputfile.mp3', fmt = 'musicxml.png')
        
        self.s.write("midi", output + "music21.mid")
        
        
