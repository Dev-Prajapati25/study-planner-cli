def num_input(prompt:str, skip:bool) -> int:
    while True:
        num = input(prompt)
        if num=="" and skip==True:return None
        try:
            num = int(num)
        except ValueError:
            print("Enter Valid Number")
        except Exception as e:
            print(f"Error occurred : {e}")
        else:
            return num