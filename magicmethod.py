class Game:
    def __init__(self,name,download):
        self.name = name
        self.download = download

    def __str__(self):
        return f"Name: {self.name}, Download: {self.download}"
    
    def __eq__(self, other):
        return self.name == other.name
        
    def __add__(self, other):
        return self.download + other.download
    

game1 = Game("game 1",100)
print(game1)
print("\n")

game2 = Game("game 1",200)
game3 = Game("game 2",200)
print(game1 == game2)
print(game1 == game3)
print("\n")

print(game1 + game2)

