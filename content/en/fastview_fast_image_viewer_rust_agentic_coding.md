---
date: 2026-03-11
title: Introducing Fastview - a fast image viewer built for speed code in Rust (by agents)
slug: fastview-fast-image-viewer-rust-agentic-coding
lang: en
cover: images/introducing_fastview.webp
author: simmessa
status: published
category: Tech
tags: Rust, AI
---

Fun facts about this post:

1. I don't know the Rust programming language (not even the hello world thing, I have produced zero lines of Rust in my life)
2. I was tired of slow bloated image viewers on Windows

_Have you ever felt the same way?_

Starting from these premises, I decided to try my luck with coding agents, and I must say I'm a bit surprised with the results...

## Tools used

I started this in Google's own [Antigravity](https://antigravity.google), if I remember correctly. It's an incredible tool for agentic coding. Too bad it's so limited in its free usage, you're definitely gonna run out of credits before completing anything even remotely useful.

And if you're like me, you don't wanna be too dependent of AI agents running somewhere else than your homelab, plus I'm cheap.

That's what made me a proud owner of a Strix Halo (funky name for [AMD AI MAX+ 395](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html)) PC, therefore my next step was pretty predictable, switch to local LLM and continue the agentic coding there.

I've had a mixed experience with the [Cline](https://cline.bot) VSCode extension, it's not bad, but it's not as good as a dedicated IDE, and VSCode extension generally are a PITA to use because... too many reasons.

![My agentic friend OpenCode](/images/opencode.jpg)

