from tkinter import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

    
bum = Tk()
bum.title("mp4saver")
bum.geometry("400x200")


def tikla():
    browser = webdriver.Chrome(executable_path="C:\\Users\\Abdullah\\Downloads\\\chromedriver_win32 (1)\\chromedriver.exe")

    browser.get("https://mp4s.org/en1/youtube-to-mp4/")
    abc = link.get()
    element=browser.find_element_by_css_selector('#form > input:nth-child(1)')
    element.send_keys(abc)
    sleep(1)
    element=browser.find_element_by_css_selector('#form > button:nth-child(2)')
    element.click()
    sleep(6)
    bot= browser.find_element_by_css_selector('#download > a:nth-child(1)')
    bot.click()
    sleep(60)
    browser.quit()

link = Entry(width = 55, justify=CENTER)
link.pack()

sb = Button(bum, text="İndir",font="impact", width = 20,command=tikla).pack()

bum.mainloop()