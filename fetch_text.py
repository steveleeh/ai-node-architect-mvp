import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # 使用真实的浏览器外壳，避免被识别为爬虫
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        )
        page = await context.new_page()
        # 尝试访问京东搜索
        await page.goto("https://m.jd.com/search/search.action?keyword=RTX4050+%E7%AC%94%E8%AE%B0%E6%9C%AC")
        # 等待商品标题加载
        await page.wait_for_timeout(3000)
        # 获取纯文本
        content = await page.evaluate("() => document.body.innerText")
        print(content[:2000]) # 打印前2000个字符
        await browser.close()

asyncio.run(run())
