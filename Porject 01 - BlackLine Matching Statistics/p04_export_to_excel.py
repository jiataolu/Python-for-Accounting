from pathlib import Path
import os
import pandas as pd
from openpyxl.styles import Font

def main():
    print("Running - Export Matching Statistics to Excel")
    this_dir=Path(__file__).resolve().parent


    df = pd.read_csv(os.path.join(this_dir, '99_matching_statistics.csv'))

    with pd.ExcelWriter('99_matching_statistics.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
        ws = writer.sheets['Sheet1']
        red_font = Font(color='FF0000')
        
        for col in ['GL_New', 'GL_New Ratio', 'Bank_New', 'Bank_New Ratio']:
            if col in df.columns:
                col_idx = df.columns.get_loc(col) + 1
                for row in range(1, len(df) + 2):
                    ws.cell(row=row, column=col_idx).font = red_font

        for col in ['GL_New Ratio', 'GL_Automatic Ratio', 'GL_Manual Ratio', 'GL_Open Ratio', 'Bank_New Ratio', 'Bank_Automatic Ratio', 'Bank_Manual Ratio', 'Bank_Open Ratio']:
            if col in df.columns:
                col_idx = df.columns.get_loc(col) + 1
                for row in range(1, len(df) + 2):
                    ws.cell(row=row, column=col_idx).number_format = '0.00%'


    print("Finished - Export Matching Statistics to Excel")

if __name__ == "__main__":
    main()