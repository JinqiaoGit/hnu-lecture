import asyncio
import time


async def func4(key='abc', during=1):
    print(key)
    # time.sleep(3)
    await asyncio.sleep(during)
    print(key)


start = time.time()
asyncio.run(asyncio.wait([func4(key='async 1', during=3), func4(key='async 2', during=1), func4(key='async 3', during=2)]))
print(time.time() - start)
