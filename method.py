class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def info(self):
        return f"Name: {self.name}, Email: {self.email}"
    
    def update_name(self, name):
        self.name = name

user1 = User("tirta","tirtadev01@gmail.com")
user1.age = 25 # add new attribute
user1.hobby = "football"

print(user1.info())

print("\n")

user2 = User("tirta2","tirta2dev01@gmail.com")
user2.age = 26 # add new attribute
print(user2.info())


# update name
user2.update_name("tirta3")
print(user2.info())

print("\n")


    
