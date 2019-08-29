"""
tkinter项目实战-屏保
分析：
    屏幕保护可以自己启动，也可手动启动
    一旦敲击键盘或移动鼠标，或者其他事件，则停止
    如果屏保事一幅画的话，则没有画框
    图像的运作时随机的，具有随机性，可能包括颜色、大小、数量、运动方向、变形
构成：
    ScreenSaver
        需要一个canvas,大小等于屏幕大小，没有边框
    ball
        颜色、大小、数量、运动方向、变形
        可移动，可以被调用

新需求：
    此屏保程序扩展成，一旦捕获事件，则判断屏保不退出
    显示一个Button，button上显示事件类型，点击button退出屏保
"""


import random
import tkinter
import tkinter.messagebox


class RandomBall(object):
    """
    定义运动的球的类
    """
    def __init__(self, canvas, scrnwidth, scrnheight):
        """
        canvas:画布，所有的内容都应该在画布上呈现出来，此处通过次变量传入
        scrnwidth/scrnheigh:屏幕的宽高
        """
        self.canvas = canvas
        self.item = 0

        # 球的大小随机
        # 球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 球出现的初始位置要随机，表示球的圆心的位置
        # xpos表示位置的X坐标
        self.xpos = random.randint(self.radius, int(scrnwidth)-self.radius)
        # ypos表示位置的Y坐标
        self.ypos = random.randint(self.radius, int(scrnheight)-self.radius)

        # 定义球的运动的速度
        # 模拟运动，随机运动速度，不断地擦掉原来的画，然后在新的地方从新绘制（每次移动一点）
        # 模拟X轴运动
        self.xvelocity = random.randint(4, 20)
        # 模拟Y轴运动
        self.yvelocity = random.randint(4, 20)

        # 定义屏幕的宽度
        self.scrnwidth = scrnwidth
        # 定义屏幕的高度
        self.scrnheight = scrnheight

        # 定义颜色
        # RGB表示法：三个数字每个数字值0-255之间表示红绿蓝三个颜色的大小
        # 在某些系统中，用英文单词也可以表示，比如red，green
        # 此处用lambda表达式
        def c():
            return random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        """
        用构造函数定义的变量值，在canvas上画一个球
        """
        # tkinter没有画圆形函数
        # 只有一个画椭圆函数，画椭圆需要定义两个坐标
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就行
        x1 = self.xpos - self.radius
        x2 = self.xpos + self.radius
        y1 = self.ypos - self.radius
        y2 = self.ypos + self.radius
        # fill表示填充颜色
        # outline表示边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 判断撞墙
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity *= -1
            # 也可写成self.xvelocity = -self.xvelocity
        if self.xpos - self.radius <= 0:
            self.xvelocity *= -1
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity *= -1
        if self.ypos - self.radius <= 0:
            self.yvelocity *= -1

        # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver(object):
    """
    定义屏保的类
    可以被启动
    """
    # 如何装随机产生的球
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()

        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都取消
        self.root.bind('<Motion>', self.my_button)
        # 同理按动键盘都退出屏保
        self.root.bind('<Key>', self.my_button)

        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    # 提示退出按键
    def my_button(self, e):
        # 询问是否退出
        p = tkinter.messagebox.askokcancel('提示', e)

        # 确认是否退出
        if p == True:
            self.root.destroy()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是指定毫秒后启动一个函数，需要启动的函数是第二个参数，这里用200毫秒
        # 可以理解为200毫秒动一次球
        self.canvas.after(200, self.run_screen_saver)


if __name__ == "__main__":
    ScreenSaver()
