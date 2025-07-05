import asyncio

# asynchronous function (CoroutineObject)
# asynchronous function starts with async keyword 
async def say_hello() -> asyncio.coroutines:
    print("Hello Everyone!")

# to run a asynchronous function, we need asyncio.run(function())
asyncio.run(say_hello())

# using await 
# await only can be used inside the async function 
async def get_data(delay, no):
    print(f"Getting data for no {no}")
    await asyncio.sleep(delay) # set a delay to simulate getting data
    print(f"Got data for no {no}")
    return {"data": "abcd", "no": no}
    
async def show_result():
    task1 = get_data(2, 1) # creates task
    task2 = get_data(3, 2)
    
    # waiting for task to execute
    result1 =  await task1
    result2 = await task2
    
    # print result 
    print(result1)
    print(result2)

asyncio.run(show_result())

# creating tasks 
async def tasks(): 
    # creates tasks to be executed 
    task1 = asyncio.create_task(get_data(1, 1))
    task2 = asyncio.create_task(get_data(3, 2))
    task3 = asyncio.create_task(get_data(2, 3))
    
    # waiting for being executed 
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1)
    print(result2)
    print(result3)

asyncio.run(tasks())

# task gather
async def tasks_gather(): 
    # creates tasks to be executed 
    task = asyncio.gathet(get_data(1, 1), get_data(3, 2), get_data(2, 3)) # gather all tasks 
    
    # wait to be executed 
    result = await task
    
    print(result)

asyncio.run(tasks())

# task group 
async def tasks_group(): 
    all_tasks = []
    
    # task group 
    async with asyncio.TaskGroup() as tg: 
        for delay, no in enumerate([1, 3, 2], start=1):
            tsk = tg.create_task(get_data(delay, no))
            all_tasks.append(tsk)
    
    results = [task.result() for task in all_tasks]
    
    for result in results: 
        print(result)
    
asyncio.run(tasks_group())
