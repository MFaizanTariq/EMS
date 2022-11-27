from sqlalchemy import create_engine, ForeignKey, Column, Date, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from os import path
from datetime import datetime

engine = create_engine('sqlite:///venv/EMS.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

class Organizer(Base):
    __tablename__ = 'organizer'

    id = Column(Integer, primary_key=True)
    og_name = Column(String(25), nullable=False)
    og_pass = Column(String(15), nullable=False)

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    ev_name = Column(String(20), unique=True)
    ev_sdate = Column(Date, nullable=False)
    ev_edate = Column(Date, nullable=False)
    ev_og = Column(Integer, ForeignKey('organizer.id'), nullable=False)
    org = relationship('Organizer', backref='event')
    reg_list = relationship('Event_R_List', backref='event')


class Talk(Base):
    __tablename__ = 'talk'

    id = Column(Integer, primary_key=True)
    tk_name = Column(String(20), nullable=False)
    tk_room = Column(Integer, nullable=False)
    tk_spkr = Column(Integer, ForeignKey('speaker.id'), nullable=False)
    tk_sdt = Column(DateTime, nullable=False)
    tk_edt = Column(DateTime, nullable=False)
    tk_ev = Column(Integer, ForeignKey('event.id'), nullable=False)
    evnt = relationship('Event', backref='talk')
    spker = relationship('Speaker', backref='talk')


class Speaker(Base):
    __tablename__ = 'speaker'

    id = Column(Integer, primary_key=True)
    spk_name = Column(String(50), nullable=False)
    spk_pass = Column(String(20), nullable=False)


class Attendee(Base):
    __tablename__ = 'attendee'

    id = Column(Integer, primary_key=True)
    attend_name = Column(String(50), nullable=False)
    attend_pass = Column(String(20), nullable=False)
    ev_list = relationship('Event_R_List', backref='attendee')
    tk_list = relationship('Talk_R_List', backref='attendee')


class Event_R_List(Base):
    __tablename__ = 'event_r_list'

    id = Column(Integer, primary_key=True)
    ev_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    attendee_id = Column(Integer, ForeignKey('attendee.id'), nullable=False)


class Talk_R_List(Base):
    __tablename__ = 'talk_r_List'

    id = Column(Integer, primary_key=True)
    tk_id = Column(Integer, ForeignKey('talk.id'), nullable=False)
    attendee_id = Column(Integer, ForeignKey('attendee.id'), nullable=False)

def database_create():
    if not path.exists('venv/' + 'EMS.db'):
        Base.metadata.create_all(engine)
        print('Created Database!')

def Add_Organizer(og_name, og_pass):
    new_org = Organizer(og_name=og_name, og_pass=og_pass)
    session.add(new_org)
    session.commit()
     
def Add_Attendee(attend_name, attend_pass):
    new_attend = Attendee(attend_name=attend_name, attend_pass=attend_pass)
    session.add(new_attend)
    session.commit()
    
def Add_Speaker(spk_name, spk_pass):
    new_spk = Speaker(spk_name=spk_name, spk_pass=spk_pass)
    session.add(new_spk)
    session.commit()

def Add_Event(ev_name, ev_sdate, ev_edate, og_name, og_pass):
    all_ogs = session.query(Organizer).all()
    for all_og in all_ogs:
        if og_name==all_og.og_name and og_pass==all_og.og_pass:    
            new_ev = Event(ev_name=ev_name, ev_sdate=ev_sdate, ev_edate=ev_edate, ev_og=all_og.id)
            session.add(new_ev)
            session.commit()
            return int(1)
    return int(2)

def Add_Talk(ev_name, tk_name, room_no, spk_name, tk_sdt, tk_edt, og_name, og_pass):
    og_chk = 0
    og_chk_cmt = 'Organizer name / passcode not found'
    ev_chk = 0
    ev_chk_cmt = ' Event name not found'
    ev_og_chk = 0
    ev_og_chk_cmt = ' You cannot add talk, only organize can add talk'
    spk_chk = 0
    spk_chk_cmt = ' Speaker name not found'
    room_chk = 1
    room_chk_cmt = ' '
    og_id = 0

    og = session.query(Organizer).filter(Organizer.og_name == og_name, Organizer.og_pass == og_pass).first()
    if og:
        og_id = og.id
        og_chk = 1
        og_chk_cmt = ' '

    ev = session.query(Event).filter(Event.ev_name == ev_name).first()
    if ev:
        ev_id = ev.id
        ev_chk = 1
        ev_chk_cmt = ' '
        room_recs = session.query(Talk).filter(Talk.tk_ev == ev_id, Talk.tk_room == room_no)

        if ev.ev_og == og_id:
            ev_og_chk = 1
            ev_og_chk_cmt = ' '

        for room_rec in room_recs:
            if room_rec:
                s_time = room_rec.tk_sdt
                e_time = room_rec.tk_edt
                if tk_sdt >= s_time and tk_sdt <= e_time:
                    room_chk = 0
                    room_chk_cmt = ' Room not free in the selected time slot '
                elif tk_edt >= s_time and tk_edt <= e_time:
                    room_chk = 0
                    room_chk_cmt = ' Room not free in the selected time slot '
                elif tk_sdt <= s_time and tk_edt >= e_time:
                    room_chk = 0
                    room_chk_cmt = ' Room not free in the selected time slot '

    spk = session.query(Speaker).filter(Speaker.spk_name == spk_name).first()
    if spk:
        spk_id = spk.id
        spk_chk = 1
        spk_chk_cmt = ' '

    if spk_chk == 1 and ev_chk == 1 and og_chk == 1 and room_chk == 1 and ev_og_chk == 1:
        new_talk = Talk(tk_name=tk_name, tk_room=room_no, tk_spkr=spk_id, tk_sdt=tk_sdt, tk_edt=tk_edt, tk_ev=ev_id)
        session.add(new_talk)
        session.commit()
        cmt = 'Talk added successfully'
        return cmt

    cmt = og_chk_cmt + ev_chk_cmt + spk_chk_cmt + room_chk_cmt + ev_og_chk_cmt
    return cmt

def Event_List():
    all_evs = session.query(Event).all()
    return all_evs

def add_to_event(attend_name, attend_pass, ev_id):
    attend_chk = 0
    attend_chk_cmt = 'Attendee name / passcode not found'
    ev_chk = 0
    ev_chk_cmt = 'Event id entered wrong'

    attend = session.query(Attendee).filter(Attendee.attend_name == attend_name, Attendee.attend_pass == attend_pass).first()
    if attend:
        attend_id = attend.id
        attend_chk = 1
        attend_chk_cmt = ' '

    ev = session.query(Event).filter(Event.id == ev_id).first()
    if ev:
        ev_chk = 1
        ev_chk_cmt = ' '

    if attend_chk == 1 and ev_chk == 1:
        new_ev_reg = Event_R_List(ev_id=ev_id, attendee_id=attend_id)
        session.add(new_ev_reg)
        session.commit()
        cmt = 'Successfully registered to the selected event'
        return cmt

    cmt = attend_chk_cmt + ev_chk_cmt
    return cmt

def atd_event_search(attend_name, attend_pass):
    attend = session.query(Attendee).filter(Attendee.attend_name == attend_name, Attendee.attend_pass == attend_pass).first()
    lt = []
    if attend:
        evs = attend.ev_list

        for ev in evs:
            ev = session.query(Event).filter(Event.id == ev.ev_id).first()
            lt.append([ev.id, ev.ev_name, ev.ev_sdate, ev.ev_edate])

        return lt

    return lt

def atd_talk_search(ev_id, sr_md, sr_par):
    lt = []

    if sr_md == 1:
        sr_par = datetime.strptime(sr_par, '%Y-%m-%d').date()
        tks = session.query(Talk).filter(Talk.tk_ev == ev_id)

        for tk in tks:
            if tk:
                tk_date = tk.tk_sdt.date()
                if sr_par == tk_date:
                    lt.append([tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

        return lt

    elif sr_md == 2:
        sr_par = int(sr_par)
        tks = session.query(Talk).filter(Talk.tk_ev == ev_id, Talk.tk_room ==sr_par)

        for tk in tks:
            if tk:
                lt.append([tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

        return lt

def talk_list(og_name, og_pass):
    og_chk = 0
    og_chk_cmt = 'Organizer name / passcode not found'
    og_id = 0
    lt = []
    og = session.query(Organizer).filter(Organizer.og_name == og_name, Organizer.og_pass == og_pass).first()
    if og:
        og_id = og.id
        og_chk = 1
        og_chk_cmt = ' '

    evs = session.query(Event).filter(Event.ev_og == og_id)
    for ev in evs:
        if ev:
            ev_id = ev.id
            tks = session.query(Talk).filter(Talk.tk_ev == ev_id)
            for tk in tks:
                if tk:
                    lt.append([ev.ev_name,tk.id ,tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

    return lt

def update_talk(tk_id, nw_sdt, nw_edt):
    tk = session.query(Talk).filter(Talk.id == tk_id).first()
    tk_ev = tk.tk_ev
    room_no = tk.tk_room
    room_chk = 1
    room_chk_cmt = ' '

    room_recs = session.query(Talk).filter(Talk.tk_ev == tk_ev, Talk.tk_room == room_no)

    for room_rec in room_recs:
        if room_rec:
            s_time = room_rec.tk_sdt
            e_time = room_rec.tk_edt
            if nw_sdt >= s_time and nw_sdt <= e_time:
                room_chk = 0
                room_chk_cmt = ' Room not free in the selected time slot '
            elif nw_edt >= s_time and nw_edt <= e_time:
                room_chk = 0
                room_chk_cmt = ' Room not free in the selected time slot '
            elif nw_sdt <= s_time and nw_edt >= e_time:
                room_chk = 0
                room_chk_cmt = ' Room not free in the selected time slot '

    if room_chk == 1:
        session.query(Talk).filter(Talk.id == tk_id).update({'tk_sdt': nw_sdt, 'tk_edt': nw_edt})
        session.commit()
        cmt = 'Time update successfully'
        res = 1
        return cmt, res, tk_id
    cmt = room_chk_cmt
    return cmt, 0

def message_sent(tk_id):
    tk = session.query(Talk).filter(Talk.id == tk_id).first()
    tk_ev = tk.tk_ev
    tk_nm = tk.tk_name
    attds = session.query(Event_R_List).filter(Event_R_List.ev_id == tk_ev)
    for attd in attds:
        print("")
        if attd:
            id = attd.attendee_id
            atd = session.query(Attendee).filter(Attendee.id == id).first()
            os.system('cls')
            print ('Mr. ',atd.attend_name,', Please note that Talk Name:',tk_nm, 'has been rescheduled' )
            input()