class Smartphone:
    """Represents a smartphone with basic attributes and functionality."""
    
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery  # Encapsulation: Battery is private

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}.")

    def charge_battery(self, amount):
        """Charges battery while ensuring it does not exceed 100%."""
        self.__battery = min(self.__battery + amount, 100)
        print(f"Battery charged to {self.__battery}%.")

# Child class with additional features
class Smartwatch(Smartphone):
    """Represents a smartwatch that inherits from Smartphone."""
    
    def __init__(self, brand, model, storage, battery, heart_rate_monitor):
        super().__init__(brand, model, storage, battery)
        self.heart_rate_monitor = heart_rate_monitor

    def track_heart_rate(self):
        print(f"Tracking heart rate using {self.brand} {self.model} smartwatch.")

# Creating objects
phone = Smartphone("Samsung", "Galaxy S23", "256GB", 80)
watch = Smartwatch("Apple", "Watch Series 9", "32GB", 90, True)

phone.call("+123456789")
watch.track_heart_rate()
watch.charge_battery(15)
