import openpyxl
import os
from polyline_script import make_polyline

def new_line_appender(new_line, svg_file_path):
    with open(svg_file_path, 'a') as file:
        file.write(new_line + '\n')

def generate_column_names(n):
    columns = []
    for i in range(1, n + 1):
        column_name = ''
        while i > 0:
            i, remainder = divmod(i - 1, 26)
            column_name = chr(65 + remainder) + column_name
        columns.append(column_name)
    return columns

def create_svg_from_spreadsheet(svg_file_path, file_path, column_size=800):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    begin_svg = f'<svg width="{column_size}" height="800" style="transform: rotate(90deg);" xmlns="http://www.w3.org/2000/svg"> <defs> <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%"> <stop offset="1%" style="top-color:rgb(205,255,225);stop-opacity:.15" /> <stop offset="9%" style="top-color:rgba(5,5,225,.6);stop-opacity:.25" /> <stop offset="10%" style="stop-color:rgb(255,5,5);stop-opacity:.35" /> <stop offset="100%" style="stop-color:rgb(0,5,0);stop-opacity:.7" /> </linearGradient> </defs> '
    end_svg = '</svg>'

    column_names = generate_column_names(column_size)
    if os.path.exists(svg_file_path):
        os.remove(svg_file_path)
    new_line_appender(begin_svg, svg_file_path)

    # NOTE: Animation effect parameters can be tweaked:
    # - Animation duration: dur="30s" below
    # - Morph intensity: polyline_script.py make_polyline() with is_animation=True uses 1.5x horizontal amplitude (vs 4x normal)
    # - Vertical spacing: multiplier parameter (1.25 for normal, 6.25 for animation creates dramatic stretching)
    # - Easing: keySplines values control the animation curve
    for name in column_names:
        polyline_coordinates = [cell.value for cell in sheet[name]]
        polyline_list = make_polyline(polyline_coordinates, multiplier=1.25, is_animation=False, peak_multiplier=-35)
        to_coords = make_polyline(polyline_coordinates, multiplier=1.25, is_animation=True, peak_multiplier=40)
        path_element = f'<path fill="url(#grad1)" stroke-width="0" d="M{polyline_list}">'
        animate_element = (
            f'<animate attributeName="d" dur="15s" values="M{polyline_list};M{to_coords};M{polyline_list}" '
            f'fill="freeze" repeatCount="indefinite" keyTimes="0;0.5;1" keySplines="0.42 0 0.58 1;0.42 0 0.58 1" calcMode="spline" />'
        )
        new_line_appender(path_element + animate_element + '</path>', svg_file_path)

    new_line_appender(end_svg, svg_file_path)
