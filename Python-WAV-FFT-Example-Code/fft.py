from __future__ import print_function
import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt

fs_rate, signal = wavfile.read("test17.wav")
print(signal)
print("Frequency sampling", fs_rate)
l_audio = len(signal.shape)
print("Channels", l_audio)
if l_audio == 2:
    signal = signal.sum(axis=1) / 2
N = signal.shape[0]
print("N : " + N)
print("Complete Samplings N", N)
secs = N / float(fs_rate)
print("secs", secs)
# sample interval in time
Ts = 1.0/fs_rate
print("Timestep between samples Ts", Ts)
# time vector as scipy arange field / numpy.ndarray
t = scipy.arange(0, secs, Ts)
FFT = abs(scipy.fft(signal))
FFT_side = FFT[range(N//2)]  # one side FFT range
freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
fft_freqs = np.array(freqs)
freqs_side = freqs[range(N//2)]  # one side frequency range
fft_freqs_side = np.array(freqs_side)
# plt.subplot(311)
# p1 = plt.plot(t, signal, "g")  # plotting the signal
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.subplot(312)
# p2 = plt.plot(freqs, FFT, "r")  # plotting the complete fft spectrum
#plt.xlabel('Frequency (Hz)')
#plt.ylabel('Count dbl-sided')
# plt.subplot(313)
# plotting the positive fft spectrum
p3 = plt.plot(freqs_side, abs(FFT_side), "b")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Count single-sided')
plt.show()