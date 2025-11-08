import json
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
    data = []
    def __init__(self, subject_name, goal_hrs = 0):
        self.subject_name = subject_name
        self.goal_hrs = goal_hrs
        self.hours = 0
        self.add_data()
        type(self).write_data()
    
    def add_data(self):
        type(self).data.append({
            "subject_name": self.subject_name,
            "goal_hrs": self.goal_hrs,
            "hours": self.hours,
        })

    @classmethod
    def write_data(cls):
        new_data = cls.data
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)

    @classmethod
    def prepare_data(cls):
        try:
            with open('data.json', 'r') as file:
                cls.data = json.load(file)
        except FileNotFoundError:
            print("Error occurred : 'data.json' file not found")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in 'data.json'.")


def new_subject(subject_name, goal_hrs):
    try:
        new_subj = Subject(subject_name, goal_hrs)
    except Exception as e:
        print(f"Some Error occurred while adding subject : {subject_name}")
    else:
        Subject.write_data()
        return