import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
try:
    import psutil as ps
    import pyttsx3
except Exception as e:
    print(str(e))
import webbrowser
import platform
import os
import subprocess
import threading

# Function to fetch available voices from pyttsx3 engine (SAPI 5 on Windows)
def fetch_sapi_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

# Global variable to hold the selected voice
selected_voice = None

# GUI Design
# Define the Window
window = ctk.CTk()

def restartsystem():
    os.system("shutdown /r")

def findos():
    OSName = platform.system()
    return OSName

fetchosname = findos()
engine = None
if fetchosname == 'Windows':
    try:
        engine = pyttsx3.init()
        voices = fetch_sapi_voices()
    except Exception as e:
        print(f"Error initializing TTS engine: {e}")

def fetchbatterypercent():
    global percent
    global Battery
    Battery = ps.sensors_battery()
    if Battery:
        percent = Battery.percent

    global BatteryLevelText
    BatteryLevelText.configure(text='Battery Level \n'+str(percent)+' %')
    window.after(10000, fetchbatterypercent)

def updatebatterylevel(event):
    BatteryLevelText.configure(text='Battery Level '+str(percent)+' %')
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            threading.Thread(target=speak_text, args=("Screen Refreshed!",)).start()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", "Screen Refreshed!"])
        except Exception as e:
            print(str(e))

def updatebatterylevelMenu():
    BatteryLevelText.configure(text='Battery Level '+str(percent)+' %')
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            threading.Thread(target=speak_text, args=("Screen Refreshed!",)).start()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", "Screen Refreshed!"])
        except Exception as e:
            print(str(e))

def FetchBatteryChargingStatus():
    Battery = ps.sensors_battery()
    if Battery:
        plugedinbool = Battery.power_plugged

    global chargeStatusText
    if plugedinbool:
        chargeStatusText = "Device Charging"
    else:
        chargeStatusText = "Device Not Charging"

    window.after(1000, FetchBatteryChargingStatus)

FetchBatteryChargingStatus()

def speak_text(text):
    global engine
    global selected_voice
    if engine:
        try:
            if selected_voice:
                engine.setProperty('voice', selected_voice.id)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error in TTS: {e}")
            try:
                engine = pyttsx3.init()
                if selected_voice:
                    engine.setProperty('voice', selected_voice.id)
                engine.say(text)
                engine.runAndWait()
            except Exception as e2:
                print(f"Error reinitializing TTS engine: {e2}")

def speakMenuitem():
    fetchosname = findos()
    if fetchosname == 'Windows':
        threading.Thread(target=speak_text, args=("battery Level "+str(percent)+"%",)).start()
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"battery Level "+str(percent)+"%"])
        except Exception as e:
            print(str(e))

def speak(event):
    fetchosname = findos()
    if fetchosname == 'Windows':
        threading.Thread(target=speak_text, args=("battery Level "+str(percent)+"%",)).start()
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"battery Level "+str(percent)+"%"])
        except Exception as e:
            print(str(e))

def speakChargingStatus(event):
    fetchosname = findos()
    if fetchosname == 'Windows':
        threading.Thread(target=speak_text, args=(chargeStatusText,)).start()
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"{chargeStatusText}"])
        except Exception as e:
            print(str(e))

def speakChargingStatusMenu():
    fetchosname = findos()
    if fetchosname == 'Windows':
        threading.Thread(target=speak_text, args=(chargeStatusText,)).start()
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"{chargeStatusText}"])
        except Exception as e:
            print(str(e))

def OnlineHelpMenu():
    webbrowser.open("https://sites.google.com/view/batteryviewer-low-vision/windows-app")

def OnlineHelp(event):
    webbrowser.open("https://sites.google.com/view/batteryviewer-low-vision/windows-app")

def contactus():
    webbrowser.open("https://sites.google.com/view/batteryviewer-low-vision/contact-us")

def About():
    messagebox.showinfo("About", "Battery % Viewer \n Version 9")

def KeyboardShortcutsPage():
    webbrowser.open("https://sites.google.com/view/batteryviewer-low-vision/windows-app/keyboard-shortcuts")

def Androidapp():
    webbrowser.open("https://play.google.com/store/apps/details?id=com.varunmanojkumar.batterylevel")

def smallsize():
    BatteryLevelText.configure(font=("Arial", 30, "bold"))

def DefaultSize():
    BatteryLevelText.configure(font=("Arial", 40, "bold"))

def LargeSize():
    BatteryLevelText.configure(font=("Arial", 50, "bold"))

# Function to set the selected voice
def set_voice(voice):
    global selected_voice
    selected_voice = voice
    # Optionally, notify user or update UI about voice selection
    print(f"Selected Voice: {voice.name}")

# Set Title of the Window
window.title("Battery % Viewer")
# Set Size of the Window
window.geometry("500x250")
window.minsize(400, 200)
# Set the Icon for the Window and the App
window.iconbitmap("ApIcon.ico")

