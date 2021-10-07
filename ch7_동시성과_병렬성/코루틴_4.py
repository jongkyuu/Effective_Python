# 코루틴_4.py

import asyncio
 
async def hello():    # async def로 네이티브 코루틴을 만듦
    print('Hello, world!')
 
loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(hello())    # run_until_complete에 코루틴 객체를 넣음. 네이티브 코루틴을 호출하면 코루틴 객체가 생성됨. hello가 끝날 때까지 기다림
loop.close()                        # 이벤트 루프를 닫음