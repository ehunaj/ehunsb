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
cl = LINE("EMBsWALkcN5b9eFACvZ4.BvIR7Jw9VfAdsJzU/uMhba.0B0gmjifbNpXr64iuuaP3WfDuDcDMsGNI5JPgtUDJVc=")
ki = LINE("EMtrt7ARXnC3xEk8Ucq4.wOkmirNWe41AVCDdjgw/za.A1FVNahoA+6huK6SgkY1RPm0OME079ykEnVFZC5BPYg=")
kk = LINE("EMBf7j3JuEw9g1lNx0Qe.pYxjKbe7w+1iIyyJvihN7G.b8RYl5BL8w2UxuqYXKvOfbffVmXDArhXDRMi7YUwDZw=")
kc = LINE("EMeJYAVgrLiRHIkxibac.xmOZkKoDi9P/nYUM4NOsla.hwTymmBJr4fixtVoC8NVwIudzJ1DCufBWH8a6ddDp2Q=")
k1 = LINE("EMwUjryeKhXe5WiOI1Ud.PVmbdG5nG77Km5hrSxbgtq.2tACTY0iXYW3UZ+v58SZVe77FePSFzAT2fXlMJJVQ5g=")
k2 = LINE("EMrr6NeeIq0ZbJSKbfde.NzWU4uHxu25IbVF0crqixG.gOLUcTKx5UMefU2voyNpABjLHx8gHA6nhXjsa4fbmD8=")
k3 = LINE("EM5mVyaw71y6pJU6UPD9.p6BZ50ZbaAbHQXlkeO8fkq./7AOtEIfFViAp2AT6zTTKSghszjeZ15k4u32NAd20J8=")
#k4 = LINE("
#k5 = LINE("
#k6 = LINE("

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

mid = cl.profile.mid
cl.Profile = cl.getProfile()
cl.Settings = cl.getSettings()

Amid = ki.profile.mid
ki.Profile = ki.getProfile()
ki.Settings = ki.getSettings()

Bmid = kk.profile.mid
kk.Profile = kk.getProfile()
kk.Settings = kk.getSettings()

Cmid = kc.profile.mid
kc.Profile = kc.getProfile()
kc.Settings = kc.getSettings()

Dmid = k1.profile.mid
k1.Profile = k1.getProfile()
k1.Settings = k1.getSettings()

Emid = k2.profile.mid
k2.Profile = k2.getProfile()
k2.Settings = k2.getSettings()

Fmid = k3.profile.mid
k3.Profile = k3.getProfile()
k3.Settings = k3.getSettings()

#Gmid = k4.profile.mid
#k4.Profile = k4.getProfile()
#k4.Settings = k4.getSettings()

#Hmid = k5.profile.mid
#k5.Profile = k5.getProfile()
#k5.Settings = k5.getSettings()

#Imid = k6.profile.mid
#k6.Profile = k6.getProfile()
#k6.Settings = k6.getSettings()

oepoll = OEPoll(cl)
call = cl

ABC = [ki,kk,kc]

Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid] #,Gmid,Hmid,Imid]
admin = ["ub3808de9f7df35f57fb366d157f9790a"]

#cl.log("Auth Token : " + str(cl.authToken))

read = json.load(readOpen)
settings = json.load(settingsOpen)

wait = {
    "invite":{},
    "Bot":True,
    "mention":"║┝──────────────\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━n  ━━━━┅═❉ই۝ई❉═┅━━━━",
    "Respontag":"Hoi Jgn ngtag semm",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by Ehun",
    "message":"Terimakasih sudah add saya",
    "AutoJoinCancel":True,
    "memberscancel":30,
    "members":1,
    }
