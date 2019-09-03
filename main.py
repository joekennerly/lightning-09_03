class Boat:
    def __init__(self):
        pass

    def move(self, speed):
        print(f"This boat moves at the speed of {speed}")

class Kayak(Boat):
    def paddle(self, speed):
        self.move(speed)

myBoat = Kayak()

myBoat.paddle("fast")