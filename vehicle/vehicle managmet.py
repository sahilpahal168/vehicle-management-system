from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def calculate_fuel_efficiency(self):
        pass

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @model.setter
    def model(self, value):
        self.__model = value

    @abstractmethod
    def get_details(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.__number_of_doors = number_of_doors

    def start_engine(self):
        return f"Car engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Car engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Car fuel efficiency: 25 MPG."

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        self.__number_of_doors = value

    def get_details(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.__number_of_doors}"


class Truck(Vehicle):
    def __init__(self, brand, model, payload_capacity):
        super().__init__(brand, model)
        self.__payload_capacity = payload_capacity

    def start_engine(self):
        return f"Truck engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Truck engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Truck fuel efficiency: 15 MPG considering payload capacity of {self.__payload_capacity} tons."

    @property
    def payload_capacity(self):
        return self.__payload_capacity

    @payload_capacity.setter
    def payload_capacity(self, value):
        self.__payload_capacity = value

    def get_details(self):
        return f"Truck: {self.brand} {self.model}, Payload Capacity: {self.__payload_capacity} tons"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.__has_sidecar = has_sidecar

    def start_engine(self):
        return f"Motorcycle engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Motorcycle engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Motorcycle fuel efficiency: 50 MPG."

    @property
    def has_sidecar(self):
        return self.__has_sidecar

    @has_sidecar.setter
    def has_sidecar(self, value):
        self.__has_sidecar = value

    def get_details(self):
        return f"Motorcycle: {self.brand} {self.model}, Sidecar: {'Yes' if self.__has_sidecar else 'No'}"

car = Car("Toyota", "Corolla", 4)
truck = Truck("Ford", "F-150", 2.5)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", True)

vehicles = [car, truck, motorcycle]

for vehicle in vehicles:
    print(vehicle.start_engine())
    print(vehicle.calculate_fuel_efficiency())
    print(vehicle.get_details())
    print(vehicle.stop_engine())
    print()