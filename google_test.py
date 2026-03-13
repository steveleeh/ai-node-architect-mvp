import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        # 访问 Google 搜索 "OpenClaw AI"
        print("正在连接 Google...")
        await page.goto("https://www.google.com/search?q=OpenClaw+AI+features", timeout=60000)
        
        # 等待结果列表加载
        await page.wait_for_selector("h3")
        
        # 抓取标题
        titles = await page.evaluate("() => Array.from(document.querySelectorAll('h3')).slice(0, 3).map(h => h.innerText)")
        print("\n=== Google 搜索结果预览 ===")
        for i, title in enumerate(titles):
            print(f"{i+1}. {title}")
            
        await browser.close()

asyncio.run(run())
