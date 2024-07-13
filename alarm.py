# defining the function for the alarm clock  
def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime)  
