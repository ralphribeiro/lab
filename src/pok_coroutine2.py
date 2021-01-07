import asyncio
from asyncio import AbstractEventLoop
import logging
from os import mkdir
from os.path import dirname, exists, join as p_join
from shutil import rmtree
from time import perf_counter_ns
from urllib.parse import urljoin

from aiofiles import open as aopen
from aiohttp import ClientSession
from requests import get

# logging.basicConfig(level=logging.INFO)

base_url = 'https://pokeapi.co/api/v2/'
pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']

folder_name = 'sprites'
_path = p_join(dirname(__file__), folder_name)

if exists(_path):
    rmtree(_path)
mkdir(_path)


def timer(func):
    def inner(*args):
        inicio = perf_counter_ns()
        r = func(*args)
        fim = perf_counter_ns()
        print(f'{func.__name__}(): {(fim-inicio)/10**6}ms')
        return r
    return inner


async def get_sprite_url(session: ClientSession, url):
    async with session.get(url) as response:
        logging.info(f'baixando url sprite: {url}')
        response.raise_for_status()
        result = await response.json()
        sprite_url = result['sprites']['front_default']
        return sprite_url


async def download_sprite(session: ClientSession, url: str) -> bytes:
    content = bytes()
    async with session.get(url) as response:
        logging.info(f'baixando: {url.rsplit("/")[-1]}')
        content = await response.content.read()
    return content


async def write_file(name: str, data: bytes):
    async with aopen(f'{name}.png', 'wb') as f:
        logging.info(f'salvando: {name}')
        r = await f.write(data)
        return r


async def get_sprites(url_sprite: str, name: str):
    async with ClientSession() as session:
        url = await get_sprite_url(session, url_sprite)
        content = await download_sprite(session, url)
        ret = await write_file(p_join(_path, name), content)
        logging.info(f'feito! {name}')


async def vai(loop: AbstractEventLoop):
    tasks = []
    for p in pokemons:
        t = loop.create_task(get_sprites(p['url'], p['name']))
        tasks.append(t)

    for task in tasks:
        await task


@timer
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(vai(loop))


if __name__ == '__main__':
    main()
