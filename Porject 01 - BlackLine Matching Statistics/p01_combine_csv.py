from pathlib import Path
import os
import pandas as pd

def main():
    print("Running - Combine Automatic and Manual Matching CSV files")

    this_dir=Path(__file__).resolve().parent
    # print (this_dir)

    # -----------------------------------------------------------------------
    #   combine automatic matching csv files into one csv file
    output_csv=os.path.join(this_dir, "01_automatic_matching.csv")
    sub_folder="02 - Automatic Matching Data"
    work_folder=os.path.join(this_dir, sub_folder)
    #print(work_folder)
    csv_files=list(Path(work_folder).glob("*.csv"))

    combined_csv=[]

    for file in csv_files:
        df=pd.read_csv(file)
        combined_csv.append(df)

    combined_df=pd.concat(combined_csv, ignore_index=True)
    combined_df.to_csv(output_csv, index=False)

    #----------------------------------------------------------------------
    #   combine manual matching csv files into one csv file
    output_csv=os.path.join(this_dir, "02_manual_matching.csv")
    sub_folder="03 - Manual Matching Data"
    work_folder=os.path.join(this_dir, sub_folder)
    print(work_folder)
    csv_files=list(Path(work_folder).glob("*.csv"))

    combined_csv=[]

    for file in csv_files:
        df=pd.read_csv(file)
        combined_csv.append(df)

    combined_df=pd.concat(combined_csv, ignore_index=True)
    combined_df.to_csv(output_csv, index=False)

    #-----------------------------------------------------------------------
    output_csv=os.path.join(this_dir, "03_all_matching.csv")

    list_df=[]

    df_automatic=pd.read_csv(os.path.join(this_dir, "01_automatic_matching.csv"))
    df_automatic_simple=df_automatic[["ID", "Matched By"]].copy()
    df_automatic_simple["Method"]="Automatic"
    list_df.append(df_automatic_simple)

    df_manual=pd.read_csv(os.path.join(this_dir, "02_manual_matching.csv"))
    df_manual_simple=df_manual[["ID", "Matched By"]].copy()
    df_manual_simple["Method"]="Manual"
    list_df.append(df_manual_simple)

    combined_df=pd.concat(list_df, ignore_index=True)
    combined_df.to_csv(output_csv, index=False)

    print("Finished - Combine Automatic and Manual Matching CSV files")

if __name__ == "__main__":
    main()