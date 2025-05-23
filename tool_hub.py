import os

from word_counter_tool.word_counter import main as word_counter_main
from calculator_tool.calculator import main as calculator_main
from string_toolkit_tool.string_toolkit import main as string_toolkit_main
from list_organizer_tool.list_organizer import main as list_organizer_main
from number_classifier_tool.number_classifier import main as number_classifier_main
from for_tool.for_practice import main as for_tool_main
from range_tool.range_practice import main as range_tool_main
from break_continue_tool.break_continue import main as break_continue_main
from loop_else_tool.loop_else import main as loop_else_main
from pass_tool.pass_demo import main as pass_tool_main
from match_tool.match_tool import match_main


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear_screen()
        print("\n✨ Welcome to the Python Tool Hub! ✨")
        print("-----------------------------------")
        print("Choose a tool:")
        print("1. Word Counter")
        print("2. Calculator")
        print("3. String Toolkit")
        print("4. List Organizer")
        print("5. Number Classifier")
        print("6. For Loop Practice")
        print("7. Range Practice")
        print("8. Break & Continue Practice")
        print("9. Loop-Else Prime Checker")
        print("10. Pass Statement Demo")
        print("11. Match Statement Demo")
        print("12. Exit")

    
        print("-----------------------------------")

        choice = input("Enter your choice (1-100): ")

        if choice == '1':
            word_counter_main()
        elif choice == '2':
            calculator_main()
        elif choice == '3':
            string_toolkit_main()
        elif choice == '4':
            list_organizer_main()
        elif choice == '5':
            number_classifier_main()
        elif choice == '6':
            for_tool_main()
        elif choice == '7':
            range_tool_main()
        elif choice == '8':
            break_continue_main()
        elif choice == '9':
            loop_else_main()
        elif choice == '10':
            pass_tool_main()
        elif choice == '11':
            match_main()
        elif choice == '12':
            print("Goodbye!")
            break

        else:
            print("\n❗ Invalid choice. Please select a valid option.")

        pause()

if __name__ == "__main__":
    main()
