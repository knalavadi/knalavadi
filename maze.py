import turtle 

FIRST_LINE_HORIZ = (-250,-200)
SECOND_LINE_HORIZ= (-250,-150)
THIRD_LINE_VERT = (-150,0)
FOURTH_LINE_VERT = (-100,50)
FIFTH_LINE_HORIZ = (-150,0)


turtle.setup(500,500)	# set the window size to 500 by 500 pixels
wn = turtle.Screen()
krisha = turtle.Turtle()


krisha.pensize(3)
krisha.pencolor("#00bfff")

krisha.penup()

krisha.setposition(FIRST_LINE_HORIZ)
krisha.pendown()
krisha.forward(150)
krisha.penup()

krisha.setposition(SECOND_LINE_HORIZ)
krisha.pendown()
krisha.forward(100)
krisha.penup()

krisha.setposition(THIRD_LINE_VERT)
krisha.pendown()
krisha.right(90)
krisha.forward(150)
krisha.penup()

krisha.setposition(FOURTH_LINE_VERT)
krisha.pendown()
krisha.forward(250)
krisha.penup()

krisha.setposition(FIFTH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(50)
krisha.penup()
turtle.mainloop()