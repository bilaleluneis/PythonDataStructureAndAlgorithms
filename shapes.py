
__author__ = "Bilal El Uneis"
__since__ = "August 2018"
__email__ = "bilaleluneis@gmail.com"

from abc import ABC, abstractmethod
from typing import List
from turtle import Turtle, Screen


# Class to work with Turtle commands and steps.
# for now this is very simplistic impl, will need to
# update it, to use property decorators,etc.
class TurtleCommands:

    def __init__(self, command: str, value: int):
        self.__command = command
        self.__value = value

    def get_command(self) -> str:
        return self.__command

    def get_number_of_steps(self) -> int:
        return self.__value


class Shape(ABC):

    # this is a class level and static vars!!
    __screen: Screen = None
    __turtle: Turtle = None
    __instance_counter = 0
    __shape_drawn_counter = 0

    def __init__(self, color: str= "blue", start_at_x: int= 0, start_at_y: int= 0):
        self.__start_at_x = start_at_x
        self.__start_at_y = start_at_y
        self.__color = color

        Shape.__instance_counter += 1
        Shape.__init_drawing_window()
        Shape.__init_drawing_pen()

    def __del__(self):
        Shape.__instance_counter -= 1

    @abstractmethod
    def _get_drawing_information(self) -> List[TurtleCommands]:
        return []  # default implementation will return empty list or array, whatever you want to call it!

    @classmethod
    def __init_drawing_pen(cls):
        if cls.__turtle is None:
            cls.__turtle = Turtle()
        cls.__turtle.pensize(5)
        cls.__turtle.speed(1)
        cls.__turtle.shape("turtle")

    @classmethod
    def __init_drawing_window(cls):
        if cls.__screen is None:
            cls.__screen = Screen()
            cls.__screen.bgcolor("black")
            cls.__screen.setup(400, 300)

    def draw(self):
        Shape.__turtle.showturtle()
        Shape.__turtle.pencolor(self.__color)
        Shape.__turtle.penup()
        Shape.__turtle.goto(self.__start_at_x, self.__start_at_y)
        Shape.__turtle.pendown()
        for turtle_command in self._get_drawing_information():
            action = getattr(Shape.__turtle, turtle_command.get_command())
            action(turtle_command.get_number_of_steps())
        Shape.__turtle.hideturtle()
        Shape.__shape_drawn_counter += 1
        if Shape.__shape_drawn_counter == Shape.__instance_counter:
            Shape.__turtle.getscreen().mainloop()


class Triangle(Shape):

    def __init__(self, color: str, start_at_x: int, start_at_y: int):
        super().__init__(color, start_at_x, start_at_y)

    def _get_drawing_information(self) -> List[TurtleCommands]:
        return [TurtleCommands("forward", 30),
                TurtleCommands("left", 120),
                TurtleCommands("forward", 30),
                TurtleCommands("left", 120),
                TurtleCommands("forward", 30),
                TurtleCommands("left", 120)]


class Square(Shape):

    def __init__(self, color: str, start_at_x: int, start_at_y: int):
        super().__init__(color, start_at_x, start_at_y)

    def _get_drawing_information(self) -> List[TurtleCommands]:
        return [TurtleCommands("forward", 30),
                TurtleCommands("left", 90),
                TurtleCommands("forward", 30),
                TurtleCommands("left", 90),
                TurtleCommands("forward", 30),
                TurtleCommands("left", 90),
                TurtleCommands("forward", 30)]


def main():
    shapes: [Shape] = [Triangle("blue", 0, 0),
                       Square("red", 100, 100),
                       Triangle("orange", 0, -100),
                       Square("green", 0, 100)]
    for shape in shapes:
        shape.draw()


# start of running code
if __name__ == "__main__":
    main()
