print("Welcome to the to-do-list program ")
tasks = []
while True :
    print("\nThis is a TO-DO List")
    print("1. Add T0-DO List" )
    print("2. View List" )
    print("3. Remove List") 
    print("4. Exit")   
    choice = input("Enter your Choiice: ")
    if choice == "1":
      n= input("Enter your task: ")
      tasks.append(n)  
    elif choice == "2":
       
       if len(tasks) == 0:
          print("No tasks yet ! ")
       else:
          i = 0
          while i < len(tasks):
             print(i + 1, "-", tasks[i])
             i = i + 1
          
            
    elif choice == "3":
       if len(tasks) == 0:
          print("No tasks yet!")
       else :
          i = 0
          while i < len(tasks):
             print(i + 1, "-",tasks[i]) 
             i = i + 1

             n = int(input("Enter task number you want to remove: "))
             tasks.pop(n-1)
             print("Task Removed! ")
    elif choice == "4":
        print("Goodbye !")
        break
    else:
       print("Invalid choice, try again!")      