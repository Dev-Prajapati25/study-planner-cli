from core import planner

def main():
    print_menu()
    choice = get_choice()

    planner(choice)


def print_menu():
    menu = """
===== STUDY PLANNER =====
1. Add Subject
2. Log Study Hours
3. View Summary
4. Delete Subject
5. Save & Exit
"""
    print(menu)

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