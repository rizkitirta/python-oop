class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


emp1 = Employee("employee 1",1000000)
emp1.displayEmployee()
print("\n")

class Programmer(Employee):
    def __init__(self, name, salary, level = "junior"):
        super().__init__(name, salary)
        self.level = level

    def speakEnglish(self):
        print(f"{self.name} can speak English")

    def displayEmployee(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Level: {self.level}")

programmer1 = Programmer("programmer 1",11000000)
programmer1.displayEmployee()
print("\n")

programmer2 = Programmer("programmer 2", 12000000, "middle")
programmer2.speakEnglish()
print("\n")