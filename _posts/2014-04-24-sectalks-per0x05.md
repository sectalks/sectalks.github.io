---
layout:     post
title:      PER0x05
summary:    Stop it or you will go blind
categories: meetup perth
---

SecTalks PER0x05

<pre>
CREATE TABLE SecTalks
(
    MeetingNo int,
    TimeStamp int, #+0800
    Location varchar(255),
    Title varchar(255),
    Description varchar(1024),
    Speaker varchar(255),
    Challenge varchar(1024),
    Contact varchar(1024)
);

INSERT INTO SecTalks VALUES
(
    5,
    1398360600,
    'Conference room, Level 4, 16 St Georges Tce'
    '#1 Stop it or you will go blind',
    'This talk will cover the different types of SQL injection, with a focus on blind injection (boolean and time-based). I will touch on some awesome tools for exploiting SQLi vulns. Finally, I will demonstrate how boolean blind SQLi was used to pick up one of the flags in the last CTF (and win a beer.)'
    'dave_au @asterisk',
    '#2 Solution to Challenge 0x03a&b'
);

COMMIT;
</pre>
