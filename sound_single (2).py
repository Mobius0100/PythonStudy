# encoding:utf-8
import sounddevice as sd
import os
import soundfile

def queryOutputId(name):

    # 查询声卡声道
    devicesList = sd.query_devices()  # 返回一个列表
    outList = []
    for index,device_msg_dict in enumerate(devicesList):
        if name in device_msg_dict["name"] and device_msg_dict["max_output_channels"] > 0 and device_msg_dict["hostapi"] == 0:
            outList.append(index)
    
    return outList

def main():
    outPutId = queryOutputId("JieLi AC46")
    print(outPutId)
    filePath = []
    filePath.append(os.getcwd() + "/Alarm.wav") 
    filePath.append(os.getcwd() + "/piku.wav") 
    print(filePath)

    for index,id in enumerate(outPutId):
        sd.default.device[1] = id            # 系统默认输出
        dataArray , sampleRate = soundfile.read(filePath[index])
        print(sampleRate)
        sd.play(dataArray,samplerate=48000,blocking=True)

if __name__ == "__main__":
    main()
