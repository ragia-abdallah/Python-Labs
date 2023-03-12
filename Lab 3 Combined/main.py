import math
import abc

print("Question 1: Create a class Rectangle with two attributes width and height. \
The class should have a method area() that returns the area of the rectangle.")


class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def get_area(self):
        return self.height * self.width


my_rect = Rectangle(5, 12)

print("Rectangle area =", my_rect.get_area())

print("\nQuestion 2: Create a class Circle with one attribute radius. The class should have \
a method circumference() that returns the circumference of the circle.")


class Circle:
    radius = 0

    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)


my_circ = Circle(4)
print("The circle circumference =", my_circ.circumference())
print("If radius is not initialized, it defaults to:", Circle.radius)

print("\nQuestion 3: Create a class Employee with three attributes name, age, and salary. \
The class should have a method raise_salary() that increases the employee's salary by a given percentage.")


class Employee:
    def __init__(self, name="John Doe", age=21, salary=0):
        self.name = name
        self.age = age
        self.salary = salary

    def raise_salary(self, percentage_increase):
        total_increase = self.salary * percentage_increase /100
        self.salary += total_increase


my_emp = Employee()
my_emp.salary = 1000
my_emp.raise_salary(20)
print("Salary after 20% increase =", my_emp.salary)

print("\nQuestion 4: Create a class Book with two attributes title and author. The class \
should have a method display() that prints the title and author of the book.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)


my_book = Book("My Title", "John Doe")
my_book.display()

print("\nQuestion 5: Create a class Car with four attributes make, model, year, and mileage. \
The class should have a method drive() that increments the mileage of the car by a given amount.")


class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles


my_car = Car("Ford", "T", "1908", 100)
my_car.drive(500)
print("The mileage on my car is now", my_car.mileage)

print("\nQuestion 6: Create a class Person with two attributes name and age. The class should \
have a constructor that initializes the name and age attributes. Also, implement \
a destructor for the class that prints a message when the object is destroyed.")


class Person:
    def __init__(self, name="John Doe", age=21):
        self.name = name
        self.age = age
        print("New person is here!")

    def __del__(self):
        print("This person is no longer with us. :(")


my_person = Person()
print("Now we kill him...")
del my_person

print("\nQuestion 7: Create a class BankAccount with two attributes account_number \
and balance. The class should have a constructor that initializes the account_number \
and balance attributes. Also, implement a destructor for the class that prints \
a message when the object is destroyed.")


class BankAccount:
    def __init__(self, acc_no, balance):
        self.account_number = acc_no
        self.balance = balance
        print("Account has been opened.")

    def __del__(self):
        print("This account has been closed.")


my_acc = BankAccount(123, 456) #ya fa2eera xD
print("Now we close the bank account")
del my_acc

print("\nQuestion 8: [Single Inheritance] Create a class Vehicle with an attribute speed. \
Create a subclass Car that inherits from Vehicle and has an attribute brand. \
Implement a method in Car that returns the brand and speed of the car.")


class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)


my_car = Car(60, "Ford")
my_car.display()

print("\nQuestion 9: [Multiple inheritance] Create a class Animal with an attribute name. \
Create a class Pet with an attribute owner.")


class Animal:
    def __init__(self, name):
        self.name = name


class Pet:
    def __init__(self, owner):
        self.owner = owner


print("Question 10: Create a subclass Dog that inherits from both Animal and Pet and has \
an attribute breed. Implement a method in Dog that returns the name, owner, and breed of the dog.")


class Dog(Animal,Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self,owner)

    def display(self):
        print("Name:", self.name)
        print("Owner:", self.owner)


my_dog = Dog("Fluffy", "Hagrid")
my_dog.display()

print("\nQuestion 11: [Multilevel inheritance] Create a class Person with an attribute name. \
Create a subclass Employee that inherits from Person and has an attribute salary. \
Create a subclass Manager that inherits from Employee and has an attribute department. \
Implement a method in Manager that returns the name, salary, and department of the manager.")


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person): 
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        #super().__init__(name)
        #Person.__init__(self, name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        #Employee.__init__(self, name, salary)
        #super(Manager, self).__init__(name, salary)
        super().__init__(name,salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


my_manager = Manager("Johnny Doer", 4000, "HR")
my_manager.display()

print("\nQuestion 12: [Hierarchical Inheritance] Create a class Shape with an attribute color. \
Create a subclass Rectangle that inherits from Shape and has attributes width and height.")
print("Question 13: Create a subclass Circle that inherits from Shape and has an attribute radius. \
Implement a method in each subclass that returns the area of the shape.")

class Shape:
    def __init__(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def get_area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)


my_rect = Rectangle("Red", 4, 6)
print("Rectangle's area is:", my_rect.get_area())
my_circ = Circle("Blue", 4)
print("Circle's area is:", my_circ.get_area())

print("Question 14: [Encapsulation] Create a class BankAccount with a private attribute balance. \
Implement methods deposit and withdraw to modify the balance, and a method get_balance to retrieve the balance.")


class BankAccount:
    def __init__(self, acc_no, balance):
        self.account_number = acc_no
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


my_acc = BankAccount(123, 456)
#print(my_acc.__balance) >> illegal
print(my_acc.get_balance())
my_acc.deposit(500)
print(my_acc.get_balance())
my_acc.withdraw(1000)
print(my_acc.get_balance()) #keda ana sha7ata xD

print("\nQuestion 15: [Polymorphism] Create a class Animal with an abstract method speak(). \
Implement subclasses Dog and Cat that override speak() to output the respective animal sounds.")


class Animal(abc.ABC):
    # @abc.abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    sound = "hwhw xD"

    def speak(self):
        print(self.sound)


class Cat(Animal):
    sound = "nwnw xDD"

    def speak(self):
        print(self.sound)


my_doggo = Dog()
print("Doggo say what?")
my_doggo.speak()
my_catto = Cat()
print("Catto say what?")
my_catto.speak()

print("\nQuestion 16: Create a class Calculator with a class method add that takes two numbers \
as arguments and returns their sum.")

class Calculator:
    @classmethod
    def add(cls, x, y):
        return x + y


print(Calculator.add(4,7))


