import tkinter as tk
from tkinter import messagebox
import psutil as ps
# from win32com.client import Dispatch
import pyttsx3
import webbrowser
import platform
import os
import time

# GUI Design
# Define the Window
window = tk.Tk()
engine = pyttsx3.init()
# install extra voices on Windows


def restartsystem():
    os.system("shutdown /r ")


def findos():
    OSName = platform.system()
    return OSName


def InstallCatherinVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Catherin.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Catherin Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")
    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


def InstallGeorgeVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\George.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "George Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallHazelVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Hazel.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Hazel Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallHemantVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Hemant.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Hemant Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallJamesVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\James.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "James Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallKalpanaVoice():

    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Kalpana.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Kalpana Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallLindaVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Linda.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Linda Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallMarkVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Mark.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Mark Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallRaviVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Ravi.reg")
            time.sleep(3)
            messagebox.askyesno(
                "Install Complete", "Ravi Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")

        except:
            print("Program not Installed")


def InstallRitchardVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Ritchard.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Ritchard Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallSeanVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Sean.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Sean Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def InstallSusanVoice():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            os.startfile("voices\One Core Voices\Susan.reg")
            time.sleep(3)
            response = messagebox.askyesno(
                "Install Complete", "Susan Voice was installed Successfully\nThe Program has made configoration changes that require you to restart your computer Do You whish to restart now?")
            if response == 1:
                restartsystem()
            else:
                pass
        except:
            print("Program not Installed")


def fetchbatterypercent():
    global percent
    global Battery
    Battery = ps.sensors_battery()
    percent = Battery.percent

    global BatteryLevelText
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    window.after(60000, fetchbatterypercent)


def updatebatterylevel(event):
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    engine.say("Screen Refreshed")
    engine.runAndWait()


def updatebatterylevelMenu():
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    engine.say("Screen Refreshed")
    engine.runAndWait()


def FetchBatteryChargingStatus():
    Battery = ps.sensors_battery()
    plugedinbool = Battery.power_plugged

    global chargeStatusText
    if plugedinbool:
        chargeStatusText = "Device Charging"
    else:
        chargeStatusText = "Device Not Charging"

    # Run the function again and again
    window.after(1000, FetchBatteryChargingStatus)


FetchBatteryChargingStatus()


def speakMenuitem():
    engine.say("battery Level"+str(percent)+"%")
    engine.runAndWait()


def speak(event):
    # speak = Dispatch("SAPI.SpVoice")
    # speak.Speak("Battery Level"+str(percent)+"%")

    engine.say("battery Level"+str(percent)+"%")
    engine.runAndWait()


def speakChargingStatus(event):
    engine.say(chargeStatusText)
    engine.runAndWait()


def speakChargingStatusMenu():
    engine.say(chargeStatusText)
    engine.runAndWait()


def LightMode(event):
    window.configure(bg="#f0f0f0")

    TitleText["bg"] = "#f0f0f0"
    TitleText["fg"] = "black"

    BatteryLevelText["bg"] = "#f0f0f0"
    BatteryLevelText["fg"] = "black"

    SayBTN["bg"] = "#A0D995"
    SayBTN["fg"] = "black"


def LightModeMenu():
    window.configure(bg="#f0f0f0")

    TitleText["bg"] = "#f0f0f0"
    TitleText["fg"] = "black"

    BatteryLevelText["bg"] = "#f0f0f0"
    BatteryLevelText["fg"] = "black"

    SayBTN["bg"] = "#A0D995"
    SayBTN["fg"] = "black"


def DarkMode(event):
    window.configure(bg="black")

    TitleText["bg"] = "black"
    TitleText["fg"] = "white"

    BatteryLevelText["bg"] = "black"
    BatteryLevelText["fg"] = "white"

    SayBTN["bg"] = "#377D71"
    SayBTN["fg"] = "white"


def DarkModeMenu():
    window.configure(bg="black")

    TitleText["bg"] = "black"
    TitleText["fg"] = "white"

    BatteryLevelText["bg"] = "black"
    BatteryLevelText["fg"] = "white"

    SayBTN["bg"] = "#377D71"
    SayBTN["fg"] = "white"


