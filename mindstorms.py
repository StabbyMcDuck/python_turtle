import turtle

def draw_square(some_turtle):
  for i in range(1,5):
    some_turtle.forward(100)
    some_turtle.right(90)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("green")
  
  # create the lil_turtle 
  lil_turtle = turtle.Turtle()
  lil_turtle.color("white")
  lil_turtle.shape("turtle")
  lil_turtle.speed("88")

  for i in range(1,37):
    draw_square(lil_turtle)
    lil_turtle.right(10)

  window.exitonclick()

draw_art()
