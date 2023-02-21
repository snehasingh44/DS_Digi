from turtle import *
speed(6)
fillcolor("pink")
pencolor("black")
side= 5

for i in range(side):
    fd(150)
    begin_fill()
    for i in range(side):
        fd(50)
        for i in range(side):
            fd(25)
            dot(10)
            rt(360/side)
        end_fill()
        lt(360/side)                   #use rt and lt
    rt(360/side)
hideturtle()
mainloop()