# import _thread
#
# if __name__ == "__main__":
#     try:
#         _thread.start_new_thread(print("jj"))
#     except:
#         print('')


import threading
import time

def download(i):
    print('开始下载文件%d'%i)
    time.sleep(5)
    print('文件下载完成')

def th(a,b):

    for i in range(a):  # 利用循环创建5个线程
        t = threading.Thread(target=b, args=(i,))
        print(len(threading.enumerate()))  # 查看线程数量和进程数量总和
        # 启动线程
        t.start()


if __name__=='__main__':
  th(2,download)


