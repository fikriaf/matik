import pyaudio
import wave
import speech_recognition as sr

# fungsi untuk merekam suara
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("rekaman.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

# fungsi untuk melakukan speech recognition
def recognize_audio():
    r = sr.Recognizer()

    filename = "rekaman.wav"
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)

    try:
        text = r.recognize_sphinx(audio_data)
        print(f'Teks hasil transkripsi: {text}')
    except sr.UnknownValueError:
        print('Speech Recognition tidak dapat mengenali audio')
    except sr.RequestError as e:
        print(f'Terdapat error pada request ke Speech Recognition; {e}')

# menjalankan program
while True:
    record_audio()
    recognize_audio()