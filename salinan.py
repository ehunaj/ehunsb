
# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import Message
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)

msg_dict = {}
msg_dict1 = {}
helpMessage = """
━━━━┅═❉ই۝ई❉═┅━━━━
║┝──[❇ STATUS ❇ ]
║│ Restart
║│ Runtime
║│ Speed
║│ Status
║│ Rtime
║│ Dell「Removechat」
║┝───────────────
║┝──[ ❇ SETTING ❇ ]
║│ Allstatus「On/Off」
║│ Notif「On/Off」
║│ Sider「On/Off」
║│ AutoAdd「On/Off」
║│ AutoJoin「On/Off」
║│ AutoLeave「On/Off」
║│ AutoRead「On/Off」
║│ CheckSticker「On/Off」
║│ DetectMention「On/Off」
║┝───────────────
║┝──[ ❇  SELF  ❇]
║│ Me
║│ Mid
║│ MyName
║│ MyBio
║│ MyPicture
║│ MyVideoProfile
║│ MyCover
║│ StealContact「@」
║│ StealMid「@」
║│ StealName「@」
║│ StealBio「@」
║│ StealPicture「@」
║│ StealVideoProfile「@」
║│ StealCover「@」
║│ CloneProfile「@」
║│ RestoreProfile
║┝───────────────
║┝──[ ❇ GROUP ❇ ]
║│ GroupCreator
║│ GroupId
║│ GroupName
║│ GroupPicture
║│ GroupTicket
║│ GroupTicket「On/Off」
║│ GroupList
║│ GroupMemberList
║│ GroupInfo
║│ Mimic「On/Off」
║│ MimicList
║│ MimicAdd「@」
║│ MimicDel「@」
║│ Tag"
║│ Lurking「On/Off」
║│ Lurkingn
║┝───────────────
║┝──[ ❇ MEDIA ❇]
║│ Kalender
║│ CheckDate「Date」
║┝───────────────
║╰❉     EHUN BOT      ❇
╰━━━━━━━━━━━━━━━━
 ━━━━┅═❉ই۝ई❉═┅━━━━
"""
wait = {
    "invite":True,
    "addbots":False,
    "dellbots":False,
    "members":1,
    "mention":"║┝──────────────\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━n  ━━━━┅═❉ই۝ई❉═┅━━━━",
    "Respontag":"Hoi Jgn ngtag semm",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by Ehun",
    "message":"Terimakasih sudah add saya",
    "qr":False
}
settings = {
    "autoAdd": False,
    "autoJoin": False,
    "autoLeave": False,
    "autoRead": False,
    "lang":"JP",
    "detectMention": True,
    "changeGroupPicture":[],
    "notifikasi": False,
    "Sider":{},
    "checkSticker": False,
    "autoJoinTicket": True,
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
        "displayName": "",
        "statusMessage": "",
        "pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}
bl = {
    "blacklist":{}
    }
setTime = {}
setTime = read["readTime"]
mulai = time.time()

myProfile["displayName"]
myProfile["statusMessage"]
myProfile["pictureStatus"]

with open('bl.json', 'r') as fp:
    bl = json.load(fp)
with open('hun.json', 'r') as fp:
    hun = json.load(fp)
def sendMessage(self, messageObject):
    return self.Talk.client.sendMessage(0,messageObject)

class LineBot(object):
    def __init__(self, resp, authQR=None):
        self.resp = resp
        self.resp = self.resp+' '
        self.authQR = authQR
        self.login(authQR)
        self.fetch()

    def AutoSave(self,op):
        msg = op.message
        self.client.unsend2(msg,self.wait)
        self.client.fancyfancy(self.wait)
        with open(self.anus, 'W') as fp:
            json.dump(self.wait,fp, sort_keys=True, indent=4, ensur_ascil=False)

    def login(self, auth):
        if auth == None:
            self.client = LINE()
        else:
            self.client = LINE(auth)
  #      self.client.log("Auth Token :" + str(self.client.authToken))
        self.mid = self.client.getProfile().mid
        self.Profile = self.client.getProfile()
        self.Settings = self.client.getSettings()

    def fetch(self):
        while True:
            try:
                self.operations = self.client.poll.fetchOperations(self.client.revision, 50)
                for op in self.operations:
                    if (op.type !=OpType.END_OF_OPERATION):
                        self.client.revision = max(self.client.revision, op.revision)
                        self.bot(op)
                        self.AutoSave(op)
            except:
                pass
    def restartBot():
        print ("[ INFO ] BOT RESETTED")
        time.sleep(3)
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def waktu(secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days, hours = divmod(hours,24)
        month, days = divmod(days,30)
        years, month = divmod(month,12)
        return '\n╠  %02d Tahun\n╠  %02d Bulan\n╠  %02d Hari\n╠  %02d Jam\n╠  %02d Menit\n╠  %02d Detik」' %(years, month, days ,hours, mins,secs)

    def sendMessage(to, Message, contentMetadata={}, contentType=0):
        mes = Message()
        mes.to, mes._from = to, profile.mid
        mes.text = text
        mes.contentType, mes. contentMetadata = contentType, contentMetadata
        if to not in messageReq:
            messageReq[to] = -1
        messageReq[to] += 1

    def command(text):
        pesan = text.lower()
        if pesan.startswith():
            cmd = pesan.replace()
        else:
           cmd = "command"
           return cmd
    def cms(string, commands): #/XXX, >XXX, ;XXX, ^XX>
        tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
        for texX in tex:
            for command in commands:
                if string == command:
                    return True
        return False
    def backupData():
        try:
            backup = settings
            f = codecs.open('temp.json','w','utf-8')
            json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
            backup = read
            f = codecs.open('read.json','w','utf-8')
            json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
            return True
        except Exception as error:
            logError(error)
            return False

    def bot(self, op):
        cl = self.client
        mid = self.mid
        bsyname = hun['teamname']
        responsename = cl.getProfile().displayName
        admin = "ub3808de9f7df35f57fb366d157f9790a"
        global time
        global ast
        global groupParam
        try:
            if op.type == 0 or op.type == 50:
                print ("[ 0 ] END OF OPERATION")
                return
            if op.type == 13:
                if self.mid in op.param3:
                    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
                if self.mid in op.param3:
                    if op.param2 in hun["botteam"]:
                        cl.acceptGroupInvitation(op.param1)
                if self.mid in op.param3:
                    if settings["autoJoin"] == True:
                        G = cl.getGroup(op.param1)
                        if len(G.members) <= wait["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.findAndAddContactsByMid(hun["botteam"])
                            cl.inviteIntoGroup(op.param1,hun["botteam"])
                            cl.acceptGroupInvitation(op.param1)
                            pass

                if op.param3 in bl['blacklist']:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                cl.cancelGroupInvitation(op.param1,[tag])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            
            if op.type == 11:
                if wait["qr"] == True:
                    if op.param2 not in hun["botteam"]  and op.param2 not in admin:
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        bl['blacklist'][op.param2] = True
            if op.type == 32:
                if op.param3 in hun["botteam"]:
                    if op.param2 in hun["botteam"]:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        bl["blacklist"][op.param2] = True
                        with open('bl.json', 'w') as fp:
                            json.dump(bl, fp, sort_keys=True, indent=4)
                        try:
                            if op.param3 not in bl["blacklist"]:
#                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.findAndAddContactsByMid(op.param3)
                                cl.inviteIntoGroup(op.param1,hun["botteam"])
                                cl.acceptGroupInvitation(op.param1)
                        except:
                            pass
            if op.type == 19:
                if op.param3 in hun["botteam"]:
                    if op.param2 in hun["botteam"]:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        bl['blacklist'][op.param2] = True
                        with open('bl.json', 'w') as fp:
                            json.dump(bl, fp, sort_keys=True, indent=4)
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,hun["botteam"])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            pass
            if op.type == 17:
                if op.param2 in bl["blacklist"]:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
            if op.type == 55:
                if op.param2 in bl["blacklist"]:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

            if op.type == 5:
                print ("[ 5 ] NOTIFIED ADD CONTACT")
                if settings["autoAdd"] == True:
                    cl.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(cl.getContact(op.param1).displayName)))

            if op.type == 26:
                print ("25")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                text = text.lower()
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    if text.lower == 'help':
                      if msg._from in admin:
                          cl.sendMessage(to, helpMessage)

                    elif text.lower() == 'clear':
                      if msg._from in admin:
                          bl["blacklist"] = {}
                          cl.sendMessage(to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")

                    elif text.lower() == 'clearbot':
                      if msg._from in admin:
                          hun["botteam"] = {}
                          cl.sendMessage(to,"ヽ( ^ω^)ﾉ└ ❉Clearbot All")

                    elif text.lower() == 'bye':
                      if msg._from in admin:
                          cl.leaveGroup(to)
                    elif text.lower() == 'invite':
                      if msg._from in admin:
                          wait['invite'] = True
                          cl.sendMessage(to,"Kirim contact nya")

                    elif text.lower() == 'join':
                      if msg._from in admin:
                          G = cl.getGroup(msg.to)
                          G.preventedJoinByTicket = False
                          cl.updateGrouo(G)
                          Ti = cl.reissueGroupTicket(msg.to)
                          hun["botteam"].acceptGroupInvitationByTicket(to,Ti)
                          G.preventedJoinByTicket = True
                          cl.updateGrouo(G)

                    elif text.lower() == 'jepit':
                      if msg._from in admin:
                          cl.findAndAddContactsByMid(msg.to)
                          cl.inviteIntoGroup(msg.to, hun["botteam"])
                          cl.acceptGroupInvitation(msg.to)

                    elif msg.text in ["Leave"]:
                      if msg._from in admin:
                          gid = cl.getGroupIdsJoined()
                          for i in gid:
                              cl.sendMessage(i,"Bot Di Paksa Keluar Oleh Owner!\nAyo left teman2\nAssalamualikum wr wb All Member\nnAdd Owner kami")
                              cl.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                              cl.leaveGroup(i)

                    elif 'Sampah' in msg.text:
                      if msg._from in admin:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                cl.cancelGroupInvitation(to,[_mid])
                    elif text.lower() == "cek":
                      if msg._from in admin:
                          try:cl.inviteIntoGroup(to,[mid]);has = "OK"
                          except:has = "NOT"
                          try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                          except:has1 = "NOT"
                          if has == "OK":sil = "🔋██ full 100%"
                          else:sil = "🔌█▒. Low 0%"
                          if has1 == "OK":sil1 = "🔋██ full 100%"
                          else:sil1 = "🔌█▒ Low 0%"
                          cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))

                    elif text.lower() == 'banlist':
                      if msg._from in admin:
                        if bl["blacklist"] == {}:
                            cl.sendMessage(to,"Tidak Ada")
                        else:
                            mcs = ""
                            for mi_d in bl["blacklist"]:
                                mcs += "->" + cl.getContact(mi_d).displayName + "\n"
                            cl.sendMessage(to,"===[Blacklist User]===\n" + mcs)
                    elif text.lower() == 'botlist':
                      if msg._from in admin:
                        if hun["botteam"] == {}:
                            cl.sendMessage(to,"Tidak Ada")
                        else:
                            mcs = ""
                            for mi_d in hun["botteam"]:
                                mcs += "->" + cl.getContact(mi_d).displayName + "\n"
                            cl.sendMessage(to,"===[TeamBot User]===\n" + mcs)


                    elif "Admindell " in msg.text:
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target not in admin:
                                  try:
                                      admin.remove(target)
                                      cl.sendMessage(to,"Berhasilmenghapus admin")
                                  except:
                                      pass
                    elif ("jemput " in msg.text):
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target not in admin:
                                  try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.sendMessage(to,"Berhasil")
                                  except:
                                      pass

                    elif msg.text in ["Cekbots"]:
                      if msg._from in admin:
                          cl.sendMessage(to,"• For Bots 「 " +self.resp+ " 」")
  
                    elif msg.text in ["Cekteam"]:
                      if msg._from in admin:
                          cl.sendMessage(to,"• GroupBotname 「 " +bsyname+ " 」")
           

                    elif ("Addbot " in msg.text):
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target in hun["botteam"]:
                                  cl.sendMessage(to," team bost")
                              else:
                                  try:
                                      hun["botteam"][target] = True
                                      with open('hun.json','w') as fp:
                                          json.dump(hun, fp, sort_keys=True, indent=4)
                                      cl.sendMessage(to," team bost")
                                  except:
                                      pass
                    elif ("Delbot " in msg.text):
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target not in hun["botteam"]:
                                  cl.sendMessage(to,"Delist team bost")
                              else:
                                  try:
                                      del hun["botteam"][target]
                                      with open('hun.json','w') as fp:
                                          json.dump(hun, fp, sort_keys=True, indent=4)
                                      cl.sendMessage(to,"Delist team bost")
                                  except:
                                      pass

                    elif ("Bot " in msg.text):
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target not in admin:
                                  try:
                                      Bots.append(target)
                                      cl.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ")
                                  except:
                                      pass

                    elif ("Kick " in msg.text):
                      if msg._from in admin:
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          targets = []
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              if target not in admin:
                                  try:
                                      bl["blacklist"][target] = True
                                      cl.kickoutFromGroup(to,[target])
                                  except:
                                      pass
                    elif text.lower() == 'dell':
                      if msg._from in admin:
                          cl.removeAllMessages(op.param2)
                          cl.sendMessage(to, "Succes Menghapus Chat")
                          cl.removeAllMessages(op.param2)
                          cl.sendMessage(to, "Succes Menghapus Chat")
                    elif text.lower() == 'speed':
                      if msg._from in admin:
                          start = time.time()
                          elapsed_time = time.time() - start
                          cl.sendMessage(to,format(str(elapsed_time)))
                    elif text.lower() == 'restart':
                      if msg._from in admin:
                          cl.sendMessage(to, "Sudah di restart...")
                          restartBot()
                    elif text.lower() == 'runtime':
                      if msg._from in admin:
                          timeNow = time.time()
                          runtime = timeNow - botStart
                          runtime = format_timespan(runtime)
                          cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
                    elif text.lower() == 'rtime':
                      if msg._from in admin:
                          eltime = time.time() - mulai
                          cl.sendMessage(to,"Ehun BotSudah BerjalanSelama :\n"+waktu(eltime))
                    elif text.lower() == 'respon':
                      if msg._from in admin:
                          cl.sendMessage(to,"Hadir")

                    elif text.lower() == 'status':
                      if msg._from in admin:
                          try:
                              ret_ = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    STATUS    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ 🔵[ON]|[OFF]🔴 ❇\n║┝───────────────"
                              if settings["autoAdd"] == True: ret_ += "\n║│🔵 Auto Add [ON]"
                              else: ret_ += "\n║│🔴 AutoAdd [OFF]"
                              if settings["autoJoin"] == True: ret_ += "\n║│🔵 AutoJoin [ON]"
                              else: ret_ += "\n║│🔴 AutoJoin [OFF]"
                              if settings["autoLeave"] == True: ret_ += "\n║│🔵 AutoLeave [ON]"
                              else: ret_ += "\n║│🔴 AutoLeave [OFF]"
                              if settings["autoRead"] == True: ret_ += "\n║│🔵 AutoRead [ON]"
                              else: ret_ += "\n║│🔴 AutoRead [OFF]"
                              if settings["notifikasi"] == True: ret_ += "\n║│🔵 Notif [ON]"
                              else: ret_ += "\n║│🔴 Notif [OFF]"
                              if settings["detectMention"] == True: ret_ += "\n║│🔵 Detect Mention [ON]"
                              else: ret_ += "\n║│🔴 Detect Mention [OFF]"
                              ret_ += "\n║┝───────────────\n║╰❉      EHUN  BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
                              cl.sendMessage(to, str(ret_))
                          except Exception as e:
                              cl.sendMessage(msg.to, str(e))
                    elif text.lower() == 'autoadd on':
                      if msg._from in admin:
                          settings["autoAdd"] = True
                          cl.sendMessage(to, "mengaktifkan Auto Add")
                    elif text.lower() == 'autoadd off':
                      if msg._from in admin:
                          settings["autoAdd"] = False
                          cl.sendMessage(to, "menonaktifkan Auto Add")
                    elif text.lower() == 'autojoin on':
                      if msg._from in admin:
                          settings["autoJoin"] = True
                          cl.sendMessage(to, "mengaktifkan Auto Join")
                    elif text.lower() == 'autojoin off':
                      if msg._from in admin:
                          settings["autoJoin"] = False
                          cl.sendMessage(to, "menonaktifkan Auto Join")
                    elif text.lower() == 'autoleave on':
                      if msg._from in admin:
                          settings["autoLeave"] = True
                          cl.sendMessage(to, "mengaktifkan Auto Leave")
                    elif text.lower() == 'autojoin off':
                      if msg._from in admin:
                          settings["autoLeave"] = False
                          cl.sendMessage(to, "menonaktifkan Auto Leave")
                    elif text.lower() == 'autoread on':
                      if msg._from in admin:
                          settings["autoRead"] = True
                          cl.sendMessage(to, "mengaktifkan Auto Read")
                    elif text.lower() == 'autoread off':
                      if msg._from in admin:
                          settings["autoRead"] = False
                          cl.sendMessage(to, "menonaktifkan Auto Read")
                    elif text.lower() == 'checksticker on':
                      if msg._from in admin:
                          settings["checkSticker"] = True
                          cl.sendMessage(to, "mengaktifkan Check Details Sticker")
                    elif text.lower() == 'checksticker off':
                      if msg._from in admin:
                          settings["checkSticker"] = False
                          cl.sendMessage(to, "menonaktifkan Check Details Sticker")
                    elif text.lower() == 'detectmention on':
                      if msg._from in admin:
                          settings["datectMention"] = True
                          cl.sendMessage(to, "mengaktifkan Detect Mention")
                    elif text.lower() == 'detectmention off':
                      if msg._from in admin:
                          settings["datectMention"] = False
                          cl.sendMessage(to, "menonaktifkan Detect Mention")

                    elif text.lower() == 'allstatus on':
                      if msg._from in admin:
                          settings["notifikasi"] = True
                          settings["autoAdd"] = True
                          settings["autoJoin"] = True
                          settings["autoLeave"] = True
                          settings["autoRead"] = True
                          settings["datectMention"] = True
                          cl.sendMessage(to, "Allstatus bot mode on")

                    elif text.lower() == 'allstatus off':
                      if msg._from in admin:
                          settings["notifikasi"] = False
                          settings["autoAdd"] = False
                          settings["autoJoin"] = False
                          settings["autoLeave"] = False
                          settings["autoRead"] = False
                          settings["datectMention"] = False
                          cl.sendMessage(to, "Allstatus bot mode on")

                    elif text.lower() == 'me':
