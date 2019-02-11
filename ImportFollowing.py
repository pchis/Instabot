# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:06:47 2019

@author: PChis
"""
#First, open up instagram and open up your "following" tab.
import pyautogui
#import sys
import pyperclip
#import unittest
#import ChromeOptions
import time
import win32api
from selenium import webdriver
import selenium.webdriver.chrome.service as service

#PATH = 'C:\Users\PChis\Anaconda3'
#options = new ChromeOptions();
#options.setBinary(PATH);
#driver = webdriver.Chrome()
counter = 0
#howmuchscroll = -650
totalscroll = 0
test = []
print(pyclip.paste())
for i in range(2410):
    pyautogui.moveTo(1331, 657)
    pyautogui.dragTo(1132, 655, button = 'left')
    pyautogui.hotkey('ctrl','c')
    #pyautogui.keyDown('ctrl')
    #pyautogui.keyDown('c')
    #pyautogui.keyUp('c')
    #pyautogui.keyUp('ctrl')
    test.append(pyperclip.paste())
    counter = counter+1
    
    if i % 5 == 0:
        pyautogui.hscroll(-64)
    else:
        pyautogui.hscroll(-65)
    #pyautogui.hscroll(howmuchscroll)
    #totalscroll += howmuchscroll
    #print(test)
   # print(i)
#Scroll one down
#win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)
#driver.executeScript("window.scrollTo(0, document.body.scrollHeight)")