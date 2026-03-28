import asyncio
from playwright.async_api import async_playwright

async def wake_streamlit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # 본인의 스트림릿 앱 URL로 수정하세요
        url = "https://your-app-url.streamlit.app/" 
        
        print(f"Connecting to {url}...")
        await page.goto(url, wait_until="networkidle")
        
        # 'Wake up' 버튼이 있는지 확인하고 클릭
        wake_button = page.get_by_role("button", name="Yes, get this app back up!")
        if await wake_button.is_visible():
            await wake_button.click()
            print("Wake-up button clicked!")
        else:
            print("App is already awake.")
            
        await asyncio.sleep(5) # 연결 유지 대기
        await browser.close()

if __name__ == "__main__":
    asyncio.run(wake_streamlit())
