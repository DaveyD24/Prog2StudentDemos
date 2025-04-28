class Albums:
    def __init__(self, albums=[]):
        self.albums = albums

    def add(self, album):
        self.albums.append(album)

    def remove(self, album):
        self.albums.remove(album)