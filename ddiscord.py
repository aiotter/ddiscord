import discord
import readline
import asyncio
import textwrap
import traceback
import sys
import io
import os
import platform
from code import compile_command
from contextlib import redirect_stdout
from pathlib import Path


async def run_debugger(client: discord.Client):
    print('Connecting to discord...', end='', flush=True)
    await client.wait_until_ready()
    print(f'\rLogged in as {client.user} ({client.user.id})')
    print('You can refer to your Client instance as `client` variable. '
          'i.e. client.guilds', end='\n\n')

    global env
    env = {'client': client}
    env.update(globals())

    while True:
        try:
            try:
                body = await client.loop.run_in_executor(None, input, '>>> ')
                while not compile_command(f'async def func():\n{textwrap.indent(body, "  ")}'):
                    body += '\n' + await client.loop.run_in_executor(None, input, '... ')

            except (EOFError, KeyboardInterrupt):
                try:
                    await client.logout()
                except asyncio.CancelledError:
                    pass
                finally:
                    break

            if not body:
                continue

            # 実行するコード内部で作成された変数を env に代入
            _local_env = {}
            body = body + '\nglobal env\nenv.update(locals())'

            # 標準出力に何も出力しない式を実行した場合、式の返り値を表示するように準備
            source = f'async def func():\n{textwrap.indent(body, "  ")}'
            source_with_return = f'async def func():\n{textwrap.indent("return " + body, "  ")}'

            try:
                exec(source_with_return, env)
            except SyntaxError:
                exec(source, env)
            func = env['func']

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                retval = await func()
            if stdout.getvalue():
                print(stdout.getvalue(), end='')
            elif retval:
                print(repr(retval))

        except Exception:
            traceback.print_exc()
            continue


def get_token():
    token = None
    token_path = Path('./token')
    token_env = os.environ.get('DISCORD_TOKEN')

    if len(sys.argv) > 1:
        if sys.argv[1] == '-':
            token = input()
        else:
            token = sys.argv[1]

    elif token_path.exists():
        token = token_path.read_text().rstrip()

    elif token_env:
        token = token_env

    print(f' - Debugger for discord.py - ')
    print(f'Running on Python {platform.python_version()}. ', end='')
    if os.name == 'posix':
        print('Send EOF (Ctrl-D) to exit.')
    elif os.name == 'nt':
        print('Send EOF (Ctrl-Z) to exit.')
    else:
        print('Send EOF to exit.')

    if not token:
        token = input('Input your token: ')

    return token


def main():
    token = get_token()
    client = discord.Client()
    client.loop.create_task(run_debugger(client))
    client.run(token)


if __name__ == '__main__':
    main()
