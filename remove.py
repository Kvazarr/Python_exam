import os
import time
import csv


def remove_case():
    cycles = False

    while cycles != True:
        os.system("clear")
        with open('quest.csv', 'r') as file:
            reader = csv.reader(file)
            counter = - 1

            for i in reader:
                    counter += 1
                    print(f"[{counter}] {i};")

        try:
            print("================================================")
            id_to_remove = int(input("/// Enter the ID of the case you want to delete(0 for exit):\n>>>"))

            if id_to_remove == 0:
                return

            id_juxtaposition(id_to_remove)
            cycles = True
        except ValueError:
            os.system("clear")
            print(f">>>Error! Remember, ID should only consist of numbers...")
            time.sleep(2)


def id_juxtaposition(id_to_remove):
    os.system("clear")
    row_to_remove = []
    row_to_keep = []
    counter = 0

    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        
        for i in reader:
            if i[0] == str(id_to_remove):
                row_to_remove = i
                counter += 1
            else:
                row_to_keep.append(i)

        if counter == 1:
            print(f"/// Your case with the ID: [{id_to_remove}] has been successfully deleted!")
            time.sleep(3)
        else:
            print(f">>>The search engine was unable to locate a case with this ID: [{id_to_remove}].")
            time.sleep(3)
            
    with open('quest.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(row_to_keep)