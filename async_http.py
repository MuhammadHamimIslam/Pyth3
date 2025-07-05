import asyncio
import aiohttp

async def get_data(url):
    async with aiohttp.ClientSession() as session: 
        async with session.get(url) as response: 
            print("Status = ", response.status) # prints status code
            print("Content type = ", response.headers["Content-Type"]) # prints the content type
            html = await response.text()
            print(html)

asyncio.run(get_data("https://httpbin.org/get"))
