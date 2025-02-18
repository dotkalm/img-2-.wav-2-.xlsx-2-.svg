import sys
import pandas as pd

def drop_every_other_column(file_path, rows_to_drop=400):
    # Read the spreadsheet
    df = pd.read_excel(file_path)
    
    # Drop every other column
    df = df.iloc[rows_to_drop:]
    # Save the modified spreadsheet
    df.to_excel(file_path, index=False)
    # Drop the first 400 rows

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python drop_every_other_column.py <path_to_spreadsheet>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    rows_to_drop = sys.argv[2]
    drop_every_other_column(file_path, int(rows_to_drop))
