class Seat(object):
    def __init__(self, aisle: int, row: str) -> None:
        self.aisle = aisle
        self.available = True

    def book(self) -> None:
        if not self.available:
            raise ValueError("Seat not available")
        else:
            self.available = False