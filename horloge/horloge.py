from datetime import datetime
import time

hh =17

mm = 12

ss = 23


def horloge():
    count = 0
    while True:
        now = datetime.now()
        date_time_str = now.strftime("%H:%M:%S")
        print(date_time_str)
        time.sleep(1)
        count += 1
        if count == 10: 
            break

def afficher_heure():
    while True:
            HH,MM,SS = str(hh),str(mm),str(ss)
            h = [hh,mm,ss]
            H = [HH,MM,SS]
            
            if len(str(hh)) + len(str(mm)) + len(str(ss)) != 6:
                for a in range(3):
                    H[a] = str(h[a])
                    if len(str(h[a])) == 1:
                        H[a] = "0" + str(h[a])
                print(H[0]+":"+H[1]+":"+H[2])
            else:
                print(str(hh)+":"+str(mm)+":"+str(ss))
                
            time.sleep(0.995)
            
            ss += 1
            if ss == 60:
                mm += 1
                ss = 0
            if mm == 60:
                hh += 1
                mm = 0
            if hh == 24:
                hh = 0

def setalarme():
    alarm_time = input("Entrez l'heure de l'alarme à régler : HH:MM:SS\n")
    alarm_hour=alarm_time[0:2]
    alarm_minute=alarm_time[3:5]
    alarm_seconds=alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    print("Setting up alarm..")
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    if(alarm_seconds==current_seconds):
                        print("Waky Waky!")


arret = False

def pause():
    global arret
    arret = True

def reactiviationhorloge():
    global arret
    arret = False



def ampmformat():
    global arret
    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p") 
        print(current_time)
        time.sleep(1)






        

