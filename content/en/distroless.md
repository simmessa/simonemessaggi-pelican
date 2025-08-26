---
date: 2019-09-1
title: Container security or how to improve security with distroless containers
lang: en
slug: distroless-containers-improve-security
cover: images/rena-1-8063.jpeg
status: published
category: Tech
Tags: Docker, Kubernetes, Distroless, Security, Talk
---

*What follows is a brief summary of a talk I composed during my collaboration with Mia Platform*

**Bio:**
My love story with computers began at 8 years, thanks to Commodore64, then I made this passion my profession.

I worked on networks, web development (back & front), such as Linux sysadm, technical project manager and I created and guided technological teams in the companies I was part of.

In recent years I have begun to adopt DevOps philosophy with great satisfaction.

I love Docker, Kubernetes and Elasticsearch.

**Job Title:**
Devops and Operation Master at Mia-Platform,

---
**Title:**
Strengthen security with distroless container

**Short Description:**
We live in the era of the container revolution and this already widespread trend will explode further in the coming years.

The containers continue to be one of the hottest trends of the moment, but if with the container we design, develop and deploy applications, why often we do not dedicate more than 5 minutes to the safety of the container?

We talk about distroless container, a promising technique created by Google with which you can limit to the maximum the attack surface of our containerized applications. We will see the main methods to realize distroless container and we will learn to:

- Analyze containers with tools to detect security vulnerabilities
- Get slender images through multi-stage builds
- Making debugging of distroless container effectively

We are in 2019, and we live now in the age of the *Container revolution*, within a few years we passed from shared hosting to VPS to the cloud and container of today.

The use of containers in production is now a "normal" and consolidated phenomenon, according to [Gartner](https://www.gartner.com/smarterwithgartner/6-best-practices-for-creating-a-container-platform-strategy/) by 2022 75% of companies will use containerized applications in production (the percentage in 2019 is about 30% and still growing).

As always happens, when new technologies emerge, the first concern is to make sure that "function" and some aspects are leaked, for this reason docker and the container have made a reputation far from good as regards the aspects of **cybersecurity.**

Many realities, due to the rush of pursuing the latest technological/informatic trend (today are the container, tomorrow...chissa'!), have left in part or entirely the safety part, and underestimated the fact that, some characteristics of isolation of the processes to which we had accustomed the VMs in the containers even exist!

If you want to see, the reduced degree of insulation offered by the container does not result from a disinterest towards the security issue but, more simply, is a feature of the containerization that serves to gain in terms of flexibility.

## Distroless container

Just to deepen the security theme, today I want to propose a technique for the safety of container that uses the approach *distroless*.

If with VMs the focus was on isolated virtual machine instances and each "dedicated" to a certain application, with the container we arrive to have almost an identity between the application itself and the container in which it turns. We come to say that **the container, at the bottom level IS the application.**

Any one of you who has taken the trouble of writing a *Dockerfile* or two knows... it's not that simple.

Because in addition to the application in the container there is a base constituted by the operating system below, light as you want, but still always present.

For my first Dockerfiles, for example, I have always entrusted myself to a base **debian*** (debian:stretch) because I had a good degree of confidence with this OS and I knew how many and which packages I could install, I also had software that was tested and stable, even if at the expense of the version number. Debian-based images easily weighed hundreds of MB but were easier to use and debug.

Then over time, I went over to the [**stretch-slim**](https://hub.docker.com/_/debian), a minimal debian distribution that however guaranteed about 80% of debian tools, in a more compact and efficient format.

Over the years, I have come to know [**Alpine**](https://hub.docker.com/_/alpine), an extremely minimal Linux distro and irresistible weight, perfect for keeping containers light and performing. Alpine is really the narrowest version of Linux on the bone I've seen, it's basically a [**busybox**](https://hub.docker.com/_/busybox) (used in the embedded world) with the addition of the apk minimal package manager. Alpine-based images tend to weigh even less than 100 MB which involves a good gain in bandwidth and time savings.

Distroless, if you want, are a step further towards efficient containers where the operating system disappears and there are only the minimum libraries needed to run our application.

This technique is not new, but exists for a few years and has been introduced by Google, which has long been in the situation of having many containerized applications deployed in production.

In a nutshell, a distroless container does without the operating system and contains only the linux kernel and the necessary libraries to the application we want to deploy. . .

## The Talk Slides

Here you'll find all the slides of this talk, in the version for the [meetup of Kubernetes Milan](https://www.meetup.com/kubernetes-milano/):

<iframe allowfullscreen="true" frameborder="0" height="569" mozallowfullscreen="true" src="https://docs.google.com/presentation/d/e/2PACX-1vQFRtZvdtt2Scc4cQM4m4vnOtn-Lvvz0OVnEBE8_hCVE05A0heatr6RG1rR-goLckrqxhPF287dL9Or/embed?start=false&loop=false&delayms=3000" webkitallowfullscreen="true" width="960"></iframe>