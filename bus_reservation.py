# Bus Reservation System
# Maximum capacity: 40 seats
# Only one seat booking at a time

total_seats = 40
booked_seats = 0

def calculate_discount(age, base_price):
    if 5 <= age <= 12:
        discount = 0.50
    elif 13 <= age <= 18:
        discount = 0.20
    elif 19 <= age <= 60:
        discount = 0.0
    elif age > 60:
        discount = 0.30
    else:
        discount = 0.0  # For ages below 5, no discount or handle separately
    return base_price * (1 - discount)

def main():
    global booked_seats
    while booked_seats < total_seats:
        try:
            num_seats = int(input("Enter the number of seats required: "))
            if num_seats > 1:
                print("Booking rejected: Only one seat can be booked at a time.")
                continue
            elif num_seats == 1:
                age = int(input("Enter the passenger's age: "))
                ticket_type = input("Select ticket type (AC/Non-AC): ").strip().lower()
                if ticket_type == "ac":
                    base_price = 800
                elif ticket_type == "non-ac":
                    base_price = 500
                else:
                    print("Invalid ticket type. Please select AC or Non-AC.")
                    continue
                
                final_price = calculate_discount(age, base_price)
                
                if booked_seats < total_seats:
                    booked_seats += 1
                    print("Booking Confirmed")
                    print(f"Final ticket cost: ₹{final_price:.2f}")
                    print(f"Seats available: {total_seats - booked_seats}")
                else:
                    print("Booking Not Confirmed, Not Enough Seats Available")
            else:
                print("Invalid number of seats. Please enter 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("All seats are booked. No more bookings possible.")

#if __name__ == "__main__":
 #   main()