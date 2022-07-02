import tkinter as tk
import psutil as ps
import pyttsx3


# Initialize the tts engine
engine = pyttsx3.init()


def fetchbatterypercent():
    Battery = ps.sensors_battery()
    percent = Battery.percent

    return percent


def speak():
    engine.say("Battery Level"+str(percent)+"%")
    engine.runAndWait()


percent = fetchbatterypercent()


# GUI Design
window = tk.Tk()
window.title("Battery App")
window.geometry("500x400")
window.minsize(450, 100)
window.iconbitmap("App Icon.ico")

TitleText = tk.Message(text="Battery % Viewer",
                       font="Arial 30 bold", justify="center", aspect="500")
TitleText .pack(side="top", fill="x")


BatteryLevelText = tk.Message(
    text="Battery Level " + str(percent) + " %", font="Arial 20 bold", aspect="500", justify="center")
BatteryLevelText.pack(fill="x", padx="20")

tk.Button(text="Say", command=speak,
          font="Arial 30 bold").pack(fill="x", padx="20")

window.bind('<Control-S>', speak)
window.mainloop()
