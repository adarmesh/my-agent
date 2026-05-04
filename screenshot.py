from pathlib import Path
from playwright.sync_api import sync_playwright

html_path = Path(__file__).parent / "login.html"
output_path = Path(__file__).parent / "screenshot.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(f"file://{html_path}")
    page.screenshot(path=str(output_path), full_page=True)
    browser.close()

print(f"Screenshot saved to {output_path}")
