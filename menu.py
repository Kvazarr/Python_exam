import os
import csv


def menu(exit):
    while exit != True:
        try:
            print("""/// Hi. It's a ""To-do List"" manager app ///\n\tChoose what you want to do today:
            \n\t\t\t1. Add a case;\t\t2. Remove a case;\n\t3. Edit a case;\t4.Search for case by: ;\t5. Show to-do list;""")
            break
        except ValueError:
            os.system("clear")
            print("Error! Make the right choice...")
