#Space Invaders

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#pointBox = turtle.Turtle()
#pointBox.color("white")
#pointBox.shape("square")
#pointBox.write("hello", align = "left")

points = 0


# Player Creation
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

enemyNo = 20

enemies = []

enemyX = -250
enemyY = 250

for i in range(enemyNo):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)


	if enemyX > 249 or enemyX < -280:
		enemy.setposition(enemyX, enemyY)
		enemyX = -250
		enemyY -= 40
	else:
		enemy.setposition(enemyX, enemyY)
		enemyX += 100

enemySpeed = 10

#Create bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

bulletState = "ready"

def move_left():
	x = player.xcor()
	x -= playerSpeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerSpeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletState
	if bulletState == "ready":
		bulletState = "fire"
		x = player.xcor()
		y = player.ycor()
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
	if distance < 15:
		return True
	else:
		return False


# Key Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:

	s = 0

	#Move Enemies
	for enemy in enemies:
		x = enemy.xcor()
		x += enemySpeed
		enemy.setx(x)
		s += 1

		if enemy.xcor() > 280:
			for enemy in enemies:
				y = enemy.ycor()
				y -= 40
				enemy.sety(y)
			enemySpeed *= -1

		if enemy.xcor() < -280:
			for enemy in enemies:
				y = enemy.ycor()
				y -= 40
				enemy.sety(y)
			enemySpeed *= -1

		#move bullet
		yBullet = bullet.ycor()
		yBullet += bulletSpeed
		bullet.sety(yBullet)

		if bullet.ycor() > 275:
			bullet.hideturtle()
			bulletState = "ready"

		for enemy in enemies:
			if isCollision(bullet, enemy):
				bullet.hideturtle()
				bulletState = "ready"
				bullet.setposition(0, -400)

				enemy.hideturtle()
				enemy.setposition(0, 500)
				points += 100

		if isCollision(player, enemy) or enemy.ycor() < -250:
			print ("Game Over")

delay = input("Press Enter to Continue")