from storage import new_subject, Subject
from utility import num_input
from tabulate import tabulate

def planner(choice : int):
    
    if choice==5:
        return False
    
    register = {
        1 : add_subject,
        2 : log_hours,
        3 : view_summary,
        4 : delete_subject,
        9 : print_data
    }
    return register[choice]()

def add_subject():
    print("\n----- ADD SUBJECT -----\n")
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
    print("\n----- LOG HOURS -----\n")

    # Get and print list of subjects
    subjects = Subject.data
    print("Subjects :")
    list_of_subjects = []

    for index, subject in enumerate(subjects):
        list_of_subjects.append([index, subject.get("subject_name")])

    print(tabulate(list_of_subjects, headers=["Index", "Subject Name"], tablefmt="grid"))

    # Get choice of subject to log hours for
    subj_index = num_input("Enter index of subject : ")
    log = num_input("Enter hours to log : ")

    # Update and write the new_data (log hours)
    Subject.update_log_hrs(subj_index, log)
    
def print_data():
    print(Subject.data)


def view_summary():
    pass

def delete_subject():
    print("\n----- DELETE SUBJECT -----\n")

    # Get and print list of subjects
    subjects = Subject.data
    print("Subjects :")
    list_of_subjects = []

    for index, subject in enumerate(subjects):
        list_of_subjects.append([index, subject.get("subject_name")])

    print(tabulate(list_of_subjects, headers=["Index", "Subject Name"], tablefmt="grid"))  

    subj_index = num_input("Enter index of subject : ")
    
    Subject.subject_delete(subj_index)

if __name__=="__main__":
    planner()