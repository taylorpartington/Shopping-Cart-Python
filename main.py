import csv
import sys
import time

import converter
import data_analysis


def applyAction(choice, data,filename):
    if choice == 'a':
        appendCSV(data,filename)
    elif choice == 'l':
        loadCSV(filename)
    elif choice == 'q':
        quitAction()
    else:
        print("error")

def appendCSV(data,filename):
    item = getUserString("What Item are you Adding?: ")
    quantity = getUserString("How many of that item?: ")
    price = getUserString("How much is it?(ex 1.99): ")
    data.append([item,quantity,price])
    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)
        csvfile.close()

def loadCSV(filename):
    analysis = data_analysis.DataAnalysis(filename)
    analysis.StatisticalOutput()
    print("Statistical Analysis Document Created (analysis.txt)")

def formatMenu():
     menu = ['\n' + 'What would you like to do?', '[a] Append Shopping List',
            '[l] Load Shopping List', '[q] Quit']
     return menu

def formatMenuPrompt():
    prompt = 'Enter an option: '
    return prompt

def quitAction():
    print("The program has been terminated.")
    time.sleep(1.5)
    sys.exit(0)

def getUserString(string):
    user_string = input(string)
    while user_string == '':
        user_string = input(string)
        user_string = user_string.strip()
    return user_string


def main():
    filename =getUserString("What is the filename?: ")
    csvconvert = converter.CSVConverter(filename)
    data = csvconvert.GetData()
    if not data:
        create_option = getUserString("Would you like to create it? (y/n): ")
        while True:
            if create_option == "y":
                csvconvert.CreateData()
                break
            elif create_option == "n":
                quitAction()
            else:
                print("Invaild")
    else:
        while True:
            menu = formatMenu()
            for options in menu:
                print(options)
            prompt = formatMenuPrompt()
            choice = getUserString(prompt)
            applyAction(choice,data,filename)


if __name__ == "__main__":
    main()