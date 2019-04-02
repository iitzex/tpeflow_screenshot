import asyncio
import time
import os

from pyppeteer import launch

SCREENSHOT = 'screenshot'

async def capture():
    # browser = await launch()
    browser = await launch(headless=True, executablePath='/usr/bin/chromium-browser') 

    page = await browser.newPage()
    await page.setViewport({'width': 850, 'height': 600})
    addr = 'https://tpeflow.herokuapp.com/'
    ts = int(time.time())

    await page.goto(addr)
    await page.screenshot({'path': f'{SCREENSHOT}/tpeflow2_{ts}.png'})
    await browser.close()


if __name__ == "__main__":
    if not os.path.isdir(SCREENSHOT):
        os.mkdir(SCREENSHOT)

    while(True):
        asyncio.get_event_loop().run_until_complete(capture())
        time.sleep(300)
