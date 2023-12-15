def task_operation(task_list,choice):# arguments taken
    sr_number = 1 # to maintain serial number of task in list 
    if(choice==1):
        print("\nEnter no of task you want to add: ") 
        # adding number of task in list
        n_of_task = int(input())
        sr_number = len(task_list) + sr_number
        for i in range(n_of_task):
            print("\nEnter task: ")
            task_list+=[str(sr_number)+" "+ input()]   
            sr_number+=1
        print(len(task_list))
    # updating task list
    elif(choice==2):       
        updating_at_index =int(input("\nEnter serial number of task to update: "))
        task_list[updating_at_index-1] =str(updating_at_index) + " " + input("\nEnter updated task: ")
        print("\nTask list is updated.\n")
    # Display task list
    elif(choice==3):
        display_tasks(task_list)
        #Exiting program
    elif(choice==4):
        print("Program Exit........")
        exit()
    # to handle invalid input 
    else:
        print("\nEnter valid input...")

# function display list of tasks
def display_tasks(task_list):
    print("*" * 20)
    print("Task list........")
    for task in task_list:
        print(task)
    print("*" * 20)

task_list = [] #Empty list created
while True:
    print("\nEnter 1 to add task")
    print("Enter 2 to update task")
    print("Enter 3 to display list of task")
    print("Enter 4 to Exit")
    choice = int(input("\nEnter your choice: "))
    task_operation(task_list,choice)