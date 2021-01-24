import asyncio
import logging
from os import mkdir
from os.path import dirname, exists
from os.path import join as p_join
from shutil import rmtree
from time import perf_counter_ns
from urllib.parse import urljoin

from aiofiles import open as aopen
from aiohttp import ClientSession
from requests import get


# logging.basicConfig(level=logging.INFO)

base_url = 'https://pokeapi.co/api/v2/'
n_poks = 250
poks = get(urljoin(base_url, f'pokemon/?limit={n_poks}')).json()['results']

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


async def get_sprite_url(session: ClientSession, url: str) -> str:
    async with session.get(url) as response:
        logging.info(f'baixando url sprite: {url}')
        response.raise_for_status()
        result = await response.json()
        return result['sprites']['front_default']


async def download_bin(session: ClientSession, url: str) -> bytes:
    async with session.get(url) as response:
        logging.info(f'baixando: {url.rsplit("/")[-1]}')
        return await response.content.read()


async def save_file(name: str, data: bytes) -> int:
    async with aopen(f'{name}.png', 'wb') as f:
        logging.info(f'salvando: {name}')
        return await f.write(data)


async def pipe_sprt(url_sprite: str, name: str):
    async with ClientSession() as session:
        url = await get_sprite_url(session, url_sprite)
        content = await download_bin(session, url)
        ret = await save_file(p_join(_path, name), content)
        logging.info(f'feito! {name}, {ret} bytes')


async def processing():
    tasks = [asyncio.create_task(pipe_sprt(p['url'], p['name'])) for p in poks]
    for task in tasks:
        await task


@timer
def main():
    asyncio.run(processing())


if __name__ == '__main__':
    main()
