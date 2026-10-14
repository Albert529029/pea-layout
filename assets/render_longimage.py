# render_longimage.py
# 用法: python render_longimage.py <预览HTML路径> <输出PNG路径>
# 依赖: pip install playwright && playwright install chromium
import sys
from playwright.sync_api import sync_playwright

html_path = sys.argv[1] if len(sys.argv) > 1 else "预览.html"
out_path  = sys.argv[2] if len(sys.argv) > 2 else "效果长图.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    # 390px 手机宽度，2x 缩放，整页截图
    page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    page.goto("file://" + html_path)
    page.wait_for_timeout(400)
    page.screenshot(path=out_path, full_page=True)
    browser.close()
print("saved:", out_path)
