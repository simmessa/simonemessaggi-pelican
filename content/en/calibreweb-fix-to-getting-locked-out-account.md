---
date: 2025-09-08
title: Calibre-web, how to fix being locked out and reset password from shell
slug: calibre-web-fix-account-lockout
lang: en
cover: images/calibre-web-cover.jpeg
author: simmessa
status: published
category: tech
tags: eBook, Selfhosted, Howto
---

I totally love [Calibre-web](https://github.com/janeczku/calibre-web/), over the years it's become my go to repository / archive for everything from webcomic to eBooks that I've download from the web.

Here's an example screenshot:

![Calibre-web gui](/images/calibre-web-gui.png)

Pretty cool huh? you can do everything from shelving your books in categories, join books from a collection, edit your review, load metadata from the internet, and the list goes on... here's what listed on the github page:

- Modern and responsive Bootstrap 3 HTML5 interface
- Full graphical setup
- Comprehensive user management with fine-grained per-user permissions
- Admin interface
- Multilingual user interface supporting 20+ languages ([supported languages](https://github.com/janeczku/calibre-web/wiki/Translation-Status))
- OPDS feed for eBook reader apps
- Advanced search and filtering options
- Custom book collection (shelves) creation
- eBook metadata editing and deletion support
- Metadata download from various sources (extensible via plugins)
- eBook conversion through Calibre binaries
- eBook download restriction to logged-in users
- Public user registration support
- Send eBooks to E-Readers with a single click
- Sync Kobo devices with your Calibre library
- In-browser eBook reading support for multiple formats
- Upload new books in various formats, including audio formats
- Calibre Custom Columns support
- Content hiding based on categories and Custom Column content per user
- Self-update capability
- "Magic Link" login for easy access on eReaders
- LDAP, Google/GitHub OAuth, and proxy authentication support

You can even read books directly from the web interface, but I must admit the resulting experience is everything but stellar...

I run my own via docker container, using the image provided by the excellent [linux-server](https://docs.linuxserver.io/images/docker-calibre-web). Setup is pretty straightforward

```bash
docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e DOCKER_MODS=linuxserver/mods:universal-calibre `#optional` \
  -e OAUTHLIB_RELAX_TOKEN_SCOPE=1 `#optional` \
  -p 8083:8083 \
  -v /path/to/calibre-web/data:/config \
  -v /path/to/calibre/library:/books \
  --restart unless-stopped \
  lscr.io/linuxserver/calibre-web:latest
```

And I love the fact this is a single container without a separate db or anything like that, it's very selfhosting friendy and easy to use.
## The lockout problem

Let's say you're logging in from mobile and you accidentally click on the "Forgot Password?" button...

![Don't click the forgot password button](/images/calibre-web-forgot-password.png)

And well, by design calibreweb will then set a *random password* for the user you selected and send it via email to the email address linked to that user.

_Except that your calibreweb install might not be allowed to send email in ANY WAY_

I know that's what mine does, as I don't let docker containers send mail in normal conditions.

_WELL, You just LOCKED yourself out of your calibre-web instance my friend :/_

Is there a way we can fix this without re-creating the calibre-web instance from scratch?
## Solution: reset that password from inside

Assuming that you're using docker, enter the calibreweb container:

```bash
docker exec -it calibre-web bash

#now that you're in just run this command:
root@xxx:/app/calibre-web# python3 cps.py -s myuser:myvery_STRONG_password789
Password for user 'myuser' changed
root@xxx:/app/calibre-web#
```

And that's all! You should now be able to login with your user and the new password.

_p.s.: Thanks to this Reddit thread for the info: [https://www.reddit.com/r/Calibre/comments/v4h16j/calibreweb_for_some_reason_i_can_no_longer_log_in_](https://www.reddit.com/r/Calibre/comments/v4h16j/calibreweb_for_some_reason_i_can_no_longer_log_in)_