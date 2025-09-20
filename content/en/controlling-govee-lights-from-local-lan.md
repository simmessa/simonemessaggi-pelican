---
date: 2025-09-20
title: Controlling Govee lights from your LAN in Home Assistant
slug: control-govee-lights-local-lan-home-assistant
lang: en
cover: images/govee_lan_led_light_dbz_lookalike.jpeg
author: simmessa
status: published
category: none
tags: Govee, Led lights, Home Assistant, DIY, Home automation, Tech
---

I'm a big fan of Govee lights ([this](https://amzn.to/3KcybEE) is the latest I've bought, and it's excellent), they're cheap, work well and you can also integrate them with your home automation.

By the way, I'm using home assistant to control my smart home.

## API key from China?

I used to apply for an API key in order to interact with the Govee ecosystem, Govee are more than happy to hand out API keys to interact with their cloud services but in my experience they sometimes fail or the Home Assistant extensions stop working and in that case, it's a mess.

Finally someone at Govee understood this and decided to enable a feature on some of their products (the most recent ones, to be fair) that would make life slightly easier for the smart home owners: **local LAN control** of Govee lights!

## What extension in Home Assistant?

There are many integrations for Govee light control, and I found this pretty confusing at first, so here's a list:

- Govee on HACS [link](https://www.home-assistant.io/integrations/govee_light_local) now discontinued :(
- GoveeLife [link](https://github.com/disforw/goveelife) which seems more of a _work in progress_ at the moment
- Govee LAN control [link](https://www.home-assistant.io/integrations/govee_light_local) / [link](https://github.com/home-assistant/core/tree/dev/homeassistant/components/govee_light_local) last commit about 1 year ago :(
- Govee MQTT [link](https://github.com/wez/govee2mqtt) last commit about 5 months ago :S

It's quite messy, I know, and if you care about integrations that are properly maintained, the situation looks a bit dire I'm afraid.

After a bit of struggle I decided to go with GoveeMQTT which should be preferable to Govee LAN control (both from the same author). At the same time I stopped using the original Govee integration found on HACS, which had issues from time to time. Smart life is complicated, you know :|
This choice also appeared as the best one since Govee LAN control doesn't even work with recent home assistant versions (the issue is very similar to this one here: [issue](https://github.com/LaggAt/hacs-govee/issues/234))

## Docker install

I run everything on Docker in my home lab, so I started from this guide:
[Docker.md](https://github.com/wez/govee2mqtt/blob/main/docs/DOCKER.md)

```yaml
version: '3.8'
services:
  pv2mqtt:
    image: ghcr.io/wez/govee2mqtt:latest
    container_name: govee2mqtt
    restart: unless-stopped
    env_file:
      - .env
    # Host networking is required
    network_mode: host
```

And converted to something that would run on k8s, for my convenience.

Keep in mind an .env file is required to set a bunch of env variables, older versions also used a _config.yaml_ file but recent ones don't need it so don't bother.

Is this able to control from LAN? Well, let me cite the project developer, when he speaks about the project features:

_Robust LAN-first design. Not all of Govee's devices support LAN control, but for those that do, you'll have the lowest latency and ability to control them even when your primary internet connection is offline._

So, that's basically what we're looking for, great news!

After you have installed and run the docker container and you're sure it's up and running with the config.yaml you just created, you can install the Govee2Mqtt Add-on, here's a guide:
[Link](https://github.com/wez/govee2mqtt/blob/main/docs/ADDON.md)

This works only if you're on HAOS or HA supervised, since I don't do that, I need to use the alternative way, described here:
[Link](https://github.com/wez/govee2mqtt/blob/main/docs/DOCKER.md)

Oh, if I had a dime for every time somebody created HA integrations via Add-ons and forget to give other users a way to make'em work... but this is an example of how this can usually be figured out.

Ok, we need to add those env vars, use a .env file if that suits you, while I put them in the k8s yaml manifest, details are irrelevant here.

```yaml
# Optional, but strongly recommended
GOVEE_EMAIL=user@example.com # DON'T PUT THIS!!!
GOVEE_PASSWORD=secret # DON'T PUT THIS!!!
# Optional, but recommended
GOVEE_API_KEY=UUID

GOVEE_MQTT_HOST=mqtt
GOVEE_MQTT_PORT=1883
# Uncomment if your mqtt broker requires authentication
#GOVEE_MQTT_USER=user
#GOVEE_MQTT_PASSWORD=password

# Specify the temperature scale to use, either C for Celsius
# or F for Fahrenheit
GOVEE_TEMPERATURE_SCALE=C

# Always use colorized output
RUST_LOG_STYLE=always

# If you are asked to set the debug level, uncomment the next line
#RUST_LOG=govee=trace

# Set the timezone for timestamps in the log
TZ=America/Phoenix
```

You should absolutely avoid putting your govee credentials in the env, or it might not even work (see [issue](https://github.com/wez/govee2mqtt/issues/141#issuecomment-1957655671)).

Come on this addon has pretty bad issues with docs... well I guess we can't complain given it's free and it works in the end, we're almost there!

One of the good news is that the MQTT devices will be auto discovered on Home Assistant, provided that you have the MQTT integration installed, that is. If you don't already have it you really should, trust me.

Ok, it's not really well documented but the docker container will also expose a decent enough HTTP interface, here's an example:

![Govee MQTT gui](/images/govee_lan_gui.png)

I especially like the fact that you can check what's being controlled via LAN API vs Govee (somewhat unreliable) cloud.

That's all, I hope your govee experience will be smooth as mine (or even smoother :) )
