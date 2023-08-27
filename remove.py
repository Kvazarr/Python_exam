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
            id_to_remove = int(input("/// Enter the ID of the case you want to delete:\n>>>"))
            id_juxtaposition(id_to_remove)
        except ValueError:
            os.system("clear")
            print(f">>>Error! Remember, ID should only consist of numbers.....")
            time.sleep(2)


def id_juxtaposition(id_to_remove):
     