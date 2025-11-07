# data = {
#     "sub1" : {"hours" : 0, "goal" : 10},
#     "sub2" : {"hours" : 0, "goal" : 10}
# }

class Subject:
    """
    subject_name : str | Name of subject or topic
    goal_hrs : int | Goal hours for the subject
    hours : int | hours completed for the subject
    """
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.goal_hrs = 0
        self.hours = 0

def main():
    pass

if __name__=="__main__":
    main()