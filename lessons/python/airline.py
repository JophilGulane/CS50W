class Flight():
    def __init__(self, capacity):
        self.capacity = capacity 
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(2)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"Added {person} to the flight successfully.")
    else:
        print(f"No available seats for {person}")