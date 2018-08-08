# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from urlparse import urlparse
from bs4 import BeautifulSoup
import time,timeit, random, sys, ast, re, os, json, subprocess, multiprocessing, threading, string, codecs
import requests, tweepy, ctypes, urllib2, urllib, tempfile, calendar, glob, shutil, unicodedata, urllib3, bs4
import html5lib
from urllib import urlopen
import wikipedia
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE() #Masukin Token Lu
cl.login(token="Evtr6obyOHc2lMVeUuf0.wPAtTDMMvev1GuCiOkg60a.RdnYFqswyyWdmpKrQ9yik58tlmapa/uwJeoM+bDbJao=")
cl.loginResult()

print "بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═══════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ ★‡SELFBOT MENU‡★
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔══════════════
║╠[★]Menu Self
║╠[★]Menu Group
║╠[★]Menu Proteksi
║╚══════════════
║Bot Type : SelfBot Free
║Jumlah Assist : 0 Assist
║Bot Version : 3.5
║System : Python 2
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║     ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║𖤓Special Thanks For𖤓
║- Allah Swt
║- PSD Team
║- TCR Team
║𖤓Support By𖤓
║♥SMULE VOICE FAMILY
║♥MARS FAMILY
╚═══════════════"""

MProteksi ="""╔══════════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║    ✰Menu Proteksi✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔═════════════════
║╠[✰]Status
║╠[✰]Protect kick on/off
║╠[✰]Protect qr on/off
║╠[✰]Protect invite on/off
║╠[✰]Protect cancel on/off
║╠[✰]Protect join on/off
║╠[✰]Namelock on/off
║╚═════════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║     ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚══════════════════"""

MGroup ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ ✰Menu On Group✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔════════════
║╠[✰]Welcome
║╠[✰]Bot?
║╠[✰]Cctv→Ciduk
║╠[✰]Sider on/off
║╠[✰]Apakah <Tanya>
║╠[✰]Kapan <Tanya>
║╠[✰]Respon
║╠[✰]Creator
║╠[✰]Tag
║╠[✰]Gn <Nama Group>
║╠[✰]Teamlist
║╠[✰]Mid @Tag
║╠[✰]Member
║╠[✰]Info group
║╠[✰]Buka/Tutup qr
║╠[✰]Link group
║╠[✰]Sider on/off
║╠[✰]Kalender
║╠[✰]Profile @Tag
║╚════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║    ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═════════════"""

MSelf ="""╔════════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║       ✰Menu Self✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔═══════════════
║╠[✰]Tag
║╠[✰]Me
║╠[✰]My mid
║╠[✰]Mid bot
║╠[✰]Team add @tag
║╠[✰]Team remove @tag
║╠[✰]Teamlist
║╠[✰]Mid @Tag
║╠[✰]Speed
║╠[✰]Ban
║╠[✰]Ban @
║╠[✰]Unban
║╠[✰]Unban @
║╠[✰]Clear ban
║╠[✰]Banlist
║╠[✰]Creator
║╠[✰]runtime
║╠[✰]Member
║╠[✰]block @
║╠[✰]blocklist
║╠[✰]Info group
║╠[✰]List group
║╠[✰]Steal group
║╠[✰]Buka/Tutup qr
║╠[✰]Link group
║╠[✰]Copy @
║╠[✰]Backup
║╠[✰]Remove all chat
║╚═══════════════
║→Perintah Hiburan←
╠[✰]Cctv→Ciduk
╠[✰]Sider on/off
╠[✰]Mimic on/off
╠[✰]Mimic add @tag
╠[✰]Mimic del @tag
╠[✰]Gambar
╠[✰]Youtube: <Judul>
╠[✰]Instagram
╠[✰]Profileig
╠[✰]Say <Terserah>
╠[✰]Kalender
╠[✰]Kedip: <Text>
╠[✰]Translate-id
╠[✰]Translate-en
║→Tambahan←
╠[✰]Respontag on/off
╠[✰]Sticker on/off
╠[✰]Contact on/off
╠[✰]Sambutan on/off
╠[✰]Check sambutan
╠[✰]Update sambutan:
╠[✰]My pp
╠[✰]My cover
╠════════════════
║Ingin Fitur Lengkapnya?
║Kalo Minat Hubungin Ane
║LINE => @hanavy1992
║Tersedia Juga :
║- Bot Protect Group
║- Selfbot + Assist
║- VPS Full Speed
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║        ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚════════════════"""
#========[Promosi Dulu Coy]=============
HargaAdmin = """╔═══════𖤓Ready𖤓════════
║𖤓Bot Protect Group𖤓
║→Indonesia←
╠[★]Registrasi 250K
╠[★]Bulan Selanjutnya 150K/Bulan
║
║→Out Of Indonesia←
╠[★]Registration 30$ USD
╠[★]The Next Month 20$ USD
║
║Total Bots → 10 Bots + 1 Backup
║1 Group → 1 Admin & 2 Staff
║
║Via :
╠[★]Bank BCA (Bank Central Asia)
╠[★]Pulsa Tri Atau Telkomsel
╠[★]Western Union
║
║Minat??? PC Line Id @hanavy1992
║http://line.me/ti/p/~hanavy1992
║════════════════════
║____[★]૦Ո૯ ƿɿ૯८૯ ੮૯คɱ[★]____
╚════════════════════"""

HargaOwner = """╔═══════𖤓Ready𖤓════════
║𖤓Become Owner Of BOTS𖤓
╠[★]You Can Full Access To Control The BOTS
╠[★]Bot With Your Name
╠[★]Adding Admin & Staff
╠[★]Protect & Cleanse Other Group
╠[★]Whatever you want for bots.
║Total Bots → 10 Bot Protect
║
║Price : 
║Rp.500.000/Bulan (Indonesia)
║50$ USD/Month (Out Of Indonesia)
║
║Via :
╠[★]Bank BCA (Bank Central Asia)
╠[★]Pulsa Tri Atau Telkomsel
╠[★]Western Union
║
║Minat??? PC Line Id @hanavy1992
║http://line.me/ti/p/~hanavy1992
╠════════════════════
║____[★]૦Ո૯ ƿɿ૯८૯ ੮૯คɱ[★]____
╚════════════════════"""

HargaSelf = """╔═══════𖤓Ready𖤓════════
║𖤓Price SelfBot𖤓
║→Indonesia←
║Selfbot Tanpa Assist → 100K/Bulan
║1 Selfbot 1 Bot Assist → 150K/Bulan
║1 Selfbot 2 Bot Assist → 170K/Bulan
║1 Selfbot 3 Bot Assist → 190K/Bulan
║1 Selfbot 4 Bot Assist → 200K/Bulan
║1 Selfbot 5 Bot Assist → 220K/Bulan
║1 Selfbot 6 Bot Assist → 240K/Bulan
║1 Selfbot 7 Bot Assist → 260K/Bulan
║1 Selfbot 8 Bot Assist → 280K/Bulan
║1 Selfbot 9 Bot Assist → 290K/Bulan
║1 Selfbot 10 Bot Assist → 300K/Bulan
║
║→Out Of Indonesia←
║Selfbot Without Assist → 5$ USD/Month
║1 Selfbot 1 Bot Assist → 10$ USD/Month
║1 Selfbot 2 Bot Assist → 15$ USD/Month
║1 Selfbot 3 Bot Assist → 20$ USD/Month
║1 Selfbot 4 Bot Assist → 25$ USD/Month
║1 Selfbot 5 Bot Assist → 30$ USD/Month
║1 Selfbot 6 Bot Assist → 35$ USD/Month
║1 Selfbot 7 Bot Assist → 40$ USD/Month
║1 Selfbot 8 Bot Assist → 45$ USD/Month
║1 Selfbot 9 Bot Assist → 50$ USD/Month
║1 Selfbot 10 Bot Assist → 55$ USD/Month
║
║Payment Via :
╠[★]Bank BCA (Bank Central Asia)
╠[★]Western Union
╠[★]Pulsa Tri Atau Telkomsel
║
║It can be a test first.
║Interest??? PC Line Id @hanavy1992
║http://line.me/ti/p/~hanavy1992
╠════════════════════
║____[★]૦Ո૯ ƿɿ૯८૯ ੮૯คɱ[★]____
╚════════════════════"""

