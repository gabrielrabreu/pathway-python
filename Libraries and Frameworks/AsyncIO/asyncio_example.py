import asyncio

# Define an asynchronous function
async def say_hello(delay):
    await asyncio.sleep(delay)
    print("Hello, world!")

# Create a new event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Run the code inside the event loop
loop.run_until_complete(say_hello(2))

# Close the event loop
loop.close()
