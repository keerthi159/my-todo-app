# constants are written on top of module
# why we do it like below is because if we change the file or filename in the directory then we simply change once
FILEPATH = "./todos.txt"


def get_todos(filepath=FILEPATH):  # default arguement
    """ read a text file and return  the list of
            to-do items.
    """
    with open("./todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH ):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print("i am outside")
print(__name__)
if __name__ == "__main__":  # variable hidden by python its value
    print("hello")
    print(get_todos())
