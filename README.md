       /////    /////    /////////////
      CCCCC/   CCCCC/   | CC-attack |/
     CC/      CC/       |-----------|/ 
     CC/      CC/       |  Layer 7  |/ 
     CC/////  CC/////   | ddos tool |/ 
      CCCCC/   CCCCC/   |___________|/

# CC-attack ![](https://img.shields.io/badge/Version-2.8-brightgreen.svg) ![](https://img.shields.io/badge/license-MIT-blue.svg)
 A script for using socks4/5 proxies to attack http server.
 
 I removed the mixed proxies flood because in my perspective, it doesn't give more performance when flooding.
 
 News:
- [x] Improved slow mode
- [x] Random Client IP(only get mode)
 
 Info:
- [x] Using Python3
- [x] Added more human-like options
- [x] Http Get  Flood
- [x] Http Post Flood
- [x] Http Slow Attack
- [x] Support HTTPS
- [x] Socks4 Proxies Downloader
- [x] Socks4 Proxies Checker
- [x] Socks5 Proxies Downloader
- [x] Socks5 Proxies Checker
- [x] Random Http post data
- [x] Random Http Header
- [x] Random Http Useragent
- [x] Removed mixed proxies flood
- [x] Added proxies mode selection
- [x] Still Improving Project
## Sth need to talk

I made a golang httpflood with socks5, its powerful when added random url, header

and with some js resovler. I used it to take down some gov website and for some reason

I decided to release it's base.

The release will not have any function, just send simple http request through socks5 with socket

You can copy this [source's](https://github.com/Leeon123/golang-httpflood) fucntion to that source.

Base: https://github.com/Leeon123/Golang_CC_Base
## Install

    pip3 install requests pysocks
    git clone https://github.com/Leeon123/CC-attack.git
    cd CC-attack

## Usage

    python3 cc.py
