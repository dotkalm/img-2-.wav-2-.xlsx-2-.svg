import sys
import os
from datetime import datetime
from img2wav import img2wav
from windowing_fft_to_spreadsheet import process_image_to_fft_excel 
from spreadsheet_opener import create_svg_from_spreadsheet 

now = datetime.now()
day_of_week = now.strftime("%A")  # Full weekday name, e.g., 'Monday'
calendar_day = now.day            # Day of the month, e.g., 12
month = now.strftime("%B")        # Full month name, e.g., 'February'
year = now.year                   # Year, e.g., 2025
fft_size = 512 
windows = 450 

def convert_image_to_wav(output_file, input_image, samplerate, bandwidth):
    img2wav(
        images=[input_image],
        output=output_file,
        samplerate=samplerate,
        bandwidth=bandwidth,
        delay=200,
        frequency=17000,
    )
    base_name = os.path.splitext(os.path.basename(output_file))[0]
    spreadsheet_output_file = os.path.join("./spreadsheets/", f"{base_name}.xlsx")
    print(f"now Converting {output_file} to {spreadsheet_output_file} with FFT size {fft_size} and {windows} windows")
    process_image_to_fft_excel(output_file, spreadsheet_output_file, fft_size, windows)

    svg_output_file = os.path.join("./svg/", f"{base_name}.svg")

    print(f"now Converting {spreadsheet_output_file} to {svg_output_file} with column size {windows}")
    create_svg_from_spreadsheet(svg_output_file, spreadsheet_output_file, windows)

if __name__ == "__main__":
    input_image = '' 

    print(f"args len {len(sys.argv)}")

    if len(sys.argv) != 2:
        print("Usage: python script.py <input_image>")
        sys.exit(1)
    else:
        input_image = sys.argv[1]

    samplerate = 66000
    bandwidth = 35000
    output_file = None

    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    if not output_file:
        base_name = os.path.splitext(os.path.basename(input_image))[0]
        output_file = os.path.join("./audio/", f"{base_name}_{day_of_week}_{calendar_day}_{month}_{year}.wav")

    if len(sys.argv) > 5:
        samplerate = int(sys.argv[3])

    if len(sys.argv) > 6:
        bandwidth = int(sys.argv[4])

    convert_image_to_wav(output_file, input_image, samplerate, bandwidth)
