class Vehicle:
	def __init__(self, make, model, year, fuel):
		self.make = make
		self.model = model
		self.year = year
		self.fuel = fuel
		self.speed = 0 # here speed is internal state attribute 
# internal state attribute: is a variable stored inside an object that tracks data about the object's current condition, which changes over time as method are run.

	def accelerate(self, amount):
		self.speed += amount
		return f'{self.model} speed: {self.speed} km/h'

	def brake(self, amount):
		self.speed = max(0, self.speed - amount) #  here amount represent how much you want to slow down. 
		# max(0, ...): this ensures your car's speed never drops below 0 into negative numbers.
		return f'{self.model} speed: {self.speed} km/h'

	def info(self):
		return f'{self.year} {self.make} {self.model} ({self.fuel})'


class Car(Vehicle):
	def __init__(self, make, model, year, doors=4):
		super().__init__(make, model, year, 'Petrol')
		self.doors = doors

	def honk(self):
		return f'{self.model}: Beep Beep!'


class ElectricCar(Car):
	def __init__(self, make, model, year, battery_kwh):
		super().__init__(make, model, year)
		self.fuel = 'Electric'
		self.battery_kwh = battery_kwh
		self.charge_pct = 100

	def charge_status(self):
		return f'{self.model} battery: {self.charge_pct}%'

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year, 'Petrol')
        self.cc = cc

    def wheelie(self):
        return f'{self.model} doing a wheelie! 🏍️'

car = Car('Toyota','Corolla',2023)
ev  = ElectricCar('Tesla','Model3',2024,75)
moto = Motorcycle('Honda','CB150',2022,150)

# Inherited methods work on all
print(car.accelerate(60))
# Corolla speed: 60 km/h
print(ev.accelerate(120))
# Model3 speed: 120 km/h

# Own methods
print(car.honk())
# Corolla: Beep Beep!
print(ev.charge_status())
# Model3 battery: 100%
print(moto.wheelie())
# CB150 doing a wheelie! 🏍️

# info() inherited by all
for v in [car, ev, moto]:
    print(v.info())
# 2023 Toyota Corolla (Petrol)
# 2024 Tesla Model3 (Electric)
# 2022 Honda CB150 (Petrol)


