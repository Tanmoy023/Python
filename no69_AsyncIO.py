import asyncio
import requests

async def func1():
    url = "https://staticg.sportskeeda.com/editor/2020/06/01db3-15926544320058-800.jpg"
    response = requests.get(url)
    open("no96Img1.png","wb").write(response.content)
    print("func1() is completed")

async def func2():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSg6nhRfybXVe81LzGx_GKcEXWVwoL_aW2lOQ&s"
    response = requests.get(url)
    open("no96Img2.jpg","wb").write(response.content)
    print("func2() is completed")

async def func3():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSj5pkjWWZH-FIs-wlVweopA5hA-M-xeKkxyw&s"
    response = requests.get(url)
    open("no96Img3.jpg", "wb").write(response.content)
    print("func3() is completed")

async def main():
    l = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(l)

asyncio.run(main())
