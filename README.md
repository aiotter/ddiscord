# ddiscord: debugger for discord.py

Powered by [discord.py](https://github.com/Rapptz/discord.py).
This help you write code on discord.py and manage your server via one-liner program.
Tested on discord.py v1.0.0 but in theory it works on v0.16.7 or later.

# How to install ddiscord
    $ python3 -m pip install ddiscord

# How to start ddiscord
There are four ways to start ddiscord, which are listed below in order of precedence.

1. Passing your token in an argument.
2. Passing your token via standard input. `-` is needed as a first argument.
3. Passing your token via the file `./token`.
4. Passing your token via environment variable `DISCORD_TOKEN`.
5. Run ddiscord first, then ddiscord will ask you the token.

Examples:

    $ ddiscord 'YOUR TOKEN HERE'
    $ echo 'YOUR TOKEN HERE' | ddiscord -
    $ echo 'YOUR TOKEN HERE' >token; ddiscord
    $ env DISCORD_TOKEN='YOUR TOKEN HERE' ddiscord

# How to use ddiscord
    $ ddiscord
     - Debugger for discord.py -
    Running on Python 3.7.2. Send EOF (Ctrl-D) to exit.
    Logged in as YourBot#0000 (012345678901234567)
    
    >>> len(client.guilds)
    1
    >>> client.user.bot
    True
    >>> await client.guilds[1].create_text_channel('test')
    <TextChannel id=012345678901234567 name='test' position=1>
    >>>


