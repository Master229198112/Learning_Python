def get_todos(filepath='E:/Learning/File/todos.txt'):
    """ Read a text file and return the list
    of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='../File/todos.txt'):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


"""if we want to print below line only when this function is expedited saperatly 
not in the main code we will use below condition"""
if __name__ == "__main__":
    print(get_todos())
