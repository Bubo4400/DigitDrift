import pandas as pd 
import os         

def openFile(fileName):
    if not os.path.isfile(fileName):
        raise ValueError(f"{fileName} does not exist")
    return pd.read_csv(fileName, on_bad_lines='skip')

def getDatasetInfo(df) -> list:
    print("Column Names: ")
    colNames = df.columns.tolist()
    sizeCol = len(colNames)
    for i in range(sizeCol):
        print(f"{i}: {colNames[i]}")

    print(f"{sizeCol}: Exit")
    print()

    col = input("Column number: ")
    if col == str(sizeCol):
        return None, None, None
    if int(col) > sizeCol:
        clearScreen()
        return getDatasetInfo(df)

    zeroIn = input("Ignore numbers between 0 and 1 (if not take the first non 0 digit)[Y/n]:
    zero = True
    if zeroIn == n or zeroIn == N:
        zero = False
    return df[colNames[int(col)]].tolist(), colNames[int(col)], zero
