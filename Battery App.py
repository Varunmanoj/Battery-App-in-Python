import tkinter as tk
from tkinter import messagebox
import psutil as ps
# from win32com.client import Dispatch
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


def speakMenuitem():
    engine.say("battery Level"+str(percent)+"%")
    engine.runAndWait()


def speak(event):
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

    SayBTN["bg"] = "#A0D995"
    SayBTN["fg"] = "black"


def DarkMode():
    window.configure(bg="black")

    TitleText["bg"] = "black"
    TitleText["fg"] = "white"

    BatteryLevelText["bg"] = "black"
    BatteryLevelText["fg"] = "white"

    SayBTN["bg"] = "#377D71"
    SayBTN["fg"] = "white"


def OnlineHelp():
    webbrowser.open(
        "https://sites.google.com/view/batteryviewer-low-vision/home")


def About():
    messagebox.showinfo("About", "Battery % Viewer \n Version 5")


def Androidapp():
    webbrowser.open(
        "https://play.google.com/store/apps/details?id=com.varunmanojkumar.batterylevel")

# Change font size


def smallsize():
    BatteryLevelText.config(font="Arial 30 bold ")


def DefaultSize():
    BatteryLevelText.config(font="Arial 40 bold ")


def LargeSize():
    BatteryLevelText.config(font="Arial 50 bold ")


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
filemenu = tk.Menu(menubar, tearoff=0,
                   activebackground="green", activeforeground="black", font="Arial 10 bold")
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=window.quit)

# Menu Items
ViewMenu = tk.Menu(menubar, tearoff=0, activebackground="green", activeforeground="black", font="Arial 10 bold",
                   )
menubar.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label="Light Mode", command=LightMode)
ViewMenu.add_command(label="Dark Mode", command=DarkMode)


# Create Submenu
submenu = tk.Menu(ViewMenu, tearoff=0, activebackground="green",
                  activeforeground="black", font="Arial 10 bold")
submenu.add_command(label="Small Font", command=smallsize)
submenu.add_command(label="Default Font", command=DefaultSize)
submenu.add_command(label="Large Font", command=LargeSize)
ViewMenu.add_cascade(label="Change Font Size", menu=submenu)


# Speak Menu
SpeakMenu = tk.Menu(menubar, tearoff=0, activebackground="green",
                    activeforeground="black", font="Arial 10 bold")
menubar.add_cascade(label="Speak", menu=SpeakMenu)
SpeakMenu .add_command(label="Speak Battery Level", command=speakMenuitem)

# Help Menu
HelpMenu = tk.Menu(menubar, tearoff=0, activebackground="green",
                   activeforeground="black", font="Arial 10 bold")
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
    text="Battery Level " + str(percent) + " %", font="Arial 40 bold", aspect="250", justify="center")
BatteryLevelText.pack(fill="x",)

# Added a Say button
SayBTN = tk.Button(text="Say", command=speak,
                   font="Arial 20 bold", activebackground="green", bg="#A0D995", bd="5",)
SayBTN.pack(fill="x")

# Key bind
SayBTN.focus()
for b in [SayBTN]:
    b.unbind_class("Button", "<Key-space>")
    b.bind("<Return>", speak)
    b.bind("<Control-s>", speak)
    b.bind("<Button-1>", speak)
    b.bind("<space>", speak)

window.mainloop()
