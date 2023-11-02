# Drinking water reminder in python

import time
import win10toast
from win32com.client import Dispatch

say="Oh Rahul ji, please remember her."

# For notification
toaster = win10toast.ToastNotifier()

# For say
speak=Dispatch("SAPI.SpVoice").speak

while True:
    toaster.show_toast("Notification", say, duration=2)
    speak(say)
    time.sleep(3)   # Get reminder after three seconds