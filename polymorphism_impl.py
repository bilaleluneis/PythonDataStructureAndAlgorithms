__author__ = "Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"

from abc import ABC, abstractmethod
import turtle


class TurtleCommands:

    def __init__(self, command: str, value: int):
        self.__command = command
        self.__value = value

    def get_command(self) -> str:
        return self.__command

    def get_number_of_steps(self) -> int:
        return self.__value


class AbstractShape(ABC):
    __list_to_draw: [TurtleCommands]
    __turtle_object = turtle.Turtle()
    __screen = turtle.Screen()

    def __init__(self, background_color: str, turtle_color: str, start_x: int, start_y: int, side_len: int):
        AbstractShape.__screen.setup(400, 400)
        AbstractShape.__screen.bgcolor(background_color)
        AbstractShape.__turtle_object.pensize(5)
        AbstractShape.__turtle_object.speed(1)
        AbstractShape.__turtle_object.shape("turtle")
        self.__turtle_color = turtle_color
        self.__start_x = start_x
        self.__start_y = start_y
        self._side_len = side_len  # declared as protected to access from subclasses.

    @abstractmethod
    def _turtle_list_command(self):
        pass

    def draw(self):
        AbstractShape.__turtle_object.pencolor(self.__turtle_color)
        AbstractShape.__turtle_object.showturtle()
        AbstractShape.__turtle_object.penup()
        AbstractShape.__turtle_object.goto(self.__start_x, self.__start_y)
        AbstractShape.__turtle_object.pendown()
        AbstractShape.__list_to_draw = self._turtle_list_command()
        for turtle_command in self.__list_to_draw:
            action = getattr(self.__turtle_object, turtle_command.get_command())
            action(turtle_command.get_number_of_steps())
        AbstractShape.__turtle_object.penup()
        AbstractShape.__turtle_object.ht()


class Square(AbstractShape):

    def __init__(self, background_color: str, turtle_color: str, start_x: int, start_y: int, side_len: int):
        super().__init__(background_color, turtle_color, start_x, start_y, side_len)

    def _turtle_list_command(self):
        return [TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 90),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 90),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 90),
                TurtleCommands("forward", self._side_len)]


class Triangle(AbstractShape):

    def __init__(self, background_color: str, turtle_color: str, start_x: int, start_y: int, side_len: int):
        super().__init__(background_color, turtle_color, start_x, start_y, side_len)

    def _turtle_list_command(self):
        return [TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 120),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 120),
                TurtleCommands("forward", self._side_len)]


class Hexagon(AbstractShape):

    def __init__(self, background_color: str, turtle_color: str, start_x: int, start_y: int, side_len: int):
        super().__init__(background_color, turtle_color, start_x, start_y, side_len)

    def _turtle_list_command(self):
        return [TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 60),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 60),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 60),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 60),
                TurtleCommands("forward", self._side_len),
                TurtleCommands("right", 60),
                TurtleCommands("forward", self._side_len)]


def main():
    shapes_to_draw = [Square("red", "green", 0, 0, side_len=60),
                      Triangle("orange", "red", 50, 50, side_len=100),
                      Hexagon("yellow", "yellow", -50, 50, side_len=50),
                      Triangle("green", "purple", -50, -50, side_len=80),
                      Square("blue", "blue", 20, -10, side_len=20)]

    for shape_to_draw in shapes_to_draw:
        shape_to_draw.draw()

    turtle.done()


# start of running code
if __name__ == "__main__":
    main()
