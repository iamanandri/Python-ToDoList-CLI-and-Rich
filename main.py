import sys

def main():
    todolist = []
    active = True
    command = ""

    print("Welcome to the Obligatory To Do List App!")

    while(active):    
        ### LISTING OUT ALL THE TASKS
        print()
        if(len(todolist)>0):
            print("### YOUR TASKS ###")
            listTask(todolist)
        else:
            print("You have no tasks!")
            print("Type \"add [what you need to do]\" (without brackets) to add your first task!")
            print("Example: add Clean up room")
                  
        print()
        
        command = input()

        match command.partition(" ")[0].lower():
            case "add":
                addTask(todolist, command)
            case "remove":
                removeTask(todolist, int(command.partition(" ")[2])-1)
            case "finish":
                finishTask(todolist, int(command.partition(" ")[2])-1)
            case "edit":
                editTask(todolist, command.partition(" ")[2])
            case "list":
                listTask(todolist)
            case "quit":
                print("All in a day's work, good byeeeee ^^")
                active = False
                sys.exit()
            case default:
                print("I don't recognize that function?")
                
def addTask(todolist, command):
    task = command.partition(" ")[2].strip("\"")
    todolist.append(task)

def removeTask(todolist, taskindex):
    todolist.pop(taskindex)

def finishTask(todolist, taskindex):
    todolist[taskindex] = f"\033[9m{todolist[taskindex]}\033[0m"

def editTask(todolist, commandArgs):
    taskIndex = int(commandArgs.partition(" ")[0])-1
    newTask = commandArgs.partition(" ")[2]
    todolist[taskIndex] = newTask

def listTask(listitem):
    for i in range(len(listitem)):
        print(f"{i+1}. {listitem[i]}")

if __name__ == "__main__":
    main()