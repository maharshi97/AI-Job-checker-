from playwright.sync_api import sync_playwright

def fetch_job_board_html(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=30000)
            content = page.content()
            browser.close()
            return content
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None