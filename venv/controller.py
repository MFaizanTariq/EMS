from venv.models import engine, Add_Organizer, Add_Attendee, database_create
from venv.models import Add_Speaker, Add_Event, Add_Talk, Event_List, add_to_event, atd_event_search, atd_talk_search
from venv.views import *
from sqlalchemy import insert, select
from sqlalchemy.orm import sessionmaker
import os

Session = sessionmaker(bind = engine)
session = Session()

def cms():
    database_create()

    while True:
        chs = Menu()

        if chs==1:
            details = Register()
            if details[0]==1:
                Add_Organizer(details[1], details[2])
                os.system('cls')
                print('Organizer successfully added')
            elif details[0]==2:
                Add_Attendee(details[1], details[2])
                os.system('cls')
                print('Attendee successfully added')
            elif details[0]==3:
                Add_Speaker(details[1], details[2])
                os.system('cls')
                print('Speaker successfully added')
            print('\nEnter any key to continue... ')
            input()

        elif chs==2:
            all_eves = Event_List()
            details = Reg_to_event(all_eves)
            res = add_to_event(details[0], details[1], details[2])
            os.system('cls')
            print (res)
            print('\nEnter any key to continue... ')
            input()

        elif chs==3:
            details = Add_New_Event()
            res = Add_Event(details[0], details[1], details[2], details[3], details[4])
            if res==1:
                os.system('cls')
                print('Event Successuly added')
            if res==2:
                os.system('cls')
                print('User name / pass code combination not exist')
            print('\nEnter any key to continue... ')
            input()

        elif chs==4:
            details = Add_New_Talk()
            res = Add_Talk(details[0], details[1], details[2], details[3], details[4], details[5], details[6], details[7])
            os.system('cls')
            print (res)
            print('\nEnter any key to continue... ')
            input()

        elif chs==5:
            stp = 1
            lt = []
            details = event_schedule(stp, '')
            lt = atd_event_search(details[0],details[1])
            stp = 2
            details = event_schedule(stp, lt)
            stp = 3
            if not details == 0:
                lt = atd_talk_search(details[0],details[1],details[2])
                event_schedule(stp, lt)

        elif chs==6:
            Guidelines()

        elif chs==7:
            break

        else:
            break