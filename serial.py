class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(100)

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
    def __init__(self, inital):
        """Create a start point for serial number generator"""
        self.start = self.current = inital

    def generate(self):
        """Increments serial number"""
        self.current += 1
        return self.current-1

    def reset(self):
        """Reset the serial number back to start"""
        self.current = self.start




