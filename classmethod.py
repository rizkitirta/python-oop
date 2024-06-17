class User:
    total = 0

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role
        User.total  += 1

    def info(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {self.__role}"
    
    def update_name(self, name):
        self.name = name

    def update_role(self, role):
        if self.__role == "admin":
            self.__role = role

    def get_role(self):
        return self.__role
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self,new_role):
        print(self.__role)
        if self.__role == "admin":
            self.__role = new_role

    @classmethod
    def total_user(cls):
        return cls.total
    
    @classmethod
    def setTotalUser(cls,total):
        cls.total = total

    @classmethod
    def newUser(cls, data_str):
        name, email, role = data_str.split(",")
        return cls(name, email, role)
    
user1 = User("tirta","tirtadev01@gmail.com", "user")
user1.age = 25 # add new attribute
user1.hobby = "football"

print(user1.info())
user1.update_role("admin")
print(user1.info())

print("\n")

# class method
print(f"Total User: {User.total_user()}")

print("\n")

user2 = User("tirta2","tirta2dev01@gmail.com", "admin")
user2.age = 26 # add new attribute
print(user2.info())

# update role
# user2.update_role("user")
# print(user2.info())

print("\n")

# class method
print(f"Total User: {User.total_user()}")

print("\n")

print(user1.__dict__)
print(user2.__dict__)

print("\n")

role1 = user1.get_role()
role2 = user2.get_role()
print(f"role user1: {role1}")
print(f"role user2: {role2}")

print("\n")

# property
print(f"property role user1: {user1.role}")
print(f"property role user2: {user2.role}")

print("\n")

user1.role = "superadmin"
user2.role = "superadmin"

print(f"property role user1: {user1.role}")
print(f"property role user2: {user2.role}")

print("\n")

# class method
User.setTotalUser(10)

print(f"Total User: {User.total_user()}")

print("\n")

# class method
# create user from string
user3_str = "tirta4,tirta4@gmail.com,user"
user3 = User.newUser(user3_str)
    
print(user3.__dict__)