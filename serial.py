"""Python serial number generator."""

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
    def __init__(self,start):
        self.start = start
        self.count = 0

    def generate(self):
            """Returns incremented serial number"""
            new_serial = self.start + self.count
            self.count += 1
            return new_serial


    def reset(self):
        """Resets the incremented serial number counter"""
        self.count = 0