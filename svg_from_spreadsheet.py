import pandas as pd
import svgwrite
import sys

def create_svg_from_spreadsheet(excel_path, width, height, svg_path): 
    # Load the spreadsheet
    df = pd.read_excel(excel_path, engine='openpyxl')

    # Normalize the amplitude data
    min_val = df.min().min()
    max_val = df.max().max()
    df_normalized = (df - min_val) / (max_val - min_val)

    # Create an SVG drawing
    dwg = svgwrite.Drawing(svg_path, profile='tiny')

    # Define artboard dimensions and bar width
    artboard_width = width 
    artboard_height = height 
    bar_width = artboard_width / len(df.columns)

    # Define gradient fill for bars
    gradient = dwg.linearGradient(start=(0, 0), end=(0, 1))
    gradient.add_stop_color(0, 'black')
    gradient.add_stop_color(1, 'white')
    dwg.defs.add(gradient)

    # Draw bars for each column of normalized amplitude data
    for i, column in enumerate(df_normalized.columns):
        x_pos = i * bar_width * 0.19
        for j, value in enumerate(df_normalized[column]):
            bar_height = value * artboard_height
            y_pos = artboard_height - bar_height
            dwg.add(dwg.rect(insert=(x_pos, y_pos), size=(bar_width, bar_height), fill=gradient.get_paint_server()))

    # Save the SVG file
    dwg.save()

    print(f"The SVG file has been created as {svg_path}")

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) != 5:
        print("Usage: python script.py <excel_path> <width> <height> <svg_path>")
        sys.exit(1)

    excel_path = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    svg_path = sys.argv[4]
    create_svg_from_spreadsheet(excel_path, width, height, svg_path)