def OnlineHelpMenu():
    webbrowser.open(
        "https://sites.google.com/view/batteryviewer-low-vision/home")


def OnlineHelp(event):
    webbrowser.open(
        "https://sites.google.com/view/batteryviewer-low-vision/home")


def About():
    messagebox.showinfo("About", "Battery % Viewer \n Version 6")


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
                   activebackground="#A0D995", activeforeground="black", font="Arial 10 bold")
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(
    label="Refresh", command=updatebatterylevelMenu, accelerator="CTRL+R")
filemenu.add_command(label="Exit", command=window.quit, accelerator='ALT+F4')

# Menu Items
ViewMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995", activeforeground="black", font="Arial 10 bold",
                   )
menubar.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label="Light Mode",
                     command=LightModeMenu, accelerator="CTRL+L")
ViewMenu.add_command(
    label="Dark Mode", command=DarkModeMenu, accelerator="CTRL+D")


# Create Submenu
submenu = tk.Menu(ViewMenu, tearoff=0, activebackground="#A0D995",
                  activeforeground="black", font="Arial 10 bold")
submenu.add_command(label="Small Font", command=smallsize)
submenu.add_command(label="Default Font", command=DefaultSize)
submenu.add_command(label="Large Font", command=LargeSize)
ViewMenu.add_cascade(label="Change Font Size", menu=submenu)


# Speak Menu
SpeakMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995",
                    activeforeground="black", font="Arial 10 bold")
menubar.add_cascade(label="Speak", menu=SpeakMenu)
SpeakMenu .add_command(label="Battery Level",
                       command=speakMenuitem, accelerator="CTRL+S")
SpeakMenu.add_command(label="Charging Indication",
                      command=speakChargingStatusMenu, accelerator="CTRL+C")
SpeakMenu.add_separator()

# Install VoicesMenu
VoicesMenu = tk.Menu(SpeakMenu, tearoff=0, activebackground="#A0D995",
                     activeforeground="black", font="Arial 10 bold")
VoicesMenu .add_command(label="Catherin", command=InstallCatherinVoice)
VoicesMenu .add_command(label="George", command=InstallGeorgeVoice)
VoicesMenu .add_command(label="Hazel", command=InstallHazelVoice)
VoicesMenu .add_command(label="Hemant", command=InstallHemantVoice)
VoicesMenu .add_command(label="James", command=InstallJamesVoice)
VoicesMenu .add_command(label="Kalpana", command=InstallKalpanaVoice)
VoicesMenu .add_command(label="Linda", command=InstallLindaVoice)
VoicesMenu .add_command(label="Mark", command=InstallMarkVoice)
VoicesMenu .add_command(label="Ravi", command=InstallRaviVoice)
VoicesMenu .add_command(label="Ritchard", command=InstallRitchardVoice)
VoicesMenu .add_command(label="Sean", command=InstallSeanVoice)
VoicesMenu .add_command(label="Susan", command=InstallSusanVoice)


SpeakMenu.add_cascade(label="Install More Voices", menu=VoicesMenu)
# Help Menu
HelpMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995",
                   activeforeground="black", font="Arial 10 bold")
menubar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu .add_command(label="Online Help",
                      command=OnlineHelpMenu, accelerator="F1")
HelpMenu.add_separator()
HelpMenu .add_command(label="About", command=About)
HelpMenu.add_separator()
HelpMenu .add_command(label="Android App", command=Androidapp)

TitleText = tk.Message(text="Battery % Viewer",
                       font="Arial 30 bold", justify="center", aspect="500")
TitleText .pack(side="top", fill="x")


BatteryLevelText = tk.Message(
    font="Arial 40 bold", aspect="250", justify="center")
BatteryLevelText.pack(fill="x")

fetchbatterypercent()

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

FetchBatteryChargingStatus()

# Keyboard Shortcuts
window.bind("<Control-l>", LightMode)
window.bind("<Control-d>", DarkMode)
window.bind("<Control-r>", updatebatterylevel)
window.bind("<Control-c>", speakChargingStatus)
window.bind("<F1>", OnlineHelp)
window.mainloop()
