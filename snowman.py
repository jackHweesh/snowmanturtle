import turtle as t

#setting
t.bgcolor("lightBlue")

#first body
t.pensize(5)
t.penup()
t.right(90)
t.forward(170)
t.left(90)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(60)
t.end_fill()
t.color("black")
t.circle(60)

#second body
t.penup()
t.left(90)
t.forward(110)
t.right(90)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(50)
t.end_fill()
t.color("black")
t.circle(50)

#head
t.penup()
t.left(90)
t.forward(90)
t.right(90)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(40)
t.end_fill()
t.color("black")
t.circle(40)

#eye1
t.penup()
t.goto(-10, 35)

t.penup()
t.left(90)
t.forward(60)
t.left(90) 
t.forward(10)
t.begin_fill()
t.circle(5)
t.end_fill()

#eye2
t.penup()
t.goto(10, 35)

t.penup()
t.right(90)
t.forward(60)
t.left(90) 
t.forward(10)
t.begin_fill()
t.circle(5)
t.end_fill()

#mouth
t.penup()
t.goto(-20, 60)
t.pendown()
t.left(90)
t.circle(20,180)

#button1
t.penup()
t.color("green")
t.goto(0,0)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

#button2
t.penup()
t.goto(0, -20)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

#button3
t.penup()
t.goto(0, -40)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

#right arm
t.penup()
t.goto(50, 0)
t.pensize(10)
t.color("brown")
t.pendown()
t.right(60)
t.forward(90)
t.backward(20)
t.left(40)
t.forward(30)
t.backward(30)
t.right(70)
t.forward(30)

#left arm
t.penup()
t.goto(-50,0)
t.pendown()
t.left(180)
t.forward(90)
t.backward(20)
t.left(40)
t.forward(30)
t.backward(30)
t.right(70)
t.forward(30)

#hat
t.penup()
t.goto(0, 110)
t.pensize(5)
t.color("darkBlue")
t.pendown()
t.left(30)

t.begin_fill()
t.forward(50)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(50)
t.right(90)
t.forward(60)
t.right(90)
t.forward(50)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(50)
t.end_fill()


#hat new color
t.penup()
t.goto(0, 110)
t.pensize(5)
t.color("purple")
t.pensize(10)
t.pendown()

t.forward(50)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(50)
t.right(90)
t.forward(60)
t.right(90)
t.forward(50)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(50)

hideturtle()