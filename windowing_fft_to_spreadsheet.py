import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import pandas as pd
import sys
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import ColorScaleRule

def process_image_to_fft_excel(audio_path, output_excel, fft_size, num_windows):
    # Load the WAV file
    sample_rate, data = wavfile.read(audio_path)

    # Ensure the data is mono
    if len(data.shape) > 1:
        data = data.mean(axis=1)

    # Define parameters
    window_size = len(data) // num_windows

    # Initialize lists to store frequency and amplitude data
    frequencies_list = []
    amplitudes_list = []

    # Process each window
    for i in range(num_windows):
        start_index = i * window_size
        end_index = start_index + window_size
        window_data = data[start_index:end_index]
        
        # Apply FFT to the windowed data
        fft_result = fft(window_data, n=fft_size)
        
        # Calculate frequencies and amplitudes
        frequencies = np.fft.fftfreq(fft_size, d=1/sample_rate)
        amplitudes = np.abs(fft_result)
        
        # Store the results
        frequencies_list.append(frequencies[:fft_size//2])
        amplitudes_list.append(amplitudes[:fft_size//2])

    # Convert lists to DataFrame
    df_frequencies = pd.DataFrame(frequencies_list).T
    df_amplitudes = pd.DataFrame(amplitudes_list).T

    # Normalize the amplitude data
    min_val = df_amplitudes.min().min()
    max_val = df_amplitudes.max().max()
    df_amplitudes_normalized = (df_amplitudes - min_val) / (max_val - min_val)

    # Reverse sort each column to rotate the image 180º
    df_amplitudes_normalized = df_amplitudes_normalized.iloc[::-1]

    # Write the DataFrame to an Excel file
    with pd.ExcelWriter(output_excel) as writer:
        df_amplitudes_normalized.to_excel(writer, sheet_name='Amplitudes', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <audio_path> <output_excel> <fft_size> <num_windows>")
        sys.exit(1)

    audio_path = sys.argv[1]
    output_excel = sys.argv[2]
    fft_size = int(sys.argv[3])
    num_windows = int(sys.argv[4])
    process_image_to_fft_excel(audio_path, output_excel, fft_size, num_windows)
