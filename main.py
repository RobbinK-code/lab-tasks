from task_utils import add_task, mark_complete, view_pending
from validation import is_valid_input

def main():
    # Initialize the structure to store tasks
    tasks = []
    
    while True:
        print("\n=== Task Management System ===")
        print("1. Add a task")
        print("2. Mark task as complete")
        print("3. View pending tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            
            # Use validation.py to check input
            if is_valid_input(description):
                add_task(tasks, description)
            else:
                print("Error: Task description cannot be empty.")
                
        elif choice == '2':
            # Show pending tasks first so the user knows which ID to pick
            has_pending = view_pending(tasks)
            
            if has_pending:
                try:
                    task_id = int(input("\nEnter the ID number of the task to complete: "))
                    mark_complete(tasks, task_id)
                except ValueError:
                    print("Error: Please enter a valid numerical ID.")
                    
        elif choice == '3':
            view_pending(tasks)
            
        elif choice == '4':
            print("Exiting Task Management System...")
            break
            
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()