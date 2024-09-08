# - Note: its under development

# Winkicord

**Effortlessly create a fully functional Discord music bot with just one line of Python code.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

Winkicord is a Python package that allows you to quickly create a Discord music bot with minimal effort. With just one line of code, you can get a music bot up and running in your Discord server. It's built on top of `discord.py`, so it's fully compatible with existing Discord bots.

## Features
- Play music from YouTube or other sources
- Pause, stop, and queue functionality
- Easy to integrate into existing bots
- Simple and minimalistic API

## Installation

Make sure you have Python 3.9 or higher installed. Then, you can install `winkicord` via `pip`:

```bash
pip install winkicord
pip install discord.py
```


```bash
import discord
from discord.ext import commands
import winkicord

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await winkicord.NodePoolCreds.set_creds(
        host="localhost",
        port=2000,
        identifier="localhost",
        password="youshallnotpass",
        inactive_timeout=14000,
        cache=130
    )
    await bot.load_extension('winkicord.music')

bot.run("YOUR_BOT_TOKEN")


**Note: This Library requires lavalink v4 [lavalink-support](https://discord.gg/lavalink-1082302532421943407)**