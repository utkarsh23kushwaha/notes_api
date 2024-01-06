from utils import *
class TerminalColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"


def main():
    i = 0
    
    while True:
     
            if i==0:
                print("Options:")
                print("1. Signup")
                print("2. Login")
                print("3. Exit")
            else:
                print("Options:")
                print("1. Signup")
                print("2. Login")
                print("3. Get All Notes")
                print("4. Create a Note")
                print("5. View Note by ID")
                print("6. Edit Note by ID")
                print("7. Delete Note by ID")
                print("8. Share a note with an exisitng User")
                print("9. Search a note with a Keyword")
                print("10. Exit")
       

            if i == 0:
                choice = input("Enter your choice (1-3): ")

                if choice == "1":
                    option = signup()
                    i = i+1
                elif choice == "2":
                    option = login()
                    i = i+1
                elif choice == "3":
                    print("Test Exited")
                    break
                else:
                    print(f"{TerminalColors.BOLD}{TerminalColors.RED} \n Invalid choice. Please enter a number between 1 and 3{TerminalColors.RESET}")
            else:

                choice = input("Enter your choice (1-10): ")

                if choice == "1":
                    option = signup()
                    print(option)
                elif choice == "2":
                    option  = login()
                elif choice == "3":
                    get_all_notes()
                elif choice == "4":
                    option = create_note()
                elif choice == "5":
                    option = get_note_by_id()
                elif choice == "6":
                    option = edit_note()
                elif choice == "7":
                    option = delete_note()
                elif choice == "8":
                    option = share_note()
                elif choice == "9":
                    option = search_note()
                elif choice == "10":
                    print("Test Exited")
                    break
                else:
                    print(f"{TerminalColors.BOLD}{TerminalColors.RED} \nInvalid choice. Please enter a number between 1 and 10.{TerminalColors.RESET}")
         
            continue_testing = input("Do you want to continue testing? (Y/N): ")
            if continue_testing.lower() == 'y':
                continue
            
            elif continue_testing.lower() == 'n':
                break
            
            else:
                print(f"{TerminalColors.BOLD}{TerminalColors.RED} \n Please Enter a  Valid Choice{TerminalColors.RESET}")
                while continue_testing.lower() != 'y'and continue_testing.lower() !='n':
                    print(f"{TerminalColors.BOLD}{TerminalColors.RED} \n Please Enter a  Valid Choice{TerminalColors.RESET}")
                    continue_testing = input("Do you want to continue testing? (Y/N): ")
                    if continue_testing.lower() == 'n':
                        break
                if continue_testing.lower() == 'n':
                        break
                

if __name__ == "__main__":
    main()
