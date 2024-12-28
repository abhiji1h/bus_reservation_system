import pandas as pd
import random
import time
from datetime import datetime

bus_data = pd.read_csv("C:\\Users\\aswat\\New folder\\dtp.csv")

while True:
        print("\nAdmin Menu:")
        print("1. Add Bus")
        print("2. Delete Bus")
        print("3. Modify Bus")
        print("4. View All Buses")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            bus_name = input("Enter Bus Name: ")
            source = input("Enter Source: ")
            destination = input("Enter Destination: ")
            departure_time = input("Enter Departure Time (HH:MM): ")
            arrival_time = input("Enter Arrival Time (HH:MM): ")
            seats = int(input("Enter Number of Seats: "))
            driver_name = input("Enter Driver's Name: ")
        elif choice == "2":
               bus_name = input("Enter Bus Name to Delete: ")
               print(f"\nBus {bus_name} deleted successfully!")
        elif choice == "3":
               bus_name = input("Enter Bus Name to Modify: ")
               new_source = input("Enter New Source: ")
               new_destination = input("Enter New Destination: ")
               new_departure_time = input("Enter New Departure Time (HH:MM): ")
               new_arrival_time = input("Enter New Arrival Time (HH:MM): ")
               new_seats = int(input("Enter New Number of Seats: "))
               new_driver_name = input("Enter New Driver's Name: ")
        elif choice == "4":
               print(bus_data)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

