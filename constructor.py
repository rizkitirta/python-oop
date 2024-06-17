class User:
    total_user = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_user += 1

user1 = User("tirta","tirtadev01@gmail.com")
user1.age = 25 # add new attribute
user1.hobby = "football"

print(user1.name)
print(user1.email)
print(user1.age)
print(user1.hobby)

print(user1.total_user)

print("\n")

user2 = User("tirta2","tirta2dev01@gmail.com")
user2.age = 26 # add new attribute

print(user2.name)
print(user2.email)
print(user1.total_user)

print("\n")


    
