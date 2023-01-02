from turtle import*
bgcolor("black")
right(90)
pos=[(-50,50),(30,50)]
for x,y in pos:
    up()
    goto(x,y)
    down()
    fillcolor("dark red")
    begin_fill()

    for i in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()
up()
goto(-50,50)
down()
left(22)
fillcolor('red')
begin_fill()
for i in range(2):
    forward(217)
    left(68)
    forward(40)

     op()
