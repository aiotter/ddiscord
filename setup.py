from setuptools import setup
from pathlib import Path

here = Path(__file__).parent

with (here/'README.md').open(encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ddiscord',
    version='0.2.1',
    description='Debugger for discord.py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aiotter/ddiscord',
    author='aiotter',
    author_email='ogran.std@gmail.com',
    license='MIT',
    python_requires='>=3.6, <4',
    py_modules=['ddiscord'],
    install_requires=['discord.py>=0.16.7'],
    entry_points={
        'console_scripts':[
            'ddiscord = ddiscord:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
