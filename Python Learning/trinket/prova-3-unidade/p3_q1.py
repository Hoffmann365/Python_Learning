taskList = []
priorityList = []

# entradas
while True:
    print("Qual a tarefa? ")
    task = input()
    if task == "fim": break
    print("Qual a prioridade dessa tarefa?")
    taskPriority = int(input())
    taskList.append(task)
    priorityList.append(taskPriority)

listT = len(priorityList)

# saidas

# prioridade 1
for i in range(listT):
    if priorityList[i] == 1:
        print(taskList[i])
# prioridade 2
for i in range(listT):
    if priorityList[i] == 2:
        print(taskList[i])
# prioridade 3
for i in range(listT):
    if priorityList[i] == 3:
        print(taskList[i])