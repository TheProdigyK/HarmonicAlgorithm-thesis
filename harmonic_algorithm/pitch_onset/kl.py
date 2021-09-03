from __future__ import division
import numpy as np
from scipy.signal import get_window
from tqdm import tqdm

def nextpow2(x):
    return 2**np.ceil(np.log2(x))

class PitchGenerate(object):

        
    # lista ordenada de frecuencias utilizadas para encontrar el tono más cercano
    
    # las frecuencias oscilan entre 65 Hz y 2100 Hz.
    frequencies = np.array([2**(n/12.0)*440 for n in range(-33,28)])


    # lista ordenada de nombre de tono y octavas, que corresponden al
    
    
    notes = [
        {'pname': 'C', 'oct': 2},
        {'pname': 'C#', 'oct': 2},
        {'pname': 'D', 'oct': 2},
        {'pname': 'D#', 'oct': 2},
        {'pname': 'E', 'oct': 2},
        {'pname': 'F', 'oct': 2},
        {'pname': 'F#', 'oct': 2},
        {'pname': 'G', 'oct': 2},
        {'pname': 'G#', 'oct': 2},
        {'pname': 'A', 'oct': 2},
        {'pname': 'A#', 'oct': 2},
        {'pname': 'B', 'oct': 2},
        {'pname': 'C', 'oct': 3},
        {'pname': 'C#', 'oct': 3},
        {'pname': 'D', 'oct': 3},
        {'pname': 'D#', 'oct': 3},
        {'pname': 'E', 'oct': 3},
        {'pname': 'F', 'oct': 3},
        {'pname': 'F#', 'oct': 3},
        {'pname': 'G', 'oct': 3},
        {'pname': 'G#', 'oct': 3},
        {'pname': 'A', 'oct': 3},
        {'pname': 'A#', 'oct': 3},
        {'pname': 'B', 'oct': 3},
        {'pname': 'C', 'oct': 4},
        {'pname': 'C#', 'oct': 4},
        {'pname': 'D', 'oct': 4},
        {'pname': 'D#', 'oct': 4},
        {'pname': 'E', 'oct': 4},
        {'pname': 'F', 'oct': 4},
        {'pname': 'F#', 'oct': 4},
        {'pname': 'G', 'oct': 4},
        {'pname': 'G#', 'oct': 4},
        {'pname': 'A', 'oct': 4},
        {'pname': 'A#', 'oct': 4},
        {'pname': 'B', 'oct': 4},
        {'pname': 'C', 'oct': 5},
        {'pname': 'C#', 'oct': 5},
        {'pname': 'D', 'oct': 5},
        {'pname': 'D#', 'oct': 5},
        {'pname': 'E', 'oct': 5},
        {'pname': 'F', 'oct': 5},
        {'pname': 'F#', 'oct': 5},
        {'pname': 'G', 'oct': 5},
        {'pname': 'G#', 'oct': 5},
        {'pname': 'A', 'oct': 5},
        {'pname': 'A#', 'oct': 5},
        {'pname': 'B', 'oct': 5},
        {'pname': 'C', 'oct': 6},
        {'pname': 'C#', 'oct': 6},
        {'pname': 'D', 'oct': 6},
        {'pname': 'D#', 'oct': 6},
        {'pname': 'E', 'oct': 6},
        {'pname': 'F', 'oct': 6},
        {'pname': 'F#', 'oct': 6},
        {'pname': 'G', 'oct': 6},
        {'pname': 'G#', 'oct': 6},
        {'pname': 'A', 'oct': 6},
        {'pname': 'A#', 'oct': 6},
        {'pname': 'B', 'oct': 6},
        {'pname': 'C', 'oct': 7}
    ]

    def __init__(self, **kwargs):
        # frecuencia fundamental mínima para detectar
        if 'min_f0' in kwargs:
            self._min_f0 = kwargs['min_f0']
        else:
            self._min_f0 = 65

        # frecuencia fundamental máxima para detectar
        if 'max_f0' in kwargs:
            self._max_f0 = kwargs['max_f0']
        else:
            self._max_f0 = 2100

        # longitud del marco de análisis
        if 'frame_len_sec' in kwargs:
            self._frame_len_sec = kwargs['frame_len_sec']
            if self._frame_len_sec != 0.046 and self._frame_len_sec != 0.093:
                raise ValueError('Analysis frame length must be 46ms or 93ms')
        else:
            self._frame_len_sec = 0.093

        if 'window_func' in kwargs:
            self._window_func = kwargs['window_func']
        else:
            self._window_func = 'hanning'

        # ancho de bin del espectro estimado del parcial
        # de los fundamentales detectados
        if 'partial_width' in kwargs:
            self._partial_width = kwargs['partial_width']
        else:
            self._partial_width = 10

        '''
        Derived parameters
        '''
        if self._frame_len_sec == 0.046:
            self._alpha = 27
            self._beta = 320
            self._d = 1.0
        else:
            self._alpha = 52
            self._beta = 320
            self._d = 0.89

    def __call__(self, x, fs):
        X = self._stft(x, fs)
        Y = self._spectral_whitening(X, fs)
        return self._iterative_est(Y, fs)

    def estimate_f0s(self, x, fs):
        X = self._stft(x, fs)

        # Blanquear espectralmente la señal para suprimir la información tímbrica
        Y = self._spectral_whitening(X, fs)

        # estimación iterativa de los períodos fundamentales en el archivo de audio
        f0_estimations = self._iterative_est(Y, fs)
        
        # obtener notas que correspondan a estas estimaciones de frecuencia
        notes = []
        for frame_ests in f0_estimations:
            notes.append([self._freq_to_note(f) for f in frame_ests])

        return f0_estimations, notes

    def _freq_to_note(self, freq):
        i_note = np.argmin(np.abs(PitchGenerate.frequencies-freq))
        return PitchGenerate.notes[i_note]

    def _stft(self, x, fs):
        '''
        transformada de Fourier de corto tiempo en la señal que en si es
         Hann con ventana y relleno de ceros al doble de su longitud.
         Hopsize = longitud de la ventana
        '''

        frame_len_samps = int(fs * self._frame_len_sec)             #O(1)
        win = get_window(self._window_func, frame_len_samps)        #O(1) la ventana de Hann es una formula sin bucles

        # zero-pad al doble de la longitud del marco frame
        K = int(nextpow2(2*frame_len_samps))                        #O(1)
        X = np.array([np.fft.fft(win*x[i:i+frame_len_samps], K) 
                     for i in range(0, len(x)-frame_len_samps, frame_len_samps)])   # O(n log(n) *  W)
        #O(n^2 log(n) + 3)
        return X

    def _spectral_whitening(self, X, fs, nu=0.33):
        '''
        Aplanado espectral ('blanqueamiento') de la señal de entrada dada en el dominio de frecuencia,
         para suprimir la información tímbrica.
   
        PARAMETROS
         ----------
         X (T, K): señal de entrada en el dominio de la frecuencia con tramas T y FFT de longitud K
         fs: frecuencia de muestreo de la señal de entrada
         nu (flotar): cantidad de blanqueamiento espectral
        '''

        T, K = X.shape              #O(1)
        nyquist_freq = fs/2         #O(1)
        nyquist_bin = K>>1          #O(1)

       
        # Calculo de las frecuencias centrales c_b (Hz) de las subbandas en la escala de la banda crítica
         # c_b = 229 * (10 ^ [(b + 1) /21.4] -1)
         # calculo de una subbanda por debajo y por encima del rango para obtener la cabeza y la cola
         # de frecuencias de las ventanas triangulares
        c = []      # frecuencia central de bandas criticas
        b = 0       # indice de bandas criticas
        while True:
            centre_freq = 229*(10**((b+1)/21.4)-1)
            if centre_freq < nyquist_freq:
                c.append(centre_freq)
                b += 1
            else:
                break

        c = np.asarray(c)
        c_bins = np.asarray(np.floor(c*K/fs), np.int)

        # coeficientes de compresión de subbanda -> gamma (K/2,)
        gamma = np.zeros([T, nyquist_bin])


        for b in range(1,len(c_bins)-1):
            H = np.zeros(nyquist_bin)

            left = c_bins[b-1]
            centre = c_bins[b]
            right = c_bins[b+1]

            # Construyendo la respuesta de potencia triangular para cada subbanda.
            H[left:centre+1] = np.linspace(0, 1, centre - left + 1)
            H[centre:right+1] = np.linspace(1, 0, right - centre + 1)

            # multiplicado por 2, ya que la energía es simétrica con respecto a la tasa de nyquist
            gamma[:,centre] = np.sqrt((2/K)*np.sum(H*(np.abs(X[:,:nyquist_bin])**2), axis=1))**(nu-1)
    
            # interpolar entre el bin central anterior y el bin central actual 
            #para cada marco STFT
            for t in range(T):
                gamma[t,left:centre] = np.linspace(gamma[t,left], gamma[t,centre], centre - left)

        # calcular el espectro blanqueado. Solo es necesario almacenar la mitad del espectro para el análisis.
        # dado que la energía del contenedor es simétrica con respecto a la frecuencia de nyquist
        Y = gamma * X[:,:nyquist_bin]

        return Y

    def _iterative_est(self, Y, fs):
        f0_estimations = []

        T = Y.shape[0]
        # ventana STFT
        for t in tqdm(range(T)):
            # espectro de magnitud residual del frame de análisis
            Y_t_R = np.abs(Y[t,:])

            # estimaciones de frecuencia fundamental para el frame actual
            f0_frame_estimations = []

            # realizar un seguimiento de las prominencias de las estimaciones del período en este frame
            S = -1
            salience_hats = []



            tau_hat, salience_hat, Y_t_D = self._search_smax(Y_t_R, fs, tau_prec=0.5) #n^3 *logn
            salience_hats.append(salience_hat)

            f0_frame_estimations.append(fs/tau_hat)
            f0_estimations.append(f0_frame_estimations)


            cur_S = self._calc_S(salience_hats)
            if cur_S <= S:
                break
            else:
                Y_t_R -= self._d*Y_t_D
                Y_t_R[Y_t_R < 0] = 0

                S = cur_S

        return f0_estimations

    def _calc_S(self, salience_hats, gamma=0.7):
        '''
        Calculamos una suma normalizada de prominencias para determinar 
        si es necesario buscar más frecuencias fundamentales en el espectro.
        '''

        j = len(salience_hats)
        S = sum(salience_hats)/(j**gamma)

        return S

    def _search_smax(self, Y_t_R, fs, tau_prec=1.0):
        Q = 0           # index de un nuevo block
        q_best = 0      # index del mejor block
       
        tau_low = [round(fs/self._max_f0)] # samples/cycle
        tau_up = [round(fs/self._min_f0)]  # samples/cycle
        smax = [0]

        while tau_up[q_best] - tau_low[q_best] > tau_prec:
            Q += 1
            tau_low.append((tau_low[q_best] + tau_up[q_best])/2)
            tau_up.append(tau_up[q_best])
            tau_up[q_best] = tau_low[Q]

            for q in [q_best, Q]:
                salience, _ = self._calc_salience(Y_t_R, fs, tau_low[q], tau_up[q])
                if q == q_best:
                    smax[q_best] = salience
                else:
                    smax.append(salience)

            q_best = np.argmax(smax)

        # período fundamental estimado del frame
        tau_hat = (tau_low[q_best] + tau_up[q_best])/2

        # calculamos el espectro del período fundamental detectado y los armónicos
        salience_hat, harmonics = self._calc_salience(Y_t_R, fs, tau_low[q_best], tau_up[q_best])
        K = len(Y_t_R)<<1
        Y_t_D = self._calc_harmonic_spec(fs, K, harmonics)

        return tau_hat, salience_hat, Y_t_D

    def _calc_salience(self, Y_t_R, fs, tau_low, tau_up):
        salience = 0

        tau = (tau_low + tau_up)/2
        delta_tau = tau_up - tau_low

         # calculamos el número de armónicos bajo la frecuencia nyquist
         # la siguiente declaración es equivalente a floor((fs/2) / fo)
        num_harmonics = int(np.floor(tau/2))

        # calcular todos los harmonic weights
        harmonics = np.arange(num_harmonics)+1
        g = (fs/tau_low + self._alpha) / (harmonics*fs/tau_up + self._beta)

        nyquist_bin = len(Y_t_R)
        K = nyquist_bin<<1
        lb_vicinity = K/(tau + delta_tau/2)
        ub_vicinity = K/(tau - delta_tau/2)

        harmonics = []
        for m in range(1,num_harmonics+1):
            harmonic_lb = round(m*lb_vicinity)
            harmonic_ub = min(round(m*ub_vicinity), nyquist_bin)
            harmonic_bin = np.argmax(Y_t_R[harmonic_lb-1:harmonic_ub]) + harmonic_lb-1
            harmonic_amp = Y_t_R[harmonic_bin]
            w_harmonic_amp = g[m-1] * harmonic_amp

            # guardar las propiedades de este período fundamental y los armónicos
            harmonics.append({'bin': harmonic_bin, 'amp': w_harmonic_amp})

            salience += w_harmonic_amp

        return salience, harmonics

    def _calc_harmonic_spec(self, fs, K, harmonics):
        nyquist_bin = K>>1
        # inicializar el espectro de armónicos detectados
        Y_t_D = np.zeros(nyquist_bin)

        # calculamos el espectro parcial para cada armónico

        frame_len_samps = int(fs * self._frame_len_sec)
        win = get_window(self._window_func, frame_len_samps) 
        window_spec = np.abs(np.fft.fft(win, K))
        partial_spectrum = np.hstack((window_spec[self._partial_width::-1],
                                    window_spec[1:self._partial_width+1]))
        # normalizamos el espectro
        partial_spectrum /= np.max(partial_spectrum)

        for h in harmonics:
            h_lb = max(0, h['bin']-self._partial_width)
            h_ub = min(nyquist_bin-1, h['bin']+self._partial_width)
            
            # traducimos el espectro de la función de ventana a la posición del armónico
            Y_t_D[h_lb:h_ub+1] = h['amp']*partial_spectrum[h_lb-h['bin']+self._partial_width:h_ub-h['bin']+self._partial_width+1]

        return Y_t_D

    def collapse_notes(self, notes):
        '''
        Contraemos notas consecutivas (notas que abarcan más de
        un marco de análisis).
        '''
        
        notes_c = []
        prev_frame = []
        for frame_n in notes:
            if len(frame_n) > 1:
                n_set = set([n['pname']+str(n['oct']) for n in frame_n])
                frame_n = [{'pname': n[:-1], 'oct': int(n[-1])} for n in n_set]
            
            if len(frame_n) != len(prev_frame):
                notes_c.append(frame_n)
            elif not np.all([n1['pname'] == n2['pname'] and n1['oct'] == n2['oct'] 
                            for n1,n2 in zip(prev_frame, frame_n)]):
                notes_c.append(frame_n)

            prev_frame = frame_n

        return notes_c


def estimate_multipitch(signal, sampleRate, polyphony_max=6):
    freq_est = PitchGenerate(max_poly=polyphony_max)
    f0_estimates, notes = freq_est.estimate_f0s(signal, sampleRate)
    #notes_c = freq_est.collapse_notes(notes)
    return f0_estimates
