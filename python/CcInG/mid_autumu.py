import random
import turtle
import time


def love(x, y):  # 在(x,y)处画爱心
    lv = turtle.Turtle()
    lv.hideturtle()
    lv.up()
    lv.goto(x, y)  # 定位到(x,y)

    def curvemove():
        for i in range(20):
            lv.right(10)
            lv.forward(2)

    lv.color('red', 'pink')
    lv.speed(100)
    lv.pensize(1)
    lv.down()
    lv.begin_fill()
    lv.left(140)
    lv.forward(23)
    curvemove()
    lv.left(120)
    curvemove()
    lv.forward(22)
    lv.write("中秋节快乐", font=("Arial", 12, "normal"),
             align="center")  

    lv.left(140)  # 画完复位
    lv.end_fill()


def tree(branchLen, t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
            t.pensize(random.uniform((branchLen + 5) /
                      4 - 2, (branchLen + 6) / 4 + 5))
            t.down()
            t.forward(branchLen)
            love(t.xcor(), t.ycor())  # 传输现在turtle的坐标
            t.up()
            t.backward(branchLen)
            t.color("brown")
            time.sleep(0.01)
            return

        t.pensize(random.uniform((branchLen+5)/4-2, (branchLen+6)/4+5))
        t.down()
        t.forward(branchLen)

        # 以下递归
        ang = random.uniform(15, 45)
        t.right(ang)
        tree(branchLen-random.uniform(12, 16), t)  # 随机决定减小长度
        t.left(2*ang)
        tree(branchLen-random.uniform(12, 16), t)  # 随机决定减小长度
        t.right(ang)
        t.up()
        t.backward(branchLen)


if __name__ == '__main__':
    myWin = turtle.Screen()
    turtle.tracer(False)
    turtle.title("中科合迅-电子仿真部祝福")
    t = turtle.Turtle()
    myWin.screensize(800,600,"white")
    t.hideturtle()
    t.speed(1000)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    t.pensize(32)
    t.forward(60)
    tree(100, t)
    myWin.exitonclick()
