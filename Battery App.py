import tkinter as tk
import psutil as ps


def fetchbatterypercent():
    Battery = ps.sensors_battery()
    percent = Battery.percent
    ChargingStatus = Battery.power_plugged
    if ChargingStatus:
        ChargingText = "Charging Battery"
    else:
        ChargingText = "Device Unplugged"
    return percent, ChargingText


percent, pluggedstatus = fetchbatterypercent()


# GUI Design
window = tk.Tk()
window.title("Battery App")

TitleText = tk.Message(text="Battery % Viewer")
TitleText .pack()


BatteryLevelText = tk.Message(text="Battery Level " + str(percent) + " %")
BatteryLevelText.pack()

ChargingStatusText = tk.Message(text=pluggedstatus)
ChargingStatusText.pack()

window.mainloop()
