class Strategy:
    def __init__(self):
        self.__focus = "Attack"
    
    def change_stratgy(self):
        if self.__focus == "Attack":
            self.__focus = "Defence"
        else:
            self.__focus = "Attack"
        print(f"Strategy changed to {self.__focus}")
    
    def __str__(self):
        return self.__focus