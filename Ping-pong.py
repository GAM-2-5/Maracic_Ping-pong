import turtle

okvir=turtle.Screen()
okvir.bgcolor('black')
okvir.setup(width=800, height=500)
okvir.tracer(0)

ploča_l=turtle.Turtle()
ploča_l.shape('square')
ploča_l.shapesize(stretch_wid=4, stretch_len=0.5)
ploča_l.color('white')
ploča_l.goto(350, 0)
ploča_l.speed(0)
ploča_l.penup()

ploča_d=turtle.Turtle()
ploča_d.shape('square')
ploča_d.shapesize(stretch_wid=4, stretch_len=0.5)
ploča_d.color('white')
ploča_d.goto(-350, 0)
ploča_d.speed(0)
ploča_d.penup()

loptica=turtle.Turtle()
loptica.shape('square')
loptica.color('white')
loptica.goto(0, 0)
loptica.speed(0)
loptica.penup()

def ploča_l_gore():
    y=ploča_l.ycor()
    y+=10

def ploča_l_dolje():
    y=ploča_l.ycor()
    y-=10
    
def ploča_l_gore():
    y=ploča_l.ycor()
    y+=10

def ploča_l_dolje():
    y=ploča_l.ycor()
    y-=10

while True:
    okvir.update()
