import pyaudio
import wave

# konfigurasi pyaudio
chunk = 1024  # jumlah frame yang dibaca setiap kali
sample_format = pyaudio.paInt16  # format bit depth dari sampel audio
channels = 2  # jumlah channel (mono/stereo)
fs = 44100  # sampling rate (frekuensi sampling)

# inisialisasi PyAudio
p = pyaudio.PyAudio()

# mulai rekaman
print("Merekam...")
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
frames = []
for i in range(0, int(fs / chunk * 5)):  # merekam selama 5 detik
    data = stream.read(chunk)
    frames.append(data)

# menghentikan rekaman
stream.stop_stream()
stream.close()
p.terminate()
print("Rekaman selesai.")

# menyimpan rekaman ke file audio
wf = wave.open("rekaman.wav", "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()
print("Rekaman disimpan sebagai rekaman.wav.")
