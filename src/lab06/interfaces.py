from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def to_string(self):
        pass


class Loginable(ABC):

    @abstractmethod
    def login(self):
        pass