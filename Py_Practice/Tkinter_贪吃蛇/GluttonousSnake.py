"""
分析
构成：
    蛇 Snake
    食物 Food
    世界 World
思路：
    食物是一个独立的事物
    蛇是一个独立的事物
    世界也是，但世界只负责显示
"""
import random
import threading
import time
from tkinter import Tk
import tkinter
import multiprocessing


class Food(object):
    """
    功能：
        出现在画面上的某个地方
        一旦被吃增加分数
    """
    def __init__(self, queue):
        """
        自动生成一个食物
        """
        self.new_food()
        self.queue = queue

    def new_food(self):
        """
        产生一个食物
        产生一个食物的过程就是随机产生一个食物的坐标
        """
        # 注意横纵坐标的产生范围
        x = random.randrange()
        y = random.randrange()

        # postion 存放食物的位置
        self.postion = x, y

        # 队列就是一个不能够随意访问的内部元素，只能从头弹出一个元素
        # 只能从队伍为佳元素的list
        # 消息格式自己定义
        # 定义：消息是一个dict，k代表消息类型，v代表此类型的数据
        self.queue.put({"food": self.postion})


class Snake(threading.Thread):
    """
    功能：
        蛇能动，由按键控制
        蛇每次移动后需要重新计算蛇头的位置
        能检测游戏是否结束
    """
    def __init__(self, world, queue):
        threading.Thread.__init__(self)
        self.world = world
        self.queue = queue
        self.posints_earned = 0 # 游戏分数
        self.food = Food(self.queue)
        self.snake_points = [(492, 55), (485, 55), (465, 55), (455,55)]

        self.start()

    def run(self):
        """
        一旦启动多线程调用此函数
        要求蛇一直都在跑，除非游戏结束
        :return:
        """
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.5) # 控制蛇的速度
            self.move()

    def move(self):
        """
        负责蛇的移动
            计算蛇头的坐标
            当蛇头与食物相遇（重叠），则通知world加分，重新生成食物
            否则，蛇继续移动
        """
        # 重新计算蛇头位置
        new_snake_point = self.cal_new_pos()

        # 蛇头位置与食物位置重叠
        if self.food.postion == new_snake_point:
            self.posints_earned += 1
            self.queue.put({"points_earned": self.posints_earned})
            # 食物被吃了，产生新的食物
            self.food.new_food()
        else:
            # 需要注意蛇的信息保存方式
            # 每次移动都是删除存放蛇的最前位置，并在后面追加
            self.snake_posints.pop(0)
            # 判断程序是否退出，欣慰新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_posints.apped(new_snake_point)

    def cal_new_postion(self):
        """
        计算新的蛇头的位置
        :return: new_snake_point
        """
        last_x, last_y = self.snake_postion[-1]
        # direction 负责储存蛇移动的方向
        if self.direction == "Up":
            # 每次移动的跨度是10像素
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Down":
            new_snake_point == last_x, last_y - 10
        elif self.direction == "Left":
            new_snake_point == last_x + 10, last_y
        elif self.direction == "Right":
            new_snake_point == last_x - 10, last_y

        return new_snake_point

    def key_pressad(self, e):
        # keysym是按键名称
        self.dierection = e.keysym2

    def check_game_over(self, snake_point):
        """
        判断蛇头是否和墙相撞
        :param snake_point:
        :return: None
        """
        x, y = snake_point[0], snake_point[1]
        if not - 5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})


class World(Tk):
    """
    用来模拟整个游戏画板
    """
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        # 定义画板
        self.canvas = tkinter.Canvas(self, width=500, height=300, bg='red')
        self.canvas.pack()

        # 画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill='black', width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(450, 20, fill='white', text="SCORE:0")
        self.queue_handler()

    def queue_handler(self):
        try:
            # 需要不断从消息队列拿到消息，所以使用死循环
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                if task.get("move"):
                    points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇
                    self.canvas.coords(self.snake, *points)
                if task.get("food"):
                    self.postion

                # 处理食物
                # 处理得分

        except self.queue.empty:    # 爆出队列为空异常
            if not self.is_game_over:
                # after 在多少秒后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        """
        游戏结束，清理现场
        :return: None
        """
        self.is_game_over = True
        self.canvas.create_text("Game Over")
        qb = Button(self, text='Quit', command=self.destroy)
        rb = Button(self, text='Again', command=self.__init__)


if __name__ == "__main__":
    q = multiprocessing.Queue()
    world = World(q)

    snake = Snake(world, q)

    # 绑定上下左右键
    world.bind('<key-Up>', snake.key_pressad)
    world.bind('<key-Down>', snake.key_pressad)
    world.bind('<key-Left>', snake.key_pressad)
    world.bind('<key-Right>', snake.key_pressad)

    world.mainloop()

