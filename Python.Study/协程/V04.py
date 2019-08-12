"""
使用协程去播放两个播放列表，一个是movie，一个是music
类的方式完成
多进程 multiprocessing 去完成
"""
import asyncio

movie_list = ["复仇者.mp4", "钢铁侠.avi", "斗破.rmvb", "xxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


async def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("正在播放{}".format(i))
            await asyncio.sleep(3)
        if i.split(".")[1] in music_format:
            print("正在播放{}".format(i))
            await asyncio.sleep(3)
        else:
            print("播放列表为空")


loop = asyncio.get_event_loop()
task = [play(movie_list), play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()
