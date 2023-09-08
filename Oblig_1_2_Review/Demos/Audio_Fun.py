import numpy as np
from IPython.display import Audio

notes = ([" ","E","E"," ","E"," ","C","E"," ","G"," ","g"," ","C"," ","g"," ","e"," ","a"," ","h"," ","b","a","g","E","G",
          " ","A","F","G"," ","E"," ","C","D","h"," ","C"," ","g"," ","e"," ","a"," ","h"," ","b","a","g","E","G"," ","A",
          "F","G"," ","E"," ","C","D","h"," "," ","G","J","F","S"," ","E"," ","t","a","C"," ","a","C","D"," ","G","J","F",
          "S"," ","E"," ","V"," ","V","V"," "," ","G","J","F","S"," ","E"," ","t","a","C"," ","a","C","D"," ","U"," ","D",
          " ","C"," "," ","G","J","F","S"," ","E"," ","t","a","C"," ","a","C","D"," ","G","J","F","S"," ","E"," ","V"," ",
          "V","V"," "," ","G","J","F","S"," ","E"," ","t","a","C"," ","a","C","D"," ","U"," ","D"," ","C"," "])
beats = ([1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,1,2,1,1,1,1,2,1,
          1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,
          6,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,6])

notes_to_frequencies = {
    'c': 262, 'd': 294, 'e': 330, 'f': 349,
    'g': 392, 't': 415, 'a': 440, 'b': 466,
    'h': 494, 'C': 523, 'D': 587, 'S': 622,
    'E': 659, 'F': 698, 'J': 740, 'G': 784,
    'A': 880, 'V': 1047, 'U': 622 
}

tones_data = []

for  note, beat in zip(notes, beats):
    duration = beat/10
    if note == ' ':
        tones_data.append((0, duration))
    else:
        tones_data.append((notes_to_frequencies.get(note, 0), duration))
    tones_data.append((0, duration/10))

sample_rate = 44100
melody = []

def generate_tone(frequency, duration, rate):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    fade_duration = (0.2 * duration) 
    fade_in = np.linspace(0, 1, int(rate * fade_duration), endpoint=False)
    fade_out = np.linspace(1, 0, int(rate * fade_duration), endpoint=False)
    fundamental_tone = np.sin(2 * np.pi * frequency * t)
    harmonic1 = np.sin(2 * np.pi * 3 * frequency * t * 5)
    harmonic2 = np.sin(2 * np.pi * 4 * frequency * t * 2)
    harmonic3 = np.sin(2 * np.pi * 4 * frequency * t * 1)
    harmonic4 = 0.5 * np.sin(2 * np.pi * 3 * frequency * t)
    harmonic5 = 0.2 * np.sin(2 * np.pi * 4 * frequency * t)
    harmonic6 = 0.1 * np.sin(2 * np.pi * 4 * frequency * t)
    tone = fundamental_tone + harmonic1 + harmonic2 + harmonic3 + harmonic4 + harmonic5 + harmonic6
    echo_delay = int(rate * 0.1)
    echo = np.zeros_like(tone)
    echo[echo_delay:] = tone[:-echo_delay]
    tone_with_echo = tone + 0.2 * echo

    tone_with_echo[:len(fade_in)] *= fade_in
    tone_with_echo[-len(fade_out):] *= fade_out

    return tone_with_echo

for freq, duration in tones_data:
    tone = generate_tone(freq, duration, sample_rate)
    melody = np.concatenate((melody, tone))
    
audio = Audio(melody/(max(abs(melody))*16), rate=sample_rate, normalize=False)
with open('./Mario.wav', 'wb') as f:
    f.write(audio.data)