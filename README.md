# Hello-World
# - Alvaro Alejandro Cabañas Calvillo 
# - ITD 
# - Ags
# Equipo 2
## **Semana Tec**

🥇
🎱
✈️
🩹

🍓
# 2. Tipos de letra

**bold text**

*initialized text*

>Block

>Hola

>Bye

# 3. Lista enumerada
1. Gorditas Doña Tota, Cd. Victoria
2. Tortas de la Barda, Tampico
3. La Parroquia, Veracruz
4. Chilaquiles Tec - ITESM

# 4. LISTA DE VIÑETAS
-  Tacos Güero
-  Tacos la Morelense
-  Tacos el Porton


# 5. Código

```Python 

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

```

# 6. Regla
------

# 7. Link
- [Mark](https://www.markdownguide.org/cheat-sheet/)
- [Git](https://docs.github.com/es/get-started/start-your-journey/hello-world)
# 8. Imagenes
 ![Feria SNM](https://www.mexicodesconocido.com.mx/sites/default/files/nodes/inline/feria-san-marcos-aguascalientes-2016-2.jpg)


# 9. Tabla

| Materia | Periodo|
| ----------- | ----------- |
| Modelacion de Negocios | PRIMER |
| Administración de datos| SEGUNDO |

# 10. Lista de equipo
- [x] Alvaro Cabañas
- [ ] Update the website
- [ ] Contact the media

