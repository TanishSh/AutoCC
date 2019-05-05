"""
Main file
"""

import speech_recognition as sr
import pyaudio
import wave
import soundcard as sc
import threading
import socket
import pyaudio
import wave
import display


import json

def open_json():
    with open('AutoCC-9917161c773d.json') as json_file:
        data = json.load(json_file)
        str_data = json.dumps(data)
        #print(data)
        return str_data


#Settings
def record_system():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 7
    WAVE_OUTPUT_FILENAME = "file.wav"

    recording = True

    p = pyaudio.PyAudio()

    for i in range(0, p.get_device_count()):
        print(i, p.get_device_info_by_index(i)['name'])
    # print("Recording Audio")

    # device_index = int(input('Device index: '))
    device_index = 2

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=device_index)

    print("*recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # var 'data' holds all the volume?
    print("*done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("*closed")

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("Done here")



def recognize_speech():

    test = sr.AudioFile("file.wav")
    r = sr.Recognizer()
    with test as source:
        audio = r.record(source)
        # r.recognize_google_cloud(audio, open_json())
    return r.recognize_google_cloud(audio, open_json())

if __name__ == '__main__':
    #gobject.threads_init()
    # Kick off queue thread to print text to screen
    print("kicking off thread")
    qthread = threading.Thread(target=display.init, args=())
    print("here1")
    # qthread.setDaemon(True)
    qthread.start()
    print("here2")
    # Infinite Loop:
    while (1):
        print("here3")
        record_system()  # Record system audio output for 5secs
        print("recording done")
        # out = recognize_speech()
        print("speech to text done")
        # print(out)
        display.queue()


