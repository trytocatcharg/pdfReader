import random
import threading
import pyautogui
from time import sleep

import webbrowser

url = 'https://presearch.org/'
url_image_button = 'C:\AQLITE_LAST\lupa.png'
url_image_search = 'C:\AQLITE_LAST\search.png'
# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Users/MENSASDD/AppData/Local/Google/Chrome/Application/chrome.exe %s'

# http://api.stackexchange.com/docs/questions#order=desc&sort=creation&tagged=python%3Bjavascript%3Bangular&filter=default&site=stackoverflow&run=true

# Linux
# chrome_path = '/usr/bin/chromium-browser %s'


list = [5,20,45]
count_thread = 1
count_total_second = 80
# list = []
# # seconds = 86400 # seconds in day
# seconds = 120 # seconds in 2 minute
# count_thread = 32
# count_total_second = 0

# for i in range(count_thread):
#     second_random = random.randrange(1, seconds, 2)
#     list.append(second_random) 


list.sort() # order by seconds


def execute_action(sec_wait):
    # sleep(sec_wait)
    # tname = threading.current_thread().ident
    webbrowser.get(chrome_path).open(url)
    sleep(sec_wait)
    retry = 10
    count_retry = 1
#     v = None
#     while v is None:
#         v = pyautogui.locateOnScreen(url_image_search,grayscale=True) ##save the extension as image
#         count_retry = count_retry + 1
#         if count_retry == retry:
#                 print ('retry complete')
#                 break
    
#     if count_retry == retry:
#             return

    # #trigger click event using the pyutogui click method
    sleep(sec_wait)
    # pyautogui.click(x=v[0],y=v[1],clicks=1,interval=0.0,button="left")

    # sleep(sec_wait)
    rnd_type_interval = random.randrange(1, 5, 2)
    pyautogui.typewrite('Hello world!', interval=rnd_type_interval)
    
    sleep(1)
    pyautogui.press('enter')

for i in range(count_total_second):
    if i in list:
        execute_action(5)

# def deamon_master(sec_wait):
#     sleep(sec_wait)
    
# for i in range(count_thread):
#     sec = list[i]
#     hilo1 = threading.Thread(target=execute_action,
#                             args=(sec,)
#                             )
#     hilo1.start()


# hilo_master = threading.Thread(target=deamon_master,
#                          args=(count_total_second,),
#                          daemon=True)

# hilo_master.start()
    