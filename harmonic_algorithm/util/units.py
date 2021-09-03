import numpy as np


def convertTime(time, fromUnit, to, **kwargs):
    if fromUnit == "frames":
        if to == "frames":
            pass
        elif to == "samples":
            time *= kwargs['hopSize']
        elif to == "seconds":
            time *= float(kwargs['hopSize']) / float(kwargs['sampleRate'])
        else:
            raise ValueError("'to' unit not valid")
    elif fromUnit == "samples":
        if to == "frames":
            time /= float(kwargs['hopSize'])
        elif to == "samples":
            pass
        elif to == "seconds":
            time /= float(kwargs['sampleRate'])
        else:
            raise ValueError("'to' unit not valid")
    elif fromUnit == "seconds":
        if to == "frames":
            time *= float(kwargs['sampleRate']) / float(kwargs['hopSize'])
        elif to == "samples":
            time *= float(kwargs['sampleRate'])
        elif to == "seconds":
            pass
        else:
            raise ValueError("'to' unit not valid")
    else:
        raise ValueError("'from' unit not valid")

    return time


def Hz_to_MIDI(frequency, A4=440):
    ref = 69 - 12 * np.log2(A4)
    midi = np.zeros(frequency.shape)
    index = np.where(frequency >= 20)
    midi[index] = 12 * np.log2(frequency[index]) + ref
    return midi

def Hz_to_MIDI2(frequency, A4=440):
    
    midi = np.zeros(frequency.shape)
    index = np.where(frequency >= 20)

    midi[index] = (np.log2(frequency[index]/A4) * 12) + 69
    return midi


def convertFreq(frequency, fromUnit, to, A4=440):
    ref = 69 - 12 * np.log2(A4)
    fromUnit = fromUnit.lower()
    to = to.lower()

    if fromUnit == "hz":
        if to == "hz":
            pass
        elif to == "midi":
            freq = []
            for f in frequency:
                if f < 20:
                    freq.append(0)
                else:
                    freq.append(12 * np.log2(f) + ref)
            frequency = np.array(freq)
        else:
            raise ValueError("'to' unit not valid")
    elif fromUnit == "midi":
        if to == "hz":
            frequency = np.power(2, (frequency - ref) / 12.0)
        elif to == "midi":
            pass
        else:
            raise ValueError("'to' unit not valid")
    else:
        raise ValueError("'from' unit not valid")

    return frequency


def dB_to_power(db):
    return 10.0 ** (float(db) / 10.0)
