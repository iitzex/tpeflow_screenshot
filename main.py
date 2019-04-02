import asyncio
import time

from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    addr = 'https://tpeflow.herokuapp.com/'
    ts = int(time.time())

    await page.goto(addr)
    await page.screenshot({'path': f'tpeflow2_{ts}.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
