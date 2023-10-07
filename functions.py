FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of 
    todo items
    """

    with open(filepath, '+r') as file:
            todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
     """
     Write the todo items list in the text file
     """
     with open(filepath, '+w') as file:
            file.writelines(todos)
