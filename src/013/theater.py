from typing import List

class Theater(object):
    def __init__(self, seats: List[Seat] = None) -> None:
        self.seats = seats

    @property
    def available_seats(self) -> List[Seat]:
        return [seat for seat in self.seats if seat.available]
