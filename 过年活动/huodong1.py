# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:14:35 2021

@author: ZiyaoHe
"""


#稳定版， 优点：不需要樱饼 缺点：需要空出电脑
#选择一个窗口然后输出它的大小
import win32gui
import pyautogui 
import time

#记得要以管理员的身份运行

#import win32api
#titlename = "阴阳师-网易游戏"
#几秒打完御魂？
#start2check=43
##get screen 
#hwnd = win32gui.FindWindow(0, titlename)
##get 阴阳师 window position
#left, top, right, bottom = win32gui.GetWindowRect(hwnd)
#pyautogui.click([left+100,top+15],clicks=1) 
#print(left,top,right,bottom)
#模板匹配： https://blog.csdn.net/zhuisui_woxin/article/details/84400439

#从后台打开游戏
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setforegroundwindow
#win32gui.SetForegroundWindow(hwnd)
def findAndClick(coord):
    #选择随机点
    import random
    x=random.uniform(coord.left,coord.left+coord.width)
    y=random.uniform(coord.top,coord.top+coord.height)
    #移动鼠标
    pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)  
   
    time.sleep(1)
    pyautogui.click(clicks=2, interval=1) 
while (True):
    #定义开始
    coord=pyautogui.locateOnScreen('tiaozhan.png')
    if(coord!=None):
        findAndClick(coord)
    #    print(coord)
    #    print(x)
        #time.sleep(start2check)
        #continue
        coord1=pyautogui.locateOnScreen('dianji.png')
        while(coord1==None):#没等到继续挑战
            time.sleep(0.5)
            coord1=pyautogui.locateOnScreen('hun.png')
        #点击继续挑战
        time.sleep(1)
        findAndClick(coord1)
       
    else:
        time.sleep(1)
        coord1=pyautogui.locateOnScreen('tiaozhan.png')
        if(coord1!=None):
            findAndClick(coord1)
            coord=coord1
        coord2=pyautogui.locateOnScreen('hun.png')
        if(coord2!=None):
            findAndClick(coord2)
        print("没找到")