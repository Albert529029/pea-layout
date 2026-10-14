# 输出规范 · 骨架模板 · 字号颜色 · 质检清单

支撑 SKILL.md「步骤 3」。排版源码（进入微信/秀米的片段）必须严格遵循本规范；预览 HTML 外壳的 `<style>` 仅用于浏览器预览，绝不可进源码。

---

## 一、HTML 骨架模板（源码片段）

排版源码以 `<section>` 为基本容器，外层包一个总 `<section>` 作为画布。结构如下（占位符 `[...]` 替换为实际内容）：

```html
<section style="max-width:680px; margin:0 auto; padding:0 18px; background:#BG; color:#TXT; font-family:'PingFang SC','Microsoft YaHei',sans-serif; font-size:16px; line-height:1.9; letter-spacing:0.3px;">

  <!-- 顶部装饰 -->
  <section style="text-align:center; padding:24px 0 12px;">
    [SVG 装饰 / 标题区]
  </section>

  <!-- 大标题 -->
  <section style="padding:10px 0 18px; text-align:center;">
    <p style="margin:0; font-size:24px; font-weight:bold; color:#MAIN; letter-spacing:1px;">文章主标题</p>
    <p style="margin:8px 0 0; font-size:13px; color:#SUB;">副标题 / 引语</p>
  </section>

  <!-- 章节分隔 -->
  [分隔线组件]

  <!-- 正文段落 -->
  <section style="padding:12px 0;">
    <p style="margin:0 0 14px; text-indent:2em; color:#TXT;">正文第一段……</p>
    <p style="margin:0 0 14px; text-indent:2em; color:#TXT;">正文第二段……</p>
  </section>

  <!-- 重点句 / 引用 -->
  [引用卡组件]

  <!-- 双栏 / 卡片 -->
  [双栏组件]

  <!-- 文末 -->
  [渐变祝福卡 / 虚线互动卡]

</section>
```

---

## 二、字号规范（微信阅读舒适区间）

| 角色 | 字号 | 字重 | 备注 |
|---|---|---|---|
| 主标题 | 22–26px | bold | 字间距 1–2px，居中 |
| 章节标题 | 17–19px | bold | 可配编号组件 |
| 副标题 / 引语 | 13–14px | normal | 用辅色 |
| 正文 | 15–16px | normal | 行高 1.8–2.0，段首缩进 2em |
| 引用 | 15px | italic | 配引用卡 |
| 注释 / 出处 | 12px | normal | 右对齐或弱色 |
| 卡片内文 | 13px | normal | 行高 1.7–1.8 |

> 微信默认正文 16px。治愈/散文可 15px 显精致；科技/资讯可 16px 显清晰。

---

## 三、颜色规范

- 全文 4–5 色：**主色 / 辅色 / 点缀 / 背景 / 文字**，来自本文配色，禁止临时加色。
- 文字与背景对比度需达标：浅底用深字（`#TXT` 取 `#222~#5A` 区间），深底用浅字（`#TXT` 取 `#E6~#FFF`）。
- 链接/强调用主色或点缀，不用纯蓝 `#0000EE`（微信默认链接色破坏设计）。
- 渐变仅用 `linear-gradient`，角度 90–135deg，两端取本文主辅色。

---

## 四、间距与留白

- 画布左右内边距 18px（手机不顶边）。
- 章节间垂直 padding 12–18px，大区块（卡片/引用）上下 margin 14–18px。
- 疏朗风：段落间 16–20px；紧凑风：10–12px。一篇内节奏统一。
- 圆角：卡片 10–12px，徽章 50%（圆），小标签 6px。

---

## 五、质检清单（输出前逐项核对，对照红线）

- [ ] 所有样式均为 inline `style="..."`，无 `<style>`/`<link>`/`class`/`id`/JS/外链。
- [ ] 装饰至少 3 种不同类型，且含 SVG 插画类（1 或 2）。
- [ ] SVG 内联、`xmlns` 已写、属性全在元素上、无 `<style>` 子标签、颜色与配色一致。
- [ ] 并排布局用 `<table>` 实现，未用 flex/grid/position。
- [ ] 色彩方案与上一篇不同（差异化策略已触发 ≥3 条）。
- [ ] 源码片段完整可独立粘贴，无截断、无占位未替换的 `#MAIN` 等。
- [ ] 正文行高/字号符合规范，手机阅读舒适。
- [ ] 标题、引用、卡片层次清晰，无大段纯文字堆砌。
- [ ] 文中有图片处已用 `<!-- 此处插入图片 -->` 占位 + 说明框。
- [ ] 预览外壳 `<style>` 未混入源码。
- [ ] 三份文件命名前缀一致（`{主题}-公众号排版-`）。
