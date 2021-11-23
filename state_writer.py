from turtle import Turtle


class State_writer(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()

    def draw(self, x: int, y: int, state: str) -> None:
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.write(state)
