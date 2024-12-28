import pandas as pd
import random
import time
from datetime import datetime


bus_data = pd.DataFrame(columns=["Bus Name", "Source", "Destination", "Departure Time", "Arrival Time", "Seats Available", "Driver Name"])


def display_buses():
    if bus_data.empty:
        print("No buses available.")
    else:
        print("\nCurrent Bus Schedule:")
        print(bus_data)
        

def add_bus():
    bus_name = input("Enter Bus Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    departure_time = input("Enter Departure Time (HH:MM): ")
    arrival_time = input("Enter Arrival Time (HH:MM): ")
    seats = int(input("Enter Number of Seats: "))
    driver_name = input("Enter Driver's Name: ")

   
    global bus_data
    new_bus = pd.DataFrame([[bus_name, source, destination, departure_time, arrival_time, seats, driver_name]], columns=bus_data.columns)
    bus_data = pd.concat([bus_data, new_bus], ignore_index=True)
    print(f"\nBus {bus_name} added successfully!")

def delete_bus():
    bus_name = input("Enter Bus Name to Delete: ")
    global bus_data
    bus_data = bus_data[bus_data["Bus Name"] != bus_name]
    print(f"\nBus {bus_name} deleted successfully!")

def modify_bus():
    bus_name = input("Enter Bus Name to Modify: ")
    if bus_name in bus_data["Bus Name"].values:
        new_source = input("Enter New Source: ")
        new_destination = input("Enter New Destination: ")
        new_departure_time = input("Enter New Departure Time (HH:MM): ")
        new_arrival_time = input("Enter New Arrival Time (HH:MM): ")
        new_seats = int(input("Enter New Number of Seats: "))
        new_driver_name = input("Enter New Driver's Name: ")

        bus_data.loc[bus_data["Bus Name"] == bus_name, ["Source", "Destination", "Departure Time", "Arrival Time", "Seats Available", "Driver Name"]] = [new_source, new_destination, new_departure_time, new_arrival_time, new_seats, new_driver_name]
        print(f"\nBus {bus_name} modified successfully!")
    else:
        print(f"\nBus {bus_name} not found.")

def admin_options():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Bus")
        print("2. Delete Bus")
        print("3. Modify Bus")
        print("4. View All Buses")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_bus()
        elif choice == "2":
            delete_bus()
        elif choice == "3":
            modify_bus()
        elif choice == "4":
            display_buses()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


def view_available_buses():
    display_buses()

def select_seat(bus_name):
    if bus_name in bus_data["Bus Name"].values:
        bus_info = bus_data[bus_data["Bus Name"] == bus_name].iloc[0]
        available_seats = bus_info["Seats Available"]
        if available_seats > 0:
            print(f"\nAvailable seats for {bus_name}: {available_seats}")
            seat_choice = int(input(f"Select a seat (1 to {available_seats}): "))
            if 1 <= seat_choice <= available_seats:
                print(f"Seat {seat_choice} has been reserved for you on {bus_name}.")
            
                bus_data.loc[bus_data["Bus Name"] == bus_name, "Seats Available"] -= 1
                return True
            else:
                print("Invalid seat number.")
                return False
        else:
            print("Sorry, no available seats.")
            return False
    else:
        print("Bus not found.")
        return False

def make_payment():
    payment_successful = random.choice([True, False])
    if payment_successful:
        print("\nPayment Successful!")
        return True
    else:
        print("\nPayment Failed. Please try again.")
        return False

def user_options():
    while True:
        print("\nUser Menu:")
        print("1. View Available Buses")
        print("2. Book Seat")
        print("3. Make Payment")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_available_buses()
        elif choice == "2":
            bus_name = input("Enter Bus Name to Book Seat: ")
            if select_seat(bus_name):
                print("Seat booked successfully. Proceed to payment.")
        elif choice == "3":
            if make_payment():
                print("Booking confirmed!")
            else:
                print("Booking failed!")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")


def main():
    while True:
        print("\nBus Reservation System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_username = input("Enter Admin Username: ")
            admin_password = input("Enter Admin Password: ")
            if admin_username == "admin" and admin_password == "admin123":
                admin_options()
            else:
                print("Invalid admin credentials.")
        elif choice == "2":
            user_name = input("Enter User Name: ")
            user_password = input("Enter User Password: ")
            if user_name == "user" and user_password == "user123":
                user_options()
            else:
                print("Invalid user credentials.")
        elif choice == "3":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

