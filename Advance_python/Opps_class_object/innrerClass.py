"""
Python Inner Classes

An inner class is a class defined inside another class. 
The inner class can access the properties and methods of the outer class.
    
Inner classes are useful for grouping classes that are only used in one place, 
making your code more organized.



"""

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

"""
#Multiple Inner Classes

class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()


"""