import os
import time
import random
import csv
from create import create_data, check_id

def edit_case():
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
            id_to_edit = int(input("/// Enter the ID of the case you want to edit(0 for exit):\n>>>"))

            if id_to_edit == 0:
                return

            id_juxtaposition(id_to_edit)
            cycles = True
        except ValueError:
            os.system("clear")
            print(f">>>Error! Remember, ID should only consist of numbers...")
            time.sleep(2)



def id_juxtaposition(id_to_edit):
    os.system("clear")
    main_rows = []
    editing_row = []    
    keeping_rows = []
    counter = 0
    cycles = 0

    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        
        for i in reader:
            if i[0] == str(id_to_edit):
                editing_row.append(i)
                editing_row = editing_case()
                main_rows = keeping_rows + editing_row
                counter += 1
                break
            else:
                keeping_rows.append(i)

    if counter == 1:
        with open('quest.csv', 'r') as file:
            reader_second = csv.reader(file)

            for i in reader_second:
                try:
                    if i[0] == str(main_rows[cycles][0]):
                        cycles += 1
                        continue
                    elif i[0] == str(id_to_edit):
                        cycles += 1
                        continue
                    else:
                        main_rows.append(i)
                        cycles += 1
                except IndexError:
                    main_rows.append(i)
                    
        with open('quest.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(main_rows)

        os.system("clear")
        print(f"/// Your case with the ID: [{id_to_edit}] has been successfully edited!")
        time.sleep(3)
    else:
        print(f">>>The search engine was unable to locate a case with this ID: [{id_to_edit}].")
        time.sleep(3)


def editing_case():
    temp_row = []
    editing_row = []

    new_name_case = input("Enter the name of your case: ")
    new_priority_case = input("Enter choice the priority of your case: 1.High;\t2.Low;\n>>>")
    new_description_case = input("Enter the description of your case: ")
    new_data_case = create_data()

    if new_priority_case == '1':
        new_priority_case = 'High'
    elif new_priority_case == '2':
        new_priority_case = 'Low'
    else:
        new_priority_case = 'Indeterminate'

    id = random.randint(100000, 999999)
    id = check_id(id)

    temp_row = [[id, new_name_case, new_priority_case, new_description_case, new_data_case]]

    return temp_row