import os
from datetime import datetime

def Menu():
    os.system('cls')
    print('-----------------------------------------')
    print('Welcome to Concordia Conference System')
    print('-----------------------------------------')
    print('1. Register yourself!!!!')
    print('2. Register to a conference')
    print('3. Create new conference')
    print('4. Add new Talk to existing conference')
    print('5. Check schedule of registered conference')
    print('6. Change talk schedule')
    print('7. Update Talk title')
    print('8. Guidelines for using the software')
    print('9. Exit')
    chs = int(input ())
    return chs

def Guidelines():
    os.system('cls')
    print('------------------------------------------------------------------------')
    print('                       Concordia Conference System')
    print('------------------------------------------------------------------------')
    print('                       General guidelines for usage')
    print('------------------------------------------------------------------------')
    print('1. To use the software, you have to register with a name and passcode')
    print('2. There is no login page, but you will be asked for your passcode for \n conference creation / registration')
    print('3. For creating conference / talk register as "Organizer"')
    print('4. For registering to an conference, register as "Attendee"')
    print('5. For creating talks, ask the concerned speaker to register first')
    print('6. Remember your passcode')
    print('----------------------------------')
    print('Press any key to continue')
    input ()
    return


def Register():
    os.system('cls')
    print('----------------------------------')
    print('   Concordia Conference System')
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

def Add_New_Conference():
    os.system('cls')
    print('----------------------------------')
    print('    Concordia Conference System')
    print('----------------------------------')
    print('     Conference creation')
    print('----------------------------------')
    print('Mention Conference Name: ')
    cn_name = input()
    print('Mention Conference Start Date: (YYYY-MM-DT)')
    cn_sdate = input()
    print('Mention Conference End Date: (YYYY-MM-DT)')
    cn_edate = input()
    print('Enter your name: ')
    og_name= input()
    print('Enter your passcode: ')
    og_pass= input()
    cn_sdate = datetime.strptime(cn_sdate, '%Y-%m-%d').date()
    cn_edate = datetime.strptime(cn_edate, '%Y-%m-%d').date()

    return cn_name, cn_sdate, cn_edate, og_name, og_pass

def Add_New_Talk():
    os.system('cls')
    print('----------------------------------')
    print('   Concordia Conference System')
    print('----------------------------------')
    print('     Talk addition')
    print('----------------------------------')
    print('Mention Conference Name: ')
    cn_name = input()
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
    print('Enter conference organizer name: ')
    og_name= input()
    print('Enter organizer passcode: ')
    og_pass= input()
    tk_sdt = datetime.strptime(tk_sdt, '%Y-%m-%d %H:%M')
    tk_edt = datetime.strptime(tk_edt, '%Y-%m-%d %H:%M')

    return cn_name, tk_name, room_no, spk_name, tk_sdt, tk_edt, og_name, og_pass


def Reg_to_Conference(all_cns):
    os.system('cls')
    print('----------------------------------')
    print('  Concordia Conference System')
    print('----------------------------------')
    print('  Registration to a conference')
    print('----------------------------------')
    print('ID   Name   Start Date    End Date')
    for all_cn in all_cns:
        print(all_cn.id,'  ',all_cn.cn_name,'  ',all_cn.cn_sdate, '  ',all_cn.cn_edate)
    print('----------------------------------')
    print('Enter your name:')
    attend_name = input()
    print('Enter your passcode')
    attend_pass = input()
    print('Enter conference id for registration:')
    cn_id = int(input())
    return attend_name, attend_pass, cn_id

def Conference_Schedule(stp, lt):
    os.system('cls')
    print('--------------------------------------------------------------')
    print('                Concordia Conference System')
    print('--------------------------------------------------------------')
    print('                    Conference schedule')
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
            print('Choose conference id for displaying schedule:')
            cn_id = int(input())
            print('Choose method for search (1: date, 2: room #)')
            sr_md = int(input())
            if sr_md == 1:
                print('Mention Date:')
                sr_par = input()
            elif sr_md == 2:
                print('Mention Room #:')
                sr_par = input()
            return cn_id, sr_md, sr_par
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

def Change_Schedule(stp, lt):
    os.system('cls')
    print('----------------------------------')
    print('  Concordia Conference System')
    print('----------------------------------')
    print('     Update talk time')
    print('----------------------------------')

    if stp == 1:
        print('Enter your name:')
        og_name = input()
        print('Enter your passcode')
        og_pass = input()
        return og_name, og_pass

    elif stp == 2:
        if lt:
            print('Conference Name   Talk ID Talk Name    Room #   Speaker Name      Start Time       End Time')
            print('--------------------------------------------------------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0], ' ', lt[a][1], ' ', lt[a][2], ' ', lt[a][3], ' ', lt[a][4], ' ', lt[a][5], ' ', lt[a][6])
            print('--------------------------------------------------------------------------------')
            print('Enter talk ID for changing schedule')
            tk_id = int(input())
            print('Mention new start time: (YYYY-MM-DT HH:MM)')
            nw_sdt = input()
            print('Mention new end time: (YYYY-MM-DT HH:MM)')
            nw_edt = input()
            nw_sdt = datetime.strptime(nw_sdt, '%Y-%m-%d %H:%M')
            nw_edt = datetime.strptime(nw_edt, '%Y-%m-%d %H:%M')
            return tk_id, nw_sdt, nw_edt
        return 0

def Update_Talk(stp, lt):
    os.system('cls')
    print('----------------------------------')
    print('  Concordia Conference System')
    print('----------------------------------')
    print('     Talk title update')
    print('----------------------------------')

    if stp == 1:
        print('Enter your name:')
        spk_name = input()
        print('Enter your passcode')
        spk_pass = input()
        return spk_name, spk_pass

    elif stp == 2:
        if lt:
            print('Talk ID    Talk Name      Start Time       End Time')
            print('-----------------------------------------------------------------')
            sz = len(lt)
            for a in range(sz):
                print(lt[a][0], ' ', lt[a][1], ' ', lt[a][2], ' ', lt[a][3])
            print('-----------------------------------------------------------------')
            print('Enter talk id for changing title')
            tk_id = int(input())
            print('Enter new title')
            nw_title = input()
            return tk_id, nw_title
        print('No assigned talk found')
        input()
        return 0