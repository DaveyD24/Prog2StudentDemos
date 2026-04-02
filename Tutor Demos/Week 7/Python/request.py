from abc import ABC, abstractmethod

class Request(ABC):
    
    @abstractmethod
    def get_request_line(self):
        pass

    @abstractmethod
    def handle(self):
        pass