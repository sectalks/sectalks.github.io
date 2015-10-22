---
layout:     post
title:      PER0x00
summary:    Design Flaws Pwning easy as one, two, three by munmap and Patch In The Middle Subverting Client Upgrades by gman
categories: meetup perth
---
is happening.....

############
SecTalks 0x00
############
############
#Speaker I
munmap - doing his best to be a corporate guy
#Title
Design Flaws: Pwning easy as one, two, three!
#Abstract
This will be a talk around design and logic flaws vs. memory corruption bugs. Nowadays, people are more and more focused on design flaws as opposed to memory corruption bugs because of all of the defensive mechanisms in place such as DEP, ASLR, Stack and Heap Cookies, ASCII Armor, RELRO, etc. Logic and design flaw exploitation is usually a lot less time-consuming and way more reliable since attackers don't mess with all of the aforementioned mechanisms. I'll be demonstrating a real-world attack scenario against products such as [CENSORED], chaining multiple design and logic flaws in order to achieve full system compromise.

#Speaker II
gman - another corporate guy
#Title
Patch In The Middle: Subverting Client Upgrades
#Abstract
Man in the middle proofs of concept often focus on stealing credentials, but a well implemented MITM on an untrusted network opens up a number of other interesting possibilities, particularly with regards to data tampering. You may have seen for example pranks with a MITM proxy where all website images are replaced with (lets say) lolcats, and perhaps using SSL and not trusting bogus certs or unknown SSH host fingerprints may mitigate this to an extent, but how about applications which aren't as paranoid as we are? Plenty of apps have auto update functionality, but how trusting are they with regards to the patches they download? In this session I take a look at the a client MITM attack framework 'Evilgrade' which is designed to subvert the auto-update function on a number of common apps, including Skype, Winamp, Virtualbox and others.
############


See you all!
