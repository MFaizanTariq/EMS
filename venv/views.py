import os
from datetime import datetime

def Menu():
    os.system('cls')
    print('-----------------------------------------')
    print('Welcome to Conference Management System')
    print('-----------------------------------------')
    print('1. Register yourself!!!!')
    print('2. Register for an Event')
    print('3. Create new event')
    print('4. Add new Talk to existing event')
    print('5. Check schedule of registered events')
    print('6. Change talk schedule')
    print('7. Guidelines for using the software')
    print('8. Exit')
    chs = int(input ())
    return chs

def Guidelines():
    os.system('cls')
    print('------------------------------------------------------------------------')
    print('                     Welcome to Conference Management System')
    print('------------------------------------------------------------------------')
    print('                         General guidelines for usage')
    print('------------------------------------------------------------------------')
    print('1. To use the software, you have to register with a name and passcode')
    print('2. There is no login page, but you will be asked for your passcode for \n event creation / registration')
    print('3. For creating event / talk register as "Organizer"')
    print('4. For registering to an event, register as "Attendee"')
    print('5. For creating talks, ask the concerned speaker to register first')
    print('6. Remember your passcode')
    print('----------------------------------')
    print('Press any key to continue')
    input ()
    return


def Register():
    os.system('cls')
    print('----------------------------------')
    print('     Conference Management System')
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
    print('     Conference Management System')
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
    print('     Conference Management System')
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
    print('Mention talk start time: (YYYY-MM-DT HH:MM)')
    tk_sdt = input()
    print('Mention talk end time: (YYYY-MM-DT HH:MM)')
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
    print('  Conference Management System')
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
    print('--------------------------------------------------------------')
    print('                Conference Management System')
    print('--------------------------------------------------------------')
    print('                   Event schedule search')
    print('--------------------------------------------------------------')
        
    if stp == 1:
        print('Enter your name:')
        attend_name = input()
        print('Enter your passcode')
        attend_pass = input()
        return attend_name, attend_pass

    elif stp == 2:
        if lt:
            print('ID #  Name   Start Date    End Date')
            print('----------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0],' ', lt[a][1],' ', lt[a][2],' ', lt[a][3])
            print('----------------------------------')
            print('Choose event id for displaying schedule:')
            ev_id = int(input())
            print('Choose method for search (1: date, 2: room #)')
            sr_md = int(input())
            if sr_md == 1:
                print('Mention Date:')
                sr_par = input()
            elif sr_md == 2:
                print('Mention Room #:')
                sr_par = input()
            return ev_id, sr_md, sr_par
        print('----------------------------------')
        input()
        return 0

    elif stp == 3:
        if lt:
            print('Name      Room #  Speaker Name:          Start Time            End Time')
            print('--------------------------------------------------------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0],' ', lt[a][1],' ', lt[a][2],' ', lt[a][3],' ', lt[a][4])
            print('--------------------------------------------------------------------------------')
        print('--------------------------------------------------------------------------')
        input()
        return

def change_schedule(stp, lt):
    os.system('cls')
    print('----------------------------------')
    print('  Conference Management System')
    print('----------------------------------')
    print('     Event schedule search')
    print('----------------------------------')

    if stp == 1:
        print('Enter your name:')
        og_name = input()
        print('Enter your passcode')
        og_pass = input()
        return og_name, og_pass

    elif stp == 2:
        if lt:
            print('Event Name   Talk ID Talk Name    Room #   Speaker Name      Start Time       End Time')
            print('--------------------------------------------------------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0], ' ', lt[a][1], ' ', lt[a][2], ' ', lt[a][3], ' ', lt[a][4], ' ', lt[a][5], ' ', lt[a][6])
            print('--------------------------------------------------------------------------------')
            print('Enter talk name for changing schedule')
            tk_id = int(input())
            print('Mention new start time: (YYYY-MM-DT HH:MM)')
            nw_sdt = input()
            print('Mention new end time: (YYYY-MM-DT HH:MM)')
            nw_edt = input()
            nw_sdt = datetime.strptime(nw_sdt, '%Y-%m-%d %H:%M')
            nw_edt = datetime.strptime(nw_edt, '%Y-%m-%d %H:%M')
            return tk_id, nw_sdt, nw_edt
        return 0