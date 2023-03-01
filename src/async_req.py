import asyncio

from httpx import AsyncClient


async def req(name):
    url = 'http://192.168.1.4:8000'
    async with AsyncClient() as client:
        response = await client.get(url, timeout=10)
        print(name, response)
    return response


def chunked_client(num_chunks):
    semaphore = asyncio.Semaphore(num_chunks)

    async def pipe_sprt(name):
        nonlocal semaphore
        async with semaphore:
            return await req(name)
    return pipe_sprt


async def pool():
    http_chunked = chunked_client(200)
    resps = await asyncio.gather(
        *[asyncio.create_task(http_chunked(n)) for n in range(1000)])



if __name__ == '__main__':
    asyncio.run(pool())
