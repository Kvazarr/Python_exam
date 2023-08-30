import os
import time
import datetime
import csv


def search_case():
    cycles = False

    while cycles != True:
        with open('quest.csv', 'r') as file:
            os.system("clear")
            reader = csv.reader(file)
            counter = 1

            try:
                choise = int(input("1. By name;\n2. By priority;\n3. By date;\n>>>"))
            except ValueError:
                os.system("clear")
                print(">>>Error! Make the right choise...")
                time.sleep(2)


            if choise == 1:
                search_by_name = input("/// Enter the name of case you want to find:\n>>>")
                os.system("clear")
                print("================================")

                for i in reader:
                    if search_by_name.lower() == i[1].lower():
                        print(f"[{counter}] {i};")
                        counter += 1
                
                print("================================")
                input("/// Press enter to continue...")

                cycles = True
            elif choise  == 2:
                search_by_priority = input("/// Enter the priority of case you want to find:\n>>>")
                os.system("clear")
                print("================================")

                for i in  reader:
                    if search_by_priority.lower() == i[2].lower():
                        print(f"[{counter}] {i};")
                        counter += 1

                print("================================")
                input("/// Press enter to continue...")

                cycles = True
            elif choise == 3:
                while cycles != True:
                    os.system("clear")

                    try:        
                        year = int(input("Enter the year >>> "))
                        month = int(input("Enter the month >>> "))
                        day = int(input("Enter the day >>> "))
                        date = datetime.date(year, month, day)
                        os.system("clear")
                        print("================================")

                        for i in reader:
                            if str(date) == i[4]:
                                print(f"[{counter}] {i};")
                                counter += 1

                        print("================================")
                        input("/// Press enter to continue...")

                        cycles = True
                    except ValueError:
                        os.system("clear")
                        print(">>>Error! Remember, dates should only consist of numbers...")
                        time.sleep(2.5)
            else:
                os.system("clear")
                print(">>>Error! Make the right choise...")