# Add Widgets
# Add Menu
menubar = tk.Menu(window)
window.configure(menu=menubar)

# Menu Items
filemenu = tk.Menu(menubar, tearoff=0, font=("Arial", 20, "bold"))
menubar.add_cascade(label="File", menu=filemenu, underline=0)
filemenu.add_command(label="Refresh", command=updatebatterylevelMenu, accelerator="Command+R", underline=0)

fetchosname = findos()
if fetchosname == 'Windows':
    filemenu.add_command(label="Exit", command=window.quit, accelerator='ALT+F4', underline=0)
elif fetchosname == 'Darwin':
    filemenu.add_command(label="Exit", command=window.quit)

ViewMenu = tk.Menu(menubar, tearoff=0, font=("Arial", 20, "bold"))
menubar.add_cascade(label="View", menu=ViewMenu, underline=0)

# Create Submenu
submenu = tk.Menu(ViewMenu, tearoff=0, font=("Arial", 20, "bold"))
submenu.add_command(label="Small Font", command=smallsize, underline=0)
submenu.add_command(label="Default Font", command=DefaultSize, underline=0)
submenu.add_command(label="Large Font", command=LargeSize, underline=0)
ViewMenu.add_cascade(label="Change Font Size", menu=submenu, underline=0)

SpeakMenu = tk.Menu(menubar, tearoff=0, font=("Arial", 20, "bold"))
menubar.add_cascade(label="Speak", menu=SpeakMenu, underline=0)
SpeakMenu.add_command(label="Battery Level", command=speakMenuitem, accelerator="CTRL+S", underline=0)
SpeakMenu.add_command(label="Charging Indication", command=speakChargingStatusMenu, accelerator="CTRL+C", underline=0)

# Submenu for changing voice
if fetchosname == 'Windows':
    voices_submenu = tk.Menu(SpeakMenu, tearoff=0, font=("Arial", 20, "bold"))
    voices = fetch_sapi_voices()
    for i, voice in enumerate(voices):
        voices_submenu.add_command(label=voice.name, command=lambda v=voice: set_voice(v), underline=0)
    SpeakMenu.add_cascade(label="Change Voice", menu=voices_submenu, underline=0)

HelpMenu = tk.Menu(menubar, tearoff=0, font=("Arial", 20, "bold"))
menubar.add_cascade(label="Help", menu=HelpMenu, underline=0)
HelpMenu.add_command(label="Online Help", command=OnlineHelpMenu, accelerator="F1", underline=0)
HelpMenu.add_command(label="Keyboard Shortcuts", command=KeyboardShortcutsPage, underline=0)
HelpMenu.add_command(label="Contact US", command=contactus, underline=0)
HelpMenu.add_separator()
HelpMenu.add_command(label="About", command=About, underline=0)
HelpMenu.add_separator()
HelpMenu.add_command(label="Get Android App", command=Androidapp, underline=0)



BatteryLevelText = ctk.CTkLabel(window, font=("Arial", 50, "bold"), justify="center")
BatteryLevelText.pack(fill="x")

fetchbatterypercent()

SayBTN = ctk.CTkButton(window, text="Say", command=speak, font=("Arial", 30))
SayBTN.pack(fill="x")

rightclickmenu = tk.Menu(window, title="right Click Menu", tearoff=0, font=("Arial", 15, "bold"))
rightclickmenu.add_command(label="Speak Battery Level", command=speakMenuitem, accelerator="CTRL+S", underline=6)
rightclickmenu.add_command(label="Speak Charging Status", command=speakChargingStatusMenu, accelerator="CTRL+C", underline=6)
rightclickmenu.add_separator()
rightclickmenu.add_command(label="Refresh", command=updatebatterylevelMenu, accelerator="CTRL+R", underline=0)

def popMenuonrightclick(event):
    rightclickmenu.tk_popup(event.x_root, event.y_root)

FetchBatteryChargingStatus()

if fetchosname == 'Windows':
    SayBTN.focus()
    for b in [SayBTN]:
        b.unbind_class("Button", "<Key-space>")
        b.bind("<Return>", speak)
        b.bind("<Control-s>", speak)
        b.bind("<Button-1>", speak)
        b.bind("<space>", speak)

    window.bind("<Control-r>", updatebatterylevel)
    window.bind("<Control-R>", updatebatterylevel)
    window.bind("<Control-c>", speakChargingStatus)
    window.bind("<Control-C>", speakChargingStatus)
    window.bind("<Control-S>", speak)
    window.bind("<F1>", OnlineHelp)
    window.bind("<Button-3>", popMenuonrightclick)

elif fetchosname == 'Darwin':
    SayBTN.focus()
    for b in [SayBTN]:
        b.unbind_class("Button", "<Key-space>")
        b.bind("<Return>", speak)
        b.bind("<Command-s>", speak)
        b.bind("<Button-1>", speak)
        b.bind("<space>", speak)
        
window.mainloop()
