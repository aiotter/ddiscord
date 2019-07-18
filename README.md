ddiscord: debugger for discord.py
=====

Powered by [discord.py](https://github.com/Rapptz/discord.py).
This helps you write code for discord.py and manage your server via one-liner programs.
Tested on discord.py v1.0.0 but in theory it works on v0.16.7 and above.

## Usage
    $ ddiscord
     - Debugger for discord.py -
    Running on Python 3.7.2. Send EOF (Ctrl-D) to exit.
    Logged in as YourBot#0000 (012345678901234567)
    You can refer to your Client instance as `client` variable. i.e. client.guilds
    
    >>> len(client.guilds)
    1
    >>> client.user.bot
    True
    >>> await client.guilds[0].create_text_channel('test')
    <TextChannel id=012345678901234567 name='test' position=1>
    >>> for channel in client.get_all_channels():
    ...     if channel.name == 'test':
    ...         await channel.send('announcement test!')
    ... 
    >>>

## Installation
    $ python3 -m pip install ddiscord

## Logging On
There are four ways to log into your bot in ddiscord. They are listed below in look up order.

1. Passing your token as an argument.
2. Passing your token via standard input. `-` is needed as a first argument.
3. Storing your token in a file named `token` in the current directory.
4. Passing your token via environment variable `DISCORD_TOKEN`.
5. Run ddiscord first, then ddiscord will ask you the token.

Examples:

    $ ddiscord 'YOUR TOKEN HERE'
    $ echo 'YOUR TOKEN HERE' | ddiscord -
    $ echo 'YOUR TOKEN HERE' >token; ddiscord
    $ env DISCORD_TOKEN='YOUR TOKEN HERE' ddiscord
