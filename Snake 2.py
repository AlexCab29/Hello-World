"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import  choice, randrange
from turtle import *

from freegames import square, vector

#se inicializan las variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
counter = 0

snake_color = 'black'
food_color = 'green'

# Definir un objeto de tipo turtle para escribir información de los alumnos
writer = Turtle(visible=False)


def info_alumnos():
    writer.up()
    writer.goto(-100, 190)
    writer.color('blue')
    writer.write("Alejandro Guzman Bortoni A01704787", align = 'left', font=("chalkboard", 15, "normal"))
    writer.goto(-100, 170)
    writer.color('red')
    writer.write("Alvaro Cabañas A01625742",  align = 'left', font=("chalkboard", 15, "normal"))
    writer.goto(-100, 150)
    writer.color('green')
    writer.write("Sebastian Peñafiel A01198539",  align = 'left', font=("chalkboard", 15, "normal"))


#se definen las funciones
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


#se verifica si la cabeza de la serpiente esta dentro de los limites
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food(counter, food):
    """Move food to a random position."""
    if counter % 12 == 0 and counter != 0:
        direc = [vector(10,0), vector(-10, 0), vector(0, 10), vector(0, -10)]
        food += choice(direc)
        if not inside(food):
            food -= choice(direc)
    if food in snake:
        food += choice(direc)
        if not inside(food):
            food -= choice(direc)
        
        

#se define la funcion para mover la serpiente
def move():
    """Move snake forward one segment."""
    global counter
    head = snake[-1].copy()
    head.move(aim)

    counter += 1

    #se verifica si la serpiente ha chocado con los bordes o con ella misma
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    #se verifica si la serpiente ha comido la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

        # Asignar un nuevo color aleatorio a la comida
        global food_color
        global snake_color
        food_color = (randrange(256)/255, randrange(256)/255, randrange(256)/255)
        snake_color = (randrange(256)/255, randrange(256)/255, randrange(256)/255) 
    else:
        snake.pop(0)
    #se limpia la pantalla
    clear()
    #se dibuja el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)
    # Dibujar un círculo para la comida en lugar de un cuadrado
    move_food(counter, food)
    up()
    goto(food.x, food.y)
    dot(9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
title("Sebastian Peñafiel, Alejandro Guzman, Alvaro Cabañas")  # Cambiar el título de la ventana
info_alumnos()
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()