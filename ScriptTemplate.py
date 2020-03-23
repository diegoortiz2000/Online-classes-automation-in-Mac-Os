import time
from appscript import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ch_options = Options()  # Chrome Options
ch_options.add_argument('Path')  # Profile
browser = webdriver.Chrome(options=ch_options)  # Stores a chrome profile in path
browser.get('Zoom class link')  # Opens zoom class
time.sleep(2)  # Timer to give time to chrome to open the zoom app
browser.close()  # Closes the chrome window
time.sleep(7)  # Timer to let zoom load the class
app('System Events').keystroke('\r')  # Presses enter to accept prompt in the zoom app to automatically switch class
