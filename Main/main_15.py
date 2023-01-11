import time

"""if module is in same directory"""
# import functions
# from functions import get_todos, write_todos

"""if module is in other directory"""
from module.functions import get_todos, write_todos

"""if function in in other folder like module folder we have to use
from folder_name import module_name"""
# from module import functions

now = time.strftime("%b %d, %Y:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        """if we used from functions(module_name) import function_name
        then we can directly use the function without module name"""
        todos = get_todos()

        """ if we used import functions then we have to use 
        module_name.name_of_function to call"""
        # todos = functions.get_todos()

        todos.append(todo + '\n')

        write_todos(todos, '../File/todos.txt')

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(filepath='../File/todos.txt', todos_arg=todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")
