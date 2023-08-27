import os
import random
import csv


def create_case():
    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        header = ["ID", "Name", "Priority", "Description", "Data"]

        for i in reader:
            if i[0] == "ID":
                break
            else:
                with open('quest.csv', 'w') as file:
                    file.truncate(0)
                    writer = csv.writer(file)
                    writer.writerow(header)

    with open('quest.csv', 'a') as file:
        os.system("clear")
        name_case = input("Enter the name of your case: ")
        priority_case = input("Enter the priority of your case: ")
        description_case = input("Enter the description of your case: ")
        data_case = input("Enter the date and time of execution of your case: ")

        id = random.randint(100000, 999999)
        id = check_id(id)
        dates = [id, name_case, priority_case, description_case, data_case]

        writer = csv.writer(file)
        writer.writerow(dates)


def check_id(id):
    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        list_id = []
        check = False
        temp = 0

        for i in reader:
            if i[0] == 'ID':
                continue
            list_id.append(i[0])

    while check != True:
        for i in list_id:
            if i == str(id):
                temp += 1

        if temp == 1:
            id = random.randint(1000000, 9999999)
            return id
        else:
            check = True
            return id
