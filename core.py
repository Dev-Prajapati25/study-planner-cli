from storage import new_subject

def planner(choice : int):
    
    if choice==5:
        return False
    
    register = {
        1 : add_subject,
        2 : log_hours,
        3 : view_summary,
        4 : delete_subject,
    }
    return register[choice]()

def add_subject():
    print("----- ADD SUBJECT -----")
    subj_name = input("Enter Subject Name : ")
    while True:
        goal_hrs = input("Enter goal hours (enter for default '0'): ")
        try:
            if goal_hrs == "":
                goal_hrs = 0
            else:
                goal_hrs = int(goal_hrs)
        except ValueError:
            print("Enter valid number for goal hours !")
        else:
            return new_subject(subj_name, goal_hrs)

def log_hours():
    pass

def view_summary():
    pass

def delete_subject():
    pass

if __name__=="__main__":
    planner()