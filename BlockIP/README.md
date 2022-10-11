STATUS: Production ready. Ip's captured by my own setup to avoid off the shelf products that might be fingerprinted by malicious actors. Best way to use the list is to be able to filter what this list captures in some way and be able to then concentrate on possible attacks not blocked by this list after so you can see more easily what is hitting your firewall.

##### Clarifying using the 4 lists suggested (This, Firehol, Spamhaus):
The reason for suggesting you use this list in conjunction with the 2 Spamhaus and Firehol list is to provide some overlap and redundancy. If you only use 1 list then if it goes offline then you are unprotected for some period of time. Also as the method used to generate the lists is different there will be slightly different IP's in each list (and some overlap between them ie some IP's will be in more than 1 list). You dont Have to use the lists I suggest, for example if you really dont like firehol then you could use some other list (Dshield has a good list for example). Im simply passing on what worked well for me. My list I generate doesnt exclude IP's in the other lists or anything like that, I just might not pickup IP's they do. In short, feel free to ignore my suggested lists and use your own based on your own assesment, but this is working for me so its what I suggest for now. Maybe it will change one day if a list becomes bad/abandoned or someone lets me know of a better combination.

# StrictBlockPAllebone
Manually curated IP Blocklist of malicios IP's captured that scan/attempt to connect to services. Recommended to update your firewalls every few days with this list. Please read how to use before implementing. Anyone can use.

##### Quick Setup lists:

###### Note!
###### Firewall Maximum Table Entries must be increased when using this list. Goto Firewall - Settings - Advanced - Firewall Maximum Table Entries:
###### Default size is: 200000 - CHANGE THIS TO 800000 to allow more entries.

Direct link to this list:

https://raw.githubusercontent.com/pallebone/StrictBlockPAllebone/master/BlockIP.txt

Other Lists used:

https://www.spamhaus.org/drop/drop.txt

https://www.spamhaus.org/drop/edrop.txt

https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level1.netset

Tip: I set the lists to update staggered so for example if you set your lists to update every 3 days, I would set the first list to update 3 days, the second list to update 3 days, 1 hour, the third list 3 days and 2 hours and so on to ensure if there is an issue at one time, then they dont all fail updating at the exact same time. There is some overlap on the lists by design so this method should ensure you always have some protection even in the case of a problem etc.

##### Setup expects you to implement all 4 lists for proper protection. If you know how to add 4 blocklists already to your firewall you can do that without reading the rest of the readme. If you prefer some guidance, a short guide is below to assist you.


# Notes/Warnings

###### Note!
###### Firewall Maximum Table Entries must be increased when using this list. Goto Firewall - Settings - Advanced - Firewall Maximum Table Entries:
###### Default size is: 200000 - CHANGE THIS TO 800000 to allow more entries. You can view how full the table entries are under Firewall - Aliases and will see something like this:
<img src="./SizeTable.png">


Allowlist:
It is possible that a legitimate IP might be blocked by this list, so it is recommended that if you find someone is blocked to your services by this list, that you have an allowlist setup to accomodate that possibility. This list is simply what I created, using my own tools and detection methods, if some legitimate IP gets blocked in error, I apologise. Having an allowlist will mitigate any blocked addresses you see in the logs.

In addition, the list is fairly strict. Once an IP gets added, its considered risky and wont be removed for an entire 12 months or so. This might seem unfair, but risky networks have no place expecting their traffic to pass firewalls, and should be encoraged to take better care. This means this list is not for everyone, nor every application. Please make an assesment to see if this list works for you, before simply using it. It will block a lot, for a long time, so take that in mind.

If you feel an IP is listed that should not be, raise a ticket and I will make an assesment. Please ask nicely :)


# How to use

# Overview:

Note: This guide will show you how to setup the blocklist using a popular firewall, OPNSense. If using a different firewall, simply take the logical steps as approprate for your own firewall.

