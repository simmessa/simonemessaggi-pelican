---
date: 2016-02-06
title: For those seeking to bruteforce your SSH server
lang: en
slug: bruteforce-ssh-server
cover: images/K-Line.jpg
status: published
category: Tech
tags: SSH, Fail2ban, Security
---

Today a quick recipe to avoid unauthorized access to your favorite SSH server.

*Article originally published on 6 February 2016 at Simmessa.com*

If you have public servers on the internet, with door 22 open (and if you read this blog I hope you have...), maybe it's time to give an eye to the authentication logs of your server:

`tail -f /var/log/auth.log`

Got it? Well, if you're lucky you'll notice a lot of unauthorized access attempts, right?

By default, the PAM of your Linux server does nothing but wait for connection attempts, if more than 3 login errors close the prompt and wait for a new attempt, but is it right, according to you, to give scripters all these endless brute force attempts on SSH?

I don't think so, and then we're throwing an ally.

** Fail2ban **

*This is the site of the tool [Fail2ban](http://www.fail2ban.org/)*

The concept behind this useful demon is simple, if you miss more than tot login attempts ban!

The ban is usually temporary, but it can serve to dissuade the reapers enough to let them divert attention from our server and devote themselves to other, perhaps more productive.

##How do you install Fail2ban? (on Debian)

Simple, just apt-get:

$ sudo apt-get install fail2ban

At this point we customize the configuration of the demon by copying the .conf file:

`sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

Well, now we can switch to customization of the config:

`sudo vi /etc/fail2ban/jail.conf`

The most important lines to change determine the behavior of fail2ban, for example wantom be quiet not to cut us out alone a day when we will inevitably get hit by a babbeite attack!

``
# \"ignoreip\" can be an IP address, a CIDR mask or a DNS host

127.0.0.1/8 192.168.1.0/24
bantime = 600
maxretry = 6
``

I also suggest to keep the number of maxretry high, 3 are a few days and can help us not to harm.

The bantime is time (in seconds) so we want to ban \"badans\", 10 minutes could already make the scripters dexist (if they are able to write scripts, at least).

Another aspect that deserves mention is the automatic sending of emails if an unauthorized access attempt is intercepted:

``
# Destination email address used solely for the
interpolations in jail.{conf,local} configuration files.
destemail = mail@nonexist.caz
``

But eye, your server must be able to send mail because it works, alternatively you can deliver to a local account... do you!

The last part of **Fail2ban*** is that of the actions, which determines what happens when a client crosses the Maxretry threshold.

First of all, the ban, which happens as a temporary configuration of iptables:

`banaction' = iptables-multiport'

and therefore, the type of transport used to send the mail:

'mta = sendmail'

This is all, I recommend, if you have ssh boxes around, protect yourself. . . !