import librosa

# Load the audio file
audio_file = librosa.load("askinolayim.mp3")

# Extract the audio features
tempo = librosa.beat.tempo(audio_file, sr=44100)
pitch = librosa.feature.spectral_pitch(audio_file, sr=44100)[0]

# Increase the tempo
new_tempo = tempo * 1.2

# Change the pitch
new_pitch = pitch * 1.2

# Save the new audio file
librosa.output.write_wav("askin_olayim_nightcore.wav", audio_file, sr=44100, tempo=new_tempo, pitch=new_pitch)
