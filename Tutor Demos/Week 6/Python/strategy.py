class Strategy:
    def __init__(self):
        self.__focus = "Attack"
    
    def change_strategy(self):
        self.__focus = "Attack" if self.__focus == "Defence" else "Attack"
        print(f"Strategy changed to {self.__focus}")
    
    def __str__(self):
        return self.__focus