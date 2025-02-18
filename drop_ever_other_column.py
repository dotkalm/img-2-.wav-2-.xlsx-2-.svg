import sys
import pandas as pd

def drop_every_other_column(file_path):
    # Read the spreadsheet
    df = pd.read_excel(file_path)
    
    # Drop every other column
    df = df.iloc[:, ::2]
    
    # Save the modified spreadsheet
    df.to_excel(file_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python drop_every_other_column.py <path_to_spreadsheet>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    drop_every_other_column(file_path)
