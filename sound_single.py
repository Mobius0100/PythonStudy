import sounddevice as sd
import os
import soundfile

def query_output_id(name):

    # 查询声卡声道
    devices_list = sd.query_devices()  # 返回一个列表
    out_list = []
    for index,device_msg_dict in enumerate(devices_list):
        if name in device_msg_dict["name"] and device_msg_dict["max_output_channels"] > 0 and device_msg_dict["hostapi"] == 0:
            out_list.append(index)
    
    return out_list

def main():
    outputid = query_output_id("JieLi AC46")
    print(outputid)
    file_path = []
    file_path.append(os.getcwd() + "\\alarm.wav") 
    file_path.append(os.getcwd() + "\\3.wav") 
    print(file_path)

    for index,id in enumerate(outputid):
        sd.default.device[1] = id
        date_array , sample_rate = soundfile.read(file_path[index])
        print(sample_rate)
        sd.play(date_array,samplerate=sample_rate)
        sd.wait()

if __name__ == "__main__":
    main()
