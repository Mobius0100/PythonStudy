# Socket编程

## 基本流程
服务端：
```python
    ss = socket()    #创建套接字
    ss.bind()        #绑定地址与端口
    ss.listen()      #监听连接

    inf_loop:        #循环工作
        cs = ss.accept()    # 收到客户端连接
        loop:               # 客户端与服务端通信过程
            cs.recv()/ cs.send()
        cs.close()
    ss.close()
```
客户端：
```python
    cs = socket()  # 创建套接字
    cs.connetc()   # 连接服务器
    loop:          # 通信过程
        cs.send() / cs.recv()  
    cs.close()
```
## UDP不同函数
```python
    ss = socket()
    ss.bind()
    inloop:
        cs = ss.recvfrom() / ss.sendto()     # 接受或发送数据
    ss.close()
```
## 编码注意事项
1. 传输需要传字节byte，而不是str
2. BUFFSIZ用来控制缓冲区大小
3. 注意from import 和import的区别，前者调用函数时不需要写库名

## 计算机防火墙设置
如果处于同一网段的两台机器无法相互ping通，则有可能是防火墙设置问题
### Windows设置
控制面板-Defender防火墙-高级设置-入站规则
将**文件和打印机共享-回显请求-ICMPv4/6-in**启用

网络高级共享设置里将**启用网络发现**和**启用文件和打印机共享**打开

## 使用settimeout设置超时异常

