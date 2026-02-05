from enum import Enum

class Status(Enum):
    FINISHED="finished"
    IN_PROGRESS="In progress"
class Task:
    def __init__(self,name,description):
        self.name=name #Task title
        self.status=Status.IN_PROGRESS #Initial status
        self.description=description #Task details
    def __str__(self):   
        return f"[{self.status.value}] {self.name}: {self.description}"
class TaskList:
    def __init__(self):
        self.task=[] #Internal list of Task objects
    def addTask(self,new_task):
        self.task.append(new_task) #Add object to list
    def deleteTask(self,task_to_remove):
        self.task.remove(task_to_remove) #Remove object
    def MarkAsFinished(self,task_to_mark):
        task_to_mark.status=Status.FINISHED #Update object status
        print(f"Task '{task_to_mark.name}' is done!")
    def displayList(self):
        print("--Your To Do list--")
        for t in self.task: print(t) #Print each task
    def filterListe(self,status_to_find):
        #Return filtered sub-list
        return [t for t in self.task if t.status==status_to_find]

task1=Task("Take a shower","Bring a balm")
task2=Task("Wash my hair","Grab my comb and shampoo")
task3=Task("Prepare my meal prep","Buy pineapple")
to_add=TaskList()
to_add.addTask(task1)
to_add.addTask(task2)
to_add.addTask(task3)
to_add.MarkAsFinished(task1)
results=to_add.filterListe(Status.IN_PROGRESS) #Store the list
for t in results: print(t) #Display the list
to_add.displayList()


