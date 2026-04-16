class Seat:
    def __init__(self, number):
        self.number = number
        self.booked = False

    def book(self):
        if not self.booked:
            self.booked = True
            print("Joy bron qilindi:", self.number)
        else:
            print("Joy band:", self.number)

    def show_seat(self):
        status = "Band" if self.booked else "Bo'sh"
        print(self.number, "-", status)


class Cinema:
    def __init__(self):
        self.seats = []

    def add_seat(self, seat):
        self.seats.append(seat)

    def show_seats(self):
        for seat in self.seats:
            seat.show_seat()


def main():
    c = Cinema()

    s1 = Seat(1)
    s2 = Seat(2)

    c.add_seat(s1)
    c.add_seat(s2)

    s1.book()

    c.show_seats()


main()
