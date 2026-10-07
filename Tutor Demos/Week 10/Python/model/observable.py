class Observable:
    def __init__(self):
        self.__subscribers = []

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.__subscribers:
            subscriber()