import turtle


#izgled igraćeg okvira (boja, dimenzije)
okvir=turtle.Screen()
okvir.bgcolor('black')
okvir.setup(width=800, height=500)
okvir.tracer(0)


#lijeva ploča, tj. lijevi igrač (izgled,pozicija u okviru,...)
ploča_l=turtle.Turtle()
ploča_l.penup()
ploča_l.shape('square')
ploča_l.shapesize(stretch_wid=4, stretch_len=0.5)
ploča_l.color('white')
ploča_l.goto(-350,0)
ploča_l.speed(0)


#desna ploča, tj. desni igrač (izgled,pozicija u okviru,...)
ploča_d=turtle.Turtle()
ploča_d.penup()
ploča_d.shape('square')
ploča_d.shapesize(stretch_wid=4, stretch_len=0.5)
ploča_d.color('white')
ploča_d.goto(350,0)
ploča_d.speed(0)


#loptica (izgled,pozicija u okviru,...)
loptica=turtle.Turtle()
loptica.penup()
loptica.shape('circle')
loptica.color('white')
loptica.goto(0,0)
loptica.speed(0)
loptica.dx=0.3
loptica.dy=-0.3


#za koliko se lijeva ploča pomiče gore pritiskom tipke na tipkovnici
def ploča_l_gore():
	y=ploča_l.ycor()
	y+=20
	ploča_l.sety(y)


#za koliko se lijeva ploča pomiče dolje pritiskom tipke na tipkovnici
def ploča_l_dolje():
	y=ploča_l.ycor()
	y-=20
	ploča_l.sety(y)


#za koliko se desna ploča pomiče gore pritiskom tipke na tipkovnici
def ploča_d_gore():
	y=ploča_d.ycor()
	y+=20
	ploča_d.sety(y)


#za koliko se desna ploča pomiče dolje pritiskom tipke na tipkovnici
def ploča_d_dolje():
	y=ploča_d.ycor()
	y-=20
	ploča_d.sety(y)


#pomicanje ploča pomoću tipkovnica-kontrole igre
okvir.listen()
okvir.onkeypress(ploča_l_gore,'w')
okvir.onkeypress(ploča_l_dolje,'s')
okvir.onkeypress(ploča_d_gore,'Up')
okvir.onkeypress(ploča_d_dolje,'Down')


#zbrajanje bodova
bodovi=turtle.Turtle()
bodovi.color('white')
bodovi.penup()
bodovi.goto(0,200)
bodovi.speed(0)
bodovi.hideturtle()
bodovi.write('Igrač_1: 0   Igrač_2: 0',align='center',font=('Calibri Body',24,'normal'))


#dodavanje bodova kad ih igrač osvoji, tj. kad loptica lupi iza ploče
bodovi_1=0
bodovi_2=0


#petlja za igru
while True:
    okvir.update()	


    loptica.setx(loptica.xcor()+loptica.dx)  #pomak loptice
    loptica.sety(loptica.ycor()+loptica.dy)


    if loptica.ycor()>240:  #loptica ne može otići iz okvira na gore/dolje
        loptica.sety(240)
        loptica.dy*=-1
        
    if loptica.ycor()<-240:
        loptica.sety(-240)
        loptica.dy*=-1


    if loptica.xcor()>390:  #loptica ne može otići iz okvira lijevo/desno
        loptica.goto(0,0)
        loptica.dx*=-1
        bodovi_1+=1
        bodovi.clear()
        bodovi.write('Igrač_1: {}   Igrač_2: {}'.format(bodovi_1,bodovi_2),align='center',font=('Calibri Body',24,'normal'))

        
    if loptica.xcor()<-390:
        loptica.goto(0,0)
        loptica.dx*=-1
        bodovi_2+=1
        bodovi.clear()
        bodovi.write('Igrač_1: {}   Igrač_2: {}'.format(bodovi_1,bodovi_2),align='center',font=('Calibri Body',24,'normal'))


    if (loptica.xcor()>340 and loptica.xcor()<350) and (loptica.ycor()<ploča_d.ycor()+50 and loptica.ycor()>ploča_d.ycor()-50):  #loptica se odbija od desne ploče
        loptica.setx(340)
        loptica.dx*=-1


    if (loptica.xcor()<-340 and loptica.xcor()>-350) and (loptica.ycor()<ploča_l.ycor()+50 and loptica.ycor()>ploča_l.ycor()-50):  #loptica se odbija od lijeve ploče
        loptica.setx(-340)
        loptica.dx*=-1
        

    if bodovi_1 == 10:
        poruka=turtle.Turtle()
        poruka.color('white')
        poruka.penup()
        poruka.goto(0,0)
        poruka.speed(0)
        poruka.hideturtle()
        loptica.dx=loptica.dx/100
        loptica.dy=loptica.dy/100
        poruka.write('Igrač_1 je pobijedio!',align='center',font=('Calibri Body',30,'normal'))
        

    if bodovi_2 == 10:
        poruka=turtle.Turtle()
        poruka.color('white')
        poruka.penup()
        poruka.goto(0,0)
        poruka.speed(0)
        poruka.hideturtle()
        loptica.dx=loptica.dx/100
        loptica.dy=loptica.dy/100
        poruka.write('Igrač_2 je pobijedio!',align='center',font=('Calibri Body',30,'normal'))
 



