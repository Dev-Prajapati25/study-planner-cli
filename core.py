def planner(choice : int):
    register = {
        1 : add_subject,
        2 : log_hours,
        3 : view_summary,
        4 : delete_subject,
        5 : save_and_exit
    }
    return register[choice]()

def add_subject():
    print("Hello from 'add_subject'")

def log_hours():
    pass

def view_summary():
    pass

def delete_subject():
    pass

def save_and_exit()->int:
    return 5


if __name__=="__main__":
    planner()