HargaVPS = """╔════════𖤓Ready𖤓═════════
║𖤓Price VPS LINUX𖤓
║𖤓NO ROOT𖤓
╠[★] 2 Core 16GB Ram 100k/Bulan
║𖤓FULL ROOT𖤓
╠[★]1 Core 1GB RAM 200k/Bulan
╠[★]1 Core 2GB RAM 300k/Bulan
╠[★]1 Core 3GB RAM 500k/Bulan
╠═══════════════════════
║Speed Py2 : 0.07
║Speed py3 : 0.02
╠═══════════════════════
║Pembayaran Via :
╠[★]Bank BCA (Bank Central Asia)
║
║IP Kebanned Diganti Yang Baru
╚═══════════════════════"""

TutorPy2 = """╔═══════𖤓Python2𖤓════════
║𖤓Bahan Yang Harus Di Install𖤓
╠[★]apt install python-pip
╠[★]pip install thrift==0.9.3
╠[★]pip install rsa
╠[★]pip install requests
╠[★]pip install gtts
╠[★]pip install wikipedia
╠[★]pip install google
╠[★]pip install googletrans
╠[★]pip install html5lih
╠[★]pip install datetime
╚═════════════════════"""

TutorPy3 = """╔═══════𖤓Python3𖤓════════
║𖤓Bahan Yang Harus Di Install𖤓
╠[★]apt install python3-pip
╠[★]pip3 install thrift==0.10.0
╠[★]pip3 install rsa
╠[★]pip3 install requests
╠[★]pip3 install gtts
╠[★]pip3 install wikipedia
╠[★]pip3 install google
╠[★]pip3 install googletrans
╠[★]pip3 install html5lih
╠[★]pip3 install datetime
╠[★]pip3 install linepy
╚═════════════════════"""

KAC=[cl]
midCL = cl.getProfile().mid

Bots=[midCL,"u5a9693b5d9a6544575814708a0a1bad0","u804b2f467610a226326479f7041d7969"]
owner=["u5a9693b5d9a6544575814708a0a1bad0","u804b2f467610a226326479f7041d7969"]
admin=["u5a9693b5d9a6544575814708a0a1bad0","u804b2f467610a226326479f7041d7969"]
staff=["u5a9693b5d9a6544575814708a0a1bad0","u804b2f467610a226326479f7041d7969"]

