"""
使用多线程去播放两个播放列表，一个是movie，一个是music
类的方式完成
多进程 mutilprocession 去完成
"""
import threading as thread
import time

movie_list = ["复仇者.mp4", "钢铁侠.avi", "斗破.rmvb", "xxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("正在播放{}".format(i))
            time.sleep(3)
        if i.split(".")[1] in music_format:
            print("正在播放{}".format(i))
            time.sleep(3)
        else:
            print("播放列表为空")


class MyThread(thread.Thread):
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def run(self):
        play(self.playlist)


if __name__ == "__main__":
    m1 = MyThread(movie_list)
    m2 = MyThread(music_list)
    m1.start()
    m2.start()
