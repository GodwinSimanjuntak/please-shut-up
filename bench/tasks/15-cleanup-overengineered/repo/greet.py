from abc import ABC, abstractmethod


class GreetingStrategy(ABC):
    @abstractmethod
    def build(self, name):
        ...


class DefaultGreetingStrategy(GreetingStrategy):
    def build(self, name):
        return f"Hello, {name}!"


class GreetingStrategyFactory:
    _registry = {"default": DefaultGreetingStrategy}

    @classmethod
    def create(cls, kind="default"):
        return cls._registry[kind]()


class Greeter:
    def __init__(self, strategy=None):
        self.strategy = strategy or GreetingStrategyFactory.create()

    def greet(self, name):
        return self.strategy.build(name)


def greet(name):
    return Greeter().greet(name)
