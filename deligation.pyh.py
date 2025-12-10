class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

    def stop(self):
        self.engine.stop()
        print("Car has stopped.")
# Usage
my_car = Car()
my_car.start()
my_car.stop()