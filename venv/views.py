import os
from datetime import datetime

def Menu():
    os.system('cls')
    print('----------------------------------')
    print('Welcome to Event Management System')
    print('----------------------------------')
    print('1. Register')
    print('2. Register for Event')
    print('3. Register New Event')
    print('4. Add New Talk to existing event')
    print('5. Check schedule of registered events')
    print('6. Exit')
    chs =input ()
    return int(chs)


def Register():
    os.system('cls')
    print('----------------------------------')
    print('     Event Management System')
    print('----------------------------------')
    print('  Member registration screen')
    print('----------------------------------')
    print('Mention type of registration: ')
    print('1. Organizer: ')
    print('2. Attendee: ')
    print('3. Speaker: ')
    typ= int(input())
    print('Enter name: ')
    name= input()
    print('Enter passcode: ')
    pass_code= input()
    return typ, name, pass_code

def Add_New_Event():
    os.system('cls')
    print('----------------------------------')
    print('     Event Management System')
    print('----------------------------------')
    print('     Event addition')
    print('----------------------------------')
    print('Mention Event Name: ')
    ev_name = input()
    print('Mention Event Start Date: (YYYY-MM-DT)')
    ev_sdate = input()
    print('Mention Event End Date: (YYYY-MM-DT)')
    ev_edate = input()
    print('Enter your name: ')
    og_name= input()
    print('Enter your passcode: ')
    og_pass= input()
    ev_sdate = datetime.strptime(ev_sdate, '%Y-%m-%d').date()
    ev_edate = datetime.strptime(ev_edate, '%Y-%m-%d').date()

    return ev_name, ev_sdate, ev_edate, og_name, og_pass

def Add_New_Talk():
    os.system('cls')
    print('----------------------------------')
    print('     Event Management System')
    print('----------------------------------')
    print('     Talk addition')
    print('----------------------------------')
    print('Mention Event Name: ')
    ev_name = input()
    print('Mention Talk Name: ')
    tk_name = input()
    print('Mention Speaker Name: ')
    spk_name = input()
    print('Choose room #: ')
    room_no = int(input())
    print('Mention Event Start Time: (YYYY-MM-DT HH:MM)')
    tk_sdt = input()
    print('Mention Event End Time: (YYYY-MM-DT HH:MM)')
    tk_edt = input()
    print('Enter event organizer name: ')
    og_name= input()
    print('Enter organizer passcode: ')
    og_pass= input()
    tk_sdt = datetime.strptime(tk_sdt, '%Y-%m-%d %H:%M')
    tk_edt = datetime.strptime(tk_edt, '%Y-%m-%d %H:%M')

    return ev_name, tk_name, room_no, spk_name, tk_sdt, tk_edt, og_name, og_pass


def Reg_to_event(all_eves):
    os.system('cls')
    print('----------------------------------')
    print('     Event Management System')
    print('----------------------------------')
    print('    Event Registration Screen')
    print('----------------------------------')
    print('ID   Name   Start Date    End Date')
    for all_eve in all_eves:
        print(all_eve.id,'  ',all_eve.ev_name,'  ',all_eve.ev_sdate, '  ',all_eve.ev_edate)
    print('----------------------------------')
    print('Enter your name:')
    attend_name = input()
    print('Enter your passcode')
    attend_pass = input()
    print('Enter event id for registration:')
    ev_id = int(input())
    return attend_name, attend_pass, ev_id

def event_schedule(stp, lt):
    os.system('cls')
    print('----------------------------------')
    print('     Event Management System')
    print('----------------------------------')
    print('     Event schedule search')
    print('----------------------------------')
        
    if stp == 1:
        print('Enter your name:')
        attend_name = input()
        print('Enter your passcode')
        attend_pass = input()
        return attend_name, attend_pass

    elif stp == 2:
        if lt:
            print('Name   Start Date    End Date')
            print('----------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0], '  ', lt[a][1], '  ', lt[a][2])
            print('----------------------------------')
            input()
            return
        print('Attendee name / passcode combination not found')
        print('----------------------------------')
        input()

