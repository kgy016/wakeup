import asyncio
from playwright.async_api import async_playwright

async def wake_streamlit():
    # 여기에 깨우고 싶은 모든 스트림릿 주소를 넣으세요 (콤마로 구분)
    urls = [
        "https://reverseplayer-jqh24cc38qz5yqfkadappf5.streamlit.app/",
        "https://rebootyoutube-q5kwcky4tcpsvssiznmxby.streamlit.app/",
        "https://luckytoday-hkfwgtw6qmfdvhmwqe8f7r.streamlit.app/",
        "https://imagereshape-nsdjpunaxpe9my5bdzmcfl.streamlit.app/",
        "https://eattoday-pseyfcpwwwjzfd5mbqidj4.streamlit.app/"
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        
        for url in urls:
            page = await context.new_page()
            print(f"--- {url} 접속 시도 중 ---")
            
            try:
                # 페이지 접속 (네트워크가 조용해질 때까지 최대 30초 대기)
                await page.goto(url, wait_until="networkidle", timeout=60000)
                
                # 'Wake up' 버튼이 있는지 확인 (텍스트로 찾기)
                wake_button = page.get_by_role("button", name="Yes, get this app back up!")
                
                if await wake_button.is_visible():
                    await wake_button.click()
                    print(f"✅ {url}: 깨우기 버튼 클릭 완료!")
                    # 버튼 클릭 후 로딩 대기
                    await asyncio.sleep(10) 
                else:
                    print(f"✨ {url}: 이미 깨어있거나 버튼이 없습니다.")
                
            except Exception as e:
                print(f"❌ {url}: 접속 실패 (에러: {e})")
            
            finally:
                await page.close() # 한 페이지 끝나면 닫고 다음으로 이동
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(wake_streamlit())
