import turtle as t


turtle = t.Turtle()
screen = t.Screen()



def mov_forwards():
    turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=mov_forwards)

screen.exitonclick()