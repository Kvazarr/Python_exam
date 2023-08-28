import os
import random
import time
import datetime
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
        priority_case = input("Enter choice the priority of your case: 1.High;\t2.Low;\n>>>")
        description_case = input("Enter the description of your case: ")
        data_case = create_data()
        
        if priority_case == '1':
            priority_case = 'High'
        elif priority_case == '2':
            priority_case = 'Low'
        else:
            priority_case = 'Indeterminate'

        id = random.randint(100000, 999999)
        id = check_id(id)
        dates = [id, name_case, priority_case, description_case, data_case]

        writer = csv.writer(file)
        writer.writerow(dates)

        os.system("clear")
        print("/// Your scheduled case has been successfully created in the \"Show to-do list\" section!")
        time.sleep(3)


def create_data():
    cycles = False
    hour = 24

    while cycles != True:
        os.system("clear")
        try:
            year = int(input("Date and time by which you must complete the case: \nEnter the year: "))

            if year >= 2023 and year <= 2100:
                while cycles != True:
                    try:
                        month = int(input("Enter the month: "))

                        if month >= 1 and month <=12:
                            while cycles != True:
                                try:
                                    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: #31
                                        day = int(input("Enter the day: "))

                                        if day >= 1 and day <= 31:
                                            selected_time = datetime.datetime(year, month, day, hour)
                                            return selected_time
                                        else:
                                            os.system("clear")
                                            print(">>>Error! Enter the correct day within a radius of 1 to 31...")
                                            time.sleep(2.5)
                                    elif month == 4 or month == 6 or month == 9 or month == 11: #30
                                        day = int(input("Enter the day: "))

                                        if day >=1 and day <= 30:
                                            selected_time = datetime.datetime(year, month, day, hour)
                                            return selected_time
                                        else:
                                            os.system("clear")
                                            print(">>>Error! Enter the correct day within a radius of 1 to 30...")
                                            time.sleep(2.5)
                                    else: #28
                                        day = int(input("Enter the day: "))

                                        if day >= 1 and day <= 28:
                                            selected_time = datetime.datetime(year, month, day, hour)
                                            return selected_time
                                        else:
                                            os.system("clear")
                                            print(">>>Error! Enter the correct day within a radius of 1 to 28...")
                                            time.sleep(2.5)
                                except ValueError:
                                    os.system("clear")
                                    print(">>>Error! The time of day should only consist of numbers...")
                                    time.sleep(2.5)
                        else:
                            os.system("clear")
                            print(">>>Error! Enter the correct month...")
                            time.sleep(2)
                    except ValueError:
                        os.system("clear")
                        print(">>>Error! The time of month should only consist of numbers...")
                        time.sleep(2.5)
            else:
                os.system("clear")
                print(">>>Error! Enter the correct year...")
                time.sleep(2)
        except ValueError:
            os.system("clear")
            print(">>>Error! The time of year should only consist of numbers...")
            time.sleep(2.5)


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
