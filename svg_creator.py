import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import pandas as pd
import svgwrite

def create_svg():
    # Load the WAV file
    sample_rate, data = wavfile.read('input.wav')

    # Ensure the data is mono
    if len(data.shape) > 1:
        data = data.mean(axis=1)

    # Define parameters
    fft_size = 1024
    num_windows = 512
    window_size = len(data) // num_windows

    # Initialize list to store amplitude data
    amplitudes_list = []

    # Process each window
    for i in range(num_windows):
        start_index = i * window_size
        end_index = start_index + window_size
        window_data = data[start_index:end_index]

        # Apply FFT to the windowed data
        fft_result = fft(window_data, n=fft_size)

        # Calculate amplitudes
        amplitudes = np.abs(fft_result)

        # Store the results
        amplitudes_list.append(amplitudes[:fft_size//2])

    # Convert list to DataFrame
    df_amplitudes = pd.DataFrame(amplitudes_list).T

    # Normalize the amplitude data
    min_val = df_amplitudes.min().min()
    max_val = df_amplitudes.max().max()
    df_amplitudes_normalized = (df_amplitudes - min_val) / (max_val - min_val)

    # Reverse sort each column to rotate the image 180º
    df_amplitudes_normalized = df_amplitudes_normalized.iloc[::-1]

    # Create an SVG drawing
    dwg = svgwrite.Drawing('output.svg', profile='tiny')

    # Define artboard dimensions and bar width
    artboard_width = 1000
    artboard_height = 500
    bar_width = artboard_width / num_windows

    # Define gradient fill for bars
    gradient = dwg.linearGradient(start=(0, 0), end=(0, 1))
    gradient.add_stop_color(0, 'black')
    gradient.add_stop_color(1, 'white')
    dwg.defs.add(gradient)

    # Draw bars for each column of normalized amplitude data
    for i, column in enumerate(df_amplitudes_normalized.columns):
        x_pos = i * bar_width * 0.19
        for j, value in enumerate(df_amplitudes_normalized[column]):
            bar_height = value * artboard_height
            y_pos = artboard_height - bar_height
            dwg.add(dwg.rect(insert=(x_pos, y_pos), size=(bar_width, bar_height), fill=gradient.get_paint_server()))

    # Save the SVG file
    dwg.save()

    print("The SVG file has been created as output.svg.")
