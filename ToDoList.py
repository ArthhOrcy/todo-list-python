tasks = []


def addTask():
  task = input("Digite uma tarefa: ")
  tasks.append(task)
  print(f"Tarefa '{task}' adicionada a lista.")


def listTasks():
  if not tasks:
    print("Nao existem tarefas atualmente.")
  else:
    print("Tarefas atuais:")
    for index, task in enumerate(tasks):
      print(f"Tarefas #{index}. {task}")


def deleteTask():
  listTasks()
  try:
    taskToDelete = int(input("Digite # para deletar: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Tarefa {taskToDelete} foi deletada.")
    else:
      print(f"Tarefa #{taskToDelete} nao encontrada.")
  except:
    print("Input invalido.")


if __name__ == "__main__":
  print("Bem vindo a lista de tarefas :)")
  while True:
    print("\n")
    print("Por favor selecione uma das proximas opcoes")
    print("------------------------------------------")
    print("1. Adicione uma tarefa")
    print("2. Delete uma tarefa")
    print("3. Liste as tarefas")
    print("4. Sair")

    choice = input("Digite sua opcao: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      deleteTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Input invalido. Por favor tente de novo.")

  print("Ate logo!")