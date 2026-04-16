def movie_theatre_booking():
    TOTAL_CAPACITY = 350
    remaining_seats = TOTAL_CAPACITY

    total_bookings = 0
    tickets_sold = 0
    rejected_bookings = 0

    print("🎬 Welcome to Movie Theatre Booking System")
    while remaining_seats > 0:
        try:
            tickets = int(input("\nEnter number of tickets (1-15) or 0 to exit: "))

            # Exit condition
            if tickets == 0:
                print("\nBooking stopped by user.")
                break

            # Validate ticket count
            if tickets < 1 or tickets > 15:
                print("❌ Invalid number of tickets. You can book between 1 and 15 tickets only.")
                continue

            # Check seat availability
            if tickets > remaining_seats:
                print(f"❌ Only {remaining_seats} seats available.")
                continue

            ages = []
            valid_booking = True

            # Collect ages using for loop
            for i in range(tickets):
                age = int(input(f"Enter age for person {i+1}: "))

                # Age restriction check
                if age < 12:
                    valid_booking = False
                    continue   # skip further checks for this person

                ages.append(age)

            # Booking decision
            if not valid_booking:
                print("❌ BOOKING REJECTED - Age restriction")
                rejected_bookings += 1
                continue

            # Confirm booking
            remaining_seats -= tickets
            tickets_sold += tickets
            total_bookings += 1

            print(f"✅ BOOKING CONFIRMED - {tickets} tickets")

            # Stop if theatre is full
            if remaining_seats == 0:
                print("\n🎉 Theatre is now FULL!")
                break

        except ValueError:
            print("❌ Invalid input. Please enter numeric values only.")
            continue

    # Final Report
    print("\n================ FINAL REPORT ================")
    print(f"Total Successful Bookings : {total_bookings}")
    print(f"Total Tickets Sold        : {tickets_sold}")
    print(f"Rejected Bookings         : {rejected_bookings}")
    print(f"Remaining Seats           : {remaining_seats}")
    print("=============================================")


# Run the system
movie_theatre_booking()