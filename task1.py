def task_operation(task_list,n):
    sr_number = 1
    if(n==1):
        print("\nEnter no of task you want to add: ")
        n_of_task = int(input())
        sr_number = len(task_list) + sr_number
        for i in range(n_of_task):
            print("\nEnter task: ")
            task_list+=[str(sr_number)+" "+ input()]   
            sr_number+=1
        print(len(task_list))
    elif(n==2):
        updating_at_index =int(input("\nEnter serial number of task to update: "))
        task_list[updating_at_index-1] =str(updating_at_index) + " " + input("\nEnter updated task: ")
        print("\nTask list is updated.\n")
    elif(n==3):
        display_tasks(task_list)
    elif(n==4):
        print("Program Exit........")
        exit()
    else:
        print("\nEnter valid input...")
            
def display_tasks(task_list):
    print("*" * 20)
    print("Task list........")
    for task in task_list:
        print(task)
    print("*" * 20)

task_list = []
while True:
    print("\nEnter 1 to add task")
    print("Enter 2 to update task")
    print("Enter 3 to display list of task")
    print("Enter 4 to Exit")
    n = int(input("\nEnter your choice: "))
    task_operation(task_list,n)