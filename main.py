# functions are in another python file
import time

from functions import get_todos, write_todos
# or you can write 'import functions' and write functions.get_todos() in the code

right_now = time.strftime("%d %b %Y, %A - %H:%M:%S")
print(f"Hello, right now is {right_now}")   # executes this line when you run main file


while True:
    user_decision = input("add, show, edit, complete or exit? ")
    user_decision = user_decision.strip()

    # programın ilk halinde match case functionı vardı onları silip if koyduk yerine

    if user_decision.startswith("add"):
        todo = user_decision[4:] + "\n"    # "\n" is to add a break line after the item

        # file = open('todolist.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # to write these 3 lines more efficient way use the with function:

        todos = get_todos()

        todos.append(todo)
        write_todos(todos)  # does not return anything, so don't need to store in a variable

    elif user_decision.startswith("show"):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos] -> to remove the bracket in result (list comprehension)

        for index, item in enumerate(todos):
            item = item.capitalize()
            row = f"{index + 1}- {item}"
            print(row)
        print("Good Luck!")

    elif user_decision.startswith("edit"):
        try:     # to make the error messages more user-friendly, if there are any
            number = user_decision[5:]
            number = int(number) - 1

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:     # assigning a message for the ValueError, if it occurs
            print("Your command is not valid!")
            continue  # this function ignores everything under and goes at the beginning of the code

    elif user_decision.startswith("complete"):
        try:
            deleted =int(user_decision[9:])

            todos = get_todos()

            one_item = todos.pop(deleted - 1).strip('\n')

            write_todos(todos)

            one_item = one_item.capitalize()
            print(f"{one_item} is completed. Good Job!")
        except IndexError:
            error_message = f"there is no number {deleted}, try again please"
            print(error_message)
            continue

    elif user_decision.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("goodbye!")