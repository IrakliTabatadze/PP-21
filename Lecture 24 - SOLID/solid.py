# S O L I D


###################################################
# S - Single Responsibility Principle
###################################################

from zipfile import ZipFile


##############
# Incorrect
##############
class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, file_content):
        with open(self.filename, 'w') as file:
            return file.write(file_content)

    def compress(self):
        with ZipFile('test.zip', 'w') as archive:
            archive.write(self.filename)

    def decompress(self):
        with ZipFile('test.zip', 'r') as archive:
            archive.extractall()




##############
# Correct
##############

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, file_content):
        with open(self.filename, 'w') as file:
            return file.write(file_content)

class ZipFileManager:
    def __init__(self, filename):
        self.filename = filename

    def compress(self):
        with ZipFile('test.zip', 'w') as archive:
            archive.write(self.filename)

    def decompress(self):
        with ZipFile('test.zip', 'r') as archive:
            archive.extractall()


###################################################
# O -  Open Closed Principle
###################################################

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 5)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


###################################################
# L - Liskov Substitution Principle
###################################################

#########################
# Incorrect
#########################

class KitchenApp:

    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self, temperature):
        pass

class Toster(KitchenApp):
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self, temperature):
        pass

class Juicer(KitchenApp):
    def on(self):
        pass

    def off(self):
        pass


#########################
# Correct
#########################


class KitchenApp:
    def on(self):
        pass

    def off(self):
        pass

class Juicer(KitchenApp):
    def on(self):
        pass

    def off(self):
        pass

class KitchenAppWithTemp(KitchenApp):
    def set_temperature(self, temp):
        pass

class Toster(KitchenAppWithTemp):
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self, temp):
        pass



###################################################
# I - Interface Segregation Principle
###################################################

####################
# Incorrect
####################


class Device:
    def printing(self):
        pass

    def scanning(self):
        pass


class Printer(Device):
    def printing(self):
        pass


printer = Printer()
printer.scanning()

class Scanner(Device):
    def scanning(self):
        pass

scanner = Scanner()
scanner.printing()

class MultifunctionalPrinter(Device):
    pass

multifunctional_printer = MultifunctionalPrinter()
multifunctional_printer.scanning()
multifunctional_printer.printing()


####################
# Correct
####################

class Printer:
    def printing(self):
        pass

class Scanner:
    def scanning(self):
        pass


class PrintingDevice(Printer):
    pass

printing_device = PrintingDevice()
printing_device.printing()


class ScannerDevice(Scanner):
    pass

scanning_device = ScannerDevice()
scanning_device.scanning()


class MultifunctionalPrinter(Printer, Scanner):
    pass

multifunctional_printer = MultifunctionalPrinter()
multifunctional_printer.printing()
multifunctional_printer.scanning()


###################################################
# D - Dependency Inversion Principle
###################################################


####################
# Incorrect
####################

class Logger:
    def logs(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')


class Calculator:
    def __init__(self):
        self.logger = Logger()

    def add(self, x, y):
        result = x + y
        self.logger.log(f"{x} + {y} = {result}")
        return result

calculator = Calculator()
calculator.add(2, 3)
calculator.add(4, 5)
calculator.add(6, 7)
calculator.add(8, 9)



####################
# Incorrect
####################


from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')


class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def addition(self, a, b):
        result = a + b
        self.logger.log(f"{a} + {b} = {result}")
        return result


calculator = Calculator(Logger())
calculator.addition(20, 20)