import turtle as t

accumulator = 0
xcoords = []
ycoords = []
r = []
g = []
b = []
listt=[]
file = open('imageData.txt', 'r')
data = file.read()
data_list = data.split('\n')
for line in data_list:
    newlist = line.split(',')
    for i in newlist:
        listt.append(int(i))
file.close()

wn = t.Screen()
wn.setup(500,500)
wn.colormode(255)
t.tracer(0)

for i in listt:
    if accumulator % 5 == 0:
        xcoords.append(i)
    elif accumulator % 5 == 1:
        ycoords.append(-i)
    elif accumulator % 5 == 2:
        r.append(i)
    elif accumulator % 5 == 3:
        g.append(i)
    elif accumulator % 5 == 4:
        b.append(i)
    accumulator += 1

pen = t.Turtle()
pen.penup()

for i in range(len(xcoords)):
    pen.goto(xcoords[i]-250, ycoords[i]+250)
    pen.color(r[i], g[i], b[i])
    pen.begin_fill()
    for j in range(4):
        pen.forward(5)
        pen.right(90)
    pen.end_fill()

t.update()
t.done()
