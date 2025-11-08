import os
from core import planner

menu = """
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit
"""

def main():
    if not os.path.exists("data.json"):
        try:
            with open("data.json", "x") as file:
                pass
        except FileExistsError:
            pass
    
    while True:
        print(menu)
        choice = get_choice()
        callee_func = planner(choice)
        if callee_func == 5:
            print("Exiting Study Planner")
            break

def get_choice():
    while True:
        try:
            choice = int(input("Enter Choice : "))
        except ValueError:
            print("Enter valid choice !!")
        except Exception as e:
            print(f"Error occurred : {e}")
        else:
            return choice

if __name__=="__main__":
    main()