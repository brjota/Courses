---
layout: single
title: PWK/OSCP Review
date: 2020-02-10
classes: wide
tags:
  - Review
  - OSCP
  - OffSec
---

# Penetration Testing with Kali Linux & OSCP Certification

```
54/54 lab boxes rooted, 4/5 exam hosts* 
```

### Prior Experience:
- Using MS08_067 a few times
- 3 months linux/windows basic admin experience: adding users, moving around via command line, configuring networking
- Wanted to learn some penetration testing with plenty of free time after work

#### 3 months out:
- I purchased a VIP subscription to hackthebox (HTB) and worked my way through some of the recommended machines. I worked my way from the easier boxes to the harder ones. At first I would follow along with IppSec's videos, eventually leading to only watching the videos when I got stuck or after I rooted the box to see what I might have missed.
  - [Old OSCP Like Boxes](https://forum.hackthebox.eu/discussion/612/oscp-practice)
  - [IppSec's Youtube](https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA/videos)
- Later this list was put together
    [New OSCP Like Boxes](https://docs.google.com/spreadsheets/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/edit#gid=1839402159)

- I also purchased a 3 month subscription to virtualhackinglabs (VHL). In retrospect a month of VHL would have been enough. However, at the $100/month price just buy a year of HTB VIP instead (unless you're looking to spend money). HTB offers a lot more content that you'll be able to take advantage of after passing OSCP. 
  - [Virtual Hacking Labs](https://www.virtualhackinglabs.com)
  
- It was recommended to also try a list of vulnhub VMs, however after failing to get the first 3 kioptrix boxes to work (networking) I gave up on the vulnhub list.
  - [Abatchy's OSCP like VMs](https://www.abatchy.com/2017/02/oscp-like-vulnhub-vms)

#### 1 week out:
- At this point I had around 20 boxes rooted in HTB and another 26 in VHL. I felt like I had a good beginner knowledge base for the upcoming lab. At this point I downloaded the PWK VM, set it up to my liking (config files, settings, NO UPDATES, etc) and took the rest of the week off to relax.
- I did not do any kind of cloud syncing, I just ran a backup script every evening before I suspended my VM which saved everything to a share drive.

***

#### 0 day: 2 March 19
- The first 8 days of my time was spent going through the pdf, exercises and videos. I'd read a chapter in the pdf, watch the videos, and do the exercises in that order. I was not able to finish all exercises in those 9 days, but I did continue working on them randomly when I needed a break from the lab. Eventually I got them all finished and documented for the extra points (I'd NOT recommend going for the 5 points. For myself it took almost 2 days to document and format the report). On day 9 I started and rooted my first lab machine.
- There are 4 ranges within the lab: the first if the biggest and your host is able to communicate with it, the second network consists of a few hosts, the third has a few more hosts than the second but also has a connection to an inner fourth network. 

#### Jumping in! 11 March - 10 April
- Because I'm sometimes bad with timing decisions, I moved on 11 March and didn't get internet hooked up for 3 days. During that time I re-watched the Buffer Overflow video a few times, taking notes and walked through dostackbufferoverflowgood several times. During the next 28 days I gained access to the 2 smaller networks rooting 28 boxes over 150 hours of lab time.
  - [DoStackBufferOverflowGood](https://github.com/justinsteven/dostackbufferoverflowgood)
- After around 20 roots (manually running scans for enumeration) I joined an awesome community. One of the Admins developed a tool called AutoRecon. This tool automates all enumeration (you provide the IP) and saves the results to a folder. You just sift through the results for what's interesting. At this point AutoRecon really stepped up my root speed. Twice I was able to root 4 boxes a day. AutoRecon is great, BUT you must know what to look for in the output. Otherwise it will drown you with information.
  - [InfoSec Prep Discord](https://discord.gg/qm9fxYU)
  - [AutoRecon](https://github.com/Tib3rius/AutoRecon)
  
#### Finishing strong! 11 April - 11 May
- Around this time I updated my computer (again bad with timing decisions) from a 2015 15" Book Pro to a beast (i9 9900k, 32gb RAM, 1tb 970 evo m.2, 2080ti, 2x Asus pg279qz, uplift sit/stand desk). A day was spent building and installing software, I knew I was going to wipe the desktop after the exam so software installation was minimal.
- Early on I finished up both smaller networks and gained access to the inner network. While the inner network seems to be less populated there were new techniques and concepts taught here which were not covered elsewhere in the labs. Definitely make an attempt to get here.
- After 185 hours I rooted 25 more boxes, bringing my total to 54. There IS a 55th box, however it's not "official" and not many people have rooted it. When I was last in the lab I was able to connect to the vulnerable service, I was able to get the exploit to work locally with a replicated VM, but I was unable to exploit the service in the lab. Close but oh well. 

#### Motivation? 12 May - 31 May
- Getting burnt out is real, after rooting my last box I took a week off to decompress. Afterwards I finished on my lab report, re-did the buffer overflow and dostackbufferoverflowgood to make sure my template and methodology was good. I also reviewed my notes from some of the harder boxes I ran across in the lab.

#### Ready? 6 June 19
- I stocked up on energy drinks (Bang[300mg caffeine] and Monster[140mg caffeine]), along with sushi, and pizza. My plan was to eat a normal breakfast with a bang around 10:30, have sushi around 3pm with a monster around 6pm and cold pizza for dinner. Wake up and drink a bang, quickly eat some pizza and get right back to it. The goal was quick non greasy meals leaving more time to take the test. TONS of caffeine. Short 5 minute brakes randomly.

#### SET! 7 June 19
- I scheduled my exam to start at noon. 15 minutes prior the email came, everything was setup in minutes. I followed the general advice that you find online; kick off your scans in the background (AutoRecon is great for this) and then start the buffer overflow box. 

- Timestamps are from my exam attempt
  - 1200 - GO!
  - 1400 - I still had not got a shell on the first box (ridiculous mistake looking back) so I moved on 
  - 1639 - My first root on system #2!!
  - 1723 - Unprivileged shell on system #3!!
  - 1740 - I found the privesc but for some reason stopped trying after it failed (misunderstanding the error). I spent the next 2 hours digging around/rerunning the same survey commands before I moved on to system #4
  - 1948 - * Around this time I started with the "time sink" (system #4). I learned a VERY valuable lesson here. IF something doesn't seem right, ask! Yes, the motto is "TRY HARDER!". HOWEVER, if there is 1000% no way a box is vulnerable to anything... ASK THE PROCTOR if something is broken! Better to ask and be told everything is working as intended instead of spending 7+ hours trying to discover a service which was not running
  - 2015 - Thankfully my first run in with the time sink didn't last long. Moving on to system #5
  - 2059 - Unprivileged shell on system #5!!
  - 2144 - Root on system 5!!! 
  - 2157 - At this point I reverted system #4 because who knows. Maybe the running config was busted (Offsec said you don't have to revert them), and I started my scan over for system #4
  - 2210 - After messing around for 2 hours earlier to get a simple buffer overflow to work, I was obviously missing something. So, I did something radical. I deleted everything and started from scratch. BEST. IDEA. EVER. Sometimes starting over is easier than troubleshooting
  - 2311 - Rooted system #1!! At this point I had 55 points, if I could just root system #3 I would have 80 points and pass
  - 0200 - For the next 3 hours I jumped around reading every file from system #4's scan results over and over and over, trying everything I saw online. Praying my google-fu was missing something. It wasn't. Drained, I took a 4 hour nap
  - 0620 - Started again, right back at system #4
  - 0748 - Jumped back to system #3, an hour later I revisited my failed privesc from earlier. I decided to try things differently
  - 0857 - Root on system #3!! What a feeling! Assuming I didn't screw up my exam report, I just passed OSCP! 
  - 0910 - After confirming I had all the screenshots and commands documented I jumped back to system #4. Obviously I got nowhere and wasted the remaining time of my exam
   - The exam report was easy enough; I grabbed all the screenshots and commands that were needed while I was taking the test


#### Take away:
  - Use the discord group, it's way more active than the official forums. There is a strict zero tolerance policy towards cheating and you will get banned from it
  - Speaking of forums, use them! They are a resource, just like any blog/video/etc you find. If I was stuck on a lab box for 40+ minutes I'd go read a hint. If you're stuck and don't know where to look next, a hint which leads to rooting a box provides a better learning opportunity then never rooting it would
  - AutoRecon is great, but if you're not comfortable reading nmap/tool output it won't be useful
  - Offsec IRC is dead
  - Skip documenting the exercises. I was obsessed with making sure the bonus points would save me if needed. After speaking with numerous people who passed I've come to realize: if you're relying on 5 bonus points to pass then you still have more to learn in the lab
  - Don't count an unprivileged shell on a system for any points in the exam. Offsec has never confirmed they are worth half points. Maybe one is worth 3 and another is worth 15. Maybe there are different tests where they are worth different amounts. Everyone who passes has a different experience, you should focus on getting root, not calculating imaginary points
  - There is an /r/oscp, but the community is better on discord
  - Make a plan and stick to it. I bought 90 days of lab time but didn't need it all. I decided I wanted to spend 30-40 hours a week in the lab, on top of a full time job. Some weeks I was in the lab as little as 32 hours and as many as 64 hours, one Saturday I was in the lab for 16 hours! Most weekends were 8+ hours, twice I rooted 4 boxes in a day, in total I spent 392 hours in the lab
  - From the very first box you go after, get in the habit of documenting the commands you ran, take screenshots of them and the output (unless they're not on the path to root), screenshotting your proof, etc. Don't wait until the exam to start this habbit
