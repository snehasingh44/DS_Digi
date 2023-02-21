from turtle import *
for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        lt(60)                   #use rt and lt
        write(i, font=("Arial", 10))
    rt(60)

hideturtle()
mainloop()

#another
from turtle import *
for i in range(6):
    fd(100)
    for i in range(6):
        fd(50)
        for i in range(6):
            fd(25)
            dot(10)
            lt(60)
        lt(60)                   #use rt and lt
    rt(60)

hideturtle()
mainloop()