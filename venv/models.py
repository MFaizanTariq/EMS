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
    def Add_Organizer(og_name, og_pass):
        new_org = Organizer(og_name=og_name, og_pass=og_pass)
        session.add(new_org)
        session.commit()


class Conference(Base):
    __tablename__ = 'conference'

    id = Column(Integer, primary_key=True)
    cn_name = Column(String(20), unique=True)
    cn_sdate = Column(Date, nullable=False)
    cn_edate = Column(Date, nullable=False)
    cn_og = Column(Integer, ForeignKey('organizer.id'), nullable=False)
    org = relationship('Organizer', backref='conference')
    reg_list = relationship('Conference_R_List', backref='conference')

    def Add_Conference(cn_name, cn_sdate, cn_edate, og_name, og_pass):
        all_ogs = session.query(Organizer).all()
        for all_og in all_ogs:
            if og_name == all_og.og_name and og_pass == all_og.og_pass:
                new_cn = Conference(cn_name=cn_name, cn_sdate=cn_sdate, cn_edate=cn_edate, cn_og=all_og.id)
                session.add(new_cn)
                session.commit()
                return int(1)
        return int(2)

    def Conference_List():
        all_cns = session.query(Conference).all()
        return all_cns


class Talk(Base):
    __tablename__ = 'talk'

    id = Column(Integer, primary_key=True)
    tk_name = Column(String(20), nullable=False)
    tk_room = Column(Integer, nullable=False)
    tk_spkr = Column(Integer, ForeignKey('speaker.id'), nullable=False)
    tk_sdt = Column(DateTime, nullable=False)
    tk_edt = Column(DateTime, nullable=False)
    tk_cn = Column(Integer, ForeignKey('conference.id'), nullable=False)
    cvnt = relationship('Conference', backref='talk')
    spker = relationship('Speaker', backref='talk')
    def Add_Talk(cn_name, tk_name, room_no, spk_name, tk_sdt, tk_edt, og_name, og_pass):
        og_chk = 0
        og_chk_cmt = 'Organizer name / passcode not found'
        cn_chk = 0
        cn_chk_cmt = ' Conference name not found'
        cn_og_chk = 0
        cn_og_chk_cmt = ' You cannot add talk, only organize can add talk'
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
    
        cn = session.query(Conference).filter(Conference.cn_name == cn_name).first()
        if cn:
            cn_id = cn.id
            cn_chk = 1
            cn_chk_cmt = ' '
            room_recs = session.query(Talk).filter(Talk.tk_cn == cn_id, Talk.tk_room == room_no)
    
            if cn.cn_og == og_id:
                cn_og_chk = 1
                cn_og_chk_cmt = ' '
    
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
    
        if spk_chk == 1 and cn_chk == 1 and og_chk == 1 and room_chk == 1 and cn_og_chk == 1:
            new_talk = Talk(tk_name=tk_name, tk_room=room_no, tk_spkr=spk_id, tk_sdt=tk_sdt, tk_edt=tk_edt, tk_cn=cn_id)
            session.add(new_talk)
            session.commit()
            cmt = 'Talk added successfully'
            return cmt
    
        cmt = og_chk_cmt + cn_chk_cmt + spk_chk_cmt + room_chk_cmt + cn_og_chk_cmt
        return cmt

    def atd_talk_search(cn_id, sr_md, sr_par):
        lt = []

        if sr_md == 1:
            sr_par = datetime.strptime(sr_par, '%Y-%m-%d').date()
            tks = session.query(Talk).filter(Talk.tk_cn == cn_id)

            for tk in tks:
                if tk:
                    tk_date = tk.tk_sdt.date()
                    if sr_par == tk_date:
                        lt.append([tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

            return lt

        elif sr_md == 2:
            sr_par = int(sr_par)
            tks = session.query(Talk).filter(Talk.tk_cn == cn_id, Talk.tk_room == sr_par)

            for tk in tks:
                if tk:
                    lt.append([tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

            return lt

    def update_talk_time(tk_id, nw_sdt, nw_edt):
        tk = session.query(Talk).filter(Talk.id == tk_id).first()
        tk_cn = tk.tk_cn
        room_no = tk.tk_room
        room_chk = 1
        room_chk_cmt = ' '

        room_recs = session.query(Talk).filter(Talk.tk_cn == tk_cn, Talk.tk_room == room_no)

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

    def update_talk_title(tk_id, nw_title):
        session.query(Talk).filter(Talk.id == tk_id).update({'tk_name': nw_title})
        session.commit()
        cmt = 'Title updated successfully'
        return cmt


class Speaker(Base):
    __tablename__ = 'speaker'

    id = Column(Integer, primary_key=True)
    spk_name = Column(String(50), nullable=False)
    spk_pass = Column(String(20), nullable=False)
    def Add_Speaker(spk_name, spk_pass):
        new_spk = Speaker(spk_name=spk_name, spk_pass=spk_pass)
        session.add(new_spk)
        session.commit()


class Attendee(Base):
    __tablename__ = 'attendee'

    id = Column(Integer, primary_key=True)
    attend_name = Column(String(50), nullable=False)
    attend_pass = Column(String(20), nullable=False)
    cn_list = relationship('Conference_R_List', backref='attendee')
    
    def Add_Attendee(attend_name, attend_pass):
        new_attend = Attendee(attend_name=attend_name, attend_pass=attend_pass)
        session.add(new_attend)
        session.commit()


class Conference_R_List(Base):
    __tablename__ = 'conference_r_list'

    id = Column(Integer, primary_key=True)
    cn_id = Column(Integer, ForeignKey('conference.id'), nullable=False)
    attendee_id = Column(Integer, ForeignKey('attendee.id'), nullable=False)


def database_create():
    if not path.exists('venv/' + 'EMS.db'):
        Base.metadata.create_all(engine)
        print('Created Database!')
     




def add_to_conference(attend_name, attend_pass, cn_id):
    attend_chk = 0
    attend_chk_cmt = 'Attendee name / passcode not found'
    cn_chk = 0
    cn_chk_cmt = 'Conference id entered wrong'

    attend = session.query(Attendee).filter(Attendee.attend_name == attend_name, Attendee.attend_pass == attend_pass).first()
    if attend:
        attend_id = attend.id
        attend_chk = 1
        attend_chk_cmt = ' '

    cn = session.query(Conference).filter(Conference.id == cn_id).first()
    if cn:
        cn_chk = 1
        cn_chk_cmt = ' '

    if attend_chk == 1 and cn_chk == 1:
        new_cn_reg = Conference_R_List(cn_id=cn_id, attendee_id=attend_id)
        session.add(new_cn_reg)
        session.commit()
        cmt = 'Successfully registered to the selected conference'
        return cmt

    cmt = attend_chk_cmt + cn_chk_cmt
    return cmt

def atd_conference_search(attend_name, attend_pass):
    attend = session.query(Attendee).filter(Attendee.attend_name == attend_name, Attendee.attend_pass == attend_pass).first()
    lt = []
    if attend:
        cns = attend.cn_list

        for cn in cns:
            cn = session.query(Conference).filter(Conference.id == cn.cn_id).first()
            lt.append([cn.id, cn.cn_name, cn.cn_sdate, cn.cn_edate])

        return lt

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

    cns = session.query(Conference).filter(Conference.cn_og == og_id)
    for cn in cns:
        if cn:
            cn_id = cn.id
            tks = session.query(Talk).filter(Talk.tk_cn == cn_id)
            for tk in tks:
                if tk:
                    lt.append([cn.cn_name,tk.id ,tk.tk_name, tk.tk_room, tk.spker.spk_name, tk.tk_sdt, tk.tk_edt])

    return lt


def message_sent(tk_id):
    tk = session.query(Talk).filter(Talk.id == tk_id).first()
    tk_cn = tk.tk_cn
    tk_nm = tk.tk_name
    attds = session.query(Conference_R_List).filter(Conference_R_List.cn_id == tk_cn)
    for attd in attds:
        print("")
        if attd:
            id = attd.attendee_id
            atd = session.query(Attendee).filter(Attendee.id == id).first()
            os.system('cls')
            print ('Mr. ',atd.attend_name,', Please note that Talk Name:',tk_nm, 'has been rescheduled' )
            input()

def spkr_list(spk_name, spk_pass):
    spk_chk = 0
    spk_id = 0
    lt = []
    spk = session.query(Speaker).filter(Speaker.spk_name == spk_name, Speaker.spk_pass == spk_pass).first()
    if spk:
        spk_id = spk.id
        spk_chk = 1

    if spk_chk == 1:
        tks = session.query(Talk).filter(Talk.tk_spkr == spk_id)
        for tk in tks:
            if tk:
                lt.append([tk.id, tk.tk_name, tk.tk_sdt, tk.tk_edt])

        return lt

    else:
        os.system('cls')
        print ('Speaker name / pass code not found')
        input()

