# Online-classes-automation-in-Mac-Os
Educational tutorial on how to automate your online classes in Mac OS with python and selenium
## Preparation
First of all this is for Mac, make sure you have the latest release of homebrew and latest release of python installed via homebrew. Coding in python is minimal part of this tutorial its more about how to use different Mac OS	tools.

Any ways you need to install in your terminal Selenium and appscript, remember its with `pip3 install "name"`

You also need to install the chromedrivers for selenium in hombres with `brew cask install chromedriver`
We are using goole chrome with selenium, this script its custom made for chrome so it will only work in chrome. 

If you are using an IDE like I am using pycharm, you also need to install selenium and appscript in your pycharm terminal for testing.

## How to adapt script
```
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
``` 
For security reasons Chrome or any other browser asks if you want to open an app, unfortunately AFAIK there’s no way to accept this prompt other than with python GUI, but it isn’t as reliable. So to overcome this the scripts creates and stores a chrome profile for selenium. There use to be a tick box that said always open the app from this site but for some reason is gone, to gain it back you need to run this on your Macs terminal

`defaults write com.google.Chrome ExternalProtocolDialogShowAlwaysOpenCheckbox -bool true`

This brings back the tick mark, so you only need to accept the prompt manually once and it will remember to always open the app. 

`ch_options.add_argument('Path')`
In this line you need to put the path were your selenium chrome profile will be stored and opened, I stored mine in a folder inside documents, the path will be the same for all scripts because they’ll share the same user.


So you need to run one of your scripts, tick the box and click accept, then it will store the preferences in your chrome profile that the script created for selenium. When you do this you need to remove browser.close() otherwise you will not have time to tick the box and accept. Then revert the code to its original state.

Once you have your scripts ready, you need to copy and paste this script for each class, so you will multiple scripts to join your multiple classes, obviously change the zoom link for each script. Make sure to have your scripts organized in a folder with a proper name.

Then its time to open automator, automator is an app that’s already included in Mac OS, the name is pretty self explanatory. We are going to use automator to make each script an app. To do this open automator select app, then add a run shell script here you’ll have to install selenium and appscript inside this shell to idk why to do so its the same than in the terminal but add --User at the end of each pip3 install ‘name’ user, you only need to do this once and it will work with all the scripts. Once selenium and appscript are installed in the automator shell you can delete the code for installing them and type this in the automator shell

```
export PATH=/usr/local/bin:$PATH
python3 /path to where you stored your python script
```


Then save the automator app with the name of the online class its attached to, for example math for the script with the link to my math class. Create an automator app for each script, (each class)

## Final steps

Then you’ll have to open the normal calendar app included with Mac OS and create an event for each class in one week. Then for each class of the week create an alert, custom , open app and select the app you created for that class and select at time of event so it triggers when your class starts. This is very useful cause it on the native Mac OS so it works flawlessly and its very reliable, a plus is that it sends and alert to all your devices so you can now in your iPhone that your class started and that your Mac connected to it.

## Extra steps
To fake a virtual camera use webcamoid I believe you need to disable SIP in order for it to work (google how to disable SIP) In webcamoid use an old recording of you and configure Zoom to use that virtual cam instead of the face time one. Make sure to open each app manually at least once to grant access to keystrokes.

In energy saver configure your Mac to turn on at the time your early class starts, make sure you leave your laptop connected to power otherwise it wont start. Use an app like amphetamine to avoid your Mac to sleep, or configure it from powersaver.

Also configure	webcamoid to start at login other wise it will show a weird screen as your camera.

Finally this is just a fun project that grants me a bit more sleep in the case I need it, im personally waking up early to attend classes, this just makes switching zoom rooms effortless and its also a safe net. Attend your classes don’t cheat and I hope this was a fun project for you too.

Also im not an expert, Im a beginner in my second semester in computer science school didn’t tech me how to do any of this in fact they haven’t teach me lots of useful things for my career yet. Im pretty sure there’s another way to make this better and I know its not only a script to do all but this is how I did it. And sorry for grammar or if it isn’t very clear English its not my native tongue, im from México and live in México. Good luck with COVID, keep your elder relatives safe.
