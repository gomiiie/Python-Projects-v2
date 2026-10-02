import time

def countdown(t):
    while (t > 0):
        sec = t%60
        mins = t//60
        hours, mins = mins//60, mins%60

        print(f"{hours:02}:{mins:02}:{sec:02}", end = "\r")
        time.sleep(1)
        t -= 1

    print("Time to go!")

t = int(input("Enter the time you wish to wait in seconds: "))
countdown(t)