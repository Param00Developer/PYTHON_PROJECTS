from notifypy import Notify
import time
def water_notify(min):
    notification = Notify()
    notification.title = "Drink Water ..."
    notification.message = f"Water reminder for {min} minutes"
    notification.icon = ".\Images\drop.png"
    notification.send()
time_=float(input("Enter time in mintue for your reminder : "))
sec=time_*60
time.sleep(sec)
water_notify(time_)