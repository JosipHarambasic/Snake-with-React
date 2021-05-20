import turtle
import math
import random


# set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

# set score
score = 0
# Draw Score
score_pre = turtle.Turtle()
score_pre.speed(0)
score_pre.color("white")
score_pre.penup()
score_pre.setposition(-290, 275)
scoreString = "Score: %s" % score
score_pre.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pre.hideturtle()
# Draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#hello
# movement of the player
playerSpeed = 15

numberOfEnemies = 5
enemies = []
for i in range(numberOfEnemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    # Create Enemy
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 2
# number of enemies

# Create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletState = "ready"


# move player left
def moveLeft():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def moveRight():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)


def fireBullet():
    # declare bulletState as a global if it needs change
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(fireBullet, "space")

# Main gameLoop
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        # Move enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        # Move the bullet

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            # reset the enemy
            enemy.setposition(-200, 250)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scoreString = "Score: %s" % score
            score_pre.clear()
            score_pre.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(enemy, player):
            player.hideturtle()
            print("Game Over")
            break

    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

        # check if the bullet reached the top
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletState = "ready"
