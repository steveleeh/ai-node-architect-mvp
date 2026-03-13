import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # 加入你在 openclaw.json 里配置过的那个本地代理
        browser = await p.chromium.launch(
            headless=True, 
            args=['--no-sandbox'],
            proxy={'server': 'http://127.0.0.1:7890'}
        )
        context = await browser.new_context()
        page = await context.new_page()
        try:
            print("正在尝试通过代理连接 Google...")
            await page.goto("https://www.google.com/search?q=OpenClaw+AI", timeout=15000)
            title = await page.title()
            print(f"成功！网页标题是: {title}")
        except Exception as e:
            print(f"代理连接失败: {str(e)}")
        await browser.close()

asyncio.run(run())
