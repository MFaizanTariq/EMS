from venv.models import engine, Organizer, Attendee, database_create, Speaker, Conference, Talk
from venv.models import add_to_conference, atd_conference_search, talk_list
from venv.models import message_sent, spkr_list
from venv.views import *
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
            details = Reg_to_conference(all_cns)
            res = add_to_conference(details[0], details[1], details[2])
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
            stp = 1
            lt = []
            details = conference_schedule(stp, '')
            lt = atd_conference_search(details[0],details[1])
            stp = 2
            details = conference_schedule(stp, lt)
            stp = 3
            if not details == 0:
                lt = Talk.atd_talk_search(details[0],details[1],details[2])
                conference_schedule(stp, lt)

        elif chs==6:
            details = change_schedule(1, '')
            lt = talk_list(details[0], details[1])
            details = change_schedule(2, lt)
            if not details == 0:
                cmt = Talk.update_talk_time(details[0],details[1],details[2])
                os.system('cls')
                print(cmt[0])
                if cmt[1]==1:
                    message_sent(cmt[2])
                    print('Email sent to attendees')
                input()

        elif chs==7:
            details = update_talk(1, '')
            lt = spkr_list(details[0], details[1])
            details = update_talk(2, lt)
            if not details == 0:
                cmt = Talk.update_talk_title(details[0],details[1])
                os.system('cls')
                print(cmt)
                input()

        elif chs==8:
            Guidelines()

        elif chs==9:
            break

        else:
            break