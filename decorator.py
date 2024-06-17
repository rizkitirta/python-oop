def info(funct):
    def wrapper():
        print("*"*10)
        print(funct())
        print("*"*10)

    return wrapper

@info
def say_hello():
    return "Hello World"

hello_world = info(say_hello)
print(hello_world())

print("\n")

# decorator
say_hello()