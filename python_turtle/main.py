import turtle

t = turtle.Turtle()

t.color("white", "grey")
t.getscreen().bgcolor("black")

def square(a: int):
    t.begin_fill()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()

colors: list[str] = ["red","orange","yellow", "green","blue","purple"]

t.speed(0)
i: int = 0
a: int = 0
while True:
    t.forward(i)
    t.left(i * 120)
    if i % 3 == 0:
        t.left(120)
        if i % 60 == 0:
            for j in range(6):
                t.forward(i)
                t.left(60)
            a += 1
            t.color(colors[a%6])
    i = i + 1