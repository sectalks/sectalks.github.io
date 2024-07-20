---
layout:     post
title:      SYD0x09 
summary:    Practical SMEP Bypass Techniques on Linux
categories: meetup sydney
---
SYD0x09 (10th session)

# 1 Practical SMEP Bypass Techniques on Linux

The Linux kernel has always been an appealing target for exploit developers due to the exploitation complexity associated with user-space processes (ASLR, NX, Canaries, Fortify, RELRO etc.). Common ret2usr (return-to-user) attacks typically redirect kernel control flow to data residing in user space. These attacks were successful until around 2013 before the introduction of 3rd generation Intel Core processors (Ivy Bridge) with SMEP support. SMEP (Supervisor Mode Execution Protection) is a hardware feature that prevents attempts to execute code residing in user-space pages that are not owned by the kernel. This kernel-hardening approach is now widely adopted and effectively mitigates common exploitation patterns of kernel vulnerabilities.

This presentation introduces practical Linux SMEP bypasses involving in-kernel ROP and spraying techniques. We will demonstrate how to convert an existing exploit code to a fully-weaponised SMEP-aware exploit. The talk will concentrate on a specific vulnerability but the exploitation techniques presented are generic and can be applied to other Operating Systems that employ explicit sharing of the virtual address space among user processes and the kernel.

By Vitaly Nikolenko

"Vitaly is a security researcher specialising in malware analysis and exploit development. He’s currently focused on Linux kernel exploitation techniques (SMEP/SMAP and in-kernel ASLR bypasses) and the associated countermeasures."

# 2  60minutes CTF SYD0x09

Bring your gears+3g connection! (no laptop => no CTF!)

# 3 After the event drinks 

Assembly Bar, 488 Kent Street, Sydney NSW
