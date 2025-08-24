from read import read_land_data
from operation import display_lands, rent_land, return_land
from datetime import datetime

def welcome_message():
    print("\n")
    print("\t\t\t\t\t\tTechno Property Nepal\t\t\t\t")
    print("\n")
    print("\t\t\t\t\tContact no:98435435556 || Email:technorental@gmail.com")
    print("\n")
    print("\t\t\t\t\t\tPutalisadak, Kathmandu")
    print("-" * 133)

def main_loop():
    land_data = read_land_data()

    while True:
        print("Choose an option:")
        print("-" * 133)
        print("Press 1 to Display Available Lands")
        print("Press 2 to Rent Land")
        print("Press 3 to Return Land")
        print("Press 4 to Exit")
        print("-" * 133)

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 1:
            display_lands(land_data)
        elif user_choice == 2:
            rent_land(land_data)
        elif user_choice == 3:
            return_land(land_data)
        elif user_choice == 4:
            print("\nThank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

welcome_message()
main_loop()
