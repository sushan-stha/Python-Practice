# countdown timer program
import time
my_time = int(input("Enter the time in seconds:"))
for x in reversed(range(1, my_time)): #reversed-> count backward. Another step: range(my_time, 0, -1)
    seconds = x % 60
    hour = int(x / 3600)
    minutes = int(x / 60)%60  #%60 means minute field donot go above 60
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    # print(x)
    time.sleep(1) #.sleep(2) creates 2sec gap between one and another

print("Times Up!!")