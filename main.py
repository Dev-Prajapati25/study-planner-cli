"""
Entry Point file
"""

import os
from core import planner
from storage import Subject
from utility import num_input


menu = """
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit
"""

def main():

    # Create 'data.json' if it does not exists
    if not os.path.exists("data.json"):
        try:
            with open("data.json", "x") as file:
                pass
        except FileExistsError:
            pass

    # Fetch existing data from 'data.json' into Subject.data
    Subject.prepare_data()
    
    # App loop
    while True:
        print(menu)
        choice = num_input("Enter choice : ", skip=False)
        core_func_response = planner(choice)
        if core_func_response == False:
            print("Exiting Study Planner")
            break
            



if __name__=="__main__":
    main()