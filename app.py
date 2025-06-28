import datetime
import time
import os
import platform

def play_alarm_sound() :
    if platform.system() == "Windows" :
        os.system("start alarm.mp3")
    else:
        os.system("afplay alarm.mp3")

def set_alarm(alarm_time) :
    print(f"Alarm is set for{alarm_time}")
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M")
        if current_time==alarm_time :
            print("Wake up! Alarm Ringing! ")
            play_alarm_sound()
        time.sleep(30)

if __name__=="__main__" :
    user_input=input("enter alarm time in HH:MM format (24-hour) :")
    set_alarm(user_input)
