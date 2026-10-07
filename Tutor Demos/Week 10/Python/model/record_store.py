from model.album import Album
from model.observable import Observable

class RecordStore(Observable):
    def __init__(self, albums):
        super().__init__()
        self.__albums = albums
    
    def get_albums(self):
        return self.__albums

    def remove(self, album):
        self.__albums.remove(album)
        self.notify()