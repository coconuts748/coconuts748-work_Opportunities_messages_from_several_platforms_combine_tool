import tkinter as tk
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import ast
import textwrap
from urllib.parse import unquote,quote
import requests
from bs4 import BeautifulSoup
import re
from tkinter import messagebox

total_search_content = []

def preparation():
    print('chrome_driver_running.......')

    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options,service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def preparation_head_less():
    print('chrome_driver_headless_running.......')

    options = ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    chrome = webdriver.Chrome(options=options,service=Service('chromedriver.exe'))
    chrome.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
        'source': 'Object.defineProperty(navigable, "webdriver", {get: () => undefined})"'
    })
    return chrome

def show_search_content():
    print('整理数据中......')
    def inner_show_search_content():
        with open('search_result.txt', 'a', encoding='utf-8') as f:
            try:
                f.write(str(total_search_content))
            except TypeError or ValueError:
                messagebox.showinfo('提示','系统错误')

        if messagebox.askyesno('提示','是否完成查看?'):
            messagebox.showinfo('提示','相关信息以成功储存,现可查看!!')
            inner_show_search_content_root.destroy()

    inner_show_search_content_root = tk.Tk()
    inner_show_search_content_root.title('搜索结果')

    inner_show_search_content_button = tk.Button(inner_show_search_content_root,text='完成查看',command=inner_show_search_content)
    inner_show_search_content_button.pack()

    inner_show_search_content_root.mainloop()
