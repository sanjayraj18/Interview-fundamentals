# async def
# async def defines an asynchronous function. Calling it creates a coroutine object; its body does not execute immediately.
async def greet():
    print("Hello")

coroutine = greet()
print(coroutine)  # <coroutine object greet ...>


# Run it using asyncio.run():
import asyncio
async def greet():
    print("Hello")

asyncio.run(greet())


# await pauses the current async function until another async operation finishes. During the wait, the event loop may run other tasks
import asyncio

async def get_data():
    await asyncio.sleep(2)
    return "Data received"


async def main():
    result = await get_data()
    print(result)


asyncio.run(main())


# asyncio.gather()
# asyncio.gather() runs multiple async operations concurrently and waits for all their results.
import asyncio

async def download(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")
    return name

async def main():
    results = await asyncio.gather(
        download("file1"),
        download("file2"),
        download("file3"),
    )

    print(results)

asyncio.run(main())
# Starting file1
# Starting file2
# Starting file3
# Finished file1
# Finished file2
# Finished file3
# ['file1', 'file2', 'file3']


# async def          → defines an async function
# await              → waits for one async operation and gets its result
# asyncio.gather()   → runs multiple async operations concurrently