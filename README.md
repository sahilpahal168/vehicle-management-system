Vehicle Management System

A simple Python project that demonstrates the use of Object-Oriented Programming (OOP) principles such as abstraction, inheritance, encapsulation, and polymorphism.

The system models different types of vehicles — Car, Truck, and Motorcycle — and provides functionalities like starting/stopping engines, calculating fuel efficiency, and displaying vehicle details.

🚀 Features

Abstract base class Vehicle with common attributes and methods.

Specialized classes:

Car: Includes number of doors.

Truck: Includes payload capacity.

Motorcycle: Supports sidecar option.

Demonstrates method overriding for vehicle-specific behaviors.

Encapsulation of attributes using Python properties (@property).

Example usage with sample objects.

📂 Project Structure
vehicle managmet.py   # Main Python script containing all classes and demo

🛠️ Technologies Used

Python 3.x

abc module (Abstract Base Classes)

▶️ How to Run

Clone or download this repository.

Run the script:

python vehicle\ managmet.py


You will see sample outputs for a Car, Truck, and Motorcycle.

📌 Example Output
Car engine of Toyota Corolla started.
Car fuel efficiency: 25 MPG.
Car: Toyota Corolla, Doors: 4
Car engine of Toyota Corolla stopped.

Truck engine of Ford F-150 started.
Truck fuel efficiency: 15 MPG considering payload capacity of 2.5 tons.
Truck: Ford F-150, Payload Capacity: 2.5 tons
Truck engine of Ford F-150 stopped.

Motorcycle engine of Harley-Davidson Street 750 started.
Motorcycle fuel efficiency: 50 MPG.
Motorcycle: Harley-Davidson Street 750, Sidecar: Yes
Motorcycle engine of Harley-Davidson Street 750 stopped.

📖 Learning Objectives

This project is a great way to practice and understand:

Abstraction (abstract base class Vehicle)

Inheritance (Car, Truck, Motorcycle extend Vehicle)

Polymorphism (methods like start_engine behave differently per vehicle)

Encapsulation (private attributes with getters/setters)

🔮 Future Enhancements

Add more vehicle types (e.g., Bus, Bicycle, Electric Car).

Implement real fuel efficiency calculations based on parameters.

Support serialization (saving/loading vehicles to a file).

Add a CLI or GUI for user interaction.
