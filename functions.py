import time
FILEPATH = "todolist.txt"


def get_todos(filepath=FILEPATH):     # creating a custom function for repetitive codes
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath = FILEPATH):
# Non-default parameters should come first in a function definition, then the default parameters.
    """ Write the to-do items in the text file."""
    with open(filepath, 'w') as file:  # w is for write; must be 'r' for read
        file.writelines(todos_argument)  # does not need to return anything


right_now = time.strftime("%d %b %Y, %A - %H:%M:%S")
print(f"Hello, right now is {right_now}")   # executes this line when you run main file

if __name__ == "__main__":  # does not execute this line when you run main file
    print(get_todos())