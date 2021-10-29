import sounddevice as sd
import os
import soundfile
import threading

# 使用 sox 修改音频属性
# sox -V xx.wav -n
# 复制一份wav文件保存audio_ok_name, 利用sox调整参数：通道-1 位-16 采样率-16k
# subprocess.call(["sox {} -r 16000 -b 16 -c 1 {}".format(audio_name, audio_ok_name)], shell=True)

DATA_TYPE = "float32"

def query_output_id(name):

    # 查询当前主机能用的声卡声道
    devices_list = sd.query_devices()  # 返回一个列表
    out_list = []
    for index,device_msg_dict in enumerate(devices_list):
        if name in device_msg_dict["name"] and device_msg_dict["max_output_channels"] > 0 and device_msg_dict["hostapi"] == 0:
            out_list.append(index)
    
    return out_list

# ======================
# 播放函数，用于多线程调用
# 输入：音频数据，
def play_on_usb(audio_data,stream_object):
    stream_object.write(audio_data)

def rawfile(outid,filepath):
    files = []
    streams = []

    for file_path,out in zip(filepath,outid):
        audio_data , samplerate = soundfile.read(file_path,dtype=DATA_TYPE)
        files.append(audio_data)
        output = sd.OutputStream(device=out,dtype=DATA_TYPE,samplerate=samplerate)
        output.start()
        streams.append(output)

    return files,streams

def main():
    outputid = query_output_id("JieLi AC46")
    print(outputid)
    file_path = []
    file_path.append(os.getcwd() + "\\3.wav") 
    file_path.append(os.getcwd() + "\\1.wav") 
    print(file_path)
    
    files,streams = rawfile(outputid,file_path)

    print("playing!")

    # 创建线程，注意for in zip的用法
    # zip将两个序列压缩成一个对象，返回一个列表
    # for in将zip列表中的值分别赋给变量
    # 
    threads = [threading.Thread(target=play_on_usb, args = [filepath,stream]) for filepath,stream in zip(files,streams)]
    for thread in threads:
        thread.start()
    
    for thread,device_index in zip(threads, outputid):
        print("Waiting for device", device_index,"to finish!")
        thread.join()
   
if __name__ == "__main__":
    main()
