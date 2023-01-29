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
import time
import subprocess

# GUI Design
# Define the Window
window = tk.Tk()


def restartsystem():
    os.system("shutdown /r ")


def findos():
    OSName = platform.system()
    return OSName


fetchosname = findos()
if fetchosname == 'Windows':
    engine = pyttsx3.init()

# install extra voices on Windows


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
    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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
    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


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

    else:
        messagebox.showinfo("Works on Windows Only",
                            "The extra voices can be installed on Windows only.")


def fetchbatterypercent():
    global percent
    global Battery
    Battery = ps.sensors_battery()
    if Battery:
        percent = Battery.percent

    global BatteryLevelText
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    window.after(10000, fetchbatterypercent)


def updatebatterylevel(event):
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say("Screen Refreshed!")
            engine.runAndWait()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", "Screen Refreshed!"])
        except Exception as e:
            print(str(e))


def updatebatterylevelMenu():
    BatteryLevelText['text'] = 'Battery Level '+str(percent)+' %'
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say("Screen Refreshed!")
            engine.runAndWait()
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

    # Run the function again and again
    window.after(1000, FetchBatteryChargingStatus)


FetchBatteryChargingStatus()


def speakMenuitem():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say("battery Level"+str(percent)+"%")
            engine.runAndWait()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"battery Level"+str(percent)+"%"])
        except Exception as e:
            print(str(e))


def speak(event):
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say("battery Level"+str(percent)+"%")
            engine.runAndWait()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"battery Level"+str(percent)+"%"])
        except Exception as e:
            print(str(e))


def speakChargingStatus(event):
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say(chargeStatusText)
            engine.runAndWait()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"{chargeStatusText}"])
        except Exception as e:
            print(str(e))


def speakChargingStatusMenu():
    fetchosname = findos()
    if fetchosname == 'Windows':
        try:
            engine.say(chargeStatusText)
            engine.runAndWait()
        except Exception as e:
            print(str(e))
    elif fetchosname == 'Darwin':
        try:
            subprocess.call(["say", f"{chargeStatusText}"])
        except Exception as e:
            print(str(e))


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
        "https://www.batteryviewer.com/windows-app")


def OnlineHelp(event):
    webbrowser.open(
        "https://www.batteryviewer.com/windows-app")


def contactus():
    webbrowser.open(
        "https://www.batteryviewer.com/contact-us")


def About():
    messagebox.showinfo("About", "Battery % Viewer \n Version 8")


def KeyboardShortcutsPage():
    webbrowser.open(
        "https://www.batteryviewer.com/windows-app/keyboard-shortcuts")


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
window.minsize(400, 300)
# Set the Icon for the Window and the App
window.iconbitmap("App Icon.ico")


# Add Widgets
# Add Menu
menubar = tk.Menu(window)
window.config(menu=menubar)

# Menu Items
filemenu = tk.Menu(menubar, tearoff=0,
                   activebackground="#A0D995", activeforeground="black", font="Arial 20 bold")
menubar.add_cascade(label="File", menu=filemenu, underline=0)
filemenu.add_command(
    label="Refresh", command=updatebatterylevelMenu, accelerator="Command+R", underline=0)

fetchosname = findos()
if fetchosname == 'Windows':

    filemenu.add_command(label="Exit", command=window.quit,
                         accelerator='ALT+F4', underline=0)
elif fetchosname == 'Darwin':
    filemenu.add_command(label="Exit", command=window.quit)
# Menu Items
ViewMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995", activeforeground="black", font="Arial 20 bold",
                   )
menubar.add_cascade(label="View", menu=ViewMenu, underline=0)
ViewMenu.add_command(label="Light Mode",
                     command=LightModeMenu, accelerator="Command+L", underline=0)
ViewMenu.add_command(
    label="Dark Mode", command=DarkModeMenu, accelerator="Command+D", underline=0)


# Create Submenu
submenu = tk.Menu(ViewMenu, tearoff=0, activebackground="#A0D995",
                  activeforeground="black", font="Arial 20 bold")
submenu.add_command(label="Small Font", command=smallsize, underlin=0)
submenu.add_command(label="Default Font", command=DefaultSize, underline=0)
submenu.add_command(label="Large Font", command=LargeSize, underline=0)
ViewMenu.add_cascade(label="Change Font Size", menu=submenu, underline=0)


# Speak Menu
SpeakMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995",
                    activeforeground="black", font="Arial 20 bold")