So I switched to [OpenCode](https://opencode.ai) and besides being free and [open source](https://github.com/anomalyco/opencode), **DAMN**, it's good!

Not the cli / TUI (Text User Interface) one tho, I'm not a big fan of TUI tools for productivity and you know how I love hitting hard on keyboards. Do I need to provide [proof](https://www.simonemessaggi.it/2020/12/en/my-brief-history-mechanical-keyboards-part1/)?
I'm talking 'bout the windows version, I like the convenience of proper graphics. I know, I'm such a lazy bastard and not _sysadmin from hell_ enough, take that for granted.

Well OpenCode desktop main perk is that it's very agentic coding oriented, and completely removes the editor part from the equation.

_You can look, but you can't touch, that's OpenCode rule #1._

## Vibe coding but not done by yours truly

Yes, as I admitted in the foreward, I don't know crap about Rust, except maybe for the very [basic specs](https://en.wikipedia.org/wiki/Rust_(programming_language)#:~:text=It%20is%20noted%20for%20its,%2C%20concurrency%2C%20and%20memory%20safety.&text=Rust%20supports%20multiple%20programming%20paradigms,data%20types%2C%20and%20pattern%20matching.):

- it's a compiled language
- puts emphasis on performance
- it's type and memory safe
- can do concurrency pretty well

I hear you asking: Why does this make Rust ideal for an image viewer?

Well it's fast and modern and **compiled**.

Let's dive a bit into the "compiled" part, it looks like I am not alone in asking agents to write Rust code, because, with compiled languages, there's an (not so) hidden benefit:

_A compiled language will get rid of the most blatant errors made by AI during coding._

Wanna know what others think about this? Check [this blog](https://aarambhdevhub.medium.com/why-im-exploring-agentic-ai-in-rust-and-you-should-too-916f2ac6c413) or also [this post on reddit](https://www.reddit.com/r/vibecoding/comments/1ncrn2y/is_it_me_or_is_rust_the_ultimate_vibe_coding/).

## What features for an image viewer which might as well be the anti-image viewer?

I've tried a bunch of image viewers on Windows since I got on Windows 10 and 11 and I think they're mostly bad.

### The Windows bundle: Paint and Photos and...

I don't wanna get mad but... is it so hard to come up with some fast and easy image viewer embedded in your host OS ???

It's **very hard**, apparently.

#### PAIN-t

Paint has been restyled for this new century and... it still sucks big time, it doesn't help that it's not made for viewing, mostly for editing, but it fails as an editor and OF COURSE it has Copilot because... why not?!?

And, it uses the ribbon interface, the single worst idea in the history of modern computing, ever.

![Paint has ribbons, and fails](/images/paint_a_ribbon.png)

#### What about Photos?

Well, if there's a decent one in the Microsoft OS bundle, maybe this is the one... oh wait, it turns out [it's not!](https://www.pcworld.com/article/2456238/this-windows-programme-secretly-eats-up-resources-how-to-switch-it-off.html)

Well the same story applies here, add features, add Copilot, don't optimize, add the kitchen sink and espresso machine... make it unusable, CHECK.

Don't trust me? I understand, here, [LET ME GOOGLE THAT FOR YOU](https://letmegooglethat.com/?q=why+the+windows+photos+app+is+so+slow%3F).

#### Wait, there's the snippet app too!

Yes, the one that comes up with WIN + SHIFT + S and takes marvelous screenshots, well, it's not a viewer, it's just for screenshots, nothing to see here, go away and don't ever try to use this OS your way again!

![Oh, I love taking snippets of the Snipping Tool!](/images/snipping_tool.jpg)

Well, honestly it's not so bad as a viewer and you can even take notes on it but it's not really targeted for our usage isn't it?

### Third party apps

I've tried a bunch of third party image viewers.

I'm still fond of what Google did with Picasa a long time ago, wonderful vision and the will to go with it in a time when Google didn't seem a little bit EVIL. 

_Looks like last century right? THAT'S BECAUSE IT IS_

Google was founded in 1998, Picasa was originally published by Lifescape in 2002, before the big G acquired them and made them collapse in a black hole, so, lots of old century vibes.

![Picasa, discontinued in 2016](/images/picasa.jpg)

Oh, and Picasa was eventually discontinued in 2016. Great news for the [Killed by Google](https://killedbygoogle.com) graveyard!

Generally speaking, e lot of the good and fast image viewers are ancient:

- [Acdsee](https://www.acdsee.com/en/index/?srsltid=AfmBOopS4ObAa_TU8KwGl5_bNmEnYy6HqaMoQaOonQoB1gD3ZaZQwPsx) now makes AI and photo/video editing suites
- [FastStone](https://www.faststone.org) image viewer is incredibly still mantained, has a shareware license, but I couldn't convince myself to try it
- [IrfanView](https://www.irfanview.com) is also still there, looks very dated, I don't really have fond memories of it
- [ImageGlass](https://imageglass.org), I had my expectations high for this one, a new kid on the block, but it failed to deliver, way too naggy with updates, features I don't want and use, oh, and the UI is an absolute mess IMO

This bitter aftertaste left me with an amazing new opportunity, code my own or, better yet, ask some AI agents nicely to do it on my behalf

## Enters the Fastview

Ok, you can find [Fastview on my Github](https://github.com/simmessa/fastview), it's free and released with a permissive MIT release, which is kind of a requirement in the agentic coding world, it seems.

The [Releases](https://github.com/simmessa/fastview/releases) page at the time of writing has 3 versions, up to [v0.2.1](https://github.com/simmessa/fastview/releases/tag/v0.2.1) where you can download the Windows AMD64 binary (sorry Arm lovers).

You can bet your agentic ass there's gonna be more releases during the course of the year, as I plan to make the agents work even harder :D

The app's pretty basic, the goal here is speed and ease of use, with NO configurability whatsoever:

- there's no icon in the GUI (except for a yellow folder "slab")
- will open standard file types: jpg, png, webp
- controls are basic, arrows, backspace for navigation, esc to exit, yep, OLD SCHOOL
- mouse will pan, wheel zoom, not much else
- there's inbuilt help, a single screen with a list of keybindings, HARDCORE
- the app's gonna use your disk for cache, relevant portions of it, the goal here's speed, not saving space
- since we live in a AI gen world, there's a prompt detection feature from metadata, it's not perfect but it might work
- exif data is also read, with auto rotation
- you can navigate folders inside the app so that you don't waste your time in Explorer
- useful informations show in the title bar
- the app will open a single instance only, by design
- if already open in bg, the app is faster, but I'm not yet forcing you to a bg demon, for now.

## Time to test my claims

Here's the project link [binary](https://github.com/simmessa/fastview/releases/download/v0.2.1/fastview_v0.2.1.zip), but does it live up to the hype?

Well, it's fine for casual usage, and I've been using it for all my image viewing on my PC since the first usable build (v0.1) so I'm pretty satisfied with the results.

_Is it a clean, uber optimized, incredibly well thought Rust app? NOPE._

![Here, have some butter outdated screenshot](/images/fastview_butter_screenshot.jpg)

I don't need that, I just wanted an independent solution to my problem, and have fun with coding agents, and I'm pleased with the outcome, as usual YMMV.

So, if you dare try something that has been produced by the seemingly innocuous but soon to become out overlords, go on. Feel free to star the repo or follow if you'd like future updates.

That's all, happy image viewing everybody!