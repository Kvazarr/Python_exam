import os
import time
import datetime
import calendar
import csv


def show_case():
    cycles = False
    cycles2 = False

    while cycles != True:
        os.system("clear")
        with open('quest.csv', 'r') as file:
            reader = csv.reader(file)
            counter = 1

            while cycles2 != True:
                try:
                    choise = int(input("/// Show the cases for:\n1. A  day;\n2. A week;\n3. A month;\n4. A year;\n>>>"))
                except ValueError:
                    os.system("clear")
                    print(">>>Error! Make the right choise... ")
                    time.sleep(2)
                    os.system("clear")

                if choise == 1:
                    os.system("clear")
                    today = datetime.date.today()
                    for i in reader:
                        if i[4] == str(today):
                            print(f"[{counter}] {i};")
                            counter += 1
                    cycles2 = True
                elif choise == 2:
                    os.system("clear")
                    show_week()
                    cycles2 = True
                elif choise == 3:
                    os.system("clear")
                    show_month()
                    cycles2 = True
                elif choise == 4:
                    os.system("clear")
                    show_year()
                    cycles2 = True
                else:
                    os.system("clear")
                    print(">>>Error! Make the right choise...")
                    time.sleep(2)
                
        print("===============================================")
        try:
            next_step = int(input("/// Enter a choice about what you'd like to do next: \n1. Sort by priority;\n2. Sort by date;\n0. Exit;\n>>>"))

            if next_step == 1:
                sort_priority()
                cycles = True
            elif next_step == 0:
                cycles = True
        except ValueError:
            os.system("clear")
            print(">>>Error! Enter the correct choice...")
            time.sleep(2)
            


def show_week():
    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        today = datetime.date.today()
        counter = 1

        start_of_weak = today - datetime.timedelta(days=today.weekday())
        end_of_weak = start_of_weak + datetime.timedelta(days=6)

        for i in reader:
            temp = i[4]
            if temp >= str(start_of_weak) and  temp <= str(end_of_weak):
                print(f"[{counter}] {i};")
                counter += 1



def show_month():
    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        today = datetime.date.today()
        counter =  1

        start_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        for i in reader:
            temp = i[4]
            if temp >= str(start_of_month) and temp <= str(last_day_of_month):
                print(f"[{counter}] {i};")
                counter += 1


def show_year():
    with open('quest.csv', 'r') as file:
        reader = csv.reader(file)
        today_year = datetime.datetime.now().year
        counter = 1

        for i in reader:
            temp = i[4]
            data_year = datetime.datetime.strptime(temp, '%Y-%m-%d')
            if data_year.year == today_year:
                print(f"[{counter}] {i};")
                counter += 1
            
            



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