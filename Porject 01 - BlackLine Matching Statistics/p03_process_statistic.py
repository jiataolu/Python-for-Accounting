from pathlib import Path
import os
import pandas as pd
import numpy as np

def main():
    print("Running - Statistic of matching result")
    this_dir=Path(__file__).resolve().parent

    output_csv=os.path.join(this_dir, "99_matching_statistics.csv")


    #-------------------------------------------------------------------------
    # 01 process GL data
    df_gl=pd.read_csv(os.path.join(this_dir, "11_source_data_GL.csv"))

    df_sta = pd.DataFrame({'BU_GL': df_gl['BU_GL'].unique()
    })

    # to count new rule matching
    new_counts =df_gl[df_gl['By New Rule'] == 'New Rule'].groupby('BU_GL')['By New Rule'].count().reset_index(name='GL_New')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['GL_New'] = df_sta['GL_New'].fillna(0).astype(int)

    # to count GL Posting
    total_counts = (df_gl.groupby('BU_GL').size().reset_index(name='GL_Total'))
    df_sta = df_sta.merge(total_counts, on='BU_GL', how='left')
    df_sta['GL_Total'] = df_sta['GL_Total'].fillna(0).astype(int)

    # to count Automatic matching
    new_counts =df_gl[df_gl['Method'] == 'Automatic'].groupby('BU_GL')['Method'].count().reset_index(name='GL_Automatic')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['GL_Automatic'] = df_sta['GL_Automatic'].fillna(0).astype(int)

    # to count Manual matching
    new_counts =df_gl[df_gl['Method'] == 'Manual'].groupby('BU_GL')['Method'].count().reset_index(name='GL_Manual')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['GL_Manual'] = df_sta['GL_Manual'].fillna(0).astype(int)

    # to count open posting
    missing_counts = (df_gl[df_gl['Method'].isna()].groupby('BU_GL').size().reset_index(name='GL_Open'))
    df_sta = df_sta.merge(missing_counts, on='BU_GL', how='left')
    df_sta['GL_Open'] = df_sta['GL_Open'].fillna(0).astype(int)


    #-------------------------------------------------------------------------
    #02 to process Bank data

    df_gl=pd.read_csv(os.path.join(this_dir, "12_source_data_Bank.csv"))

    # df_sta = pd.DataFrame({'BU_GL': df_gl['BU_GL'].unique()})

    # to count new rule matching
    new_counts =df_gl[df_gl['By New Rule'] == 'New Rule'].groupby('BU_GL')['By New Rule'].count().reset_index(name='Bank_New')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['Bank_New'] = df_sta['Bank_New'].fillna(0).astype(int)

    # to count Bank Posting
    total_counts = (df_gl.groupby('BU_GL').size().reset_index(name='Bank_Total'))
    df_sta = df_sta.merge(total_counts, on='BU_GL', how='left')
    df_sta['Bank_Total'] = df_sta['Bank_Total'].fillna(0).astype(int)

    # to count Automatic matching
    new_counts =df_gl[df_gl['Method'] == 'Automatic'].groupby('BU_GL')['Method'].count().reset_index(name='Bank_Automatic')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['Bank_Automatic'] = df_sta['Bank_Automatic'].fillna(0).astype(int)

    # to count Manual matching
    new_counts =df_gl[df_gl['Method'] == 'Manual'].groupby('BU_GL')['Method'].count().reset_index(name='Bank_Manual')
    df_sta = df_sta.merge(new_counts, on='BU_GL', how='left')
    df_sta['Bank_Manual'] = df_sta['Bank_Manual'].fillna(0).astype(int)

    # to count open posting
    missing_counts = (df_gl[df_gl['Method'].isna()].groupby('BU_GL').size().reset_index(name='Bank_Open'))
    df_sta = df_sta.merge(missing_counts, on='BU_GL', how='left')
    df_sta['Bank_Open'] = df_sta['Bank_Open'].fillna(0).astype(int)


    #-------------------------------------------------------------------------
    # 03 to calculate matching rate
    df_sta['GL_New Ratio'] = (df_sta['GL_New'] / df_sta['GL_Total']) 
    df_sta['GL_Automatic Ratio'] = (df_sta['GL_Automatic'] / df_sta['GL_Total'])
    df_sta['GL_Manual Ratio'] = (df_sta['GL_Manual'] / df_sta['GL_Total'])
    df_sta['GL_Open Ratio'] = (df_sta['GL_Open'] / df_sta['GL_Total'])
    df_sta['Bank_New Ratio'] = (df_sta['Bank_New'] / df_sta['Bank_Total'])
    df_sta['Bank_Automatic Ratio'] = (df_sta['Bank_Automatic'] / df_sta['Bank_Total'])
    df_sta['Bank_Manual Ratio'] = (df_sta['Bank_Manual'] / df_sta['Bank_Total'])
    df_sta['Bank_Open Ratio'] = (df_sta['Bank_Open'] / df_sta['Bank_Total'])


    #-------------------------------------------------------------------------
    # Change order of columns
    new_order_col=["GL_Total", "GL_New", "GL_New Ratio", "GL_Automatic", "GL_Automatic Ratio", "GL_Manual", "GL_Manual Ratio", "GL_Open", "GL_Open Ratio","Bank_Total", "Bank_New", "Bank_New Ratio", "Bank_Automatic", "Bank_Automatic Ratio", "Bank_Manual", "Bank_Manual Ratio", "Bank_Open", "Bank_Open Ratio"]

    df_sta=df_sta[["BU_GL"] + new_order_col]



    df_sta.to_csv(output_csv, index=False)
    print("Finished - Statistic of matching result")

if __name__ == "__main__":
    main()