#                          sendMessageWithMention(to, msg._from) 
                          cl.sendContact(to, msg._from)
                    elif text.lower() == 'mid':
                          #sendMessageWithMention(to, msg._from)
                          cl.sendMessage(to,"[MID]\n" +  msg._from)

                    elif text.lower() == 'myname':
                      if msg._from in admin:
                          mme = cl.getContact(msg._from)
                          cl.sendMessage(to,"[DisplayName]\n" + mme.displayName)
                    elif text.lower() == 'mybio':
                      if msg._from in admin:
                          mme = cl.getContact(msg._from)
                          cl.sendMessage(to,"[StatusMessage]\n" + mme.statusMessage)
                    elif text.lower() == 'mypicture':
                      if msg._from in admin:
                          mme = cl.getContact(msg._from)
                          cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + mme.pictureStatus)
                    elif text.lower() == 'myvideoprofile':
                      if msg._from in admin:
                          mme = cl.getContact(msg._from)
                          cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + mme.pictureStatus + "/vp")
                    elif text.lower() == 'mycover':
                      if msg._from in admin:
                          mme = cl.getContact(msg._from)
                          cover = cl.getProfileCoverURL(msg._from)
                          cl.sendImageWithURL(to, cover)
                    elif text.lower() == "stealcontact ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                mi_d = contact.mid
                                cl.sendContact(to, mi_d)
                    elif text.lower() == "stealmid ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                            for ls in lists:
                                ret_ += "\n{}" + ls
                                cl.sendMessage(msg.to, str(ret_))
                    elif text.lower() == "stealname ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                cl.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                    elif text.lower() == "stealbio ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                contact = cl.getContact(ls)
                                cl.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                    elif text.lower() == "stealpicture ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                                cl.sendImageWithURL(msg.to, str(path))
                    elif text.lower() == "stealvideoprofile ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                                cl.sendImageWithURL(msg.to, str(path))
                    elif text.lower() == "stealcover ":
                      if msg._from in admin:
                        if cl != None:
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                              names = re.findall(r'@(\w+)', text)
                              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                              mentionees = mention['MENTIONEES']
                              lists = []
                              for mention in mentionees:
                                  if mention["M"] not in lists:
                                      lists.append(mention["M"])
                              for ls in lists:
                                  path = cl.getProfileCoverURL(ls)
                                  cl.sendImageWithURL(msg.to, str(path))
                    elif text.lower() == "cloneprofile ":
                      if msg._from in admin:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                contact = mention["M"]
                                break
                            try:
                                cl.cloneContactProfile(contact)
                                cl.sendMessage(msg.to, "clone member ")
                            except:
                                cl.sendMessage(msg.to, "Gagal clone member")
                    elif text.lower() == 'restoreprofile':
                      if msg._from in admin:
                        try:
                            Profile.displayName = str(myProfile["displayName"])
                            Profile.statusMessage = str(myProfile["statusMessage"])
                            Profile.pictureStatus = str(myProfile["pictureStatus"])
                            cl.updateProfileAttribute(8, Profile.pictureStatus)
                            cl.updateProfile(Profile)
                            cl.sendMessage(msg.to, "restore profile ")
                        except:
                            cl.sendMessage(msg.to, "Gagal restore profile")

                    elif text.lower() == "mimicadd ":
                      if msg._from in admin:
                          targets = []
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              try:
                                  settings["mimic"]["target"][target] = True
                                  cl.sendMessage(msg.to,"Target ditambahkan!")
                                  break
                              except:
                                  cl.sendMessage(msg.to,"Added Target Fail !")
                                  break
                    elif text.lower() == "mimicdel ":
                      if msg._from in admin:
                          targets = []
                          key = eval(msg.contentMetadata["MENTION"])
                          key["MENTIONEES"][0]["M"]
                          for x in key["MENTIONEES"]:
                              targets.append(x["M"])
                          for target in targets:
                              try:
                                  del settings["mimic"]["target"][target]
                                  cl.sendMessage(msg.to,"Target dihapuskan!")
                                  break
                              except:
                                  cl.sendMessage(msg.to,"Deleted Target Fail !")
                                  break
                    elif text.lower() == 'mimiclist':
                      if msg._from in admin:
                        if settings["mimic"]["target"] == {}:
                            cl.sendMessage(msg.to,"Tidak Ada Target")
                        else:
                            mc = "╔══[ Mimic List ]"
                            for mi_d in settings["mimic"]["target"]:
                                mc += "\n╠ "+cl.getContact(mi_d).displayName
                            cl.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                    elif "mimic" in msg.text.lower():
                      if msg._from in admin:
                          sep = text.split(" ")
                          mic = text.replace(sep[0] + " ","")
                          if mic == "on":
                              if settings["mimic"]["status"] == False:
                                  settings["mimic"]["status"] = True
                                  cl.sendMessage(msg.to,"Reply Message on")
                          elif mic == "off":
                              if settings["mimic"]["status"] == True:
                                  settings["mimic"]["status"] = False
                                  cl.sendMessage(msg.to,"Reply Message off")


                    elif text.lower() == 'groupcreator':
                      if msg._from in admin:
                          group = cl.getGroup(to)
                          GS = group.creator.mid
                          cl.sendContact(to, GS)
                    elif text.lower() == 'groupid':
                      if msg._from in admin:
                          gid = cl.getGroup(to)
                          cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                    elif text.lower() == 'grouppicture':
                      if msg._from in admin:
                          group = cl.getGroup(to)
                          path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                          cl.sendImageWithURL(to, path)
                    elif text.lower() == 'groupname':
                      if msg._from in admin:
                          gid = cl.getGroup(to)
                          cl.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                    elif text.lower() == 'groupticket':
                      if msg._from in admin:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                ticket = cl.reissueGroupTicket(to)
                                cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            else:
                                cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                    elif text.lower() == 'groupticket on':
                      if msg._from in admin:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            if group.preventedJoinByTicket == False:
                                cl.sendMessage(to, "Grup qr sudah terbuka")
                            else:
                                group.preventedJoinByTicket = False
                                cl.updateGroup(group)
                                cl.sendMessage(to, "membuka grup qr")
                    elif text.lower() == 'groupticket off':
                      if msg._from in admin:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            if group.preventedJoinByTicket == True:
                                cl.sendMessage(to, "Grup qr sudah tertutup")
                            else:
                                group.preventedJoinByTicket = True
                                cl.updateGroup(group)
                                cl.sendMessage(to, "menutup grup qr")
                    elif text.lower() == 'groupinfo':
                      if msg._from in admin:
                          group = cl.getGroup(to)
                          try:
                              gCreator = group.creator.displayName
                          except:
                              gCreator = "Tidak ditemukan"
                          if group.invitee is None:
                              gPending = "0"
                          else:
                              gPending = str(len(group.invitee))
                          if group.preventedJoinByTicket == True:
                              gQr = "Tertutup"
                              gTicket = "Tidak ada"
                          else:
                              gQr = "Terbuka"
                              gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                          path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                          ret_ = "╔══[ Group Info ]"
                          ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                          ret_ += "\n╠ ID Group : {}".format(group.id)
                          ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                          ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                          ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                          ret_ += "\n╠ Group Qr : {}".format(gQr)
                          ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                          ret_ += "\n╚══[ Group Info ]"
                          cl.sendMessage(to, str(ret_))
                          cl.sendImageWithURL(to, path)
                    elif text.lower() == 'groupmemberlist':
                      if msg._from in admin:
                        if msg.toType == 2:
                            group = cl.getGroup(to)
                            ret_ = "╔══[ Member List ]"
                            no = 0 + 1
                            for mem in group.members:
                                ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                no += 1
                            ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                            cl.sendMessage(to, str(ret_))
                    elif text.lower() == 'grouplist':
                      if msg._from in admin:
                          groups = cl.groups
                          ret_ = "╔══[ Group List ]"
                          no = 0 + 1
                          for gid in groups:
                              group = cl.getGroup(gid)
                              ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                              no += 1
                          ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                          cl.sendMessage(to, str(ret_))

                    elif text.lower() == "botlist":
                      if msg._from in admin:
                          ma = ""
                          a = 0
                          for m_id in Bots:
                              a = a + 1
                              end = '\n'
                              ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                          cl.sendMessage(msg.to,"🔰ʙᴏᴛʟɪsᴛ🔰\n\n\n"+ma+"\n%s ʙᴏᴛs" %(str(len(Bots))))

                    elif text.lower() == 'notif on':
                      if msg._from in admin:
                        if settings["notifikasi"] == True:
                          if settings["lang"] == "JP":
                              cl.sendMessage(msg.to,"notif mode on")
                          else:
                              settings["notifikasi"] = True
                              if settings["lang"] == "JP":
                                  cl.sendMessage(msg.to,"notif mode on")

                    elif text.lower() == 'notif off':
                      if msg._from in admin:
                        if settings["notifikasi"] == False:
                          if settings["lang"] == "JP":
                              cl.sendMessage(msg.to,"notif mode off")
                          else:
                              settings["notifikasi"] = False
                              if settings["lang"] == "JP":
                                  cl.sendMessage(msg.to,"notif mode off")
                    elif text.lower() == 'tag':
                      if msg._from in admin:
                        if msg.toType == 0:
                            sendMention(to, to, "", "")
                        elif msg.toType == 2:
                              group = cl.getGroup(to)
                              midMembers = [contact.mid for contact in group.members]
                              midSelect = len(midMembers)//20
                              for mentionMembers in range(midSelect+1):
                                  no = 0
                                  ret_ = "╔══[ Mention Members ]"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠ {}. @!".format(str(no))
                                  ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                                  cl.sendMention(msg.to, ret_, dataMid)
                    elif text.lower() == 'changepictureprofile':
                      if msg._from in admin:
                          settings["changePicture"] = True
                          cl.sendMessage(to, "Silahkan kirim gambarnya")
                    elif text.lower() == 'changegrouppicture':
                      if msg._from in admin:
                        if msg.toType == 2:
                          if to not in settings["changeGroupPicture"]:
                              settings["changeGroupPicture"].append(to)
                              cl.sendMessage(to, "Silahkan kirim gambarnya")
                    elif text.lower() == 'lurking on':
                      if msg._from in admin:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                              if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                              if bln == str(k): bln = bulan[k-1]
                          readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          if msg.to in read['readPoint']:
                              try:
                                  del read['readPoint'][msg.to]
                                  del read['readMember'][msg.to]
                                  del read['readTime'][msg.to]
                              except:
                                  pass
                              read['readPoint'][msg.to] = msg.id
                              read['readMember'][msg.to] = ""
                              read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                              read['ROM'][msg.to] = {}
                              with open('read.json', 'w') as fp:
                                  json.dump(read, fp, sort_keys=True, indent=4)
                                  cl.sendMessage(msg.to,"Lurking already on")
                          else:
                              try:
                                  del read['readPoint'][msg.to]
                                  del read['readMember'][msg.to]
                                  del read['readTime'][msg.to]
                              except:
                                  pass
                              read['readPoint'][msg.to] = msg.id
                              read['readMember'][msg.to] = ""
                              read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                              read['ROM'][msg.to] = {}
                              with open('read.json', 'w') as fp:
                                  json.dump(read, fp, sort_keys=True, indent=4)
                                  cl.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                    elif text.lower() == 'lurking off':
                      if msg._from in admin:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                              if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                              if bln == str(k): bln = bulan[k-1]
                          readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          if msg.to not in read['readPoint']:
                              cl.sendMessage(msg.to,"Lurking already off")
                          else:
                              try:
                                  del read['readPoint'][msg.to]
                                  del read['readMember'][msg.to]
                                  del read['readTime'][msg.to]
                              except:
                                  pass
                              cl.sendMessage(msg.to, "Delete reading point:\n" + readTime)

                    elif text.lower() == 'lurking reset':
                      if msg._from in admin:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                              if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                              if bln == str(k): bln = bulan[k-1]
                          readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          if msg.to in read["readPoint"]:
                              try:
                                  del read["readPoint"][msg.to]
                                  del read["readMember"][msg.to]
                                  del read["readTime"][msg.to]
                              except:
                                  pass
                              cl.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                          else:
                              cl.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")

                    elif text.lower() == 'lurking':
                      if msg._from in admin:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                              if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                              if bln == str(k): bln = bulan[k-1]
                          readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          if receiver in read['readPoint']:
                              if read["ROM"][receiver].items() == []:
                                  cl.sendMessage(receiver,"[ Reader ]:\nNone")
                              else:
                                  chiya = []
                                  for rom in read["ROM"][receiver].items():
                                      chiya.append(rom[1])
                                  cmem = cl.getContacts(chiya) 
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan = '[ Reader ]:\n'
                              for x in range(len(cmem)):
                                  xname = str(cmem[x].displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@c\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                              text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                              try:
                                  cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              except Exception as error:
                                  print (error)
                                  pass
                          else:
                              cl.sendMessage(receiver,"Lurking has not been set.")

                    elif text.lower() == 'sider on':
                      if msg._from in admin:
                          try:
                              del cctv['point'][msg.to]
                              del cctv['sidermem'][msg.to]
                              del cctv['cyduk'][msg.to]
                          except:
                              pass
                          cctv['point'][msg.to] = msg.id
                          cctv['sidermem'][msg.to] = ""
                          cctv['cyduk'][msg.to]=True 
                          settings["Sider"] = True
                          cl.sendMessage(msg.to,"SIDER SUDAH ON")

                    elif text.lower() == 'sider off':
                      if msg._from in admin:
                        if msg.to in cctv['point']:
                            cctv['cyduk'][msg.to]=False
                            settings["Sider"] = False
                            cl.sendMessage(msg.to,"SIDER SUDAH OFF")
                        else:
                            cl.sendMessage(msg.to,"SIDER SUDAH OFF")

                    elif text.lower() == 'kalender':
                          tz = pytz.timezone("Asia/Makassar")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                              if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                              if bln == str(k): bln = bulan[k-1]
                          readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          cl.sendMessage(to, readTime)                 
                    elif "checkdate" in msg.text.lower():
                      if msg._from in admin:
                          sep = msg.text.split(" ")
                          tanggal = msg.text.replace(sep[0] + " ","")
                          r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                          data=r.text
                          data=json.loads(data)
                          ret_ = ""
                          ret_ += "Date Of Birth : {}".format(str(data["data"]["lahir"]))
                          ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                          ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                          ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                          ret_ += ""
                          cl.sendMessage(to, str(ret_))
                    elif "/ti/g/" in msg.text.lower():
                          if settings["autoJoinTicket"] == True:
                              link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                              links = link_re.findall(text)
                              n_links = []
                              for l in links:
                                  if l not in n_links:
                                     n_links.append(l)
                              for ticket_id in n_links:
                                  group = cl.findGroupByTicket(ticket_id)
                                  cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                  cl.sendMessage(to, "Masuk : %s" % str(group.name))
                elif msg.contentType == 13:
                    if wait['invite'] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to, _name + " Berada Di Grup Ini")
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.sendMessage(msg.to,"Invite " + _name)
                                    wait['invite'] = False
                                    break
                                except:
                                    cl.sendMessage(msg.to,"Limit Invite")
                                    wait['invite'] = False
                                    break

                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = ""
                        ret_ += "STICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                        ret_ += ""
                        cl.sendMessage(to, str(ret_))

                elif msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        cl.updateProfilePicture(path)
                        cl.sendMessage(to, "mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = cl.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                cl.updateGroupPicture(to, path)
                                cl.sendMessage(to, "mengubah foto group")
                elif msg.contentType == 13:
                  if msg._from in admin:
                    if wait["addbots"] == True:
                        if msg.contentMetadata["mid"] in hun["botteam"]:
                            cl.sendMessage(msg.to, "• Managed to promote being the team bots")
                        else:
                            hun["botteam"][msg.contentMetadata["mid"]] = True
                            with open('hun.json', 'w') as fp:
                                json.dump(hun, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "• Managed to promote being the team bots")
                elif msg.contentType == 13:
                  if msg._from in admin:
                    if wait["delbots"] == True:
                        if msg.contentMetadata["mid"] in hun["botteam"]:
                            del hun["botteam"][msg.contentMetadata["mid"]]
                            with open('hun.json', 'w') as fp:
                                json.dump(hun, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to,"• Managed to expel team bots")
                        else:
                            cl.sendMessage(msg.to,"• Managed to expel team bots")
            if op.type == 26:
                print ("[ 26 ] RECEIVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in mid and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                           if clMID in mention["M"]:
                            if settings["detectMention"] == True:
                              sendMention(receiver, sender, "", " \nWoy Jgn ngetag semm kak ?? ")

                if msg.contentType == 0 and sender not in mid and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                           if admin in mention["M"]:
                             if settings["detectMentionadmin"] == True:
                                sendMention(receiver, sender, "", " \nJangan ngetag Creator ku kak\nDia gi sibuk!!!!!!")


#"╭━━━━┅═❉ই۝ई❉═┅━━━\n║╭Woy kak","", "\n║│Kesepian ya  🙋\n║╰❉ Jangan ngetag semm😁\n╰━━━━━━━━━━━━━━━━")

#"", " \nWoy kamu kesepian yak?? ")

            if op.type == 17:
                if settings["notifikasi"] == True:
                    if op.param2 in Bots:
                        return
                    ginfo = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                    cl.sendMessage(op.param1,"Halo... " + cl.getContact(op.param2).displayName + "\nSelamat datang di\n💎 " + str(ginfo.name) + " 💎" + "\n jangan lupa ngenot \n& Semoga betah ya😃")
                    cl.sendImageWithURL(op.param1,image)

            if op.type == 15:
                if settings["notifikasi"] == True:
                    if op.param2 in mid:
                        return
                    ginfo = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                    cl.sendImageWithURL(op.param1,image)
                    cl.sendMessage(op.param1,"Naah nahh.... " + cl.getContact(op.param2).displayName + "\nBaper tingkat tinggi😂")

        #if op.type == 55:
            #print ("[ 55 ] NOTIFIED READ MESSAGE")
            #try:
                #if cctv['cyduk'][op.param1]==True:
                    #if op.param1 in cctv['point']:
                        #Name = cl.getContact(op.param2).displayName
                        #if Name in cctv['sidermem'][op.param1]:
                            #pass
                        #else:
                            #cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                            #if " " in Name:
                                #nick = Name.split(' ')
                                #if len(nick) == 2:
                                    #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + nick[0] + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                    #time.sleep(0.2)
                                    #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                                #else:
                                    #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + nick[0] + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                    #time.sleep(0.2)
                                    #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                            #else:
                                #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + Name + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                #time.sleep(0.2)
                                #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                    #else:
                        #pass
                #else:
                    #pass
            #except:
                #pass
            if op.type == 55:
                print ("Sider")
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                siderMembers(op.param1, [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            if op.type == 55:
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                        backupData()
                    else:
                        pass
                except:
                    pass
        except: #Exception as error:
            pass #logError(error)

    def fetch(self):
        while True:
            try:
                self.operations = self.client.poll.fetchOperations(self.client.revision, 50)
                for op in self.operations:
                     if (op.type !=OpType.END_OF_OPERATION):
                         self.client.revision = max(self.client.revision, op.revision)
                         self.bot(op)
                         self.AutoSave(op)
            except:
                pass
