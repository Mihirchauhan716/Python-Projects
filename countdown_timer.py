

import time

sec = int(input("Enter time in seconds: "))
while sec > 0:
    print(sec)
    time.sleep(1)
    sec -= 1

print("Time's up!")
