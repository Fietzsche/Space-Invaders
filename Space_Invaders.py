#Space Invaders

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")



# Player Creation
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

enemyNo = 23

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

	enemyX += 100

	if enemyX > 280:
		enemyX = -250
		enemyY -= 40
		enemy.setposition(enemyX, enemyY)
	else:
		enemy.setposition(enemyX, enemyY)

enemySpeed = 5

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

	#Move Enemies
	for enemy in enemies:
		x = enemy.xcor()
		x += enemySpeed
		enemy.setx(x)

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
				enemy.setposition(0, -500)

		if isCollision(player, enemy):
			print ("Game Over")
			break

delay = input("Press Enter to Continue")