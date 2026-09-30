from model.album import Album

class RecordStore:
    def __init__(self):
        self.__album = Album("Stardust", "Serenity", 12, 34.99)
    
    def get_album(self):
        return self.__album