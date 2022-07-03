import tkinter as tk
import psutil as ps
from win32com.client import Dispatch


def fetchbatterypercent():
    Battery = ps.sensors_battery()
    percent = Battery.percent

    return percent


def speak():
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak("Battery Level"+str(percent)+"%")


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


percent = fetchbatterypercent()


# GUI Design
# Define the Window
window = tk.Tk()
# Set Title of the Window
window.title("Battery App")
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
filemenu.add_command(label="Exit", command=window.quit)

# Menu Items
ViewMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label="Light Mode", command=LightMode)
ViewMenu.add_command(label="Dark Mode", command=DarkMode)

SpeakMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Speak", menu=SpeakMenu)
SpeakMenu .add_command(label="Speak Battery Level", command=speak)


TitleText = tk.Message(text="Battery % Viewer",
                       font="Arial 30 bold", justify="center", aspect="500")
TitleText .pack(side="top", fill="x")


BatteryLevelText = tk.Message(
    text="Battery Level " + str(percent) + " %", font="Arial 20 bold", aspect="500", justify="center")
BatteryLevelText.pack(fill="x",)

# Added a Say button
SayBTN = tk.Button(text="Say", command=speak,
                   font="Arial 30 bold")
SayBTN.pack(fill="x")


window.mainloop()
