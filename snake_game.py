#Learning turtle
import turtle
import time
import random


delay = 0.1


#score
score = 0
high_score = 0

#setting up the screen
wn = turtle.Screen()
wn.title ("Snake Game by @ LIMOO")
wn.bgcolor ("green")
wn.setup (width=600, height=600)
wn.tracer(0)  #turns off the screen update

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)




segments = []


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGH SCORE: 0", align="center", font = ("Courier", 24, "normal"))


def go_up():
    if head.direction !="down":
        head.direction = "up"

def go_down():
    if head.direction !="up":
        head.direction = "down"

def go_left():
    if head.direction !="right":
        head.direction = "left"

def go_right():
    if head.direction !="left":
        head.direction = "right"


def move():
    if head.direction =="up":
        head.sety(head.ycor()+20)

    if head.direction =="down":
        head.sety(head.ycor()-20)

    if head.direction =="left":
        head.setx(head.xcor()-20)
    
    if head.direction =="right":
        head.setx(head.xcor()+20)


wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")



while True:
    wn.update()

    #checking for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments
        segments.clear()

        #reset score
        score = 0

        #reset the delay
        delay = 0.1

        #update the score display
        pen.clear()
        pen.write("SCORE: {}  HIGH SCORE: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal"))
    
    
    #checking for a collisiion btwn snake & food
    if head.distance(food)<20:
        #moving food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #adding a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)


        #shortening the delay
        delay -=0.001 


        #Increase the score
        score +=10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("SCORE: {}  HIGH SCORE: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal")) 

    #moving the end segment in reverse order
    for index in range (len (segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move()


    #check for head collission with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

        #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

        #clear the segments list
            segments.clear()

            #reset score
            score = 0

            #reset the delay
            delay = 0.1

            #update the score display
            pen.clear()
            pen.write("SCORE: {}  HIGH SCORE: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal"))

    time.sleep(delay)



wn.mainloop()
