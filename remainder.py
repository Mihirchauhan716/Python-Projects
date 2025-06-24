

import time

msg = input("Enter reminder message: ")
sec = int(input("Remind after how many seconds: "))

time.sleep(sec)
print("Reminder:", msg)
