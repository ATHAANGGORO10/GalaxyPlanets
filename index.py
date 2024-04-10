import turtle
from math import *
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.up()
sun.goto(0, 0)


class Star(turtle.Turtle):
    def __init__(self, size, color):
        super().__init__(shape="circle")
        self.shapesize(size)
        self.color(color)
        self.up()


def place_star(star, min_distance):
    while True:
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        too_close = False
        for existing_star in stars:
            if (
                abs(existing_star.xcor() - x) < min_distance
                and abs(existing_star.ycor() - y) < min_distance
            ):
                too_close = True
                break
        if not too_close:
            star.goto(x, y)
            break


stars = []
for _ in range(100):
    size = random.uniform(0.1, 0.3)
    color = random.choice(["white", "lightgray", "lightyellow"])
    star = Star(size, color)
    place_star(star, 55)
    stars.append(star)


class Planet(turtle.Turtle):
    def __init__(self, name, radius, color, speed):
        super().__init__(shape="circle")
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
        self.speed = speed

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)


mercury = Planet("Mercury", 40, "grey", 0.01)
venus = Planet("Venus", 80, "orange", 0.006)
earth = Planet("Earth", 100, "blue", 0.002)
mars = Planet("Mars", 150, "red", 0.0014)
jupiter = Planet("Jupiter", 180, "brown", 0.004)
saturn = Planet("Saturn", 230, "pink", 0.0036)
uranus = Planet("Uranus", 250, "light blue", 0.0032)
neptune = Planet("Neptune", 280, "black", 0.001)

myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


def update_planet_name(x, y):
    pass  # Kosongkan fungsi agar tidak melakukan apa-apa


turtle.onscreenclick(update_planet_name)

# Tambahkan event listener untuk menutup jendela ketika tombol "q" ditekan
screen.listen()
screen.onkey(screen.bye, "q")

while True:
    screen.update()
    for planet in myList:
        planet.move()
        planet.angle += planet.speed
