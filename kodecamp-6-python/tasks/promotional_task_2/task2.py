# Movie Theater Ticket Booking
# Book seats in a row of 10. False = open, True = booked.
# Loop until the user enters 0. Handle taken seats and invalid seat numbers.

seats = [False] * 10  # 10 seats, all open


def book_seat(seat_number):
    index = seat_number - 1
    if seats[index]:
        print(f"Seat {seat_number} is already booked.")
        return
    seats[index] = True
    print(f"Seat {seat_number} booked successfully.")


def show_seats():
    print("\nSeat map (O = open, X = booked):")
    for i, booked in enumerate(seats, start=1):
        status = "X" if booked else "O"
        print(f"  {i}: {status}")


while True:
    show_seats()
    choice = input("\nEnter seat number to book (1-10), or 0 to finish: ")

    try:
        seat_number = int(choice)
    except ValueError:
        print("Please enter a whole number.")
        continue

    if seat_number == 0:
        print("Booking session ended.")
        break

    try:
        book_seat(seat_number)
    except IndexError:
        print("Please choose a seat between 1 and 10.")
