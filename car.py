class Car:
    def _init_(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print(f"brand:{self.brand},speed:{self.speed}km/h")
    def create_car():
        car1=Car("toyota",180)
        return car1
my_car=Car.create_car()
my_car.display()
