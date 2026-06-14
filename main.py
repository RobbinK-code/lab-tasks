import task_utils
import validation

def main():
    tasks = []
    
    while True:
        print("\n1. Add a task")
        print("2. Mark task as complete")
        print("3. View pending tasks")
        print("4. Check progress")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            if validation.check_length(description):
                task_utils.add_task(tasks, description)
            else:
                print("Error: Description cannot be empty.")
                
        elif choice == '2':
            task_utils.view_pending(tasks)
            task_id_str = input("Enter task ID to complete: ")
            
            # This triggers the ValueError check in validation.py
            task_id = validation.check_number(task_id_str) 
            
            if task_id != -1:
                task_utils.mark_complete(tasks, task_id)
            else:
                print("Error: Please enter a valid number.")
                
        elif choice == '3':
            task_utils.view_pending(tasks)
            
        elif choice == '4':
            # Check your starter code: if it's named track_progress, change this line
            task_utils.check_progress(tasks)
            
        elif choice == '5':
            break

if __name__ == "__main__":
    main()