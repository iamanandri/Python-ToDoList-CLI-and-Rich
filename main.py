import sys

def main():
    todolist = []
    
    commandArgs = {
        "todolist": todolist
    }
    active = True
    commands = {
        "add": {
            "function": addTask,
            "desc": "Add new tasks",
            "hasArgs": True
            },
        "remove": {
            "function": removeTask,
            "desc": "Remove tasks",
            "hasArgs": True
            },
        "cross": {
            "function": crossTask,
            "desc": "Cross tasks you've finished",
            "hasArgs": True
            },
        "uncross": {
            "function": uncrossTask,
            "desc": "Uncrosses tasks",
            "hasArgs": True
            },
        "edit": {
            "function": editTask,
            "desc": "Edit tasks",
            "hasArgs": True
            },
        "list": {
            "function": listTask,
            "desc": "List tasks",
            "hasArgs": True
            },
        "quit": {
            "function": quitApp,
            "desc": "Quit the program tasks",
            "hasArgs": False
            },
        "roadmap": {
            "desc": "List out future plans for this tool",
            "list": [
                "Add pomodoro timer"
            ],
        },
        "help": {
            "desc": "List out all commands"
        }
    }
    
    print("Welcome to the Obligatory To Do List App!")

    while(active):    
        ### LISTING OUT ALL THE TASKS
        print()
        if(len(todolist)>0):
            print("### YOUR TASKS ###")
            listTask(commandArgs)
        else:
            print("You have no tasks!")
            print("Type \"add [what you need to do]\" (without brackets) to add your first task!")
            print("Example: add Clean up room")
        print()
        
        command = input()
        commandKey = command.partition(" ")[0].lower()
        print()
        
        commandArgs.update({
            "command": command
        })
        
        try:
            if commandKey in commands:
                if "function" in commands[commandKey]:
                    if commands[commandKey]["hasArgs"]:
                        commands[commandKey]["function"](commandArgs)
                    else:
                        commands[commandKey]["function"]()
                elif commandKey == "help":
                    for x, y in commands.items():
                        print(f"{x}\t{y["desc"]}")
                elif "list" in commands[commandKey]:
                    for i in range(len(commands[commandKey]["list"])):
                        print(f"{i+1}. {commands[commandKey]["list"][i]}")
            else:
                print("Command not recognized")
        except KeyError:
            print(f"Key error: {KeyError.args}")

def addTask(commandArgs):
    todolist = commandArgs["todolist"]
    command = commandArgs["command"]
    
    task = command.partition(" ")[2].strip("\"")
    tasksToAdd = task.split(", ")
    for x in tasksToAdd:
        todolist.append(x)

def removeTask(commandArgs):
    todolist = commandArgs["todolist"]
    command = commandArgs["command"]
    
    tasksToRemove = command.partition(" ")[2].split(", ")
    for x in range(len(tasksToRemove)):
        todolist[int(tasksToRemove[x])-1] = ""

    for x in todolist:
        if "" in todolist:
            todolist.remove("")
        
def crossTask(commandArgs):
    todolist = commandArgs["todolist"]
    command = commandArgs["command"]
    
    tasksToCross = command.partition(" ")[2].split(", ")
    for x in range(len(tasksToCross)):
        todolist[int(tasksToCross[x])-1] = f"\033[9m{todolist[int(tasksToCross[x])-1]}\033[0m"

def uncrossTask(commandArgs):
    todolist = commandArgs["todolist"]
    command = commandArgs["command"]
    
    taskToUncross = command.partition(" ")[2].split(", ")
    for x in range(len(taskToUncross)):
        todolist[int(taskToUncross[x])-1] = todolist[int(taskToUncross[x])-1].replace("\033[9m", "\033[0m")

def editTask(commandArgs):
    todolist = commandArgs["todolist"]
    command = commandArgs["command"]
    
    taskIndex = int(command.partition(" ")[2].partition(" ")[0])-1
    newTask = command.partition(" ")[2]
    todolist[taskIndex] = newTask

def listTask(commandArgs):
    todolist = commandArgs["todolist"]
    
    for i in range(len(todolist)):
        print(f"{i+1}. {todolist[i]}")
        
def quitApp():
    print("All in a day's work, good niiiight!")
    sys.exit()
        
if __name__ == "__main__":
    main()