import turtle 

#starting coordinates of maze lines
FIRST_LINE_HORIZ = (-450,-350)  
SECOND_LINE_HORIZ= (-450,-300) 
THIRD_LINE_VERT = (-350,-150)  
FOURTH_LINE_VERT = (-300,-100)
FIFTH_LINE_HORIZ = (-350,-150)  
SIXTH_LINE_HORIZ = (-300,-100) 
SEVENTH_LINE_VERT = (-425,-150) 
EIGTH_LINE_VERT = (-375,-100) 
NINETH_LINE_HORIZ = (-375,0) 
TENTH_LINE_HORIZ = (-425, 50) 
ELEVENTH_LINE_VERT = (-225,50) 
TWELVETH_LINE_VERT = (-175,0) 
THIRTEENTH_LINE_HORIZ = (-225,250) 
FOURTEENTH_LINE_HORIZ = (-175,200) 
FIFTEENTH_LINE_VERT = (25,200) 
SIXTEENTH_LINE_VERT = (75,250) 
SEVENTEENTH_LINE_HORIZ = (25,-50)
EIGHTEENTH_LINE_HORIZ = (75,-100)
NINETEENTH_LINE_VERT = (-125,-50)
TWENTIETH_LINE_VERT = (-75,-100)
TWENTIFIRST_LINE_HORIZ = (-75,-150)
TWENTISECOND_LINE_HORIZ = (-125,-200)
TWENTITHIRD_LINE_VERT = (25,-200)
TWENTIFOURTH_LINE_VERT = (75,-150)
TWENTIFIFTH_LINE_HORIZ = (75,-300)
TWENTISIXTH_LINE_HORIZ = (25,-250)


turtle.setup(1000,1000)	# set the window size to 1000 by 1000 pixels
wn = turtle.Screen()
krisha = turtle.Turtle()

#pen color and size
krisha.pensize(3.5)
krisha.pencolor("#00afff") 


krisha.penup()

#draws maze trajectory 
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

krisha.pencolor("#00cfff") 

krisha.setposition(FOURTH_LINE_VERT)
krisha.pendown()
krisha.forward(250)
krisha.penup()

krisha.setposition(FIFTH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(75)
krisha.penup()


krisha.setposition(SIXTH_LINE_HORIZ)
krisha.pendown()
krisha.forward(75)
krisha.penup()

krisha.setposition(SEVENTH_LINE_VERT)
krisha.pendown()
krisha.right(90)
krisha.forward(200)
krisha.penup()


krisha.pencolor("#00efff") 

krisha.setposition(EIGTH_LINE_VERT)
krisha.pendown()
krisha.forward(100)
krisha.penup()

krisha.setposition(NINETH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(200)
krisha.penup()

krisha.setposition(TENTH_LINE_HORIZ)
krisha.pendown()
krisha.forward(200)
krisha.penup()

krisha.setposition(ELEVENTH_LINE_VERT)
krisha.pendown()
krisha.left(90)
krisha.forward(200)
krisha.penup()


krisha.pencolor("#00ccdd") 

krisha.setposition(TWELVETH_LINE_VERT)
krisha.pendown()
krisha.forward(200)
krisha.penup()

krisha.setposition(THIRTEENTH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(300)
krisha.penup()

krisha.setposition(FOURTEENTH_LINE_HORIZ)
krisha.pendown()
krisha.forward(200)
krisha.penup()

krisha.setposition(FIFTEENTH_LINE_VERT)
krisha.pendown()
krisha.right(90)
krisha.forward(250)
krisha.penup()


krisha.setposition(SIXTEENTH_LINE_VERT)
krisha.pendown()
krisha.forward(350)
krisha.penup()

krisha.pencolor("#00ccbb") 

krisha.setposition(SEVENTEENTH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(150)
krisha.penup()

krisha.setposition(EIGHTEENTH_LINE_HORIZ)
krisha.pendown()
krisha.forward(150)
krisha.penup()

krisha.setposition(NINETEENTH_LINE_VERT)
krisha.pendown()
krisha.left(90)
krisha.forward(150)
krisha.penup()

krisha.setposition(TWENTIETH_LINE_VERT)
krisha.pendown()
krisha.forward(50)
krisha.penup()

krisha.pencolor("#00eeaa") 

krisha.setposition(TWENTIFIRST_LINE_HORIZ)
krisha.pendown()
krisha.left(90)
krisha.forward(150)
krisha.penup()

krisha.setposition(TWENTISECOND_LINE_HORIZ)
krisha.pendown()
krisha.forward(150)
krisha.penup()

krisha.setposition(TWENTITHIRD_LINE_VERT)
krisha.pendown()
krisha.right(90)
krisha.forward(50)
krisha.penup()

krisha.setposition(TWENTIFOURTH_LINE_VERT)
krisha.pendown()
krisha.forward(150)
krisha.penup()

krisha.setposition(TWENTIFIFTH_LINE_HORIZ)
krisha.pendown()
krisha.right(90)
krisha.forward(150)
krisha.penup()

krisha.setposition(TWENTISIXTH_LINE_HORIZ)
krisha.pendown()
# krisha.right(90)
krisha.forward(150)
krisha.penup()


#krisha.pencolor("#00ffaa") 




# krisha.pencolor("#00ff00") # last pencolor

turtle.mainloop() #keeps turtle open until user exits 