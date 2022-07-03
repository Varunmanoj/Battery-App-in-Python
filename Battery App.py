import tkinter as tk
from tkinter import messagebox
import psutil as ps
from win32com.client import Dispatch
import pyttsx3
import webbrowser


def fetchbatterypercent():
    Battery = ps.sensors_battery()
    percent = Battery.percent

    return percent


def FetchBatteryChargingStatus():
    Battery = ps.sensors_battery()
    plugedinbool = Battery.power_plugged

    if plugedinbool:
        chargeStatusText = "Device Charging"
    else:
        chargeStatusText = "Device Not Charging"
    return chargeStatusText


ChargingStatusText = FetchBatteryChargingStatus()
engine = pyttsx3.init()


def speak():
    # speak = Dispatch("SAPI.SpVoice")
    # speak.Speak("Battery Level"+str(percent)+"%")

    engine.say("battery Level"+str(percent)+"%")
    engine.runAndWait()


def speakChargingStatus():
    engine.say(ChargingStatusText)
    engine.runAndWait()


def LightMode():
    window.configure(bg="#f0f0f0")

    TitleText["bg"] = "#f0f0f0"
    TitleText["fg"] = "black"

    BatteryLevelText["bg"] = "#f0f0f0"
    BatteryLevelText["fg"] = "black"

    SayBTN["bg"] = "#f0f0f0"
    SayBTN["fg"] = "black"


def DarkMode():
    window.configure(bg="black")

    TitleText["bg"] = "black"
    TitleText["fg"] = "white"

    BatteryLevelText["bg"] = "black"
    BatteryLevelText["fg"] = "white"

    SayBTN["bg"] = "black"
    SayBTN["fg"] = "white"


def OnlineHelp():
    webbrowser.open(
        "https://sites.google.com/xaviers.edu.in/battery-viewer/home")


def About():
    messagebox.showinfo("About", "Battery % Viewer \n Version 3")


def Androidapp():
    webbrowser.open(
        "https://play.google.com/store/apps/details?id=com.varunmanojkumar.batterylevel")


def refresh():
    window.update()


percent = fetchbatterypercent()


# GUI Design
# Define the Window
window = tk.Tk()
# Set Title of the Window
window.title("Battery % Viewer")
# Set Size of the Window
window.geometry("500x400")
window.minsize(450, 100)
# Set the Icon for the Window and the App
window.iconbitmap("App Icon.ico")

# Add Widgets
# Add Menu
menubar = tk.Menu(window)
window.config(menu=menubar)

# Menu Items
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Refresh", command=refresh)
filemenu.add_command(label="Exit", command=window.quit)

# Menu Items
ViewMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label="Light Mode", command=LightMode)
ViewMenu.add_command(label="Dark Mode", command=DarkMode)

# Speak Menu
SpeakMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Speak", menu=SpeakMenu)
SpeakMenu .add_command(label="Speak Battery Level", command=speak)

HelpMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu .add_command(label="Online Help", command=OnlineHelp)
HelpMenu.add_separator()
HelpMenu .add_command(label="About", command=About)
HelpMenu.add_separator()
HelpMenu .add_command(label="Android App", command=Androidapp)

TitleText = tk.Message(text="Battery % Viewer",
                       font="Arial 30 bold", justify="center", aspect="500")
TitleText .pack(side="top", fill="x")


BatteryLevelText = tk.Message(
    text="Battery Level " + str(percent) + " %", font="Arial 20 bold", aspect="250", justify="center")
BatteryLevelText.pack(fill="x",)

# Added a Say button
SayBTN = tk.Button(text="Say", command=speak,
                   font="Arial 30 bold")
SayBTN.pack(fill="x")


window.mainloop()
