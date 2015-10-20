import turtle 


turtle.setup(1000,1000)
wn = turtle.Screen()
krisha = turtle.Turtle()
turtleCursor = (-210,500)


#pensize, pencolor, speed of maze drawn
krisha.pensize(10)
krisha.pencolor("#00afff") 
krisha.speed(8)

#draws sprial 

for i in range(12):
    krisha.forward(i * 35)
    krisha.right(90)


#cursor
# krisha.setposition(turtleCursor)
screen = turtle.getscreen()
krisha.setposition(turtleCursor)
def gotoandprint(x,y):
  if(-5 <= x <= 5 and 0 <= y <= -40): #vertical - line 1 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (-75 <= x <= 5 and -40 <= y <= -30): # horizontal - line 2 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"
  
  elif (-75 <= x <= -65 and -40 <= y <= 75): #vertical-  line 3 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (-75 <= x <= 75 and 65 <= y <= 75): #horizontal - line 4 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (65 <= x <= 75 and -105 <= y <= 75): # vertical - line 5 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (-145 <= x <= 75 and -105 <= y <= -95): # horizontal - line  6
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (-145 <= x <= -135 and -105 <= y <= 145): # vertical - line 7
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (-145 <= x <= 145 and 135 <= y <= 145): #horizontal - line 8 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  elif (135 <= x <= 145 and -174 <= y <= 145):  #vertical - line 9 
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"

  #   # gotoresult = turtle.goto(x, y)
  #   # print(turtle.xcor(), turtle.ycor())
  #   # return gotoresult
  

  else:
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

screen.onscreenclick(gotoandprint)


def intersection(topPoint, turtlePoint, bottomPoint):
  print "topPoint: ", topPoint
  print "bottomPoint: ", bottomPoint
  print "turtle.pos(): ", turtle.pos()
  print "turlePoint.xcor(): ", turtlePoint.xcor()
  print "turlePoint.ycor(): ", turtlePoint.ycor()
  if turtlePoint.xcor() <= max(topPoint[0], bottomPoint[0]) and turtlePoint.xcor() >= min(topPoint[0], bottomPoint[0]) and turtlePoint.ycor() <= max(topPoint[1], bottomPoint[1]) and turtlePoint.ycor() >= min(topPoint[1], bottomPoint[1]):
    print "hit boundary"
  if turtlePoint.xcor() > -450 and turtlePoint.xcor()< -350  and turtlePoint.ycor < -300  and turtlePoint.ycor > -350:
    pass
   
turtle.mainloop()  
turtle.done()









