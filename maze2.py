import turtle 

turtle.setup(1500,1500)	# set the window size to 1000 by 1000 pixels
wn = turtle.Screen()
krisha = turtle.Turtle()
turtleCursor = (0,0)


Maze_Lines =(
	((0,0), (125,0)), #first line horizontal
	((0,-25), (150,-25)), #second line

	((125,0), (125, 150)), #third line vertical
	((150,-25), (150,125)), #fourth line

	((125,150), (275, 150)), #fifth line horizontal
	((150,125), (300, 125)), #sixth line

	((275, 150), (275, 300)), #seventh line vertical 
	((300, 125), (300, 275)), # eighth line

	((275, 300), (450, 300)), #nineth line horizontal high point 
	((300,275), (425, 275)), #tenth line

	((450,300), (450, 150)), #eleventh line  vertical down 
	((425, 275), (425, 125)), #twelveth Line 

	((450,150), (600, 150)), #thirteenth line horizontal 
	((425,125), (575, 125)), #fourteenth line 

	((600,150), (600, 0)), #fifthteenth line vertical 
	((575,125), (575, -25)), #sixteenth line 

	((600,0), (750, 0)), #seventeenth line horizontal
	((575,-25), (725, -25)), #eighteenth line 

	((750,0), (750, -150)), #nineteenth line vertical
	((725,-25), (725, -175)), #twentieth line 

	)



krisha.setposition(Maze_Lines[0][0])
krisha.pendown()
krisha.goto(Maze_Lines[1][1])
krisha.penup()

for line in Maze_Lines:
	origin = line[0]
	terminus = line[1]
	turtle.goto(origin)
	turtle.pendown()
	turtle.goto(terminus)
	turtle.penup()


	# or_x = origin[0]
	# or_y = origin[1]
	# ter_x = terminus[0]
	# ter_y = terminus[1]

screen = turtle.getscreen()
krisha.setposition(turtleCursor)
def gotoandprint(x,y):
  if(0 <= x <= 150 and -25 <= y <= 0): #vertical - line 1 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (125 <= x <= 150 and 0 <= y <= 150): # horizontal - line 2 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult
  
  elif (125 <= x <= 300 and 125<= y <= 150): #vertical-  line 3 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (275 <= x <= 400 and 125 <= y <= 300): #horizontal - line 4 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (275 <= x <= 400 and 125 <= y <= 300): # vertical - line 5 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (425 <= x <= 450 and 125 <= y <= 300): # horizontal - line  6
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (425 <= x <= 600 and 125 <= y <= 150): # vertical - line 7
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  elif (575 <= x <= 750 and -25 <= y <= 0): #horizontal - line 8 
 	gotoresult = turtle.goto(x, y)
 	print(turtle.xcor(), turtle.ycor())
	print (topPoint, bottomPoint)
	return gotoresult

  elif (725 <= x <= 750 and -150 <= y <= 0):  #vertical - line 9 
    gotoresult = turtle.goto(x, y)
    print(turtle.xcor(), turtle.ycor())
    print (topPoint, bottomPoint)
    return gotoresult

  #   # gotoresult = turtle.goto(x, y)
  #   # print(turtle.xcor(), turtle.ycor())
  #   # return gotoresult
  

  else:
    krisha.reset() 
    krisha.write("Game over", font=("Arial", 40, "normal")) 
    print "error"
screen.onscreenclick(gotoandprint)






# screen = turtle.getscreen()
# krisha.setposition(turtleCursor)
# def gotoandprint(x,y):
# 	gotoresult = turtle.goto(x, y)
# 	print(turtle.xcor(), turtle.ycor())
# 	return gotoresult
# screen.onscreenclick(gotoandprint)

turtle.mainloop()
