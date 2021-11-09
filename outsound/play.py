from threading import *
import time
from playsound import playsound
import pyaudio
import wave
# 定义数据流块
CHUNK = 1024
class MyThread(Thread):
    def init(self,filename):
        self.wf = wave.open(filename, 'rb')  # (sys.argv[1], 'rb')
        self.p = pyaudio.PyAudio()  # 创建一个播放器
    # def init(self,filename):
        # 打开数据流
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                             channels=self.wf.getnchannels(),
                             rate=self.wf.getframerate(),
                             output=True)
        # 读取数据
        self.data = self.wf.readframes(CHUNK)

        self.__flag =  Event()  # 用于暂停线程的标识
        self.__flag.set()
        self.ifdo = True

    def run (self):

        while self.ifdo and self.data != '' :
            self.__flag.wait()
            print('I am running...')
            # time.sleep(2)

            # 播放
            self.stream.write(self.data)
            self.data = self.wf.readframes(CHUNK)
        # self.data = ''
    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞
        print("pause")

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞
        print("resume")
    def stop (self):
        print('I am stopping it...')
        self.ifdo = False
    # def restart(self):
    #     self.ifdo


if __name__ == "__main__":
    tr = MyThread()
    tr.init("outsound\\alarm.wav")
    # tr.setDaemon(True)
    tr.start()
    time.sleep(3)
    tr.stop()