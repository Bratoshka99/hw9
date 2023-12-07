def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Error: {e}")
            return "Enter user name"
    return wrapper
@input_error
def hello():
    return "How can I help you?"
@input_error
def add_contact(command):
    return f"Added contact: {name} with phone {phone}"
@input_error
def change_contact(command):
    return f"Changed phone for {name} to {new_phone}"
@input_error
def phone_number(command):
    return f"Phone number for {name}: {phone}"
@input_error
def show_all():
    return "List of all contacts"
def main():
    contacts = {}
    while True:
        user_input = input("Enter your command: ").lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            response = hello()
        elif user_input.startswith("add"):
            response = add_contact(user_input)
        elif user_input.startswith("change"):
            response = change_contact(user_input)
        elif user_input.startswith("phone"):
            response = phone_number(user_input)
        elif user_input == "show all":
            response = show_all()
        else:
            response = "Invalid command. Try again."
        print(response)
if __name__ == "__main__":
    main()
