# PROMOTIONAL TASK 2 — Task 2: Movie Theater Ticket Booking
#
# Requirements:
#   - List of 10 booleans: False = open, True = booked
#   - Function: book_seat(seat_number)  (seats numbered 1 to 10)
#   - Loop: keep asking until user types 0 to finish
#   - Conditional: if seat is True, say it is taken; if open, set to True
#   - Exception: try/except IndexError → "Please choose a seat between 1 and 10."

# False = available, True = booked
seats = [False] * 10


def book_seat(seat_number):
    """Book one seat. Uses list index seat_number - 1."""
    index = seat_number - 1

    # Accessing seats[index] raises IndexError if seat_number is out of range (e.g. 15)
    if seats[index]:
        print(f"  Sorry, seat {seat_number} is already booked.")
    else:
        seats[index] = True
        print(f"  Seat {seat_number} booked successfully!")


def display_seats():
    print("\n  Seat map:")
    for i, booked in enumerate(seats, start=1):
        label = "X" if booked else str(i)
        print(f"    Seat {i}: [{label}]  (X = booked, number = open)")


def run_theater():
    """LOOP: ask for a seat until user enters 0."""
    print("\n" + "=" * 50)
    print("    Movie Theater Ticket Booking")
    print("=" * 50)

    try:
        while True:
            display_seats()
            user_input = input("\n  Enter seat (1-10) to book, or 0 to finish: ").strip()

            try:
                seat_number = int(user_input)

                if seat_number == 0:
                    print("\n  Booking complete. Enjoy the movie!\n")
                    break

                book_seat(seat_number)

            except ValueError:
                print("  Error: Please enter a whole number.")
            except IndexError:
                print("  Please choose a seat between 1 and 10.")

    except KeyboardInterrupt:
        print("\n\n  Booking cancelled. Goodbye!\n")


if __name__ == "__main__":
    run_theater()
