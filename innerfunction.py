class Game:
    def __init__(self,name,download):
        self.name = name
        self.download = download

    def info(self,function = None):
        def get_name():
            return self.name
        
        def get_download():
            return self.download
        
        def detail():
            return f"Name: {self.name}, Download: {self.download}"
        
        switcher = {
            "get_name": get_name,
            "get_download": get_download
        }

        return switcher.get(function, detail)()

game1 = Game("game 1",100)
download = game1.info("get_name")
print(download)
print("\n")
name = game1.info()
print(name)