wait = {
    'contact':False,
    'contactDetail':False,
    'autoJoin':True,
    'autoCancel':{"off":False, "members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ ONE PIECE BOT PROTECT ≪

Ready:

≫ Bot Protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ ☆
☆ SMULE VOICE FAMILY ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~the.special_one""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "spam":{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "tambahStaff":False,
    "hapusStaff":False,
    "clock":False,
    "AutoLep":False,
    "blacklist":{},
    'pap':{},
    'changePicture':False,
    'likeOn':{},
    'Leave':{},    
    "Sider":{},
    "BlGroup":{},
    "commentLike":"""{AUTO LIKE BY}
         https://line.me/R/ti/p/%40xsj5951j
   ☆★☆★☆★☆★☆★☆★☆
        http://line.me/ti/p/~the.special_one

 ❂•••••••COSTUMER•••••••❂
         http://line.me/ti/p/~sandy_erenjaeger
""",
    "wblacklist":False,
    "dblacklist":False,
    "detectMention":False,
    "pmMention":False,
    "sticker":{},
    "Sambutan":False,
    #"PesanSambutan":"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ " + cl.getContact(op.param2).displayName + "\n╔═════════════\n║Hᴀɪ Sᴀʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ   " + str(ginfo.name) + "\n╠═════════════\n" + "║Fᴏᴜɴᴅᴇʀ ɢʀᴏᴜᴘ =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Sᴇᴍᴏɢᴀ Bᴇᴛᴀʜ ʏᴀ 😘 \n╚═════════════",
    "pname":{},
    "pro_name":{},
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":False,
    "Protectcancel":True,
    "Protectkick":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

mimic = {
    "status":False,
    "target":{},
    }

settings = {
    "simiSimi":{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()
  
contact = cl.getProfile() 
backup = cl.getProfile() 
backup.displayName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error            


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
  
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def mention(self, to, nama):
        aa = ""
        bb = ""
        strt = int(0)
        akh = int(0)
        nm = nama
        myid = self.talk.getProfile().mid
        if myid in nm:    
            nm.remove(myid)
        for mm in nm:
          akh = akh + 6
          aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
          strt = strt + 7
          akh = akh + 1
          bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
        try:
            msg = Message()
            msg.to = to
            msg.text = text
            msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}'}
            msg.contentType = 0
            self.talk.sendMessage(0, msg)
        except Exception as error:
           print(error, 'def Mention')
           
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error
        
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "Juan Pradana"   
         s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        
        if op.type == 13:
          if midCL in op.param3:
            if wait["autoJoin"] == True:
              cl.acceptGroupInvitation(op.param1)
            else:
              cl.acceptGroupInvitation(op.param1)
              cl.sendText(op.param1,"AutoJoin Off\Otomatis Leave!!!\n\nBye!!!")
              cl.leaveGroup(op.param1)
          else:
            pass
                
        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)
            
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in staff:
                pass
              else:
                try:
                  cl.cancelGroupInvitation(op.param1,gMembMids)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  wait["blacklist"][op.param2] = True
                except:
                  cl.cancelGroupInvitation(op.param1,gMembMids)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  
          if op.type == 13: #Jika Blacklist Di Invite
            if wait["Protectcancl"] == True:
              if wait["blacklist"][op.param3] == True:
                cl.sendText(op.param1,cl.getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
                random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
              
        if op.type == 17: #Jika Blacklist Join Group
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              cl.sendText(op.param1,cl.getContact(op.param2).displayName + " On Blacklist Boss\nWe Will Kick")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
              pass
          else:
            pass
            
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in staff:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Ngapain buka link goblok")
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.updateGroup(G)
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                except:
                  G.preventJoinByTicket = True
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        pass
                                                      
                    if op.param2 in Bots:
                      pass
                    elif op.param2 in admin:
                      pass
                    elif op.param2 in staff:
                      pass
                    else:
                        try:
                          cl.sendText(op.param1,"Group name lock")
                          cl.sendText(op.param1,"Haddeuh dikunci Pe'a")
                          cl.sendText(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                          c = Message(to=op.param1, from_=None, text=None, contentType=13)
                          c.contentMetadata={'mid':op.param2}
                          cl.sendMessage(c)
                          cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                            
        if op.type == 19: #Member Ke Kick
          if wait["Protectkick"] == True:
            if op.param2 in Bots:
              pass
            elif op.param2 in owner:
              pass
            elif op.param2 in admin:
              pass
            elif op.param2 in staff:
              pass
            else:
              try:
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " Gausah main kick²an kontol")
                cl.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
              except:
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 in Bots:
              pass
            elif op.param2 in admin:
              pass
            elif op.param2 in staff:
              pass
            else:
              try:
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " Canceled Invitation")
                cl.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
              except:
                pass
                
        #if op.type == 25:
        #  msg = op.message
        #  if msg.contentType == 1:
        #    if wait["changePicture"] == True:
        #      path = cl.upload_tempimage(msg_id)
        #      wait["changePicture"] = False
        #      cl.updateProfilePicture(path)
        #      cl.sendText(msg.to, "PP diganti")
            
                
        if op.type == 25:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[SimiSimi] " + "\n" + data['result']['response'].encode('utf-8'))
                                
        if op.type == 25:
          msg = op.message
          if msg.contentType == 16:
            if wait['likeOn'] == True:
              url = msg.contentMetadata["postEndUrl"]
              cl.like(url[25:58], url[66:], likeType=1005)
              #k1.like(url[25:58], url[66:], likeType=1002)
              #k2.like(url[25:58], url[66:], likeType=1004)
              #k3.like(url[25:58], url[66:], likeType=1003)
              #k4.like(url[25:58], url[66:], likeType=1001)
              #k5.like(url[25:58], url[66:], likeType=1001)
              #k6.like(url[25:58], url[66:], likeType=1002)
              #k7.like(url[25:58], url[66:], likeType=1004)
              #k8.like(url[25:58], url[66:], likeType=1003)
              #k9.like(url[25:58], url[66:], likeType=1001)
              #k10.like(url[25:58], url[66:], likeType=1001)
              cl.comment(url[25:58], url[66:], wait["commentLike"])
              #k1.comment(url[25:58], url[66:], wait["commentLike"])
              #k2.comment(url[25:58], url[66:], wait["commentLike"])
              #k3.comment(url[25:58], url[66:], wait["commentLike"])
              #k4.comment(url[25:58], url[66:], wait["commentLike"])
              #k5.comment(url[25:58], url[66:], wait["commentLike"])
              #k6.comment(url[25:58], url[66:], wait["commentLike"])
              #k7.comment(url[25:58], url[66:], wait["commentLike"])
              #k8.comment(url[25:58], url[66:], wait["commentLike"])
              #k9.comment(url[25:58], url[66:], wait["commentLike"])
              #k10.comment(url[25:58], url[66:], wait["commentLike"])
              cl.sendText(msg.to,"Like Success")                     
              wait['likeOn'] = True
              
        if op.type == 25:
          msg = op.message
          if msg.contentType == 16:
            if wait['likeOn'] == True:
              url = msg.contentMetadata["postEndUrl"]
              cl.like(url[25:58], url[66:], likeType=1005)
              #k1.like(url[25:58], url[66:], likeType=1002)
              #k2.like(url[25:58], url[66:], likeType=1004)
              #k3.like(url[25:58], url[66:], likeType=1003)
              #k4.like(url[25:58], url[66:], likeType=1001)
              #k5.like(url[25:58], url[66:], likeType=1001)
              #k6.like(url[25:58], url[66:], likeType=1002)
              #k7.like(url[25:58], url[66:], likeType=1004)
              #k8.like(url[25:58], url[66:], likeType=1003)
              #k9.like(url[25:58], url[66:], likeType=1001)
              #k10.like(url[25:58], url[66:], likeType=1001)
              cl.comment(url[25:58], url[66:], wait["commentLike"])
              #k1.comment(url[25:58], url[66:], wait["commentLike"])
              #k2.comment(url[25:58], url[66:], wait["commentLike"])
              #k3.comment(url[25:58], url[66:], wait["commentLike"])
              #k4.comment(url[25:58], url[66:], wait["commentLike"])
              #k5.comment(url[25:58], url[66:], wait["commentLike"])
              #k6.comment(url[25:58], url[66:], wait["commentLike"])
              #k7.comment(url[25:58], url[66:], wait["commentLike"])
              #k8.comment(url[25:58], url[66:], wait["commentLike"])
              #k9.comment(url[25:58], url[66:], wait["commentLike"])
              #k10.comment(url[25:58], url[66:], wait["commentLike"])
              cl.sendText(msg.to,"Like Success")                     
              wait['likeOn'] = True
                                           
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            #print(
            #" TO: {}\n".format(msg.to),
            #"FROM: {}\n".format(msg.from_),
            #"TEXT: {}\n".format(msg.text),
            #"CONTENT TYPE: {}\n".format(msg.contentType),
            #"METADATA: {}\n".format(msg.contentMetadata),
            #"TYPE: {}\n".format(msg.toType),
            #"MESSAGE ID: {}\n".format(msg.id),
            #"DATE: {}\n\n".format(msg.createdTime)
            #)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "☸ Sticker Check ☸\n\n☑ STKID : %s\n☑ STKPKGID : %s\n☑ STKVER : %s\n☸ Link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass
        
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
              if wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  cl.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  cl.sendText(msg.to,"decided not to comment")
                  
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  #ki.sendText(msg.to,"deleted")
                  #kk.sendText(msg.to,"deleted")
                  #kc.sendText(msg.to,"deleted")
                  wait["dblack"] = False

                else:
                  wait["dblack"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  #ki.sendText(msg.to,"It is not in the black list")
                  #kk.sendText(msg.to,"It is not in the black list")
                  #kc.sendText(msg.to,"It is not in the black list")
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  cl.sendText(msg.to,"already")
                  #ki.sendText(msg.to,"already")
                  #kk.sendText(msg.to,"already")
                  #kc.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  cl.sendText(msg.to,"aded")
                #ki.sendText(msg.to,"aded")
                  #kk.sendText(msg.to,"aded")
                  #kc.sendText(msg.to,"aded")

              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  #ki.sendText(msg.to,"deleted")
                  #kk.sendText(msg.to,"deleted")
                  #kc.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False

                else:
                  wait["dblacklist"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  #ki.sendText(msg.to,"It is not in the black list")
                  #kk.sendText(msg.to,"It is not in the black list")
                  #kc.sendText(msg.to,"It is not in the black list")
              elif wait["contact"] == True:
                msg.contentType = 0
                cl.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    pass
                else:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    pass
                    
              elif wait["tambahStaff"] == True:
                contact = cl.getContact(msg.contentMetadata["mid"])
                if contact in staff:
                  cl.sendText(msg.to,"already")
                  wait["tambahStaff"] = False
                else:
                  try:
                    #cl.findAndAddContactsByMid(contact)
                    staff.append(contact)
                    cl.sendText(msg.to,"Already Added To Teamlist Boss")
                    wait["tambahStaff"] = False
                  except:
                    pass
                    
              elif wait["hapusStaff"] == True:
                contact = cl.getContact(msg.contentMetadata["mid"])
                if contact not in staff:
                  cl.sendText(msg.to,"Dy Bukan Admin Boss")
                  wait["hapusStaff"] = False
                else:
                  try:
                    staff.remove(contact)
                    cl.sendText(msg.to,"Already Deleted To Teamlist Boss")
                    wait["hapusStaff"] = False
                  except:
                    pass
                    
              elif wait["contactDetail"] == True:
                    try:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cover = cl.channel.getCover(msg.contentMetadata["mid"]) 
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            cl.sendImageWithURL(msg.to, str(path))
                        except:
                            pass
                        ret_ = "╔══[ Details Contact ]"
                        ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                        ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                        ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                        ret_ += "\n╚══[ Finish ]"
                        cl.sendText(msg.to, str(ret_))
                    except:
                        cl.sendText(msg.to, "Kontak tidak valid")
              
            if msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "URL : \n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
                    
            if msg.contentType == 0:
                if msg.text == None:
                    return
                elif msg.text in ["Help","help","Key"]:
                  if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                    else:
                        cl.sendText(msg.to,helpt)

                elif msg.text in ["Menu Proteksi","Menu proteksi","menu proteksi"]:
                  if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,MProteksi)
                    else:
                        cl.sendText(msg.to,MProteksi)
                elif msg.text in ["Menu Group","Menu group","menu group"]:
                  if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,MGroup)
                    else:
                        cl.sendText(msg.to,MGroup)
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif msg.text in ["Menu Self","Menu self","menu self"]:
                  if msg.from_ in owner:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,MSelf)
                    else:
                        cl.sendText(msg.to,MSelf)
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                elif msg.text in ["Price owner","price owner","Price Owner"]:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,HargaOwner)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': 'u5a9693b5d9a6544575814708a0a1bad0'}
                        cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,HargaOwner)
                elif msg.text in ["Price admin","price admin","Price Admin"]:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,HargaAdmin)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': 'u5a9693b5d9a6544575814708a0a1bad0'}
                        cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,HargaAdmin)
                elif msg.text in ["Price self","price self","Price Self"]:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,HargaSelf)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': 'u5a9693b5d9a6544575814708a0a1bad0'}
                        cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,HargaSelf)
                        
                elif msg.text in ["Price vps","price vps","Price VPS"]:
                  #cl.sendImageWithURL(msg.to,"http://oi68.tinypic.com/2uzt4kz.jpg")
                  #cl.sendImageWithURL(msg.to,"http://oi67.tinypic.com/2wnr0oj.jpg")
                  #cl.sendText(msg.to,"VPS Linux Full Root\nTersedia Juga VPS RDP/Windows")
                    if wait["lang"] == "JP":
                    	cl.sendText(msg.to,"VPS Linux")
                        cl.sendText(msg.to,HargaVPS)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': 'ued156c86ffa56024c0acba16f7889e6d'}
                        cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,HargaVPS)
                        
                elif msg.text in ["Tutor py2","Tutor Py2"]:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,TutorPy2)
                    else:
                        cl.sendText(msg.to,TutorPy2)
                        
                elif msg.text in ["Tutor py3","Tutor Py3"]:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,TutorPy3)
                    else:
                        cl.sendText(msg.to,TutorPy3)
                        
                elif msg.text.lower() == 'runtime':
                  if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "SelfBot Sudah Berjalan Selama\n"+waktu(eltime)
                    cl.sendText(msg.to,van)
                        
                elif msg.text == "Reboot":
                  if msg.from_ in admin:
                    cl.sendText(msg.to,"Restarting...")
                    restart_program()
                    print "@Restart"
                        
                elif "Gn " in msg.text:
                  if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                    
                elif msg.text in ["Tambah Admin"]:
                  if wait["tambahStaff"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Kirim Kontaknya Boss")
                      else:
                          cl.sendText(msg.to,"done")
                  else:
                      wait["tambahStaff"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Kirim Kontaknya Boss")
                      else:
                          cl.sendText(msg.to,"done")
                          
                elif msg.text in ["Hapus Admin"]:
                  if wait["hapusStaff"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Kirim Kontaknya Boss")
                      else:
                          cl.sendText(msg.to,"done")
                  else:
                      wait["hapusStaff"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Kirim Kontaknya Boss")
                      else:
                          cl.sendText(msg.to,"done")

                elif "Team add @" in msg.text:
                  if msg.from_ in owner:
                    #print "[Command]Staff add executing"
                    _name = msg.text.replace("Team add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                    else:
                       for target in targets:
                            try:
                            	if target in staff:
                            	  cl.sendText(msg.to,"Makhluk ini Udah Di Dalam Teamlist Boss")
                                else:
                                  cl.findAndAddContactsByMid(target)
                                  staff.append(target)
                                  cl.sendText(msg.to,"Already Added To Teamlist Boss")
                            except:
                                cl.sendText(msg.to,"Done √")
                    print "[Command]Admin add executed"
                    
                elif "Team remove @" in msg.text:
                  if msg.from_ in owner:
                    #print "[Command]Staff remove executing"
                    _name = msg.text.replace("Team remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                    else:
                       for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Deleted From Teamlist")
                            except:
                                pass
                    print "[Command]Admin remove executed"
                  
                elif msg.text in ["Teamlist","teamlist","Team list"]:
                  if staff == []:
                      cl.sendText(msg.to,"Teamlist nya Kosong Boss")
                  else:
                      cl.sendText(msg.to,"Tunggu...")
                      mc = "👥Teamlist BOT👥\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                      for mi_d in staff:
                          mc += "👉 [★]" + cl.getContact(mi_d).displayName + "\n"
                      cl.sendText(msg.to,mc)
                      #print "[Command]Stafflist executed"
                      
                elif msg.text in ["Bot?"]:
                  if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    
                elif "Allname: " in msg.text:
                  string = msg.text.replace("Allname: ","")
                  if len(string.decode('utf-8')) <= 6000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    
                elif "Allbio: " in msg.text:
                  string = msg.text.replace("Allbio: ","")
                  if len(string.decode('utf-8')) <= 6000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    
                elif msg.text in ["Sambutan on"]:
                  if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                  else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                        
                elif msg.text in ["Sambutan off"]:
                  if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                  else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                    
                elif "Update sambutan: " in msg.text:
                  #if msg.from_ in admin + owner + creator:
                    wait["Sambutan"] = msg.text.replace("Update sambutan2: ","")
                    cl.sendText(msg.to,"ˢᵃᵐᵇᵘᵗᵃⁿ ᴬᵏᵗᶦᵛᵉ ᶜʰᵃⁿᵍᵉᵈ"+ datetime.today().strftime('%H:%M:%S'))
                    
                elif msg.text in ["Check sambutan"]:
                  #if msg.from_ in admin + creator + owner:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʸᵒᵘʳ ᴮᵒᵗ ᴹᵉˢˢᵃᵍᵉ\n\n" + wait["Sambutan"])
                    else:
                        cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["Sambutan"])

                elif msg.text in ["Me","me"]:
                  #if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    cl.sendMessage(msg)

                elif msg.text in ["Cancel","cancel"]:
                  if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"No one is inviting")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif msg.text in ["Buka qr","Open qr"]:
                  if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Already Opened")
                        else:
                            cl.sendText(msg.to,"Already Opened Boss")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
                  #else:
                    #cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif msg.text in ["Tutup qr","Close qr"]:
                  if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Code QR Already Closed")
                        else:
                            cl.sendText(msg.to,"Already Closed Boss")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
                  #cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif "jointicket " in msg.text.lower():
                  rplace=msg.text.lower().replace("jointicket ")
                  if rplace == "on":
                    wait["atjointicket"]=True
                  elif rplace == "off":
                    wait["atjointicket"]=False
                    cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))

                elif "Info group" == msg.text:
                  if msg.toType == 2:
                    if msg.from_ in admin:
                      ginfo = cl.getGroup(msg.to)
                      try:
                        gCreator = ginfo.creator.displayName
                      except:
                        gCreator = "Error"
                      if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                          sinvitee = "0"
                        else:
                          sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          QR = "Close"
                        else:
                          QR = "Open"
                        cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                      else:
                        cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                    else:
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                      else:
                        cl.sendText(msg.to,"Not for use less than group")
                        
                elif "Info group2" == msg.text:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Name Group : {}".format(group.name)
                    ret_ += "\n╠ID Group : {}".format(group.id)
                    ret_ += "\n╠Creator Group : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Group QR : {}".format(gQr)
                    ret_ += "\n╠Group URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        
                elif msg.text in ["Id group"]:
                  if msg.from_ in admin:
                    saya = msg.text.replace("Id group2","")
                    gid = cl.getGroup(msg.to)
                    cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                        
                elif "My mid" == msg.text:
                  middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                  cl.sendText(msg.to,middd)

                elif "Mid Bot" == msg.text:
                  if msg.from_ in admin:
                    cl.sendText(msg.to,midCL)
                
                elif msg.text in ["Pro on"]:
                    wait["Protectgr"] = True
                    wait["Protectcancl"] = True
                    wait["Protectcancel"] = True
                    wait["Protectjoin"] = True
                    wait["Protectkick"] = True
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
                    
                elif msg.text in ["Pro off"]:
                    wait["Protectgr"] = False
                    wait["Protectcancl"] = False
                    wait["Protectcancel"] = False
                    wait["Protectjoin"] = False
                    wait["Protectkick"] = False
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
                
                elif msg.text in ["Protect cancel on","protect cancel on"]:
                  if msg.from_ in owner:
                    if wait["Protectcancel"] == True:
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Canceled Invited On")
                      else:
                        cl.sendText(msg.to,"Done")
                    else:
                      wait["Protectcancel"] = True
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Canceled Invited On")
                      else:
                        cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")

                elif msg.text in ["Protect cancel off","protect cancel off"]:
                  if msg.from_ in owner:
                    if wait["Protectcancel"] == False:
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Canceled Invited Off")
                      else:
                        cl.sendText(msg.to,"Done")
                    else:
                      wait["Protectcancel"] = False
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Canceled Invited Off")
                      else:
                        cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                elif msg.text in ["Protect blacklist on","Purge on","Purge: on","purge: on"]:
                  if msg.from_ in admin:
                    if wait["Protectjoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Blacklist Activated")
                        else:
                            cl.sendText(msg.to,"Done")
                    else:
                        wait["Protectjoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Blacklist Activated")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif msg.text in ["Protect blacklist off","Purge off","Purge: off","purge: off"]:
                  if msg.from_ in admin:
                    if wait["Protectjoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Blacklist Disabled")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectjoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Blacklist Disabled")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                elif msg.text in ["Protect invite on","Invite on"]:
                  if msg.from_ in owner:
                    if wait["Protectcancl"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel All Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancl"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel All Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msh.to, "This command only for owner")

                elif msg.text in ["Protect invite off","Invite off"]:
                  if msg.from_ in owner:
                    if wait["Protectcancl"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel All Invitation Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancl"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel All Invitation Off")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msh.to, "This command only for owner")

                elif msg.text in ["Protect qr on","Qr on"]:
                  if msg.from_ in owner:
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR On")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msh.to, "This command only for owner")

                elif msg.text in ["Protect qr off","Qr off"]:
                  if msg.from_ in owner:
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect QR Off")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msh.to, "This command only for owner")

                elif msg.text in ["Protect kick on","Kick on"]:
                  if msg.from_ in owner:
                    if wait["Protectkick"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Kick On")
                        else:
                            cl.sendText(msg.to,"Protect Kick On")
                    else:
                        wait["Protectkick"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect Kick On")
                        else:
                            cl.sendText(msg.to,"Protect Kick On")

                elif msg.text in ["Protect kick off","Kick off"]:
                  if msg.from_ in owner:
                    if wait["Protectkick"] == False:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Protect Kick Off")
                        else:
                            ki.sendText(msg.to,"Protect Kick Off")
                    else:
                        wait["Protectkick"] = False
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Protect Kick Off")
                        else:
                            ki.sendText(msg.to,"Protect Kick Off")

                elif msg.text in ["Contact On","Contact on","contact on"]:
                  if msg.from_ in owner:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On\nUntuk Cek Mid Silahkan Share Kontaknya")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On\nUntuk Cek Mid Silahkan Share Kontaknya")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                elif msg.text in ["Contact Off","Contact off","contact off"]:
                  if msg.from_ in owner:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                    
                elif msg.text in ["Contact2 On","Contact2 on","contact2 on"]:
                  if msg.from_ in owner:
                    if wait["contactDetail"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Detail Kontak On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contactDetail"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Detail Kontak On")
                        else:
                            cl.sendText(msg.to,"done")
                
                elif msg.text in ["Contact2 Off","Contact2 off","contact2 off"]:
                  if msg.from_ in owner:
                    if wait["contactDetail"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Detail Kontak Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contactDetail"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Detail Kontak Off")
                        else:
                            cl.sendText(msg.to,"done")
                    
                elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                  if msg.from_ in owner:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                  if msg.from_ in owner:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")
                elif msg.text in ["Gcancel:"]:
                  if msg.from_ in owner:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
                elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on2","Auto leave:on2","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                  if msg.from_ in owner:
                    if wait["Leave"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Leave"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
                elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                  if msg.from_ in owner:
                    if wait["Leave"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Leave"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
                elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                  if msg.from_ in owner:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
                elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                  if msg.from_ in owner:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
                elif msg.text in ["Status","Set"]:
                  if msg.from_ in admin:
                    md = "╔═══════════════\n║  ⭐Status Protection⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                    if wait["Protectgr"] == True: md+="║[•]Protect QR Enable\n"
                    else: md+="║[•]Protect QR Disable\n"
                    if wait["Protectcancl"] == True: md+="║[•]Protect Invite Enable\n"
                    else: md+="║[•]Protect Invite Disable\n"
                    if wait["Protectcancel"] == True: md+="║[•]Protect Cancel Enable\n"
                    else: md+="║[•]Protect Cancel Disable\n"
                    if wait["Protectjoin"] == True: md+="║[•]Protect Blacklist Enable\n"
                    else: md+="║[•]Protect Blacklist Disable\n"
                    if wait["Protectkick"] == True: md+="║[•]Protect Kick Enable\n"
                    else: md+="║[•]Protect Kick Disable\n"
                    if wait["contact"] == True: md+="║[•]Contact ✔\n"
                    else: md+="║[•]Contact ❌\n"
                    if wait["autoJoin"] == True: md+="║[•]Auto Join ✔\n"
                    else: md +="║[•]Auto Join ❌\n"
                    if wait["Leave"] == True: md+="║[•]Auto Leave ✔\n"
                    else: md +="║[•]Auto Leave ❌\n"
                    if wait["Sider"] == True: md+="║[•]Auto Sider ✔\n"
                    else:md+="║[•]Auto Sider ❌\n"
                    if wait["detectMention"] == True: md+="║[•]Respon Tag ✔\n"
                    else:md+="║[•]Respon Tag ❌\n"
                    if wait["pmMention"] == True: md+="║[•]Respon Tag PM ✔\n"
                    else:md+="║[•]Respon Tag PM ❌\n"
                    #if wait["autoCancel"]["on"] == True:md+="║[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                    #else: md+="║[•]Group Cancel [Off]\n"
                    if wait["AutoLep"] == True: md+="║[•]Auto Leave ✔\n"
                    else: md+="║[•]Auto Leave ✖\n"
                    if wait["contactDetail"] == True: md+="║[•]Detail Kontak ✔\n"
                    else: md+="║[•]Detail Kontak ✖\n"
                    if wait["likeOn"] == True: md+="║[•]Auto like ✔\n"
                    else: md+="║[•]Auto like ❌\n"
                    if wait["autoAdd"] == True: md+="║[•]Auto Add ✔\n"
                    else: md+="║[•]Auto Add ❌\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║   ⭐૦Ո૯ ƿɿ૯८૯ ੮૯คɱ⭐\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                    cl.sendText(msg.to,md)
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")
                    
                elif msg.text in ["Link group"]:
                  if msg.from_ in admin:
                    if msg.toType == 2:
                      x = cl.getGroup(msg.to)
                      if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                    else:
                      if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                      else:
                        cl.sendText(msg.to,"Not for use less than group")
                    
                elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                  if msg.from_ in owner:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"Done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
                elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                  if msg.from_ in owner:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
                            
                elif msg.text == "Cctv":
                  #if msg.from_ in admin:
                    cl.sendText(msg.to, "Mencari CCTV...")
                    try:
                      del wait2['readPoint'][msg.to]
                      del wait2['readMember'][msg.to]
                    except:
                      pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                
                elif msg.text == "Ciduk":
                     #if msg.from_ in admin:
                      if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════\n║Dilihat Oleh%s\n╠═══════════════\n╠[Pelaku CCTV]\n%s║Awas CCTV :\n║-Bintitan\n║-Kurapan\n║-Panuan\n║-Kudisan\n║Pokoknya Yang Jelek²\n║Kalo Cctv Nya Ga Muncul\n\n║Jangan Pake Header ChromeOS\n║[%s]\n╚═══════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                      else:
                          cl.sendText(msg.to, "Ketik Cctv Dulu Njir\nBaru Ketik Ciduk\nDasar Pikun ♪")
                    
                elif "Mid @" in msg.text:
                  if msg.from_ in owner:
                    _name = msg.text.replace("Mid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                      if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                      else:
                        pass
                  
                elif "Ban " in msg.text:
                  if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                      try:
                        wait["blacklist"][target] = True
                        cl.sendText(msg.to,"Succes Banned")
                      except:
                        pass

                elif msg.text in ["Kuy", "Masuk"]:
                  if msg.from_ in owner:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    G.preventJoinByTicket(G)
                    kk.updateGroup(G)

                elif msg.text in ["Clear ban"]:
                  if msg.from_ in owner:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"Succes Clear Blacklist Boss")
                    
                elif msg.text in ["List group","List Group"]:
                  if msg.from_ in owner:
                    gids = cl.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = cl.getGroup(i).name
                      h += "[★]%s Member\n" % (cl.getGroup(i).name   + "👉" + str(len(cl.getGroup(i).members)))
                    cl.sendText(msg.to,"===========[List Group]==========\n"+ h +"Total Group :" + str(len(gids)))

                elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
                  if msg.from_ in admin:
                    cl.sendText(msg.to,"Tukang Sayur On")
                    cl.sendText(msg.to,"Tukang Jengkol On")
                    cl.sendText(msg.to,"Tukang Boker On")
                    cl.sendText(msg.to,"Tukang Kibul On")
                    cl.sendText(msg.to,"Tukang Ngupil On")
                    cl.sendText(msg.to,"Semua Tukang Udah Hadir Boss\nSiap Protect Group")
        #-------------Fungsi Respon Finish---------------------#   
                elif msg.text in ["Speed","Sp"]:
                  if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to,"「Wait Loading」")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%s/Detikี" % (elapsed_time))
        #-------------Fungsi Spam---------------------#   
                elif msg.text in ["Spam "]:
                  if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    
                    if txt[1] == "on":
                    	if jmlh <=500:
                    	     for x in range(jmlh):
                    	           cl.sendText(msg.to, teks)
                    	else:
                    	       cl.sendText(msg.to, "Out of range! ")
                    elif txt[1] == "off":
                    	if jmlh <= 500:
                    	     cl.sendText(msg.to, tulisan)
                        else:
                        	  cl.sendText(msg.to, "Out of range! ")
          #-------------Fungsi Speedbot Finish---------------------#   
                elif "Profile" in msg.text:
                	key = eval(msg.contentMetadata["MENTION"])
                	key1 = key["MENTIONEES"][0]["M"]
                	contact = cl.getContact(key1)
                	msg.contentType = 13
                	msg.contentMetadata = {"mid": key1}
                	cl.sendMessage(msg)
                	cu = cl.channel.getCover(key1)
                	path = str(cu)
                	image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                	cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                	cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                	cl.sendImageWithURL(msg.to,image)
                	cl.sendText(msg.to,"Cover " + contact.displayName)
                	cl.sendImageWithURL(msg.to,path)
        #-------------Fungsi Spamtag---------------------#     
                elif "Spamtag @" in msg.text:
                  if msg.from_ in admin:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                    	if _nametarget == g.displayName:
                    	   xname = g.displayName
                           xlen = str(len(xname)+1)
                           msg.contentType = 0
                           msg.text = "@"+xname+" "
                           msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)
                           cl.sendMessage(msg)     
                           
                           
                elif msg.text.lower() in ["ngeselin"]:
                	msg.contentType = 7
                	msg.contentMetadata={'STKID': '15971811',
                                          'STKPKGID': '1415639',
                                          'STKVER': '1'}
                	msg.text = None
                	cl.sendMessage(msg)     
                                                      
                elif msg.text.lower() in ["kangen"]:
                	msg.contentType = 7
                	msg.contentMetadata={'STKID': '10562201',
                                          'STKPKGID': '1260481',
                                          'STKVER': '1'}
                	msg.text = None
                	cl.sendMessage(msg)     
                                                      
                elif msg.text.lower() in ["halo","alo","hola"]:
                	msg.contentType = 7
                	msg.contentMetadata={'STKID': '8182903',
                                          'STKPKGID': '1201390',
                                          'STKVER': '1'}
                	msg.text = None
                	cl.sendMessage(msg)
          #-------------Fungsi Banned Send Contact Start------------------#
                elif msg.text in ["Ban"]:
                  if msg.from_ in owner:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact")
                    
                elif msg.text in ["Unban"]:
                  if msg.from_ in owner:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact")
                    
          #-------------Fungsi Banned Send Contact Finish------------------#
                elif msg.text in ["Creator"]:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': 'u5a9693b5d9a6544575814708a0a1bad0'}
                  #cl.sendText(msg.to,"======================")
                  cl.sendMessage(msg)
                  cl.sendText(msg.to,"==||Ren Ren||==")
                  #cl.sendText(msg.to,"======================")
                  cl.sendImageWithURL("http://oi64.tinypic.com/x2oua8.jpg")
                  
                elif msg.text in ["Banlist"]:
                  if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Nothing Banned User")
                    else:
                        cl.sendText(msg.to,"Blacklist user")
                        mc = "╔═════════════\n║💩Ini Para Anjing² Kita Bos💩\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                        for mi_d in wait["blacklist"]:
                            mc += "║👉" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
        #-------------Fungsi Bannlist Finish------------------#  
                elif "Say " in msg.text:
                  if msg.from_ in admin:
                        say = msg.text.replace("Say ","")
                        lang = 'id'
                        tts = gTTS(text=say, lang=lang)
                        tts.save("Indo.mp3")
                        cl.sendAudio(msg.to,"Indo.mp3")
                  else:
                    cl.sendText(msg.to,"This Command Only For Admin & Owner")

                elif '/lyric ' in msg.text.lower():
                  if msg.from_ in owner:  
                    try:
                        songname = msg.text.lower().replace('/lyric ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Song ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            cl.sendText(msg.to, hasil)
                    except Exception as wak:
                            cl.sendText(msg.to, str(wak))
                            
                elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "LinkNya: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollowerNya : "+followerIG+"\nFollowingNya : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
                elif 'Instagram ' in msg.text.lower():
                  try:
                    instagram = msg.text.lower().replace("Instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "********************\n"
                    details = "\n********************="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                  except Exception as njer:
                	cl.sendText(msg.to, str(njer))
                            
                elif "Wikipedia " in msg.text:
                  try:
                    wiki = msg.text.replace("Wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=1)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                  except:
                    try:
                        wiki = msg.text.replace("Wikipedia2 ","")
                        wikipedia.set_lang("en")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        cl.sendText(msg.to, pesan)
                    except:
                          try:
                              pesan="Text Banyak Silahkan Click link ini\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                  
                              
                elif "Gambar " in msg.text:
                  wiki = msg.text.replace("Gambar ","")
                  url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + wiki
                  raw_html =  (download_page(url))
                  items = []
                  items = items + (_images_get_all_items(raw_html))
                  path = random.choice(items)
                  try:
                      start = timeit.timeit()
                      cl.sendImageWithURL(msg.to,path)
                      cl.sendText(msg.to, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                  except Exception as e:
                      cl.sendText(msg.to, str(e))
                            
                elif "Youtube: " in msg.text:
                  if msg.from_ in admin:
                    query = msg.text.split(" ")
                    try:
                      if len(query) == 3:
                          isi = yt(query[2])
                          hasil = isi[int(query[1])-1]
                          cl.sendText(msg.to, hasil)
                      else:
                          isi = yt(query[1])
                          cl.sendText(msg.to, isi[0])
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
                elif 'Musik ' in msg.text:
                  if msg.from_ in owner:
                    songname = msg.text.replace("Musik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ki.sendText(msg.to, hasil)
                        ki.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])

                elif '/music ' in msg.text.lower():
                  if msg.from_ in owner:  
                    try:
                        songname = msg.text.lower().replace('/music ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'This is Your Music\n'
                            hasil += 'Judul : ' + song[0]
                            hasil += '\nDurasi : ' + song[1]
                            hasil += '\nLink Download : ' + song[4]
                            cl.sendText(msg.to, hasil)
                            cl.sendText(msg.to, "Please Wait for audio...")
                            cl.sendAudioWithURL(msg.to, song[4])
                    except Exception as njer:
                            cl.sendText(msg.to, str(njer))
                            
                elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])

                elif "Pp group " in msg.text:
                  if msg.from_ in owner:
                    saya = msg.text.replace('Pp group ','')
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        h = cl.getGroup(i).name
                        gna = cl.getGroup(i)
                        if h == saya:
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                  else:
                    cl.sendText(msg.to,"This Command Only For Owner")

                elif msg.text in ["My pp"]:
                  h = cl.getContact(midCL)
                  cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                  
                elif msg.text in ["Ganti pp"]:
                  wait["changePicture"] = True
                  cl.sendText(msg.to, "Kirim gambarnya")
                  
                elif msg.text in ["My cover"]:
                  h = cl.getContact(midCL)
                  cu = cl.channel.getCover(midCL)
                  path = str(cu)
                  cl.sendImageWithURL(msg.to, path)

                elif "Stealgroup" in msg.text:
                  if msg.from_ in owner:
                    group = cl.getGroup(msg.to)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + group.pictureStatus)

                elif msg.text in ["One Piece","OP","one piece","One piece"]:
                  if msg.from_ in owner:
                    cl.sendImageWithURL(msg.to,"http://oi64.tinypic.com/106xa1j.jpg")
                    cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/125rms0.jpg")
                    cl.sendImageWithURL(msg.to,"http://oi68.tinypic.com/kb8tae.jpg")
                    cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/69oy2v.jpg")
                    cl.sendImageWithURL(msg.to,"http://oi66.tinypic.com/10dxtp1.jpg")
                    cl.sendImageWithURL(msg.to,"http://oi65.tinypic.com/2ds4y78.jpg")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'uc9363b5a4bfacd981c3e3c082bc4d5ef'}
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"☆ ૦Ո૯ ƿɿ૯८૯ ੮૯คɱ ☆")
                    
                elif ".fb " in msg.text:
                  if msg.from_ in owner:
                    a = msg.text.replace(".fb ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")

                elif msg.text in ["Remove all chat"]:
                  if msg.from_ in owner:
                    cl.sendText(msg.to,"Starting Remove All Chat...")
                    cl.removeAllMessages(op.param2)
                    cl.sendText(msg.to,"All Chat In Bots Removed")

                elif msg.text in ["Member"]:
                  if msg.from_ in admin:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    cl.sendText(msg.to, msgs)

                elif msg.text in ["Conban","Contactban","Contact ban"]:
                  if msg.from_ in owner:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Nothing Blacklist")
                    else:
                        cl.sendText(msg.to,"List Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = cl.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            cl.sendMessage(M)
                elif msg.text in ["Midban","Mid ban"]:
                  if msg.from_ in owner:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        num=1
                        cocoa = "══════════List Blacklist═════════"
                        for mm in matched_list:
                            cocoa+="\n[%i] %s" % (num, mm)
                            num=(num+1)
                            cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                        cl.sendText(msg.to,cocoa)

                elif "Ban group " in msg.text:
                  grp = msg.text.replace("Ban group ","")
                  gid = cl.getGroupIdsJoined()
                  if msg.from_ in owner:
                    for i in gid:
                      h = cl.getGroup(i).name
                    if h == grp:
                      wait["BlGroup"][i]=True
                      cl.sendText(msg.to, "Success Ban Group : "+grp)
                    else:
                      pass
                  else:
                    cl.sendText(msg.to, "Just For Owner")

                elif msg.text in ["Group ban","List group ban"]:
                  if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                      cl.sendText(msg.to,"Tidak Ada")
                    else:
                      mc = ""
                      for gid in wait["BlGroup"]:
                        mc += "-> " +cl.getGroup(gid).name + "\n"
                      cl.sendText(msg.to,"===[Ban Group]===\n"+mc)
                  else:
                    cl.sendText(msg.to, "Just For Admin")

                elif msg.text in ["Group remove ban "]:
                  if msg.from_ in owner:
                    ng = msg.text.replace("Group remove ban ","")
                    for gid in wait["BlGroup"]:
                      if cl.getGroup(gid).name == ng:
                        del wait["BlGroup"][gid]
                        cl.sendText(msg.to, "Success del ban "+ng)
                      else:
                        pass
                  else:
                    cl.sendText(msg.to, "Just For Owner")
                    
                elif msg.text in ["My BCA"]:
                	cl.sendText(msg.to, "No Rekening : 7015274646\nAtas Nama : Achmad Hanafi\nJenis Bank : Bank BCA")
                
                elif msg.text in ["My HP"]:
                	cl.sendText(msg.to, "Tri →089663427204\nSimpati→081318480012")

                elif "Sider on" in msg.text:
                  if msg.from_ in admin:
                    try:
                      del cctv['point'][msg.to]
                      del cctv['sidermem'][msg.to]
                      del cctv['cyduk'][msg.to]
                    except:
                      pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    wait["Sider"] = True
                    cl.sendText(msg.to,"Siap On Cek Sider")

                elif "Sider off" in msg.text:
                  if msg.from_ in admin:
                    if msg.to in cctv['point']:
                      cctv['cyduk'][msg.to]=False
                      wait["Sider"] = False
                      cl.sendText(msg.to, "Cek Sider Off")
                    else:
                      cl.sendText(msg.to, "Heh Belom Di Set")

                elif msg.text in ["Auto like"]:
                  if msg.from_ in owner:
                    wait["likeOn"] = True
                    cl.sendText(msg.to,"Shere Post Yang Mau Di Like Boss!")

                elif "Kedip: " in msg.text:
                  if msg.from_ in owner:
                    txt = msg.text.replace("Kedip: ", "")
                    cl.kedapkedip(msg.to,txt)
                    #print "[Command] Kedapkedip"

                elif msg.text in ["Kalender","Time","Waktu"]:
                  if msg.from_ in admin:
                    timeNow = datetime.now()
                    timeHours = datetime.strftime(timeNow,"(%H:%M)")
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    inihari = datetime.today()
                    hr = inihari.strftime('%A')
                    bln = inihari.strftime('%m')
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                    cl.sendText(msg.to, rst)

                elif "Namelock on" in msg.text:
                  if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
                elif "Namelock off" in msg.text:
                  if msg.from_ in admin:
                    if msg.to in wait['pname']:
                        cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                        del wait['pname'][msg.to]
                    else:
                        cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                        
                elif "Copy @" in msg.text:
                  if msg.from_ in owner:
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                      if _nametarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                          sendText(msg.to, "Not Found...")
                        else:
                          for target in targets:
                            try:
                              cl.cloneContactProfile(target)
                              cl.sendText(msg.to, "Success Copy profile ~")
                            except Exception as e:
                              print e

                elif msg.text in ["Backup","backup"]:
                  if msg.from_ in owner:
                    try:
                      cl.updateDisplayPicture(backup.pictureStatus)
                      cl.updateProfile(backup)
                      cl.sendText(msg.to, "Backup done")
                    except Exception as e:
                      cl.sendText(msg.to, str(e))
                      
                elif msg.text.lower() == 'welcome':
                  ginfo = cl.getGroup(msg.to)
                  cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                  jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                  cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                  tts = gTTS(text=jawaban1, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                      
                elif msg.text in ["Sticker on"]:
                  if wait["sticker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Sticker ON")
                  else:
                    wait["sticker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Sticker ON")
                
                elif msg.text in ["Sticker off"]:
                  if wait["sticker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Sticker OFF")
                  else:
                    wait["sticker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Sticker OFF")
                        
                elif msg.text in ["Autolep on","autolep on"]:
                  wait["AutoLep"] = True
                  cl.sendText(msg.to,"Auto Leave ON")
                  
                elif msg.text in ["Autolep off","autolep off"]:
                  wait["AutoLep"] = False
                  cl.sendText(msg.to,"Auto Leave OFF")
                      
                elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                  wait["detectMention"] = True
                  cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                
                elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                  wait["detectMention"] = False
                  cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                  
                elif msg.text in ["Responpm on","Autoresponpm:on","Pm on","PmRespon:on"]:
                  wait["pmMention"] = True
                  cl.sendText(msg.to,"ʀᴇsᴘᴏɴ PM ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                
                elif msg.text in ["Responpm off","Autoresponpm:off","Pm off","PmRespon:off"]:
                  wait["pmMention"] = False
                  cl.sendText(msg.to,"ʀᴇsᴘᴏɴ PM ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
                                          
                elif msg.text in ["Simisimi on","Simisimi:on"]:
                  if msg.from_ in owner:
                    settings["simiSimi"][msg.to] = True
                    cl.sendText(msg.to,"Success activated simisimi")
                  
                elif msg.text in ["Simisimi off","Simisimi:off"]:
                  if msg.from_ in owner:
                    settings["simiSimi"][msg.to] = False
                    cl.sendText(msg.to,"Success deactive simisimi")
                    
                elif "Translate-id " in msg.text:
                  isi = msg.text.replace("Translate-id ","")
                  translator = Translator()
                  hasil = translator.translate(isi, dest='id')
                  A = hasil.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to, A)
                elif "Translate-en " in msg.text:
                  isi = msg.text.replace("Translate-en ","")
                  translator = Translator()
                  hasil = translator.translate(isi, dest='en')
                  A = hasil.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to, A)
                elif "Translate-ar " in msg.text:
                  isi = msg.text.replace("Translate-ar ","")
                  translator = Translator()
                  hasil = translator.translate(isi, dest='ar')
                  A = hasil.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to, A)
                elif "Translate-jp " in msg.text:
                  isi = msg.text.replace("Translate-jp ","")
                  translator = Translator()
                  hasil = translator.translate(isi, dest='ja')
                  A = hasil.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to, A)
                elif "Translate-ko " in msg.text:
                  isi = msg.text.replace("Translate-ko ","")
                  translator = Translator()
                  hasil = translator.translate(isi, dest='ko')
                  A = hasil.text
                  A = A.encode('utf-8')
                  cl.sendText(msg.to, A)

                elif "Mimic " in msg.text:
                  if msg.from_ in owner:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                      if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Mimic On Boss")
                      else:
                        cl.sendText(msg.to,"Mimic Already On Boss")
                    elif cmd == "off":
                      if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Mimic Off Boss")
                      else:
                        cl.sendText(msg.to,"Mimic Already off")
                    elif cmd == "list":
                      if mimic["target"] == {}:
                        cl.sendText(msg.to,"No target")
                      else:
                        mc = "Target Mimic\n"
                        mids = []
                        for s in range(len(mimic["target"])):
                            mids.append(mimic["target"][s])
                        cmids = cl.getContacts(mids)
                        for x in range(len(cmids)):
                            mc += "\n["+str(x)+"]"+cmids[x].displayName
                        cl.sendText(msg.to,mc)
                    elif "add " in cmd:
                      target0 = msg.text.replace("Mimic add ","")
                      target1 = target0.lstrip()
                      target2 = target1.replace("@","")
                      target3 = target2.rstrip()
                      _name = target3
                      gInfo = cl.getGroup(msg.to)
                      targets = []
                      for a in gInfo.members:
                        if _name == a.displayName:
                          targets.append(a.mid)
                      if targets == []:
                        cl.sendText(msg.to,"No targets")
                      else:
                        for target in targets:
                          try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Success added target")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                          except:
                            cl.sendText(msg.to,"Ready To Following Chat From Target Boss")
                            break
                    elif "del " in cmd:
                      target0 = msg.text.replace("Mimic del ","")
                      target1 = target0.lstrip()
                      target2 = target1.replace("@","")
                      target3 = target2.rstrip()
                      _name = target3
                      gInfo = cl.getGroup(msg.to)
                      targets = []
                      for a in gInfo.members:
                        if _name == a.displayName:
                          targets.append(a.mid)
                      if targets == []:
                        cl.sendText(msg.to,"No targets")
                      else:
                        for target in targets:
                          try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Success deleted target")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                          except:
                            cl.sendText(msg.to,"Im Not Following Again Boss\nTired, Not Get Money")
                            break
                            
        if op.type == 26:
          msg = op.message
          if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True: 
                    #msg.text.replace("@"+cl.getProfile().displayName,"")
                    if msg.from_ in pasukan1:
                      pass
                    elif msg.from_ in pasukan2:
                      pass
                    elif msg.from_ in pasukan3:
                      pass
                    elif msg.from_ in pasukan4:
                      pass
                    else:
                      contact = cl.getContact(msg.from_)
                      cu = cl.channel.getCover(msg.from_)
                      pelaku = str(cu)
                      image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                      cName = contact.displayName
                      cMid = contact.mid
                      balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                      #balas = ["Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]"]
                      balas = [cName + "\nKoplaxs nya Lagi Kojum!!! ",cName + "\nHᴀʟᴏ Fᴀɴs Bᴇʀᴀᴛ Gᴡ!! \nAᴅᴀ Pᴇʀʟᴜ ᴀᴘᴀ Tᴀɢ Gᴡ..",cName + "\nKalo Ga Penting Ga Usah Tag² \nPM Aje Ye Kan",cName + "\nKoplaxs nya Lagi Sibuk\nPM Aja Klo Penting",cName + "\nNah Tag Gw Ngajak Desah Ya...!!",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nKaya Jones Aje"]
                      path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                      ret_ = "[Auto Respond] \n" + random.choice(balas)
                      name = re.findall(r'@(\w+)', msg.text)
                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                      mentionees = mention['MENTIONEES']
                      for mention in mentionees:
                        if mention['M'] in Bots:
                          cl.sendText(msg.to,ret_)
                          jawaban1 = ("Hey Ada Apa Manggil Manggil Saya? Mau Ngajakin Nikung yah?","Ngapain Ngetek Mau Ngajakin Desah Yah")
                          tts = gTTS(text=random.choice(jawaban1), lang='id')
                          tts.save('JawabanTag.mp3')
                          cl.sendAudio(msg.to,'JawabanTag.mp3')
                          #cl.mention(op.param1, [cMid])
                          #cl.sendImageWithURL(msg.to,path)
                          #cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                          #cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                          #cl.sendImageWithURL(msg.to,image)
                          #cl.sendText(msg.to,"Cover " + contact.displayName)
                          #cl.sendImageWithURL(msg.to,pelaku)
                          msg.contentType = 7    
                          msg.text = None
                          msg.contentMetadata = {'STKID': '19665726',
                            'STKPKGID': '1566297',
                            'STKVER': '2'}                                  
                          cl.sendMessage(msg)
                          break
                        
        if op.type == 26:
          msg = op.message
          if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["pmMention"] == True: 
                    #msg.text.replace("@"+cl.getProfile().displayName,"")
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    #balas = ["Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]"]
                    balas = [cName + "\nDi Group Ngapain Tag² Aq???\nAda Yang bisa Saya Bantu???",cName + "\nKamu Yang Tag Aq di Group Itu Ya???\nAda Yang bisa Saya Bantu???",cName + "\nNgapain Tag Aku Di Room???\nMau Ajak Kojum???",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nKaya Jones Aje"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = "[Auto Respond] \n" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                      if mention['M'] in Bots:
                        cl.sendText(msg.from_,ret_)
                        cl.sendImageWithURL(msg.from_,path)
                        #msg.contentType = 7    
                        #msg.text = None
                        #msg.contentMetadata = {'STKID': '19665726',
                        #  'STKPKGID': '1566297',
                        #  'STKVER': '2'}                                  
                        #cl.sendMessage(msg,[msg.from_])
                        break
                                          
        #if op.type == 26:
        #  msg = op.message
        #  if "Apakah " in msg.text:
        #      apk = msg.text.replace("Apakah ","")
        #      rnd = ["Ngaca Woy","Tanya Mbah Gugel","Ya","Tidak","Gak","Bisa Jadi","Mungkin"]
        #      p = random.choice(rnd)
        #      lang = 'id'
        #      tts = gTTS(text=p, lang=lang)
        #      tts.save("Apakah.mp3")
        #      k1.sendAudio(msg.to,"Apakah.mp3")
        #  elif "Kapan " in msg.text:
        #    tanya = msg.text.replace("Kapan ","")
        #    jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
        #    jawaban = random.choice(jawab)
        #    tts = gTTS(text=jawaban, lang='id')
        #    tts.save('Kapan.mp3')
        #    cl.sendAudio(msg.to,'Kapan.mp3')
          elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                  text = msg.text
                  if text is not None:
                    cl.sendText(msg.to,text)
        #          else:
        #            if msg.contentType == 7:
        #  	        #msg.contentType = 7
        #              msg.text = None
        #              msg.contentMetadata = {
        #    	             "STKID": "6",
        #    	             "STKPKGID": "1",
        #    	             "STKVER": "100" }
        #    	      k1.sendMessage(msg)
        #            elif msg.contentType == 13:
        #    	        msg.contentType = 13
        #    	        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
        #    	        k1.sendMessage(msg)
#---------CCTV-------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n╠[👉]" + Name
                wait2['ROM'][op.param1][op.param2] = "╠[👉]" + Name
            else:
              cl.sendText
          except:
             pass
             
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"ᴀssᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ " + cl.getContact(op.param2).displayName + "\n╔═════════════\n║Hᴀɪ Sᴀʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ   " + str(ginfo.name) + "\n╠═════════════\n" + "║Fᴏᴜɴᴅᴇʀ ɢʀᴏᴜᴘ =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Sᴇᴍᴏɢᴀ Bᴇᴛᴀʜ ʏᴀ 😘 \n╚═════════════")
            #cl.sendText(op.param1,wait["PesanSambutan"])
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            #cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " \n + cl.getContact(op.param2).displayName +  "\n╔═════════════\n║Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " + cl.getContact(op.param2).displayName +  "\n╔═════════════\n Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ :v \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 46:
	      if op.param2 in Bots:
		    cl.removeAllMessages()
             
        if op.type == 59:
            print op
            
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
              print (e)
            
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Np = cl.getContact(op.param2).pictureStatus
                            #Name = k2.getContact(op.param2).displayName
                            #Name = k3.getContact(op.param2).displayName
                            #Name = k4.getContact(op.param2).displayName
                            #Name = k5.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Woy " + "☞ " + nick[0] + " ☜" + "\nDasar Cicitipi\nAku Doain Bintitan")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        cl.mention(op.param1, [op.param2])
                                    else:
                                        cl.sendText(op.param1, "Hehehe\nMaaf Yah " + "☞ " + nick[1] + " ☜" + "Keciduk\nMangkanya Jangan Suka Cicitipi")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        cl.mention(op.param1, [op.param2])
                                else:
                                    cl.sendText(op.param1, "Jiahahaha " + "☞ " + Name + " ☜" + "\nNgapain Cicitipi Doang???\nCICITIPI :\n★Bintitan\n★Kurapan\n★Kudisan\n★Panuan\nSemuanya Lah Pokoknya.... Wakakakakakakak...")
                                    cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    cl.mention(op.param1, [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass

    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        
#def nameUpdate():
#    while True:
#        try:
#        while a2():
#            pass
#            if wait["clock"] == True:
#                now2 = datetime.now()
#                nowT = datetime.strftime(now2,"(%H:%M)")
#                profile = cl.getProfile()
#                profile.displayName = wait["cName"] + nowT
#                cl.updateProfile(profile)
#            time.sleep(600)
#        except:
#            pass
#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()
#===========
#while True:
	bot(cl.Poll.stream(500000))
  
#Revision By Koplaxs One Piece
#Poll Diganti Dengan Poll New Version Agar Tidak Lemot Respon dan Tahan Banting :D

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
