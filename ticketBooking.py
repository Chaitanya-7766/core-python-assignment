def book_ticket(booked_seats,seat):
    if seat not in booked_seats:
        booked_seats.append(seat)
        booked_seats.sort()
    return booked_seats
def cancel_ticket(booked_seats,seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    return booked_seats
total_seats=10
booked_seats=[2,5,7]
available=[i for i in range(1,total_seats) if i not in booked_seats]
book_seat=3
cancel_seat=5
booked_seats=book_ticket(booked_seats,book_seat)
booked_seats=cancel_ticket(booked_seats,cancel_seat)
available=[i for i in range(1,total_seats) if i not in booked_seats]
print("Available Seats:",available)

