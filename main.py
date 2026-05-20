from src import benfordsLaw, loadDataset, plot
import math
import sys
import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Missing file name argument")

    fileName = sys.argv[1]
    file = loadDataset.openFile(fileName)

    run = True
    while run:
        clearScreen()
        print(f"File {fileName} opened")

        dataset, col, zero = loadDataset.getDatasetInfo(file)
        if dataset == None:
            break

        data = benfordsLaw.probOfDigits(dataset, zero)

        select = True
        while select:
            clearScreen()
            print(f"{col} selected with zero {('activated', 'deactivated')[not zero]}")
            print("0: Draw plot")
            print("1: Check Benfords Law")
            print("2: Toggle zero Feature")
            print("3: Change column")
            print("4: Exit")
            print()

            options = input("Select option: ")
            match options:
                case "0":
                    plot.processPlot(data)

                case "1":
                   benfordsLaw.BenfordLaw(data) 

                case "2":
                    zero = not zero
                    data = benfordsLaw.probOfDigits(dataset,  zero)

                case "3":
                    select = False

                case "4":
                    select = False
                    run = False

    clearScreen()