menubar.add_cascade(label="Speak", menu=SpeakMenu, underline=0)
SpeakMenu .add_command(label="Battery Level", underline=0,
                       command=speakMenuitem, accelerator="Command+S")
SpeakMenu.add_command(label="Charging Indication",
                      command=speakChargingStatusMenu, accelerator="Command+C", underline=0)
SpeakMenu.add_separator()

# Install VoicesMenu
VoicesMenu = tk.Menu(SpeakMenu, tearoff=0, activebackground="#A0D995",
                     activeforeground="black", font="Arial 20 bold")
VoicesMenu .add_command(
    label="Catherin", command=InstallCatherinVoice, underline=0)
VoicesMenu .add_command(
    label="George", command=InstallGeorgeVoice, underline=0)
VoicesMenu .add_command(label="Hazel", command=InstallHazelVoice, underline=0)
VoicesMenu .add_command(
    label="Hemant", command=InstallHemantVoice, underline=1)
VoicesMenu .add_command(label="James", command=InstallJamesVoice, underline=0)
VoicesMenu .add_command(
    label="Kalpana", command=InstallKalpanaVoice, underline=0)
VoicesMenu .add_command(label="Linda", command=InstallLindaVoice, underline=0)
VoicesMenu .add_command(label="Mark", command=InstallMarkVoice, underline=0)
VoicesMenu .add_command(label="Ravi", command=InstallRaviVoice, underline=0)
VoicesMenu .add_command(
    label="Ritchard", command=InstallRitchardVoice, underline=1)
VoicesMenu .add_command(label="Sean", command=InstallSeanVoice, underline=0)
VoicesMenu .add_command(label="Susan", command=InstallSusanVoice, underline=1)


SpeakMenu.add_cascade(label="Install More Voices",
                      menu=VoicesMenu, underline=0)
# Help Menu
HelpMenu = tk.Menu(menubar, tearoff=0, activebackground="#A0D995",
                   activeforeground="black", font="Arial 20 bold")
menubar.add_cascade(label="Help", menu=HelpMenu, underline=0)
HelpMenu .add_command(label="Online Help", underline=0,
                      command=OnlineHelpMenu, accelerator="F1")
HelpMenu.add_command(label="Keyboard Shortcuts",
                     command=KeyboardShortcutsPage, underline=0)
HelpMenu.add_command(label="Contact US", command=contactus, underlin=0)
HelpMenu.add_separator()
HelpMenu .add_command(label="About", command=About, underline=0)
HelpMenu.add_separator()
HelpMenu .add_command(label="Get Android App", command=Androidapp, underline=0)

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


# Right Click Menu
rightclickmenu = tk.Menu(window, title="right Click Menu", tearoff=0, activebackground="#A0D995",
                         activeforeground="black", font="Arial 15 bold")
rightclickmenu.add_command(label="Speak Battery Level",
                           command=speakMenuitem, accelerator="CTRL+S", underline=6)
rightclickmenu.add_command(label="Speak Charging Status",
                           command=speakChargingStatusMenu, accelerator="CTRL+C", underline=6)
rightclickmenu.add_separator()
rightclickmenu.add_command(label="Refresh",
                           command=updatebatterylevelMenu, accelerator="CTRL+R", underline=0)


def popMenuonrightclick(event):
    rightclickmenu.tk_popup(event.x_root, event.y_root)


FetchBatteryChargingStatus()
# Keyboard Shortcut
if fetchosname == 'Windows':
    SayBTN.focus()
    for b in [SayBTN]:
        b.unbind_class("Button", "<Key-space>")
        b.bind("<Return>", speak)
        b.bind("<Control-s>", speak)
        b.bind("<Button-1>", speak)
        b.bind("<space>", speak)

    window.bind("<Control-l>", LightMode)
    window.bind("<Control-L>", LightMode)

    window.bind("<Control-d>", DarkMode)
    window.bind("<Control-D>", DarkMode)

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

    window.bind("<Command-l>", LightMode)
    window.bind("<Command-L>", LightMode)

    window.bind("<Command-d>", DarkMode)
    window.bind("<Command-D>", DarkMode)

    window.bind("<Command-r>", updatebatterylevel)
    window.bind("<Command-R>", updatebatterylevel)

    window.bind("<Command-c>", speakChargingStatus)
    window.bind("<Command-C>", speakChargingStatus)
    window.bind("<Command-S>", speak)

    window.bind("<F1>", OnlineHelp)
    window.bind("<Button-3>", popMenuonrightclick)

window.mainloop()