settings = {
    "changePicture":[],
    "autoAdd": False,
    "autoJoin": False,
    "autoJoinTicket":True,
    "autoLeave": False,
    "autoRead": False,
    "lang":"JP",
    "detectMention": True,
    "detectMentionadmin": True,
    "changeGroupPicture":[],
    "notifikasi": False,
    "Sider":{},
    "checkSticker": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
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

with open('bl.json', 'r') as fp:
    bl = json.load(fp)
#with open('admin.json', 'r') as fp:
 #   admin = json.load(fp)

myProfile["displayName"] = cl.Profile.displayName
myProfile["statusMessage"] = cl.Profile.statusMessage
myProfile["pictureStatus"] = cl.Profile.pictureStatus

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━━━┅═❉ই۝ई❉═┅━━━━\n║ Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    pass
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
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

def helpmessage():
    helpMessage = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    SELFBOT    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ MENU HELP ❇\n║┝───────────────" + "\n" + \
                  "║┝──[❇ STATUS ❇ ]" + "\n" + \
                  "║│ Restart" + "\n" + \
                  "║│ Runtime" + "\n" + \
                  "║│ Speed" + "\n" + \
                  "║│ Status" + "\n" + \
                  "║│ Bot(on/off" + "\n" + \
                  "║│ Dell「Removechat」" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ SETTING ❇ ]" + "\n" + \
                  "║│ Allstatus「On/Off」" + "\n" + \
                  "║│ Notif「On/Off」" + "\n" + \
                  "║│ Sider「On/Off」" + "\n" + \
                  "║│ AutoAdd「On/Off」" + "\n" + \
                  "║│ AutoJoin「On/Off」" + "\n" + \
                  "║│ AutoLeave「On/Off」" + "\n" + \
                  "║│ AutoRead「On/Off」" + "\n" + \
                  "║│ CheckSticker「On/Off」" + "\n" + \
                  "║│ DetectMention「On/Off」" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇  SELF  ❇]" + "\n" + \
                  "║│ Me" + "\n" + \
                  "║│ MyMid" + "\n" + \
                  "║│ MyName" + "\n" + \
                  "║│ MyBio" + "\n" + \
                  "║│ MyPicture" + "\n" + \
                  "║│ MyVideoProfile" + "\n" + \
                  "║│ MyCover" + "\n" + \
                  "║│ StealContact「@」" + "\n" + \
                  "║│ StealMid「@」" + "\n" + \
                  "║│ StealName「@」" + "\n" + \
                  "║│ StealBio「@」" + "\n" + \
                  "║│ StealPicture「@」" + "\n" + \
                  "║│ StealVideoProfile「@」" + "\n" + \
                  "║│ StealCover「@」" + "\n" + \
                  "║│ CloneProfile「@」" + "\n" + \
                  "║│ RestoreProfile" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ GROUP ❇ ]" + "\n" + \
                  "║│ GroupCreator" + "\n" + \
                  "║│ GroupId" + "\n" + \
                  "║│ GroupName" + "\n" + \
                  "║│ GroupPicture" + "\n" + \
                  "║│ GroupTicket" + "\n" + \
                  "║│ GroupTicket「On/Off」" + "\n" + \
                  "║│ GroupList" + "\n" + \
                  "║│ GroupMemberList" + "\n" + \
                  "║│ GroupInfo" + "\n" + \
                  "║│ Mimic「On/Off」" + "\n" + \
                  "║│ MimicList" + "\n" + \
                  "║│ MimicAdd「@」" + "\n" + \
                  "║│ MimicDel「@」" + "\n" + \
                  "║│ Tag" + "\n" + \
                  "║│ Lurking「On/Off/Reset」" + "\n" + \
                  "║│ Lurking" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ MEDIA ❇]" + "\n" + \
                  "║│ Kalender" + "\n" + \
                  "║│ CheckDate「Date」" + "\n" + \
                  "║┝───────────────\n║╰❉      EHUN BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
    return helpMessage

def clBot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 55:
            if op.param2 in bl["blacklist"]:
                try:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
  #              group_id = op.param1
   #             user_id = op.param2
    #            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
     #       except:
      #          pass
        if op.type == 17:
            if op.param2 in bl["blacklist"]:
                try:
                    k3.kickoutFromGroup(op.param1,[op.param2])
                    sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                except:
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        sendMention(op.param1, op.param2, "", " \nBlacklistDetected")
                                    except:
                                        pass

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in admin:
                    cl.acceptGroupInvitation(op.param1)

            if op.param3 in mid:
                if op.param2 in Amid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Bmid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Cmid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Dmid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Emid:
                    cl.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in Fmid:
                    cl.acceptGroupInvitation(op.param1)
#===========================================
            if op.param3 in Amid:
                if op.param2 in mid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Bmid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Cmid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Dmid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Emid:
                    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
                if op.param2 in Fmid:
                    ki.acceptGroupInvitation(op.param1)
