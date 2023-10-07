from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # gt user input and strip space
    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.strip()

  
    if user_input.startswith("add") or user_input.startswith("new"):
        todo = user_input[4:] + "\n"

        todo_list = get_todos()
        todo_list.append(todo)

        write_todos(todos=todo_list)

    elif user_input.startswith('show'):

        todo_list = get_todos()

        new_todo_list = [ item.strip('\n') for item in todo_list]
        # for item in todo_list:
        #     new_item = item.strip('\n')
        #     new_todo_list.append(new_item)

        for index, item in enumerate(new_todo_list):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            edit_position = int(user_input[5:])
            # edit_position = int(input("Please give the positional number of the todo to edit: "))
            edit_position -= 1
            new_todo = input("Enter new todo: ") 
            
            todo_list = get_todos()

            todo_list[edit_position] = new_todo + "\n"

            write_todos(todos=todo_list)

        except ValueError:
            print("Your command is not valid.")
            continue


    elif  user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            # number = int(input("number of the todo to complete: "))

            todo_list = get_todos()

            done = todo_list.pop(number - 1)

            write_todos(todos=todo_list)

            done = done.strip('\n')
            print(f"{done} has been removed due to completion.")
        except IndexError:
            print("The item number does not exist")
            continue
        except ValueError:
            print("Your command is invalid")
            continue
        

    elif user_input.startswith('exit'):
        break
    else:
        print("Entered wrong input")


print("Bye!")

# user_prompt = "Enter a todo: "

# todo_list = []
# while True:
#     todo = input(user_prompt)
#     if len(todo) == 0:
#         break 
#     todo_list.append(todo.title())






########
# while True:
#     user_input = input("Type add, show or exit: ")
#     match user_input:
#         case 'add':
#             todo = input("Enter a todo:")
#             todo_list.append(todo)
#         case 'show':
#             print(todo_list)
#         case 'exit':
#             break


