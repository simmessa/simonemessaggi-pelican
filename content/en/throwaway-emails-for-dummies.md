---
date: 2008-03-12
title: Self hosted throwaway emails for dummies
slug: throwaway-emails-for-dummies
lang: en
cover: images/self-hosted-throwaway-email.jpeg
author: simmessa
status: published
category: Tech
tags: Tutorial, Email, Hack
---

Do you host email on your own server? Good! Do you wanna have an email that you can give away for registrations without worrying about the endless amount of spam you'll end up getting?

Then read on, maybe this stuff is for you...

One of the simple ways in which many, if not all, of the above points can be accomplished is a very simple hack of your linux/unix config.

## Having fun with your /etc/aliases

What is an /etc/aliases file on *nix systems? it's a central repository for local usernames on your server used when dealing with email delivery.

I don't really have much to say about aliases that you couldn't find on better online resources, therefore I won't provide much explanation here.

I use postfix on my server, and I frickin' love it, it makes email setup a breeze while being very powerful.

So what's there in an aliases file? Let's find out.

Here's an exempt of an actual cat of /etc/aliases:

```
    # See man 5 aliases for format

    some_alias: some_unix_username
    some_other_alias: some_other_username
```

That's pretty simple uh?

Now the big question is, what can we accomplish through some aliases manipulation?

A lot, it's a text file after all ;)

Here's what you'll find at the end of my current alias:

```
    cut...
    #weekmail_start
    this_alias_changes_every_day: my_linux_username
    #weekmail_end
```

The concept here's pretty simple, we're going to create a different, new email every day, using some parameters that change daily, so that it won't be available for spamming at later times. The point is to make up some rule with which we are able to compute the exact email address every day.

That's when some bash scripting + linux readily available commands come into play:

```bash
    #!/bin/bash

    #need day of the week

    dotw=`date +%A`
    number=`date +%d`
    month=`date +%m`

    alias="$dotw$number$month"

    alias=`echo $alias|tr "[:upper:]" "[:lower:]"`

    if [ -z $1 ]; then
    echo "Needs filename as argument."
    exit 1
    elif [ -f "$1" ]; then
    fname="$1"
    fi

    cat $fname|sed '/weekmail_start/,/weekmail_end/d' >$fname.weekmail

    cat /sbin/weekmail|sed 's/replaceme/'$alias'/' >/sbin/weekmail_changed

    cat $fname.weekmail /sbin/weekmail_changed >$fname

    newaliases
```
## Throwaway alias logic

Ok, the steps here are pretty straightforward, but let's check'em out:

1) fill some vars with stuff that is different every day, taken from the "date" command invocation and craft your throwaway alias.
2) cut away the "weekmail" part from the current /etc/aliases (this step involves the sed editor) and save the result in a temp file.
3) take a new weekmail portion from another, static file (/sbin/weekmail in this example) and replace a known string with the freshly computed alias, then store it somewhere.
4) craft a new /etc/aliases by joining the two previously created files
5) invoke "newaliases" to make sure your new alias is activated

Now you just have to put it in your crontab with "crontab -e":

```
    10 0 * * * /path_to/your_weekmail_script /etc/aliases
```

Et Voila' ! That's some nice junk email address you have there, fresh every day!

I'm pretty sure the pros of this approach after the * wildcard catchall approach (*@yourdomain.com) are self evident...

Be sure to send me some feedback if you elaborate over this hack... my script was scratched down with fingernails on a blackboard in a hurry (took me about 10 mins) and so it oughta be the bare minimum...

Hope it turns out useful for you guys, Wish you all the best!

_p.s.: I'm republishing this ancient article (2008) from my first blog. The thing is I found it still rather enjoyable today as it was when originally published. Due to the fact that email SPAM has exploded in the last 20 years_