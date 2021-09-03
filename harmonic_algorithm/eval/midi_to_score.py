import music21


def main_converter(name):
    input_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/samples/output/music21.mid"
    #input_file = "E:/UMSA/0Tesis2/TEMAS MUSICALES FINALES/Suzuki violin 1/14 Minuet_2 2.mid"
    #input_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/mir_eval/clarinete/Nueva carpeta/9 Perpetual Motion.mid"
    file = music21.converter.parse(input_file)
    components = []
    for element in file.recurse():
        es = str(element)

        if (es[0:13] == "<music21.note"):
            components.append(element)
 
    s = music21.stream.Stream()
    Violin = music21.instrument.Piano()
    Violin.midiChannel=0
    s.append(Violin)
    s.insert(0, music21.metadata.Metadata())

    count = 0
    duration = 0
    file1 = open("E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/mir_eval/clarinete/"+name+"_estimated.txt","w")
    #file1 = open("E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/mir_eval/piano/"+name+".txt","w")
    #file1 = open("E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/mir_eval/clarinete/"+name+".txt","w")
    for note in components:
        
        if (count >= 0):
            
            ant_duration = duration
            duration += note.duration.quarterLength
            if(str(note) != 'StringInstrument' and str(note) != "C major"):
                
                if(note.isNote):
                    #print(ant_duration, " ", duration, " ", note.pitch.frequency)

                    
                    text = str(ant_duration) + "   " + str(duration) + "   " + str(note.pitch.frequency) + "\n"
                    file1.write(text)
                elif(note.isRest):
                    #print(ant_duration, " ", duration, " ", note.duration.type)
                    '''
                    text = str(ant_duration) + "   " + str(duration) + "   " + str(0) + "\n"
                    file1.write(text)
                    '''                    
            
        s.append(note)
        count = count + 1

    file1.close()
    
'''
name = ""
main_converter(name)
'''
