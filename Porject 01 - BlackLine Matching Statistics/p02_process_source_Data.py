from pathlib import Path
import os
import pandas as pd
import numpy as np


def main():
    print("Running - Read and Process GL & Bank Source Data for mapping")
    this_dir=Path(__file__).resolve().parent

    new_rule="A M:1 CC, Acct, Amt, Posting Date (Grouped on Amt, Date & Doc Type)"

    df_mapping=pd.read_csv(os.path.join(this_dir, "03_all_matching.csv"))

    #-------------------------------------------------------------------------
    # 01    Process GL Data

    #selected_columns=["Match"]
    selected_columns=["Match", "Match Date", "Company Code", "Profit Center", "Account Number", "Posting Date", "Period", "Document Type", "Document Num", "Assignment", "Text", "Transaction Amount", "Transaction Currency", "Local Amount", "Local Currency", "Document Header Text", "User Name", "Document Date", "Reference", "CC Account", "Matching Flag", "Match Set Mapping"]


    output_csv=os.path.join(this_dir, "11_source_data_GL.csv")

    sub_folder="01 - BlackLine Source Data"
    work_folder=os.path.join(this_dir, sub_folder)
    # find file with keyword "Cash_SAP_GL_ALL" in the sub_folder
    file_path = next(Path(work_folder).rglob("*Cash_SAP_GL_ALL*"), None)
    print(file_path)
    df_gl=pd.read_csv(os.path.join(work_folder, file_path))

    # fiter GL data only for mapping
    df_gl = df_gl[(df_gl['Matching Flag'] == 'Y') & (df_gl['Match Set Mapping'] == 'Cash_ALL')]


    df_gl=df_gl[selected_columns].copy()


    df_work=df_gl.merge(df_mapping[["ID", "Matched By", "Method"]], left_on="Match", right_on="ID", how="left")

    df_work["By New Rule"]=np.where(df_work["Matched By"]==new_rule, "New Rule", "")

    df_work["BU_GL"]=df_work["Company Code"].astype(int).astype(str) + "_" + df_work['Account Number'].astype(int).astype(str)
                                    

    #df_work["Method"].astype(str).str.strip()
    #df_work['Method'].replace(['', 'nan', 'NaN', 'None'], 'Open')

    df_work.to_csv(output_csv, index=False)
    #print(df_work)

    #-------------------------------------------------------------------------
    # 02    Process Bank Data

    # selected_columns=["Match"]
    selected_columns=["Match", "Match Date", "Bank Identifier", "FileId Number", "Transaction Date", "Bank Acct Number", "Currency", "Txn Type Code", "Signed BAI Amount", "Comment", "Company Code", "Account Number", "Matching Flag", "Match Set Mapping", "Accounting ERP"]


    output_csv=os.path.join(this_dir, "12_source_data_Bank.csv")

    sub_folder="01 - BlackLine Source Data"
    work_folder=os.path.join(this_dir, sub_folder)
    # find file with keyword "Cash_SAP_GL_ALL" in the sub_folder
    file_path = next(Path(work_folder).rglob("*Cash_BAI_ALL*"), None)
    print(file_path)
    df_gl=pd.read_csv(os.path.join(work_folder, file_path))

    # fiter GL data only for mapping
    df_gl = df_gl[(df_gl['Matching Flag'] == 'Y') & (df_gl['Match Set Mapping'] == 'Cash_ALL')]


    df_gl=df_gl[selected_columns].copy()


    df_work=df_gl.merge(df_mapping[["ID", "Matched By", "Method"]], left_on="Match", right_on="ID", how="left")

    df_work["By New Rule"]=np.where(df_work["Matched By"]==new_rule, "New Rule", "")

    df_work["Company Code"]=df_work["Company Code"].fillna(9999999)
    df_work["Account Number"]=df_work["Account Number"].fillna(9999999)


    df_work["BU_GL"]=df_work["Company Code"].astype(int).astype(str) + "_" + df_work['Account Number'].astype(int).astype(str)                                

    #df_work["Method"].astype(str).str.strip()
    #df_work['Method'].replace(['', 'nan', 'NaN', 'None'], 'Open')

    df_work.to_csv(output_csv, index=False)
    print("Finished - Read and Process GL & Bank Source Data for mapping")


if __name__ == "__main__":
    main()