Before I started this blocklist, I was using the spamhaus ip blocklists (https://www.spamhaus.org/drop/) drop, and edrop.
I found that unfortunatly while 50% or so of malicious IP's were caught, quite a lot still got through.
As I wanted a greater net of blocked IP's, ie around 99%+ of malicious IP's blocked, I started creating my own list manually each day after manually reviewing the logs on my firewall.

This means that the list is only updated, manually, on days I check my logs. Typically this is each day during the week, not at all on weekends, and if I go on holiday there may be a week when its not updated. For this reason, there is no real point in updating the IP blocklist on your firewall more often than around every 7 days (Set this to 3 days if you are insistant you need it refreshed more often). 7 days or 3 days are the values I am expecting you to use in production (and use myself). Despite this, it is still a very good list and helps me reduce my malicious traffic by a value greater than 99% which was my goal. You can review your own firewall logs and check this fro yourself when using this list.

The below guide shows how to implement the blocklist, and optionally, create an allowlist for any IP's that you personally find are blocked, but want to allow access to services without having to remove the entire blocklist to do so.

# Implementing:

As the list expects you to already have the spamhaus/firehol lists blocked (ie try avoid only using 1 list and use a couple), and is supplementing those list (working together to provide more coverage), you should begin by adding the spamhaus blocklists to your firewall.

Step 1: Create the Aliases for the blocklists we will be using (firehol missing from this particular screenshot), and allowlist if you desire:
<img src="./Alias.png">
(please note my image shows an internal IP that I am updating my list from as I create the lists. You will however NOT use this internal IP obviously. I copy this altered list up to github when I am finished modifying it.

Each item created as follows:

##### FirewalledServices	Port(s)	 	22,80,443,3389,19132

This is the services on the firewall that are open to the outside world and forwarded to various different internal computers behind the firewall.
In my own case, I have an ssh server, a web server, an rdp server and a minecraft server.
These ports must be specified as an alias so that we can add an allow rule later on to these allowed ports, from IP's we want to allow.


##### StrictBlockPAllebone	URL Table (IPs)	 	https://raw.githubusercontent.com/pallebone/StrictBlockPAllebone/master/BlockIP.txt

This is a URL table to the blocklist. I set update period to 7 days (or 3 if you prefer).


##### AllowlistedIPs	Host(s)	 	

This is the aliases you will add IP's you want to allow into. In the screenshot you see a random test IP (obscured) I used to check it worked. You will only add your own list of IP's you deem relevant, nothing else. They will not be blocked once you add them.


##### spamhaus_drop	URL Table (IPs)	 	https://www.spamhaus.org/drop/drop.txt

The IP drop list from spamhaus. I set update period to 7 days (or 3 if you prefer).


##### spamhaus_edrop	URL Table (IPs)	 	https://www.spamhaus.org/drop/edrop.txt

The IP edrop list from spamhaus. I set update period to 7 days (or 3 if you prefer).


##### spamhaus_group	Host(s)	 	spamhaus_drop,spamhaus_edrop

An alias that contains the 2 spamhaus lists in one single alias so we can add just this alias to a firewall rule.

##### EDIT August 2020
I also now use the firehol list (http://iplists.firehol.org/) as it adds additional IP's to the overall blocking infrustructure so there is an additional source of IP's. I simply added another alias for firehol and added that to the group as per this screenshot:

<img src="./AugGroup.png">

So in effect you now have 4 blocklists at this point, the 2 spamhaus, the firehol and this one giving you 3 disparate sources of protection.
All 4 lists can either update every 7 days or 3 days if you prefer a slightly higher update frequency. I have tested quite a bit and this frequency seems to work well in my opinion.



Step 2:
Create your firewall rules under "firewall - wan" in order to allow and block the relevant traffic as follows:
<img src="./Rules.png">

##### IPv4 TCP/UDP 	AllowlistedIPs  	* 	* 	FirewalledServices  	* 	* 	Allowlist 

This simple rule allows Allowlist IP's to access the ports listed in alias "FirewalledServices" TCP or UDP and tags the label "Allowlist" for review in the logs.


##### IPv4 * 	spamhaus_group  	* 	* 	* 	* 	* 	Evil spamhaus 

This simple block rule blocks any IPv4 address using any protocol, that is on the blocklist to any and all services on the firewall. It marks a label "Evil spamhaus" for review in the logs.


##### IPv4 * 	StrictBlockPAllebone  	* 	* 	* 	* 	* 	Evil IPs 

Similar to the above rule, but for the blocklist I have created.



Step 3)

The rules now are now created. You can check the aliases work by reviewing the diagnostics - pftables area of the firewall:
<img src="./PFtables.png">

You can review the rules are matching traffic in the logs:
<img src="./Logs.png">

You may change the label to "Allowlist" to review logs that matched "Allowlist" in a similar way. Logging will need to be ON on the rules you wish to monitor in the live log.

This concludes the setup. The list should update automatically every 7 days (or 3 if you wanted it more up to date), protecting you from malicious traffic.
