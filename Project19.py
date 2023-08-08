import pyaudio
import numpy as np

CHUNK_SIZE = 1024  # количество сэмплов в буфере
FORMAT = pyaudio.paInt16  # формат сэмплов (16 бит)
CHANNELS = 1  # количество каналов (моно)
RATE = 44669  # частота дискретизации (Гц)
GAIN = 3  # усиление звука

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK_SIZE
)

while True:
    # читаем сэмплы из буфера микрофона
    data = stream.read(CHUNK_SIZE)
    # преобразуем сэмплы в массив numpy
    samples = np.frombuffer(data, dtype=np.int16)
    # усиливаем звук
    samples = samples * GAIN
    # преобразуем массив numpy обратно в байтовый поток
    data = samples.tobytes()
    # отправляем усиленный звук на динамики
    stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()
