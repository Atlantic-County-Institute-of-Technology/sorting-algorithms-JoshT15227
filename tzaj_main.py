# tzaj_main.py
# Unit 2 Project - Sorting Algorithms
# "Insertion sort walked into a bar... and carefully finds its place between two other patrons"
import os
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
# ------------------------------
# Utility Functions
# ------------------------------


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_positive_int(prompt):
    """Ensures that the user enters a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_range():

    """Asks the user for the range of values to generate."""
    while True:
        try:
            min_val = int(input("Enter the minimum value for the list: "))
            max_val = int(input("Enter the maximum value for the list: "))
            if min_val >= max_val:
                print("Minimum must be less than maximum. Please try again.\n")
                continue
            return min_val, max_val
        except ValueError:
            print("Invalid input. Please enter integers only.\n")


def generate_random_list(size, min_val, max_val):

    """Generates a random list of integers within the specified range."""
    return [random.randint(min_val, max_val) for _ in range(size)]
# ------------------------------
# Sorting Logic
# ------------------------------


def display_results(algorithm_name, result):

    """Displays sorting results and performance metrics."""
    sorted_list, loop_count, actions, time_taken = result
    print(f"\n--- {algorithm_name} Results ---")
    print("Sorted List:", sorted_list)
    print(f"Loop Count: {loop_count}")
    print(f"Sorting Actions (swaps/shifts): {actions}")
    print(f"Time Taken: {time_taken:.6f} seconds\n")
    input("Press Enter to return to the sorting menu...")


def run_sorting_menu(data_list):

    """Displays the sorting algorithm selection menu."""
    while True:
        clear_screen()
        print("=== Sorting Algorithm Menu ===")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Compare All Algorithms")
        print("5. Return to Main Menu")
        choice = input("\nEnter your choice (1–5): ")
        if choice == '1':
            clear_screen()
            print("Performing Bubble Sort...\n")
            result = bubble_sort(data_list.copy())
            display_results("Bubble Sort", result)
        elif choice == '2':
            clear_screen()
            print("Performing Insertion Sort...\n")
            result = insertion_sort(data_list.copy())
            display_results("Insertion Sort", result)
        elif choice == '3':
            clear_screen()
            print("Performing Selection Sort...\n")
            result = selection_sort(data_list.copy())
            display_results("Selection Sort", result)
        elif choice == '4':
            clear_screen()
            print("Comparing All Sorting Algorithms...\n")
            results = {
                "Bubble Sort": bubble_sort(data_list.copy()),
                "Insertion Sort": insertion_sort(data_list.copy()),
                "Selection Sort": selection_sort(data_list.copy())
            }
            for name, result in results.items():
                sorted_list, loop_count, actions, time_taken = result
                print(f"--- {name} ---")
                print(f"Loop Count: {loop_count}")
                print(f"Sorting Actions: {actions}")
                print(f"Time Taken: {time_taken:.6f} seconds\n")
            input("Press Enter to return to the sorting menu...")
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter 1–5.")
            input("Press Enter to try again...")
# ------------------------------
# Main Program Menu
# ------------------------------


def main():
    """Main program menu allowing list generation and sorting."""
    data_list = []
    while True:
        clear_screen()
        print("=== Sorting Algorithm Performance Tester ===")
        print("1. Generate a new list")
        print("2. View current list")
        print("3. Choose sorting algorithm")
        print("4. Exit")
        choice = input("\nEnter your choice (1–4): ")
        # Generate new list
        if choice == '1':
            clear_screen()
            print("=== Generate a Random List ===")
            size = validate_positive_int("Enter the number of elements: ")
            min_val, max_val = get_range()
            data_list = generate_random_list(size, min_val, max_val)
            print("\nNew list generated successfully!")
            print("Current List:", data_list)
            input("\nPress Enter to return to the menu...")
        # View current list
        elif choice == '2':
            clear_screen()
            print("=== Current List ===")
            if data_list:
                print(data_list)
            else:
                print("No list has been generated yet.")
            input("\nPress Enter to return to the menu...")
        # Sorting menu
        elif choice == '3':
            if not data_list:
                print("You must generate a list first!")
                input("Press Enter to return to the menu...")
            else:
                run_sorting_menu(data_list)
        # Exit
        elif choice == '4':
            clear_screen()
            print("Goodbye, and happy sorting! 👋")
            break
        # Invalid selection
        else:
            print("Invalid selection. Please choose 1–4.")
            input("Press Enter to try again...")


if __name__ == "__main__":

    main()
