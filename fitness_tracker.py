## Logan Nitzsche - CS 325: Software Engineering Bonus Question
## Fitness Tracking System

## Implement the data collection, storage, and display functionality, focusing on the Observer pattern and applying SOLID principles:
## SRP: Create separate classes for User, Activity, ActivityMonitor, DataStorage, and Display.
## OCP: Leverage the Observer pattern to notify the Display whenever the ActivityMonitor collects new data about the user's activity. This allows you to add new activity types without modifying existing classes.
## LSP: Ensure the Activity class and its subclasses adhere to the observer pattern's contracts, making them compatible with the notification mechanism.
## ISP: Define separate interfaces for data collection and display if they have distinct concerns.
## DIP: Inject dependencies like the DataStorage and Display into the ActivityMonitor constructor for loose coupling and easier testing.

from abc import ABC, abstractmethod
from datetime import datetime

# Interface for Data Storage to adhear to Single Responsibility Principle (SRP) and Open Closed Principal (OCP)
# Abstraction rather than a concretions adhearing to Dependency Inversion Principle (DIP)
class DataStorage(ABC):
    @abstractmethod
    def store_activity(self, activity):
        pass

# Interface for Display to adhear to Single Responsibility Principle (SRP) and Open Closed Principal (OCP)
# Abstraction rather than a concretions adhearing to Dependency Inversion Principle (DIP)
class Display(ABC):
    @abstractmethod
    def update(self, activity):
        pass

# Interface for User adhearing to Interface Segregation Principle (ISP)
class UserInterface(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

# Interface for Admin adhearing to Interface Segregation Principle (ISP)
class AdminInterface(ABC):
    @abstractmethod
    def __init__(self, name):
        pass
    
# Base class for Activity to adhear to Single Responsibility Principle (SRP) and Open Closed Principal (OCP)
# Abstraction rather than a concretions adhearing to Dependency Inversion Principle (DIP)
class Activity(ABC):
    def __init__(self, user, value):
        self.user = user
        self.value = value
        self.timestamp = datetime.now()

    @abstractmethod
    def activity_type(self):
        pass

    def __str__(self):
        return f"{self.user.name} performed {self.activity_type()} of {self.value} at {self.timestamp}"

# Activity Data Classes open for extension but closed for modification adhearing to Open Closed Principal (OCP)
# Activity subtype are substitutable for its base type adhearing to Liskov Substitution Principle (LSP)
class Steps(Activity):
    def __init__(self, user, value):
        super().__init__(user, value)

    def activity_type(self):
        return "steps"

class Distance(Activity):
    def __init__(self, user, value):
        super().__init__(user, value)

    def activity_type(self):
        return "distance"

class Calories(Activity):
    def __init__(self, user, value):
        super().__init__(user, value)
    
    def activity_type(self):
        return "calories"
    
class Swimming(Activity):
    def __init__(self, user, value):
        super().__init__(user, value)
    
    def activity_type(self):
        return "swimming"

# Class for ActivityMonitor adhearing to Single Responsibility Principle (SRP)
class ActivityMonitor:
    def __init__(self, data_storage: DataStorage, displays: list):
        self.data_storage = data_storage
        self.displays = displays

    def record_activity(self, user, activity_type, value):
        activity_class = self._get_activity_class(activity_type)
        if activity_class:
            activity = activity_class(user, value)
            self.data_storage.store_activity(activity)
            self.notify_displays(activity)
        else:
            print(f"Error: Unsupported activity type '{activity_type}'")

    def notify_displays(self, activity):
        for display in self.displays:
            display.update(activity)

    def _get_activity_class(self, activity_type):
        activity_mapping = {
            "steps": Steps,
            "distance": Distance,
            "calories": Calories,
            "swimming": Swimming
        }
        return activity_mapping.get(activity_type)

# ConsoleDisplay class open for extension but closed for modification adhearing to Open Closed Principal (OCP)
class ConsoleDisplay(Display):
    def update(self, activity):
        print(f"New activity recorded: {activity}")

# DatabaseStorage class open for extension but closed for modification adhearing to Open Closed Principal (OCP)
class DatabaseStorage(DataStorage):
    def store_activity(self, activity):
        print(f"Storing activity in database: {activity}")

# Class for User adhearing to Single Responsibility Principle (SRP)
# Clients don't depend on methods they do not use adhearing to Interface Segregation Principle (ISP)
class User(UserInterface):
    def __init__(self, name):
        self.name = name

# Clients don't depend on methods they do not use adhearing to Interface Segregation Principle (ISP)
class Admin(AdminInterface):
    def __init__(self, name):
        self.name = name


# Main
if __name__ == "__main__":
    # Create instances
    storage = DatabaseStorage()
    display = ConsoleDisplay()
    
    # Create an Activity Monitor with dependencies injected
    monitor = ActivityMonitor(storage, [display])

    # Create a user
    user = User("Logan")

    # Record activities
    monitor.record_activity(user, "steps", 1000)
    monitor.record_activity(user, "distance", 5.5)
    monitor.record_activity(user, "calories", 200)
    monitor.record_activity(user, "swimming", 30)

