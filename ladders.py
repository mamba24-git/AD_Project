## 항목수, 항목 내용, 몇번째 항목을 확인하고 싶은지 입력
pn = int(input('게임에 참가할 사람 수는?:'))
z = int(input('몇 번째 항목의 결과를 확인하시겠습니까?:'))

people = []
result = []

for i in range (0,pn):
    name = str(input('게임에 참가하는 사람의 이름을 입력해주세요:'))
    people.append(name)

def ladders():
    import turtle
    import random
    
    global pn

    ## 세로줄 그리기
    def drawcol(k):
        turtle.write(people[k], False, "center",('바탕', 10, 'bold'))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.forward(400)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        if k == 0:
            turtle.write('당첨!', False, "center",('바탕', 10, 'bold'))
        else:
            turtle.write('꽝!', False, "center",('바탕', 10, 'bold'))


    turtle.right(90)

    for j in range (0,pn):
        turtle.penup()
        turtle.goto(((j*100)-150),250)
        turtle.pendown()
        drawcol(j)

    turtle.left(90)

    points = []

    
    ## 가로줄 랜덤으로 그리기
    def drawrow():
        global pn
        x = random.randrange(-150,(100*(pn-1)-150),100)
        y = random.randrange(-190,200,10)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.forward(100)
        t = (x,y)
        points.append(t)
 
    
    for l in range (0,3*pn):
        drawrow()
        

    turtle.right(90)

    global z
    turtle.penup()
    turtle.goto(((z-1)*100-150),200)

    ## 사다리 따라서 가는것 구현
    def followline():
        global pn
        turtle.pendown()
        turtle.pencolor('red')
        if (int(turtle.xcor()),int(turtle.ycor())) in points:
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(1)
        elif (int(int(turtle.xcor())-100),int(turtle.ycor())) in points:
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(1)
        else:
            turtle.forward(1)

    ## 사다리 끝에 올 때까지 반복
    while True:
        followline()
        if int(turtle.ycor()) == -200:
            break
    turtle.penup()
    turtle.left(90)

ladders()
