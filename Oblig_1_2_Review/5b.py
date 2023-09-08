import numpy as np

def generate_tone(frequency, duration, rate):
    t = np.linspace(0, duration, int(rate*duration), endpoint=False)
    tone = np.sin(2*np.pi*frequency*t)
    return tone

### Løsning 1: Den enkleste:
# Set opp kjente lister og verdier
frekvens = [392, 0, 587, 0, 494, 0, 494, 0, 392]
varighet = [0.9, 0.1, 0.9, 0.1, 0.4, 0.1, 0.4, 0.1, 0.9]
sample_rate = 8000

# Initialiserer en tom array
melody = []

# Genererer tonene og legger dem til i melodien
for i in range(len(frekvens)):
    tone = generate_tone(frekvens[i], varighet[i], sample_rate)
    melody = np.concatenate((melody, tone))

### Løsning 2: Zip versjonen
frekvens = [392, 0, 587, 0, 494, 0, 494, 0, 392]
varighet = [0.9, 0.1, 0.9, 0.1, 0.4, 0.1, 0.4, 0.1, 0.9]
sample_rate = 8000

melody = []

for Hz, s in zip(frekvens, varighet):
    tone = generate_tone(Hz, s, sample_rate)
    melody = np.concatenate((melody, tone))

### Løsning 3: Faktisk løsning
sample_rate = 8000

total_length = 0.9+0.1+0.9+0.1+0.4+0.1+0.4+0.1+0.9 # Seconds
melody = np.zeros(int(total_length*sample_rate))

melody[0:int(0.9*sample_rate)]=generate_tone(392, 0.9, sample_rate)
melody[int(1.0*sample_rate):int(1.9*sample_rate)]=generate_tone(587, 0.9, sample_rate)
melody[int(2.0*sample_rate):int(2.4*sample_rate)]=generate_tone(494, 0.4, sample_rate)
melody[int(2.5*sample_rate):int(2.9*sample_rate)]=generate_tone(494, 0.4, sample_rate)
melody[int(3.0*sample_rate):int(3.9*sample_rate)]=generate_tone(392, 0.9, sample_rate)












### BEGIN HIDDEN TESTS

fs_test = 8000

N_test = len(melody)
assert 3*fs_test < N_test <= 4*fs_test, f"Array melody has lenght {N_test}, which does not match intended lenght of melody"


t_test = np.linspace(0, N_test/fs_test, N_test, endpoint=False)
freq_sequence = np.outer(np.array([392, 587, 494, 392]), np.ones(fs_test))
freq_sequence = freq_sequence.reshape((1,-1))[0]

tone_demod_sum = np.abs(np.sum(melody*np.exp(2j*np.pi*freq_sequence[0:N_test]*t_test)))
assert tone_demod_sum > N_test/4, f"Grading error: correct order of frequences not detected."
### END HIDDEN TESTS
