import librosa
import soundfile as sf
import os

# Generate pitch-shifted audio for a range of notes
def generate_pitch_shifted_notes(input_file, output_dir, octaves, sample_rate=44100):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the audio file
    y, sr = librosa.load(input_file, sr=sample_rate)

    # Define the semitone shifts for the specified octaves
    semitone_shifts = []
    for octave in octaves:
        for semitone in range(12):
            shift = 12 * (octave - 4) + semitone  # Octave shift + semitone offset
            semitone_shifts.append(shift)

    # Generate pitch-shifted files
    for shift in semitone_shifts:
        try:
            # Apply pitch shifting
            y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=shift)

            # Calculate the note name (optional for naming files)
            octave = 4 + shift // 12
            note_index = shift % 12
            notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            note_name = notes[note_index % 12]
            file_name = f"{note_name}{octave}.wav"

            # Save the pitch-shifted audio
            output_file = os.path.join(output_dir, file_name)
            sf.write(output_file, y_shifted, sr)
            print(f"Generated: {output_file}")
        except Exception as e:
            print(f"Error processing shift {shift}: {e}")

# Example usage
output_dir = 'notes'  # Replace with your desired output directory
input_file = 'music/314865__modularsamples__yamaha-cs-30l-straight-guitar-a4-straight-guitar-70-127.wav'  # Replace with your input file
generate_pitch_shifted_notes(input_file, output_dir, octaves=[4, 5, 6])
