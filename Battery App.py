import tkinter as tk
import psutil as ps


window = tk.Tk()
window.title("Battery App")

TitleText = tk.Message(text="Battery % Viewer")
TitleText .pack()

Battery = ps.sensors_battery()
percent = Battery.percent
ChargingStatus = Battery.power_plugged
if ChargingStatus:
    ChargingText = "Charging Battery"
else:
    ChargingText = "Device Unplugged"

BatteryLevelText = tk.Message(text="Battery Level " + str(percent) + " %")
BatteryLevelText.pack()

ChargingStatusText = tk.Message(text=ChargingText)
ChargingStatusText.pack()

window.mainloop()
