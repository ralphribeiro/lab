import asyncio
from os import mkdir
from os.path import dirname, exists, join as p_join
from requests import get
from shutil import rmtree
from urllib.parse import urljoin

from aiofiles import open as aopen
from aiohttp import ClientSession


base_url = 'https://pokeapi.co/api/v2/'
pokemons = get(urljoin(base_url, 'pokemon/?limit=20')).json()['results']

folder_name = 'sprites'
_path = p_join(dirname(__file__), folder_name)

if exists(_path):
    rmtree(_path)
mkdir(_path)


async def write_file(session, url, name):
    async with session.get(url) as response:
        print(f'baixando: {url.rsplit("/")[-1]}')
        async with aopen(f'{name}.png', 'wb') as f:
            content = await response.content.read()
            await f.write(content)


async def fetch(session, url, name):
    async with session.get(url) as response:
        result = await response.json()
        sprite_url = result['sprites']['front_default']
        await write_file(session, sprite_url, p_join(_path, name))


async def main():
    tasks = []
    async with ClientSession() as session:
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            task = asyncio.ensure_future(fetch(session, url, name))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)
