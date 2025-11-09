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