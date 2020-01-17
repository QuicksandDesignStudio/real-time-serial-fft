from os import listdir
from os.path import isfile, join
import requests
import json
import sys
import numpy as np
from matplotlib import pyplot as plt

samplePath = "samples"
API_ENDPOINT_MAKEWAV = "http://localhost:5000/fft/api/v1.0/make_wave"
API_ENDPOINT_GETWAV = "http://localhost:5000/fft/api/v1.0/get_wave"
API_ENDPOINT_DOFFT = "http://localhost:5000/fft/api/v1.0/do_fft"


def main():
    if(sys.argv[1] == "getwaves"):
        r = requests.get(url=API_ENDPOINT_GETWAV)
        allWaves = json.loads(r.text)
        print(allWaves)
    elif(sys.argv[1] == "getFFT"):
        payload = '400HZ.wav'
        r = requests.post(url=API_ENDPOINT_DOFFT, data=payload)
        returnLoad = json.loads(r.text)
        plotfft(returnLoad)

    else:
        f = open("samples/sample.txt")
        payload = {'file_name': 'gube.wav',
                   'sampling_rate': '1100', 'samples': f.read()}
        r = requests.post(url=API_ENDPOINT_MAKEWAV, data=json.dumps(payload))
        print(r.text)


def plotfft(fftdata):
    timeVector = np.array(fftdata["timeVector"])
    signal = np.array(fftdata["signal"])
    fullPhaseFrequencies = np.array(fftdata["fullPhaseFrequencies"])
    fullPhaseFFT = np.array(fftdata["fullPhaseFFT"])
    positiveFrequencies = np.array(fftdata["positiveFrequencies"])
    positiveFFT = np.array(fftdata["positiveFFT"])

    # plotting the signal
    plt.subplot(311)
    p1 = plt.plot(timeVector, signal, "g")
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # plotting the complete fft spectrum
    plt.subplot(312)
    p2 = plt.plot(fullPhaseFrequencies, fullPhaseFFT, "r")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count dbl-sided')

    # plotting the positive fft spectrum
    plt.subplot(313)
    p3 = plt.plot(positiveFrequencies, positiveFFT, "b")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count single-sided')
    plt.show()


if __name__ == "__main__":
    main()