import datetime
from write import update_land_data

def display_lands(land_data):
    print("\nAvailable Lands:")
    print("-" * 98)
    print("Kitta no.\tDistrict\tDirection\tAana\tPrice\tAvailability")
    print("-" * 98)
    for kitta_num, land_details in sorted(land_data.items()):
        print(f"{kitta_num}\t{land_details[1]}\t{land_details[2]}\t{land_details[3]}\t{land_details[4]}\t{land_details[5]}")

def rent_land(land_data):
    try:
        kitta_number = int(input("Please select the kitta number to rent: "))
        if kitta_number < 101 or kitta_number >= 101 + len(land_data):
            print("Invalid kitta number. Please try again.")
            return

        land_details = land_data[kitta_number]
        if land_details[5] != "Available":
            print(f"Land with kitta number {kitta_number} is not available for rent.")
            return

        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        anna_land = int(land_details[3])
        print(f"Kitta number {kitta_number} has {anna_land} anna of land.")
        month = int(input("Enter the number of months you want to rent for: "))
        per_month_price = int(land_details[4])

        land_data[kitta_number][5] = "Not Available"
        update_land_data(land_data)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        bill_name = f"Bill_{name}_{timestamp}.txt"
        bill_kitta_number = kitta_number
        anna = anna_land
        rented_month = month
        per_month_price_land = per_month_price
        user_land = [[bill_kitta_number, anna, rented_month, per_month_price_land]]

        print("\nLand rented successfully.")
        print(f"Please collect your bill at '{bill_name}'")
        print("Thank you for using TechnoRental services")

        generate_bill(bill_name, name, phone, user_land)

    except ValueError:
        print("Invalid input. Please try again.")

def return_land(land_data):
    try:
        kitta_number = int(input("Enter the kitta number of the land you want to return: "))
        if kitta_number < 101 or kitta_number >= 101 + len(land_data):
            print("Invalid kitta number. Please try again.")
            return

        land_details = land_data[kitta_number]
        if land_details[5] != "Not Available":
            print(f"Land with kitta number {kitta_number} is not currently rented.")
            return

        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        rented_month = int(input("Enter the number of months you rented the land for: "))
        returned_month = int(input("Enter the number of months you are returning the land after: "))
        per_month_price = int(land_details[4])
        anna_land = int(land_details[3])

        land_data[kitta_number][5] = "Available"
        update_land_data(land_data)

        total_price_with_fine = calculate_fine_or_total_price(rented_month, returned_month, per_month_price, anna_land)

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        bill_name = f"RBill_{name}_{timestamp}.txt"

        print("\nLand returned successfully.")
        print(f"Please collect your return invoice at '{bill_name}'")
        print("Thank you for using TechnoRental services")

        generate_return_invoice(bill_name, name, phone, kitta_number, rented_month, returned_month, total_price_with_fine, per_month_price)

    except ValueError:
        print("Invalid input. Please try again.")

def generate_bill(bill_name, name, phone, user_land):
    total_price = 0
    with open(bill_name, "w") as file:
        file.write("\n")
        file.write("\t\t\t\t Technoproperty\n")
        file.write("\tAddress: Kamalpokhari, Kathmandu Metropolitan\n")
        file.write("Contact no: 98435435556  Email: technorental@gmail.com\n\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Name of the customer: {name}\n")
        file.write(f"Phone of the customer: {phone}\n")
        file.write("~" * 115)
        file.write("\n\t\t Kitta No.\tAana\tMonth\tPrice per month\tTotal price\n")
        file.write("~" * 115)
        file.write("\n")

        for details in user_land:
            total_price += details[3] * details[2]  # Accumulate the total price
            file.write(f"\t\t\t{details[0]}\t\t\t{details[1]}\t\t{details[2]}\t\t{details[3]}\t\t\t{details[3] * details[2]}\n")

        file.write(f"\nTotal Price: {total_price}\n")
        file.write("Thank you for using TechnoRental services")


def generate_return_invoice(bill_name, name, phone, kitta_number, rented_month, returned_month, total_price_with_fine, per_month_price):
    with open(bill_name, "w") as file:
        file.write("Return Invoice\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Returned Land Kitta Number: {kitta_number}\n")
        file.write(f"Rented Month: {rented_month}\n")
        file.write(f"Returned Month: {returned_month}\n")
        file.write(f"Total Price (with fine if applicable): {total_price_with_fine}\n")
        if returned_month > rented_month:
            fine = total_price_with_fine - (rented_month * per_month_price)
            file.write(f"Applicable Fine: {fine}\n")
        else:
            file.write("Applicable Fine: 0\n")
        file.write("\nThank you for using TechnoRental services")

def calculate_fine_or_total_price(rented_month, returned_month, per_month_price, anna_land):
    if returned_month > rented_month:
        delayed_month = returned_month - rented_month
        fine_price = (10 / 100) * (delayed_month * per_month_price)
        total_price_with_fine = per_month_price * returned_month + fine_price
        return total_price_with_fine
    else:
        return per_month_price * rented_month
