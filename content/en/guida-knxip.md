---
date: 2015-12-31
title: Guide to the KNXnet/IP protocol i.e. KNX over IP
slug: guide-knxnet-over-ip-protocol
lang: en
cover: images/knxiprouterinterfaceoverlay.png
status: published
category: Tech
tags: IOT, Home automation, KNX
---

*Today (original article published on 31 December 2015 at Simmessa.com) I came across a useful English tutorial explaining how the KNX protocol works IP or KNX over IP, for those of you who did not know it, we are talking about Konnex, that is one of the most popular protocols for home automation and home automation, find more info about http://knx.org however the article I read seemed interesting to me and I thought to rewrite it here in Italian for those who were curious! Find the original on http://knxtoday.com/2014/01/3056/solutions-ip-and-knx-bringing-you-up-to-speed.html*

People often ask me what the limitations of KNX are and whether it is really an ancient system, even considering that it was thought almost 20 years ago.
One of the most used data in this debate is the relatively low speed of the KNX bus, with a baud rate of 9600bps, and the fact that many modern systems can communicate at speeds thousands of times faster.

But what is sometimes not considered is that at 9600bps the bus can get very long with a free topology and low consumption of connected devices.

At this baud rate, let's not forget that our bus can support up to 50 telegrams per second!

However, with the progress in using KNX there is certainly a need for greater speed, especially at the backbone level.

With centralized video surveillance and monitoring devices that are becoming very common, there is often a requirement for all telegrams to be available at the highest topological level.

With the KNX TP1 bus cable, we are therefore in the presence of a bottleneck, which IP can solve.

To support this protocol (IP) the KNX group has developed the KNX/IP telegram, now an official part of the KNX specifications. This allows us to use Ethernet as a cheap alternative and broadband to the old bus. We also have the advantage that Ethernet is already present in many residential and commercial buildings.

But it is important to understand that if LAN networks also have many benefits, the requirements of having a controlled and defined infrastructure need to maintain KNX TP1 as a basis.

![The KNX TP1 cable](/images/KNX-cable.jpg)
*fig.1 - The KNX TP1 cable*

## The KNX/IP telegram

To allow the inclusion of the IP protocol as a means of communication, the KNX group has created a standard KNX/IP telegram.

This is based on the OSI reference model that defines transport, network and physical levels.

To simplify this allows us to define how to distribute TP1 telegrams in the presence of IP networks.

The TP1 telegram is maintained, but an additional field is used to define the KNXnet/IP action, which can implement one of the following services:

* KNXnet/IP Core
* KNXnet/IP Device Management
* **KNXnet/IP Tunnelling**
* **KNXnet/IP Routing***
* KNXnet/IP Remote Logging
* KNXnet/IP Remote Configuration and Diagnosis
* KNXnet/IP Object Server

Most of these services are self-maintained and do not require our intervention, so it will be important for us to focus on the two highlighted above, **tunnelling and routing.**

## KNXnet/IP Tunnelling

The simplest mode, as well as the main one to interface with a KNX system, and allows point-to-point communication (unicast) between a single external device and the KNX system, the operation is completely analogous to using USB or a serial interface!

It’s the simplest form of communication for KNX over IP and it’s easy to understand why, as it’s enough to point a device to its IP address of the KNX IP card.

This allows us to see all bus traffic and communicate directly with each device for example for ETS programming.
It is also commonly used to communicate external systems with KNX.

Note: In ETS this method is simply defined as KNX/net IP

## KNXnet/IP Routing

Here we have a multicast-based telegram, so a KNX IP router will work from line or coupler area. By doing so we make the backbone of an ethernet-based KNX system, with higher transmission speed and installation flexibility!

The IP router will also manage the filter table to manage traffic ( congestion, etc.) where necessary.

Clearly, being multicasts, we have that to contact multiple devices we will aim at a standard multicast address, in which way we have a communication one to many, the KNX association has reserved the address of multicast 224.0.23.12 for convenience but any other address can be used, as long as it is laid on all devices.

![We use an IP router like backbone and line coupler](/images/KNX-IP-network.jpg)

*fig.2 - We use an IP router like backbone and line coupler*

With the KNXnet/IP routing we have a communication method that allows all traffic on the bus to be monitored, this is very useful in all cases where the devices require access for example to the display systems, but the disadvantage is that it does not allow to perform ETS functions as a bus monitor or download on the devices.

## What hardware do I need?

Given the main communication methods, let's take a look at the products we need to make a KNX system on IP.

The main devices we need will be interfaces (IP network cards) and routers.

**The KNX interfaces IP*** only support the KNXnet/IP tunnelling communication method, despite a single interface, such as the Weinzierl 730, can support multiple connections.

This card in fact manages up to 5 simultaneous connections that are obtained by defining multiple KNX physical addresses on the device.

Obviously this technique is very useful as we have multiple instances of ETS accessing the same KNX system or if we want to use the interface for both an ETS connection and an external board for an Audio/Video system, for example.

**The KNX IP** routers, on the contrary, support both methods of tunnelling and KNXnet/IP routing, as well as manage the filter tables that allow the device to function as coupler.

In fact, some IP routers, such as the Gira 216700, allow multiple tunnelling connections (such as interfaces).

The routing, however, by its very nature, has no limits to the number of connections that it is able to establish through the multicast protocol.

Some devices also have time servers and memory cards to record the bus.

![This is the router KNXnet / IP Gira 2167 00](/images/Gira-KNX-IP-router.jpg)
*fig.3 - This is the router KNXnet / IP Gira 2167 00*

**Please note:***

**It is very important that we remember to treat this device as a line coupler, it must be addressed correctly in our network topology, and the Medium types of all segments must be properly assigned to ETS.**

Both devices we have seen, tabs and routers generally require a voltage higher than (24V) KNX bus. This can usually be provided by the aux voltage of many PSU KNX, but we remember that generally a PSU KNX offers a maximum output of 640mA.

To avoid risk, it is better to run each device with its dedicated PSU, or, alternatively, use the Power over Ethernet (PoE) protocol if our switch allows it, the cost of the switch could increase, but the installation simplifies considerably!

## Security and remote access

Once we have implemented an IP solution, you can configure one of the above types of connection for remote access.

Using a tunnelling interface, we can establish an external direct connection if we know the WAN address. It will need a port redirection on the router to cross the firewall, however, since the KNX system does not require a password to be used, it is not the safest method. This consideration is important if a KNX system controls an entire building, for obvious security reasons!

If we needed to connect two KNX systems with KNXnet/IP routing, the VPN must necessarily support multicast traffic and have this grant from the system administrator.

## Conclusion

Considered everything, it is not strange at all for us to receive a lot of questions about KNX IP, also because it does not talk much about it during the certification KNX.

Once the above terms are understood, however, it becomes much easier to specify and install the correct products. By combining the speed and flexibility of the IP protocol with the reliability and simplicity of the KNX bus we get a very powerful, flexible and ready-to-wear system.

*The original English article written by Mark Warburton is available at:
http://knxtoday.com/2014/01/3056/solutions-ip-and-knx-bringing-you-up-to-speed.html*

**Translated by yours truly, Simone Messaggi.**