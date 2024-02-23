# Fitness Tracker System

This project implements a fitness tracker system that collects, stores, and displays user activity data, focusing on SOLID principles.

## Table of Contents
1. [Introduction](#introduction)
2. [SOLID Principles](#solid-principles)
3. [Program Descriptions](#program-descriptions)
4. [How to Run](#how-to-run)

## Introduction

The fitness tracker system is designed to help users monitor their physical activities by collecting data such as steps, distance, and calories burned. It consists of several components:

- **User**: Represents individuals using the fitness tracker.
- **Activity**: Represents specific activities performed by users, such as walking, running, or swimming.
- **ActivityMonitor**: Monitors user activities and stores them in a data storage system.
- **DataStorage**: Stores user activity data.
- **Display**: Displays user activity data to users.

## SOLID Principles

The system adheres to the following SOLID principles:

### Single Responsibility Principle (SRP)
Each component of the system has a single responsibility. For example, the `User` class is responsible for representing user data, while the `ActivityMonitor` class is responsible for monitoring and storing user activities.

### Open-Closed Principle (OCP)
The system is designed to be open for extension but closed for modification. New activity types can be easily added without modifying existing code, thanks to the Observer pattern used in the `ActivityMonitor`.

### Liskov Substitution Principle (LSP)
Subclasses such as `Steps`, `Distance`, and `Calories` adhere to the LSP, ensuring that objects of these subclasses can be substituted for objects of the `Activity` superclass without affecting the correctness of the program.

### Interface Segregation Principle (ISP)
Interfaces are tailored to specific client needs to prevent unnecessary dependencies. For example, the `UserInterface` and `AdminInterface` interfaces provide different functionalities based on user roles.

### Dependency Inversion Principle (DIP)
High-level modules such as the `ActivityMonitor` depend on abstractions rather than concrete implementations, promoting loose coupling and easier testing.

## Additional Program Descriptions

1. **s.py**: Organizes an `Order` class to follow SRP, separating distinct responsibilities into their own classes or modules.
2. **o.py**: Designs a system for calculating areas of different shapes adhering to OCP, allowing easy addition of new shapes without modifying existing code.
3. **l.py**: Ensures compliance with LSP in a 2D geometry drawing application, handling variations in behavior and integrating new shapes seamlessly.
4. **i.py**: Adheres to ISP in a library management system by designing interfaces tailored to specific user needs, preventing tight coupling and inflexibility.
5. **d.py**: Adheres to DIP in a web application logging system, decoupling application logic from specific logging libraries and enhancing flexibility and testability.

## How to Run

To run the fitness tracker system, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the directory containing the project files.
3. Run the `fitness_tracker.py` file using Python 3.
4. Ensure that all dependencies are installed (if not already) before running the program.
