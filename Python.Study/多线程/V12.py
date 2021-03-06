"""
使用多线程去播放两个播放列表，一个是movie，一个是music
_thread
threading
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


def thread_run():
    t1 = thread.Thread(target=play, args=(movie_list,))
    t2 = thread.Thread(target=play, args=(music_list,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    thread_run()
