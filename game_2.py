import turtle
import random
import math
# import os

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Star Destroyer')
#wn.bgpic('maxresdefault.gif')

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.goto(-290,310) #just outside boarders
        self.score = 0
    def update_score(self):
        self.clear() #clear old score
        self.write('Score: {}'.format(self.score),False, align='left', font=('Arial',14,'normal'))
    def change_score(self, points):
        self.score += points
        self.update_score()
    #def play_sound(self):
        #os.system('afplay {}&'.format(filename))

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0) #draw as fast as possible
        self.color('white')
        self.pensize(5)
    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('triangle')
        self.color('white')
        self.speed = (1/2)
    def move(self):
        self.forward(self.speed)
        #border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)
    #keyboard bindings
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)
    def increasespeed(self):
        self.speed += (1/4)

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0) #animation speed
        self.color('orange')
        self.shape('circle')
        self.speed = (3/4) #movement speed
        self.goto(random.randint(-250,250), random.randint(-250,250))
        self.setheading(random.randint(0,360)) #what direction is it moving initially
    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))
    def move(self):
        self.forward(self.speed)
        #border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

#check for collision between goal and player
def is_collision(p, g):
    a = p.xcor()-g.xcor()
    b = p.ycor()-g.ycor()
    #use pythagorean theorem to measure distance between player and goal
    distance = math.sqrt((a**2)+(b**2))
    if distance < 20:
        return True
    else:
        return False

#create class instances
border = Border()
player = Player()
game = Game()

#draw border
border.draw_border()

#creating multiple goals
goals = []
for count in range(6):
    goals.append(Goal())
#set keyboard bindings
turtle.listen()
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.increasespeed, 'Up')

#speed up the game
wn.tracer(0)

#Main loop
while True:
    wn.update() #only update once per loop
    player.move()
    for goal in goals:
        goal.move()
        if is_collision(player,goal):
            goal.jump() #goal goes to a random location
            game.change_score(10)
            #game.play_sound('collision.mp3')
#add exit to game when score = 100
