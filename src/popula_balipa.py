from json import dumps
from random import randint
from time import perf_counter_ns

from faker import Faker
from requests import post


fake = Faker()
Faker.seed(0)


def timer(func):
    def inner(*args):
        inicio = perf_counter_ns()
        r = func(*args)
        fim = perf_counter_ns()
        print(f'{func.__name__}(): {(fim-inicio)/10**6}ms')
        return r
    return inner


url = "http://localhost:8000/api/v1/locals"
url2 = "http://localhost:8000/api/v1/items"

# response = get(url)


def get_random_data_local():
    vol = randint(1, 1000)
    st_idx_s = chr(randint(65, 91))
    st_idx_n = randint(1, 1000)
    nd_idx_s = chr(randint(65, 91))
    nd_idx_n = randint(1, 1000)

    post_template = {"volume": vol,
                     "coordinate": f"{st_idx_s}{st_idx_n}{nd_idx_s}{nd_idx_n}"}

    yield post_template


def get_random_data_item(local_id: int):
    vol = randint(1, 1000)
    price = randint(1, 100)
    nm = fake.name()
    dsc = fake.address()

    post_template = {"name": nm,
                     "description": dsc,
                     "volume": vol,
                     "price": price,
                     "local_id": local_id
                     }

    return post_template


@timer
def main():
    # rand = get_random_data_local
    # for _ in range(1000):
    #     response = post(url=url, data=dumps(next(rand())))

    for i in range(2000):
        for _ in range(randint(1, 20)):
            rand = get_random_data_item(i)
            response = post(url=url2, data=dumps(rand))


# 19301.501008ms
# 475714.358844ms
if __name__ == '__main__':
    main()
