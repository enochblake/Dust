# def main():
#     action = input("Enter an action: ")
#     if action:
#         print("Result = Dust")
#     else:
#         print("Result = No Dust")

# if __name__ == "__main__":
#     main()


# def is_dust(gender, action):
#     if gender.lower() == "male" and action.lower() in ["buy flowers", "write a love letter", "plan a surprise"]:
#         return True
#     elif gender.lower() == "female" and action.lower() in ["cook a meal", "offer support", "listen attentively","buy a benz"]:
#         return False
#     else:
#         return None

# def main():
#     gender = input("Enter your gender (male/female): ")
#     action = input("Enter the action you want to perform: ")

#     result = is_dust(gender, action)

#     if result is not None:
#         print(f"Result: {'Dust' if result else 'No Dust'}")
#     else:
#         print("Invalid input. Please check your gender and action.")

# if __name__ == "__main__":
#     main()

# import random

# def get_random_thought(gender):
#     if gender.lower() == "male":
#         return random.choice(["buys flowers", "writes a love letter", "plans a surprise"])
#     elif gender.lower() == "female":
#         return random.choice(["cooks a meal", "offers support", "listens attentively", "buys a book"])
#     else:
#         return None

# def is_dust(gender, action):
#     if gender.lower() == "male" and action.lower() in ["buys flowers", "writes a love letter", "plans a surprise"]:
#         return True
#     elif gender.lower() == "female" and action.lower() in ["cooks a meal", "offers support", "listens attentively", "buys a book"]:
#         return False
#     else:
#         return None

# def main():
#     gender = input("Enter your gender (male/female): ")
#     action = get_random_thought(gender)

#     if action is not None:
#         print(f"Generated Action: {action}")
#         result = is_dust(gender, action)
#         print(f"Result: {'Dust' if result else 'No Dust'}")
#     else:
#         print("Invalid input. Please check your gender.")

# if __name__ == "__main__":
#     main()


def main():
    gender = input("Enter your gender (Male/Female): ")
    
    if gender.lower() == "male":
        action = input("Enter a male action: ")
        if action:
            print("Result = Dust")
        else:
            print("Result = No Dust")
    elif gender.lower() == "female":
        action = input("Enter a female action: ")
        if action:
            print("Result = No Dust")
        else:
            print("Result = Dust")
    else:
        print("Invalid gender entered. Please enter either 'Male' or 'Female'.")

if __name__ == "__main__":
    main()
