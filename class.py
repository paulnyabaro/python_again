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