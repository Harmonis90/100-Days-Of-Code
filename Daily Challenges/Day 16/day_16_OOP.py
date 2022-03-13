from prettytable import PrettyTable
# import turtle
#
# my_turtle = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("#999999")
# my_turtle.pencolor("#82DA25")
# my_turtle.pendown()
#
#
# for i in range(4):
#     my_turtle.fd(50)
#     my_turtle.lt(90)
#
# screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