#=====================------------------
            if op.param3 in Bmid:
                if op.param2 in mid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Amid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Dmid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Emid:
                    kk.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
                if op.param2 in Fmid:
                    kk.acceptGroupInvitation(op.param1)
#=====================------------------
            if op.param3 in Cmid:
                if op.param2 in mid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Amid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Emid:
                    kc.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
                if op.param2 in Fmid:
                    kc.acceptGroupInvitation(op.param1)
#=====================------------------
            if op.param3 in Dmid:
                if op.param2 in mid:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Amid:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Bmid:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    k1.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
                if op.param2 in Fmid:
                    k1.acceptGroupInvitation(op.param1)

            if op.param3 in Emid:
                if op.param2 in mid:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Amid:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Bmid:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Cmid:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    k2.acceptGroupInvitation(op.param1)
            if op.param3 in Emid:
                if op.param2 in Fmid:
                    k2.acceptGroupInvitation(op.param1)

            if op.param3 in Fmid:
                if op.param2 in mid:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Amid:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Bmid:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Cmid:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Dmid:
                    k3.acceptGroupInvitation(op.param1)
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    k3.acceptGroupInvitation(op.param1)
#=====================------------------
            if mid in op.param3:
                if wait["AutoJoinCancel"] == True:
                    G = cl.getGroup(op.param1)
                    if len (G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        sendMention(op.param1, op.param2, "","\nTrimaksih Kak Invit aku\nDiGroup" + str(G.name) + "\nMaaf Member Kurang Dari 30 Orang")
                        cl.sendContact(op.param1, 'ub3808de9f7df35f57fb366d157f9790a')
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        sendMention(op.param1, op.param2, "", " \nTrimaksih Kak Invit aku\nDiGroup" + str(G.name))
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                        k2.acceptGroupInvitationByTicket(op.param1,Ti)
                        k3.acceptGroupInvitationByTicket(op.param1,Ti)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)

            if mid in op.param3:
                if settings["autoJoin"] == True:
                    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        cl.rejectGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        sendMention(op.param1, op.param2, "", " \nTrimaksih Kak Invit aku\nDiGroup" + str(G.name))
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        k1.acceptGroupInvitationByTicket(op.param1,Ti)
                        k2.acceptGroupInvitationByTicket(op.param1,Ti)
                        k3.acceptGroupInvitationByTicket(op.param1,Ti)
                        G = k3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        k3.updateGroup(G)

            if Amid in op.param3:
                if settings["autoJoin"] == True:
                    G = ki.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        ki.rejectGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                ki.cancelGroupInvitation(op.param1,[tag])
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
            if Bmid in op.param3:
                if settings["autoJoin"] == True:
                    G = kk.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        kk.rejectGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                kk.cancelGroupInvitation(op.param1,[tag])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            if Cmid in op.param3:
                if settings["autoJoin"] == True:
                    G = kc.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        kc.rejectGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                kc.cancelGroupInvitation(op.param1,[tag])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
            if Dmid in op.param3:
                if settings["autoJoin"] == True:
                    G = k1.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        k1.rejectGroupInvitation(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                k1.cancelGroupInvitation(op.param1,[tag])
                                k1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
#================================---------
            if Emid in op.param3:
                if settings["autoJoin"] == True:
                    G = k2.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        k2.rejectGroupInvitation(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                k2.cancelGroupInvitation(op.param1,[tag])
                                k2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            if Fmid in op.param3:
                if settings["autoJoin"] == True:
                    G = k3.getGroup(op.param1)
                    if len(G.members) <= wait["members"]:
                        k3.rejectGroupInvitation(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    for tag in InviterX:
                        if tag in bl["blacklist"]:
                            try:
                                k3.cancelGroupInvitation(op.param1,[tag])
                                k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass


        if op.type == 13:
            if op.param3 in bl['blacklist']:
                try:
                    k3.cancelGroupInvitation(op.param1,[op.param3])
                    k3.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        k2.cancelGroupInvitation(op.param1,[op.param3])
                        k2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k1.cancelGroupInvitation(op.param1,[op.param3])
                            k1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kk.cancelGroupInvitation(op.param1,[op.param3])
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki.cancelGroupInvitation(op.param1,[op.param3])
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 32:
            if op.param3 in Bots:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        if op.param3 not in bl["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    pass
        if op.type == 32:
            if op.param3 in admin:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        if op.param3 not in bl["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in bl["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 not in bl["blacklist"]:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 not in bl["blacklist"]:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    pass

        if op.type == 19:
            if op.param3 in admin:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.pqram3])
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.parqm3])
                                except:
                                    try:
                                        k1.inviteIntoGroup(op.param1,[op.parqm3])
                                    except:
                                        try:
                                            k2.inviteIntoGroup(op.param1,[op.parqm3])
                                        except:
                                            try:
                                                k3.inviteIntoGroup(op.param1,[op.parqm3])
                                            except:
                                                pass

        if op.type == 19:
            if op.param3 in mid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = k1.getGroup(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                                Ti = k1.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                            except:
                                pass
        if op.type == 19:
            if op.param3 in Amid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.param2, "", " \nJangan main kick boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = k2.getGroup(op.param1)
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                k2.updateGroup(G)
                                Ti = k2.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                k2.updateGroup(G)
                            except:
                                pass

        if op.type == 19:
            if op.param3 in Bmid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.param2, "", " \nJangan main kick boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = k3.getGroup(op.param1)
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                k3.updateGroup(G)
                                Ti = k3.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                k3.updateGroup(G)
                            except:
                                pass

        if op.type == 19:
            if op.param3 in Cmid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.param2, "", " \nJangan main kick boss")
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = ki.getGroup(op.param1)
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                ki.updateGroup(G)
                                Ti = ki.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                            except:
                                pass
#==================-=-----=-=-------------
        if op.type == 19:
            if op.param3 in Dmid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.pa>
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                Ti = kk.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)
                            except:
                                pass

        if op.type == 19:
            if op.param3 in Emid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.pa>
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = kc.getGroup(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                kc.updateGroup(G)
                                Ti = kc.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                            except:
                                pass

        if op.type == 19:
            if op.param3 in Fmid:
                if op.param2 in admin:
                    pass
                if op.param2 in Bots:
                    pass
                else:
                    #sendMention(op.param1, op.pa>
                    bl['blacklist'][op.param2] = True
                    with open('bl.json', 'w') as fp:
                        json.dump(bl, fp, sort_keys=True, indent=4)
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGrouoInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGrouoInvitation(op.param1)
                        except:
                            try:
                                G = k1.getGroup(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                G.preventedJoinByTicket = False
                                k1.updateGroup(G)
                                Ti = k1.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                ki.acceptGroupInvitationByTicket(op.param1,Ti)
                                kk.acceptGroupInvitationByTicket(op.param1,Ti)
                                kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                k2.acceptGroupInvitationByTicket(op.param1,Ti)
                                k3.acceptGroupInvitationByTicket(op.param1,Ti)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)
                            except:
                                pass


        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                cl.sendMessage(msg.to,"Bot Sudah On Kembali")

        if op.type == 25 or op.type == 26:
          if wait["Bot"] == True:
            print ("[ 25 ] SEND MESSAGE")
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
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'bot on':
                  if msg._from in admin:
                      wait["Bot"] = True
                      cl.sendMessage(to,"Ok actip")
                elif text.lower() == 'bot off':
                  if msg._from in admin:
                      wait["Bot"] = False
                      cl.sendMessage(to,"Ok Non actip")
                elif text.lower() == 'invite':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      wait["invite"] = True
                      sendMention(receiver, sender, "", " \nKirim Contact nya")
                elif text.lower() == 'join':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      G = cl.getGroup(msg.to)
                      G.preventedJoinByTicket = False
                      cl.updateGroup(G)
                      Ti = cl.reissueGroupTicket(msg.to)
                      ki.acceptGroupInvitationByTicket(msg.to,Ti)
                      kk.acceptGroupInvitationByTicket(msg.to,Ti)
                      kc.acceptGroupInvitationByTicket(msg.to,Ti)
                      k1.acceptGroupInvitationByTicket(msg.to,Ti)
                      k2.acceptGroupInvitationByTicket(msg.to,Ti)
                      k3.acceptGroupInvitationByTicket(msg.to,Ti)
                      G.preventedJoinByTicket = True
                      cl.updateGroup(G)
                elif text.lower() == 'bot':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      G = cl.getGroup(msg.to)
                      lis = [Amid,Bmid,Cmid,Dmid,Emid,Fmid]
                      cl.inviteIntoGroup(msg.to,lis)
                      ki.acceptGroupInvitation(msg.to)
                      kk.acceptGroupInvitation(msg.to)
                      kc.acceptGroupInvitation(msg.to)
                      k1.acceptGroupInvitation(msg.to)
                      k2.acceptGroupInvitation(msg.to)
                      k3.acceptGroupInvitation(msg.to)

                elif text.lower() == 'kickerbye':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      k1.leaveGroup(msg.to)
                      k2.leaveGroup(msg.to)
                      k3.leaveGroup(msg.to)
                elif text.lower() == 'bye':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      ki.leaveGroup(msg.to)
                      kk.leaveGroup(msg.to)
                      kc.leaveGroup(msg.to)
                elif text.lower() == 'respon':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      ki.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 1\nHadir")
                      kk.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 2\nHadir")
                      kc.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 3\nHadir")
                      cl.sendMessage(msg.to,"b̶o̶tডা‮‮─┅═ই 4\nHadir")

                elif 'Sampah' in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(to,[_mid])
                elif text.lower() == "cek":
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        try:cl.inviteIntoGroup(to, [mid]);has = "OK"
                        except:has = "NOT"
                        try:cl.kickoutFromGroup(to, [mid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:ki.inviteIntoGroup(to, [Amid]);has = "OK"
                        except:has = "NOT"
                        try:ki.kickoutFromGroup(to, [Amid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:kk.inviteIntoGroup(to, [Bmid]);has = "OK"
                        except:has = "NOT"
                        try:kk.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:kc.inviteIntoGroup(to, [Cmid]);has = "OK"
                        except:has = "NOT"
                        try:kc.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:k1.inviteIntoGroup(to, [Dmid]);has = "OK"
                        except:has = "NOT"
                        try:k1.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        k1.sendMessage(to, "Status :\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:k2.inviteIntoGroup(to, [Dmid]);has = "OK"
                        except:has = "NOT"
                        try:k2.kickoutFromGroup(to, [Emid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        k2.sendMessage(to, "Status :\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                        try:k3.inviteIntoGroup(to, [Dmid]);has = "OK"
                        except:has = "NOT"
                        try:k3.kickoutFromGroup(to, [Fmid]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        k3.sendMessage(to, "Status :\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))

                elif "Leave" in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroupIdsJoined()
                      for i in gid:
                          cl.sendMessage(i,"Bot Di Paksa Keluar Oleh Owner!\nAyo left teman2\nAssalamualikum wr wb All Member|nAdd Owner kami")
                          ki.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                          kk.leaveGroup(i)
                          kc.leaveGroup(i)
                          k1.leaveGroup(i)
                          k2.leaveGroup(i)
                          k3.leaveGroup(i)
                          cl.leaveGroup(i)
                          cl.sendMessage(to,"Succes kluar group bos ku")

                elif ("Jemput " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          if target not in admin:
                              try:
                                  cl.inviteIntoGroup(msg.to,[target])
                                  cl.inviteIntoGroup(msg.to,[target])
                                  cl.sendMessage(to,"Success boss")
                              except:
                                  pass
                elif ("Ban " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          if target not in admin:
                              if target not in Bots:
                                  try:
                                      cl.sendMessage(to,"Success bannet boss")
                                      bl["blacklist"][target] = True
                                  except:
                                      pass


                elif ("Kick " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                elif ("Sikat " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          if target not in admin:
                              try:
                                  bl["blacklist"][target] = True
                                  klist = [ki,kk,kc,k1,k2,k3]
                                  orang = random.choice(klist)
                                  orang.kickoutFromGroup(to,[target])
                              except:
                                  pass

                elif text.lower() == 'banlist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if bl["blacklist"] == {}:
                          cl.sendMessage(to,"Tidak Ada")
                      else:
                          mcs = ""
                          for mi_d in bl["blacklist"]:
                               mcs += "->" +cl.getContact(mi_d).displayName + "\n"
                          cl.sendMessage(to,"===[Blacklist User]===\n"+ mcs)
                elif text.lower() == 'clear':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        bl["blacklist"] = {}
                        cl.sendMessage(to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")
                elif text.lower() == 'dell':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      cl.removeAllMessages(op.param2)
                      ki.removeAllMessages(op.param2)
                      kk.removeAllMessages(op.param2)
                      kc.removeAllMessages(op.param2)
                      k1.removeAllMessages(op.param2)
                      k2.removeAllMessages(op.param2)
                      k3.removeAllMessages(op.param2)
                      cl.sendMessage(to, "Menghapus Chat")
                elif text.lower() == 'speed':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      start = time.time()
                      elapsed_time = time.time() - start
                      cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      cl.sendMessage(to, "Sudah di restart...")
                      restartBot()
                elif text.lower() == 'runtime':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      timeNow = time.time()
                      runtime = timeNow - botStart
                      runtime = format_timespan(runtime)
                      cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
                elif text.lower() == 'status':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      try:
                          ret_ = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    STATUS    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ 🔵[ON]|[OFF]🔴 ❇\n║┝───────────────"
                          if settings["autoAdd"] == True: ret_ += "\n║│🔵 Auto Add [ON]"
                          else: ret_ += "\n║│🔴 Auto Add [OFF]"
                          if settings["autoJoin"] == True: ret_ += "\n║│🔵 Auto Join [ON]"
                          else: ret_ += "\n║│🔴 Auto Join [OFF]"
                          if settings["autoLeave"] == True: ret_ += "\n║│🔵 Auto Leave [ON]"
                          else: ret_ += "\n║│🔴 Auto Leave [OFF]"
                          if settings["autoRead"] == True: ret_ += "\n║│🔵 Auto Read [ON]"
                          else: ret_ += "\n║│🔴 Auto Read [OFF]"
                          if settings["notifikasi"] == True: ret_ += "\n║│🔵 Notif [ON]"
                          else: ret_ += "\n║│🔴 Notif [OFF]"
                          if settings["detectMention"] == True: ret_ += "\n║│🔵 Detect Mention [ON]"
                          else: ret_ += "\n║│🔴 Detect Mention [OFF]"
                          ret_ += "\n║┝───────────────\n║╰❉      EHUN  BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
                          cl.sendMessage(to, str(ret_))
                      except Exception as e:
                          cl.sendMessage(to, str(e))
                elif text.lower() == 'autoadd on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoAdd"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoAdd"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Add")

                elif text.lower() == 'jc on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      wait["AutoJoinCancel"] = True
                      settings["autoJoin"] = False
                      cl.sendMessage(to, "Mengaktifkan Auto JoinCancel")
                elif text.lower() == 'jc off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoJoin"] = True
                      wait["AutoJoinCancel"] = False
                      cl.sendMessage(to, "Menonaktifkan Auto JoinCancel")
                elif text.lower() == 'l on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoLeave"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Leave")
                elif text.lower() == 'l off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoLeave"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoRead"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoRead"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["checkSticker"] = True
                      cl.sendMessage(to, "mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["checkSticker"] = False
                      cl.sendMessage(to, "menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["datectMention"] = True
                      cl.sendMessage(to, "mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["datectMention"] = False
                      cl.sendMessage(to, "menonaktifkan Detect Mention")

                elif text.lower() == 'allstatus on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["notifikasi"] = True
                      settings["autoAdd"] = True
                      settings["autoJoin"] = True
                      settings["autoLeave"] = True
                      settings["autoRead"] = True
                      settings["datectMention"] = True
                      cl.sendMessage(to, "Allstatus bot mode on")

                elif text.lower() == 'allstatus off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["notifikasi"] = False
                      settings["autoAdd"] = False
                      settings["autoJoin"] = False
                      settings["autoLeave"] = False
                      settings["autoRead"] = False
                      settings["datectMention"] = False
                      cl.sendMessage(to, "Allstatus bot mode on")

                elif text.lower() == 'me':
                      sendMessageWithMention(to, msg._from) #clMID)
                      cl.sendContact(to, msg._from) #clMID)
                elif text.lower() == 'mymid':
                      sendMention(to, msg._from, "", " Ini Mid Mu kak\n=======================\n\n" +  msg._from)

                elif text.lower() == 'myname':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(mid)
                      cl.sendMessage(to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(mid)
                      cl.sendMessage(to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(mid)
                      cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideo':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(mid)
                      cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(mid)
                      cover = cl.getProfileCoverURL(mid)
                      cl.sendImageWithURL(to, cover)
                elif "Contact " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                elif "Midsi " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid nya ]"
                        for ls in lists:
                            ret_ += "\n==================\n" + ls
                        sendMention(to, mention["M"], "", str(ret_))
                elif "Name " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                            cl.sendMessage(to, "[ Display Name ]\n" + contact.displayName)
                elif "Bio " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                            cl.sendMessage(to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif "Picture " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                            cl.sendImageWithURL(to, str(path))
                elif "Vidio " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                            cl.sendImageWithURL(to, str(path))
                elif "Cover " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                                cl.sendImageWithURL(to, str(path))

                elif text.lower() == "cloneprofile ":
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.cloneContactProfile(contact)
                            cl.sendMessage(to, "clone member ")
                        except:
                            cl.sendMessage(to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      try:
                          cl.Profile.displayName = str(myProfile["displayName"])
                          cl.Profile.statusMessage = str(myProfile["statusMessage"])
                          cl.Profile.pictureStatus = str(myProfile["pictureStatus"])
                          cl.updateProfileAttribute(8, cl.Profile.pictureStatus)
                          cl.updateProfile(cl.Profile)
                          cl.sendMessage(to, "restore profile ")
                      except:
                          cl.sendMessage(to, "Gagal restore profile")
                elif "Mid @" in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      _name = msg.text.replace("Mid @","")
                      _nametarget = _name.rstrip(' ')
                      gs = cl.getGroup(msg.to)
                      for g in gs.members:
                          if _nametarget == g.displayName:
                              sendMention(to, msg._from, "", " IniMid Mu kak\n=======================\n\n" +  g.mid)
                          else:
                              pass

                elif ("Micadd " in text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              settings["mimic"]["target"][target] = True
                              cl.sendMessage(to,"Target ditambahkan!")
                              break
                          except:
                              cl.sendMessage(to,"Added Target Fail !")
                              break
                elif ("Micdel " in text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              del settings["mimic"]["target"][target]
                              cl.sendMessage(to,"Target dihapuskan!")
                              break
                          except:
                              cl.sendMessage(to,"Deleted Target Fail !")
                              break
                elif text.lower() == 'mimiclist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["mimic"]["target"] == {}:
                          cl.sendMessage(to,"Tidak Ada Target")
                      else:
                          mc = "╔══[ Mimic List ]"
                          for mi_d in settings["mimic"]["target"]:
                              mc += "\n╠ "+cl.getContact(mi_d).displayName
                          cl.sendMessage(to,mc + "\n╚══[ Finish ]")

                elif "Mimic " in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      mic = msg.text.replace("Mimic ","")
                      if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            cl.sendMessage(to,"Reply Message on")
                      elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            cl.sendMessage(to,"Reply Message off")

                elif text.lower() == 'groupcreator':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      group = cl.getGroup(to)
                      GS = group.creator.mid
                      cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroup(to)
                      cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      group = cl.getGroup(to)
                      path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                      cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroup(to)
                      cl.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            cl.sendMessage(to, "membuka grup qr")
                elif text.lower() == 'groupticket off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                            cl.sendMessage(to, "menutup grup qr")
                elif text.lower() == 'ginfo':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                elif text.lower() == 'memlist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'glist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        groups = cl.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'sambutan on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["notifikasi"] == True:
                        if settings["lang"] == "JP":
                            cl.sendMessage(to,"notif mode on")
                        else:
                            settings["notifikasi"] = True
                            if settings["lang"] == "JP":
                                cl.sendMessage(to,"notif mode on")

                elif text.lower() == 'sambutan off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["notifikasi"] == False:
                        if settings["lang"] == "JP":
                          cl.sendMessage(to,"notif mode off")
                      else:
                          settings["notifikasi"] = False
                          if settings["lang"] == "JP":
                              cl.sendMessage(to,"notif mode off")
                elif text.lower() == 'tag':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                                cl.sendMention(to, ret_, dataMid)
                elif text.lower() == 'changepictureprofile':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        settings["changePicture"] = True
                        cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'changegrouppicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                            cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'lurking on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                              cl.sendMessage(to,"Lurking already on")
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
                              cl.sendMessage(to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                          cl.sendMessage(to,"Lurking already off")
                      else:
                          try:
                              del read['readPoint'][msg.to]
                              del read['readMember'][msg.to]
                              del read['readTime'][msg.to]
                          except:
                              pass
                          cl.sendMessage(to, "Delete reading point:\n" + readTime)

                elif text.lower() == 'lurking reset':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                          cl.sendMessage(to, "Reset reading point:\n" + readTime)
                      else:
                          cl.sendMessage(to, "Lurking belum diaktifkan ngapain di reset?")

                elif text.lower() == 'lurking':
                  if msg._from in admin:
                    if wait["Bot"] == True:
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
                    if wait["Bot"] == True:
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
                      cl.sendMessage(to,"SIDER SUDAH ON")

                elif text.lower() == 'sider off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.to in cctv['point']:
                          cctv['cyduk'][msg.to]=False
                          settings["Sider"] = False
                          cl.sendMessage(to,"SIDER SUDAH OFF")
                      else:
                          cl.sendMessage(to,"SIDER SUDAH OFF")

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
                    if wait["Bot"] == True:
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
                              group1 = ki.findGroupByTicket(ticket_id)
                              ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                              ki.sendMessage(to, "Masuk : %s" % str(group1.name))
                              group2 = kk.findGroupByTicket(ticket_id)
                              kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                              kk.sendMessage(to, "Masuk : %s" % str(group2.name))
                              group3 = kc.findGroupByTicket(ticket_id)
                              kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                              kc.sendMessage(to, "Masuk : %s" % str(group3.name))
                              group4 = k1.findGroupByTicket(ticket_id)
                              k1.acceptGroupInvitationByTicket(group4.id,ticket_id)
                              k1.sendMessage(to, "Masuk : %s" % str(group4.name))
                              group5 = k2.findGroupByTicket(ticket_id)
                              k2.acceptGroupInvitationByTicket(group5.id,ticket_id)
                              k2.sendMessage(to, "Masuk : %s" % str(group4.name))
                              group6 = k3.findGroupByTicket(ticket_id)
                              k3.acceptGroupInvitationByTicket(group6.id,ticket_id)
                              k3.sendMessage(to, "Masuk : %s" % str(group6.name))

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
                if wait['invite'] == True:
                    _name =msg.contentMetadata["displayName"]
                    invite =msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    groups = ki.getGroup(msg.to)
                    groups = kk.getGroup(msg.to)
                    groups = kc.getGroup(msg.to)
                    groups = k1.getGroup(msg.to)
                    groups = k2.getGroup(msg.to)
                    groups = k3.getGroup(msg.to)
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
                                ki.findAndAddContactsByMid(target)
                                ki.inviteIntoGroup(msg.to,[target])
                                kk.findAndAddContactsByMid(target)
                                kk.inviteIntoGroup(msg.to,[target])
                                kc.findAndAddContactsByMid(target)
                                kc.inviteIntoGroup(msg.to,[target])
                                k1.findAndAddContactsByMid(target)
                                k1.inviteIntoGroup(msg.to,[target])
                                k2.findAndAddContactsByMid(target)
                                k2.inviteIntoGroup(msg.to,[target])
                                k3.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                cl.sendMessage(msg.to,"Invite " + _name)
                                wait['invite'] = False
                                break
                            except:
                                cl.sendMessage(msg.to,"Limit Invite")
                                wait['invite'] = False
                                break





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
                if msg.contentType == 0 and sender not in Bots and sender not in admin and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mid in mention["M"]:
                                if settings["detectMention"] == True:
                                    sendMention(receiver, sender, "", " \nWoy Jgn ngetag semm kak ?? ")

                if msg.contentType == 0 and sender not in Bots and sender not in admin and msg.toType == 2:
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
            print ("MEMBER JOIN TO GROUP")
            if settings["notifikasi"] == True:
                if op.param2 in Bots:
                    return
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                cl.sendMessage(op.param1,"Halo... " + cl.getContact(op.param2).displayName + "\nSelamat datang di\n💎 " + str(ginfo.name) + " 💎" + "\n jangan lupa ngenot \n& Semoga betah ya😃")
                cl.sendImageWithURL(op.param1,image)

        if op.type == 15:
            print ("MEMBER LEAVE TO GROUP")
            if settings["notifikasi"] == True:
                if op.param2 in Bots:
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
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(op.param1, image)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
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
    except Exception as error:
        logError(error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
