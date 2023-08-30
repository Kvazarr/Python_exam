import os
import time
from create import create_case
from remove import remove_case
from edit import edit_case
from search import search_case
from show import show_case


def menu(cycles):
    while cycles != True:
        try:
            os.system("clear")
            choice = int(input("""//// Hi. It's a "To-do List" manager app ////\n//Choose what you want to do today:
            \n1. Add a case;\n2. Remove a case;\n3. Edit a case;\n4. Search for case by: ;\n5. Show to-do list;\n0. Exit;\n>>> """))

            if choice == 1:
                create_case()
            elif  choice == 2:
                remove_case()
            elif choice == 3:
                edit_case()
            elif choice == 4:
                search_case()
            elif choice == 5:
                show_case()
            elif choice == 0:
                os.system("clear")
                print("/// Bye. Come again! ///")
                time.sleep(2)
                cycles = True
        except ValueError:
            os.system("clear")
            print("Error! Make the right choice...")
            time.sleep(2)
