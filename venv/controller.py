from venv.models import engine, Database_Create, Organizer, Attendee, Speaker, Conference, Talk
from venv.models import Add_to_Conference, Atd_Conference_Search, Talk_List, Send_Me    ssage, Spkr_List
from venv.views import *
from sqlalchemy.orm import sessionmaker
import os

Session = sessionmaker(bind = engine)
session = Session()

def cms():
    Database_Create()

    while True:
        chs = Menu()

        if chs==1:
            details = Register()
            if details[0]==1:
                Organizer.Add_Organizer(details[1], details[2])
                os.system('cls')
                print('Organizer successfully added')
            elif details[0]==2:
                Attendee.Add_Attendee(details[1], details[2])
                os.system('cls')
                print('Attendee successfully added')
            elif details[0]==3:
                Speaker.Add_Speaker(details[1], details[2])
                os.system('cls')
                print('Speaker successfully added')
            print('\nEnter any key to continue... ')
            input()

        elif chs==2:
            all_cns = Conference.Conference_List()
            details = Reg_to_Conference(all_cns)
            res = Add_to_Conference(details[0], details[1], details[2])
            os.system('cls')
            print (res)
            print('\nEnter any key to continue... ')
            input()

        elif chs==3:
            details = Add_New_Conference()
            res = Conference.Add_Conference(details[0], details[1], details[2], details[3], details[4])
            if res==1:
                os.system('cls')
                print('Conference Successuly added')
            if res==2:
                os.system('cls')
                print('User name / pass code combination not exist')
            print('\nEnter any key to continue... ')
            input()

        elif chs==4:
            details = Add_New_Talk()
            res = Talk.Add_Talk(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7])
            os.system('cls')
            print (res)
            print('\nEnter any key to continue... ')
            input()

        elif chs==5:
            lt = []
            details = Conference_Schedule(1, '')
            lt = Atd_Conference_Search(details[0],details[1])
            details = Conference_Schedule(2, lt)
            if not details == 0:
                lt = Talk.Atd_Talk_Search(details[0],details[1],details[2])
                Conference_Schedule(3, lt)

        elif chs==6:
            details = Change_Schedule(1, '')
            lt = Talk_List(details[0], details[1])
            details = Change_Schedule(2, lt)
            if not details == 0:
                cmt = Talk.Update_Talk_Time(details[0],details[1],details[2])
                os.system('cls')
                print(cmt[0])
                if cmt[1]==1:
                    Send_Message(cmt[2])
                    print('Email sent to attendees')
                input()

        elif chs==7:
            details = Update_Talk(1, '')
            lt = Spkr_List(details[0], details[1])
            details = Update_Talk(2, lt)
            if not details == 0:
                cmt = Talk.Update_Talk_Title(details[0],details[1])
                os.system('cls')
                print(cmt)
                input()

        elif chs==8:
            Guidelines()

        elif chs==9:
            break

        else:
            break