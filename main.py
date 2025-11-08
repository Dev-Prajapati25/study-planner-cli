"""
Entry Point file
"""

import os
from core import planner
from storage import Subject

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
        choice = num_input("Enter choice : ")
        core_func_response = planner(choice)
        if core_func_response == False:
            print("Exiting Study Planner")
            break
            

# Utility functions
def num_input(prompt:str) -> int:
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("Enter Valid Number")
        except Exception as e:
            print(f"Error occurred : {e}")
        else:
            return num

if __name__=="__main__":
    main()