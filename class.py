class Bike:
    def __init__(self, color, rim_material):
        self.color = color
        self.rim_material = rim_material

    def brake(self):
        print(self.color + ' Bike braking...')


red_bike = Bike("Yellow", "Carbon Fibre")
green_bike = Bike("Green", "Metal")

print(red_bike.color)
green_bike.brake()

class Animal:
    def __init__(self, number_of_legs, color):
        self.number_of_legs = number_of_legs
        self.color = color

    def make_sound(self):
        print("This is the noise I'm making....")

cat = Animal(4, "Grey")
dog = Animal(4, "Black")

print(cat.color)
cat.make_sound()
dog.make_sound()