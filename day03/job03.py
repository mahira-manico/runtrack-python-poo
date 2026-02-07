from enum import Enum

class Status(Enum):
    #Enumeration for fixed task statuses
    FINISHED="finished"
    IN_PROGRESS="In progress"

class Task:
    #Class representing an individual task
    def __init__(self,name,description):
        self.name=name #Task title
        self.status=Status.IN_PROGRESS #Initial status
        self.description=description #Task details
    
    def __str__(self):   
        #Formatted string for task display
        return f"[{self.status.value}] {self.name}: {self.description}"

class TaskList:
    #Class to manage a collection of Task objects
    def __init__(self):
        self.task=[] #Internal list of Task objects
    
    def addTask(self,new_task):
        #Add a Task object to the list
        self.task.append(new_task)
    
    def deleteTask(self,task_to_remove):
        #Remove a specific Task object
        self.task.remove(task_to_remove)
    
    def MarkAsFinished(self,task_to_mark):
        #Update task status using Enum reference
        task_to_mark.status=Status.FINISHED
        print(f"Task '{task_to_mark.name}' is done!")
    
    def displayList(self):
        #Print all tasks in the list
        print("--Your To Do list--")
        for t in self.task: print(t)
    
    def filterListe(self,status_to_find):
        #List comprehension to filter tasks by status
        return [t for t in self.task if t.status==status_to_find]

#Testing task management logic
task1=Task("Take a shower","Bring a balm")
task2=Task("Wash my hair","Grab my comb and shampoo")
task3=Task("Prepare my meal prep","Buy pineapple")

to_add=TaskList()
to_add.addTask(task1)
to_add.addTask(task2)
to_add.addTask(task3)

to_add.MarkAsFinished(task1)

#Filter and display only in-progress tasks
results=to_add.filterListe(Status.IN_PROGRESS)
for t in results: print(t)

to_add.displayList()


