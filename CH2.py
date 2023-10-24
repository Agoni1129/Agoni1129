from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

root = Tk()

root.title("test")

root.geometry("350x570+100+200")

label = Label(root, text="信号与系统实验课CH2", fg="red",height=1, width=50,font=("楷体",20),pady=10)
label.pack()

label1= Label(root, text="连续信号", fg="blue",height=1, width=25,font=("楷体",16),pady=-30)
label1.pack()

label1= Label(root, text="离散信号", fg="blue",height=1, width=25,font=("楷体",16),pady=160)
label1.pack()

label2= Label(root, text="电信221张嘉译3220432011", fg="blue",height=0, width=25,font=("楷体",16),pady=350,anchor="center")
label2.pack()


btn01 = Button(root,text="阶跃信号",width=12,height=2)
btn01.pack()
btn01.place(x=50,y=100)

def jyxh(e):
#阶跃信号
    plt.title("step signal",)
    t = np.linspace(-1, 1, 500, endpoint=False)
    plt.plot(t, np.array(t>0, dtype=np.int))  
    plt.grid()
    _ = plt.ylim(-0.5, 1.5)
    plt.show()
btn01.bind("<Button-1>",jyxh)

btn06 = Button(root,text="三角函数",width=12,height=2)
btn06.pack()
btn06.place(x=200,y=100)

#连续三角函数
def jyxh(e):
    t = np.linspace(0, 0.2, 500, endpoint=True)
    A = 1
    phi = np.pi / 6
    f = 10
    plt.plot(t, A*np.sin(t * 2 * np.pi * f + phi))
    plt.title("sinusoidal signal",)
    plt.grid()
    plt.show()
btn06.bind("<Button-1>",jyxh)

btn07 = Button(root,text=" 矩形信号",width=12,height=2)
btn07.pack()
btn07.place(x=50,y=180)

# 连续矩形脉冲信号
def jyxh(e):
    def rect_wave(t, c, c0):
        if t >= (c+c0):
            r = 0.0
        elif t < c0:
            r = 0.0
        else:
            r = 1
        return r
    x = np.linspace(-4, 8, 1000)
    y = np.array([rect_wave(t, 4.0, -2.0) for t in x])
    _ = plt.ylim(-0.2, 1.2)
    plt.title("Rectangular signal",)
    plt.plot(x, y)
    plt.grid()
    plt.show()

btn07.bind("<Button-1>",jyxh)

btn08 = Button(root,text=" 指数信号",width=12,height=2)
btn08.pack()
btn08.place(x=200,y=180)

# 连续指数信号
def jyxh(e):	
        t = np.linspace(-1, 5.4, 5000, endpoint=False)
        plt.plot(t, 2*np.exp(-1*t))
        plt.title("exponential signal",)
        plt.grid()
        plt.show()

btn08.bind("<Button-1>",jyxh)

btn09 = Button(root,text=" 冲激信号",width=12,height=2)
btn09.pack()
btn09.place(x=50,y=300)

# 单位脉冲信号
def jyxh(e):

    n = np.linspace(-7, 18, 25, endpoint=False)
    x = np.append(np.zeros((1, 7)), np.ones((1, 1)))
    x = np.append(x, np.zeros((1,17)))
    plt.title("impulse signall",)
    plt.stem(n, x, use_line_collection=True)
    plt.grid()
    plt.show()


btn09.bind("<Button-1>",jyxh)

btn02 = Button(root,text="阶跃信号",width=12,height=2)
btn02.pack()
btn02.place(x=200,y=300)


#生成阶跃信号
def yxhs(e):
    n = np.linspace(-7, 18, 25, endpoint=False) 
    x = np.append(np.zeros((1,7)), np.ones((1,18))) 
    plt.title("step signal",)
    plt.stem(n, x, use_line_collection=True) 
    plt.grid()
    plt.show()
btn02.bind("<Button-1>",yxhs)

btn03 = Button(root,text="指数信号",width=12,height=2)
btn03.pack()
btn03.place(x=50,y=380)

#生成指数信号
def sjb(e):
    n = np.linspace(-5, 20, 25, endpoint=False) 
    x = 0.3*np.power(1/2, n) 
    plt.stem(n, x, use_line_collection=True) 
    plt.title("exponential signal",)
    plt.grid() 
    plt.show() 


btn03.bind("<Button-1>",sjb)

btn04 = Button(root,text="正弦信号",width=12,height=2)
btn04.pack()
btn04.place(x=200,y=380)

#生成正弦信号
def cjxh(e):
        n = np.linspace(-50, 51, 101, endpoint=False)
        omega = np.pi/10
        x = 0.3*np.sin(omega*n+ np.pi/5) 
        plt.stem(n, x, use_line_collection=True)
        plt.title("sinusoidal signal",)
        plt.grid() 
        plt.show() 


btn04.bind("<Button-1>",cjxh)

btn10 = Button(root,text="退出程序",width=12,height=2)
btn10.pack()
btn10.place(x=125,y=440)

def cjxh(e):
    sys.exit()
btn10.bind("<Button-1>",cjxh)

root.mainloop()