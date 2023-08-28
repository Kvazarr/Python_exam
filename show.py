import os
import time
import csv


def show_case():
    cycles = False

    while cycles != True:
        os.system("clear")
        with open('quest.csv', 'r') as file:
            reader = csv.reader(file)
            counter = - 1

            for i in reader:
                counter += 1
                print(f"[{counter}] {i};")
        
        print("===============================")
        try:
            next_step = int(input("/// Enter a choice about what you'd like to do next: \n1. Sort by priority;\n2. Sort by date;\n0. Exit;\n>>>"))

            if next_step == 1:
                sort_priority()
                cycles = True
        except ValueError:
            os.system("clear")
            print(">>>Error! Enter the correct choice...")
            time.sleep(2)
            


def sort_priority():
    main_sorted = []
    sorted_high = []
    sorted_low = []
    sorted_indeterminate = []

    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)

        for i in reader:
            if i[2] == 'High':
                sorted_high.append(i)
            elif i[2] == 'Low':
                sorted_low.append(i)
            elif i[2] == 'Indeterminate':
                sorted_indeterminate.append(i)

        main_sorted = sorted_high + sorted_low + sorted_indeterminate

    with open('quest.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(main_sorted)

    os.system("clear")
    print("/// Your to-do list has been successfully sorted by priority!")
    time.sleep(2.5)