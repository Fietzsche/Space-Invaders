#Space Invaders

import turtle

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

# Enemy Creation
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemySpeed = 2

while True:

	#Move Enemy
	x = enemy.xcor()
	x += enemySpeed
	enemy.setx(x)

	if enemy.xcor() > 280:
		y = enemy.ycor()
		y -= 40
		enemy.sety(y)
		enemySpeed *= -1

	if enemy.xcor() < -280:
		y = enemy.ycor()
		y -= 40
		enemy.sety(y)
		enemySpeed *= -1

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

	# Key Bindings
	turtle.listen()
	turtle.onkey(move_left, "Left")
	turtle.onkey(move_right, "Right")



screen.mainloop()