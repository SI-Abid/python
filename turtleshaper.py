import turtle

def draw_square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)

pos_init=turtle.pos()
turtle.setpos(pos_init[0]-25,pos_init[1])
colors=['red', 'blue', 'purple', 'green', 'yellow']
density=100
turtle.speed(10)

for n in range(int(density/len(colors))):
    for c in colors:
        turtle.color(c)
        draw_square(200)
        turtle.rt(360/density)

turtle.exitonclick()
