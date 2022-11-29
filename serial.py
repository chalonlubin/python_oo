class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, initial):
        """Create a start point for serial number generator"""
        self.initial = initial
        self.serial = initial

    def generate(self):
        """Increments serial number"""
        self.serial += 1
        return self.serial

    def reset(self):
        """Reset the serial number back to start"""
        self.serial = self.initial
        return self.serial




