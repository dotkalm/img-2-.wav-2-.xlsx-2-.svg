import openpyxl
import string

def read_cell(file_path, sheet_name, cell_reference):
    # Load the workbook and select the sheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    
    # Read the value from the specified cell
    cell_value = sheet[cell_reference].value
    return cell_value

# Example usage
file_path = 'spreadsheets/wed_angelsc.xlsx'
sheet_name = 'Amplitudes'
cell_reference = 'B1'

value = read_cell(file_path, sheet_name, cell_reference)
print(f'The value in cell {cell_reference} is: {value}')

def generate_column_names(n):
    columns = []
    for i in range(1, n + 1):
        column_name = ''
        while i > 0:
            i, remainder = divmod(i - 1, 26)
            column_name = chr(65 + remainder) + column_name
        columns.append(column_name)
    return columns

# Generate column names for 1023 columns
column_names = generate_column_names(1023)

# Print the column names
for name in column_names:
    print(name)