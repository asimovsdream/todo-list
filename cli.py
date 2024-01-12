import time

from functions import get_todos, write_todos

right_now = time.strftime("%d %b %Y, %A - %H:%M:%S")
print(f"Hello, right now is {right_now}")

while True:
    user_decision = input("add, show, edit, complete or exit? ")
    user_decision = user_decision.strip()

    if user_decision.startswith("add"):
        todo = user_decision[4:] + "\n"

        todos = get_todos()

        todos.append(todo)
        write_todos(todos)

    elif user_decision.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.capitalize()
            row = f"{index + 1}- {item}"
            print(row)
        print("Good Luck!")

    elif user_decision.startswith("edit"):
        try:
            number = user_decision[5:]
            number = int(number) - 1

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid!")
            continue

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