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
    }
    return register[choice]()

def add_subject():
    print("\n----- ADD SUBJECT -----\n")
    subj_name = input("Enter Subject Name(enter to cancel) : ")
    if subj_name == "": return
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
        list_of_subjects.append([index, subject.get("subject_name"), subject.get("goal_hrs") ])

    print(tabulate(list_of_subjects, headers=["Index", "Subject Name", "Goal Hours"], tablefmt="grid"))

    # Get choice of subject to log hours for
    subj_index = num_input("Enter index of subject (enter to skip) : ", skip=True)
    log = num_input("Enter hours to log (enter to skip) : ", skip=True)

    if subj_index is not None and log is not None:
        # Update and write the new_data (log hours)
        Subject.update_log_hrs(subj_index, log)
    


def view_summary():
    subjects = Subject.data
    bars = []

    print("\n----- VIEW SUMMARY -----\n")
    # Prepare progress bars
    for subject in subjects:
        if not subject["goal_hrs"] == 0:
            fraction = int((subject["hours"]/subject["goal_hrs"])*10)
            notFraction = 10-fraction

            bar = "██"
            notBar = "░░"
            progress_bar = f"{subject["subject_name"]} :{subject["hours"]}/{subject["goal_hrs"]}\n\t[{bar*4}{notBar*6}] {fraction*10}% Done\n"
            bars.append(progress_bar)
        else:
            bars.append(f"{subject["subject_name"]} :{subject["hours"]}/{subject["goal_hrs"]}\n\tGoal Hours not present\n")
    
    # Print Progress bars
    for bar in bars:
        print(bar)
        print("- - - - - - - - - - - - - -")


def delete_subject():
    print("\n----- DELETE SUBJECT -----\n")

    # Get and print list of subjects
    subjects = Subject.data
    print("Subjects :")
    list_of_subjects = []

    for index, subject in enumerate(subjects):
        list_of_subjects.append([index, subject.get("subject_name")])

    print(tabulate(list_of_subjects, headers=["Index", "Subject Name"], tablefmt="grid"))  

    subj_index = num_input("Enter index of subject (enter to skip) : ", skip=True)
    
    if subj_index is not None:
        Subject.subject_delete(subj_index)

if __name__=="__main__":
    planner()