# 交付流程 · 三形态生成

支撑 SKILL.md「步骤 4」。完成排版源码后，依次产出三份文件，命名前缀统一 `{主题}-公众号排版-`，全部写入工作区并用 present_files 交付。

---

## 一、三形态总览

| 文件 | 命名 | 用途 |
|---|---|---|
| 预览 HTML | `{主题}-公众号排版-预览.html` | 浏览器双击即看效果（手机 390px 居中） |
| 源码 Markdown | `{主题}-公众号排版-源码.md` | 内嵌 html 代码块，整段复制进微信/秀米 |
| 效果长图 | `{主题}-公众号排版-效果长图.png` | 390px 手机宽度整页渲染高清长图 |

`{主题}` 用文章核心词，如 `苹果治愈文`、`长安烟火文`、`AI产品经理`。

---

## 二、预览 HTML 外壳模板（仅浏览器预览用）

> ⚠️ 外壳里的 `<style>` **严禁**进入微信/秀米源码。它只负责把排版片段在桌面浏览器里模拟成手机宽度预览。把「排版源码片段」整体塞进 `<body>` 内即可。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{主题} · 公众号排版预览</title>
<style>
  html,body{margin:0;padding:0;background:#e9e9ec;}
  .phone{width:390px;margin:24px auto;background:#fff;min-height:100vh;box-shadow:0 4px 24px rgba(0,0,0,0.12);overflow:hidden;}
</style>
</head>
<body>
  <div class="phone">
    <!-- ↓↓↓ 以下整段替换为「排版源码片段」 ↓↓↓ -->
    <section style="max-width:680px;margin:0 auto;padding:0 18px;background:#FBF6EF;color:#5A4A42;font-family:'PingFang SC','Microsoft YaHei',sans-serif;font-size:16px;line-height:1.9;">
      [此处粘贴排版源码片段]
    </section>
    <!-- ↑↑↑ 以上整段替换为「排版源码片段」 ↑↑↑ -->
  </div>
</body>
</html>
```

---

## 三、源码 Markdown 模板

源码 md 含：设计信息 + 使用说明 + 可直接复制的 html 代码块。代码块内容必须与预览 HTML 内嵌片段**逐字一致**。

```markdown
# {主题} · 公众号排版源码

## 设计说明
- 文章类型：{类型}
- 风格方向：{方向名}
- 色彩方案：主色 #xxx / 辅色 #xxx / 点缀 #xxx / 背景 #xxx / 文字 #xxx
- 装饰思路：{3 种装饰简述}
- 差异化：与上一篇差异点 {简述}

## 使用方法
1. 复制下方 ```html 代码块内的全部内容。
2. 打开微信公众号编辑器或秀米，粘贴到正文区即可。

\`\`\`html
[此处粘贴排版源码片段，纯 inline-style]
\`\`\`

> 提示：如需微调（配色/字号/某处装饰），告诉我具体位置即可。
```

---

## 四、效果长图渲染

用无头浏览器把预览 HTML 按 **390px 宽、2x 缩放、整页** 截图为 PNG。推荐 Playwright（Python）。

### 渲染脚本 `render_longimage.py`

```python
# 用法: python render_longimage.py <预览HTML路径> <输出PNG路径>
import sys
from playwright.sync_api import sync_playwright

html_path = sys.argv[1] if len(sys.argv) > 1 else "预览.html"
out_path  = sys.argv[2] if len(sys.argv) > 2 else "效果长图.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    page.goto("file://" + html_path)
    page.wait_for_timeout(400)
    page.screenshot(path=out_path, full_page=True)
    browser.close()
print("saved:", out_path)
```

### 安装与运行（首次）
```bash
pip install playwright
playwright install chromium
python render_longimage.py "{主题}-公众号排版-预览.html" "{主题}-公众号排版-效果长图.png"
```

### 降级方案（无 Playwright / 无网）
- 用系统已装的 Chromium / Chrome 走 `--headless --screenshot` 整页截图；
- 或在工作区用 Bash 启动一个本地静态服务器，浏览器开发者工具「设备工具栏 390px + 整页截图」手动导出；
- 无论如何，**长图必须是真实渲染产物，禁止占位图**。

---

## 五、交付检查

- [ ] 三份文件前缀一致，均已写入工作区。
- [ ] 预览 HTML 双击可渲染，无空白页。
- [ ] 源码 md 代码块 = 预览 HTML 内嵌片段（逐字）。
- [ ] 长图为 390px / 2x / 整页真实截图。
- [ ] 通过 present_files 一并交付。
