       /////    /////    /////////////
      CCCCC/   CCCCC/   | CC-attack |/
     CC/      CC/       |-----------|/ 
     CC/      CC/       |  Layer 7  |/ 
     CC/////  CC/////   | ddos tool |/ 
      CCCCC/   CCCCC/   |___________|/

# CC-attack ![](https://img.shields.io/badge/Version-3.7-brightgreen.svg) ![](https://img.shields.io/badge/license-GPLv2-blue.svg)
 A script for using socks4/5 proxies to attack http(s) server.

 News:
- [x] Changed input method. Now using command line arguments
- [x] Removed indicator 
- [x] Removed slow attack

 Info:
- [x] Using Python3
- [x] Added more human-like options
- [x] Http Get/Head/Post/Slow Flood
- [x] Random Http Header/Data
- [x] Socks4/5 Proxies Downloader
- [x] Socks4/5 Proxies Checker
- [x] Customize Cookies
- [x] Customize Post Data 
- [x] Support HTTPS
- [x] Support Socks4/5

## Install

    pip3 install requests pysocks
    git clone https://github.com/Leeon123/CC-attack.git
    cd CC-attack

## Usage

    python3 cc.py <arguments>

```
===============  CC-attack help list  ===============
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
=====================================================
```
    
