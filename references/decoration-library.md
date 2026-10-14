# 装饰组件库 · 可直接复用代码

本文件支撑 SKILL.md「步骤 3」。下面每个组件都是**已验证可过微信/秀米**的 inline-style 片段，颜色用占位 HEX，使用时按本文配色替换（搜索替换即可）。**至少 3 种不同类型装饰**必须出现在每篇排版中。

> 约定占位色：`主色` `#MAIN`、`辅色` `#SUB`、`点缀` `#ACC`、`背景` `#BG`、`文字` `#TXT`。复制后全量替换成本文真实色值。

---

## 1. 手绘植物 / 枝叶（SVG 插画类）

用于治愈 / 自然 / 美食类开头装饰或章节点缀。属性全写在元素上，颜色随配色。

```html
<section style="text-align:center; padding:18px 0;">
  <svg width="120" height="60" viewBox="0 0 120 60" xmlns="http://www.w3.org/2000/svg">
    <path d="M60 58 C60 40 60 30 60 18" stroke="#MAIN" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M60 40 C48 38 40 30 38 22 C50 24 58 30 60 40 Z" fill="#SUB" opacity="0.9"/>
    <path d="M60 32 C72 30 80 22 82 14 C70 16 62 22 60 32 Z" fill="#ACC" opacity="0.85"/>
    <circle cx="60" cy="14" r="4" fill="#MAIN"/>
  </svg>
</section>
```

---

## 2. 水墨山水 / 笔触（SVG 插画类）

用于新中式 / 历史 / 国风。模拟远山与笔触，墨色 + 朱砂点。

```html
<section style="text-align:center; padding:16px 0;">
  <svg width="220" height="70" viewBox="0 0 220 70" xmlns="http://www.w3.org/2000/svg">
    <path d="M0 55 C40 30 70 48 100 35 C130 22 160 44 220 30 L220 70 L0 70 Z" fill="#MAIN" opacity="0.18"/>
    <path d="M10 50 C50 34 80 46 120 36 C160 26 190 42 215 34" stroke="#MAIN" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M30 58 C60 50 90 56 130 50" stroke="#SUB" stroke-width="1.5" fill="none" opacity="0.7"/>
    <circle cx="180" cy="20" r="6" fill="#ACC"/>
  </svg>
</section>
```

---

## 3. 几何 / 波浪分隔线（CSS + SVG）

放在章节之间。几何型用细线 + 圆点；波浪型用 SVG path。

几何分隔（极简 / 科技 / 高级风）：
```html
<section style="text-align:center; padding:14px 0;">
  <svg width="200" height="12" viewBox="0 0 200 12" xmlns="http://www.w3.org/2000/svg">
    <line x1="20" y1="6" x2="90" y2="6" stroke="#MAIN" stroke-width="1"/>
    <line x1="110" y1="6" x2="180" y2="6" stroke="#MAIN" stroke-width="1"/>
    <circle cx="100" cy="6" r="3.5" fill="#ACC"/>
  </svg>
</section>
```

波浪分隔（治愈 / 自然 / 少女风）：
```html
<section style="text-align:center; padding:12px 0;">
  <svg width="200" height="14" viewBox="0 0 200 14" xmlns="http://www.w3.org/2000/svg">
    <path d="M0 7 Q25 0 50 7 T100 7 T150 7 T200 7" stroke="#SUB" stroke-width="1.5" fill="none"/>
  </svg>
</section>
```

---

## 4. 圆角编号徽章（CSS inline）

四色圆角徽章，放列表 / 步骤开头。用 `inline-block` 替代 flex。

```html
<section style="padding:6px 0;">
  <span style="display:inline-block; width:26px; height:26px; line-height:26px; text-align:center; border-radius:50%; background:#MAIN; color:#BG; font-size:13px; font-weight:bold; margin-right:10px;">1</span>
  <span style="font-size:15px; font-weight:bold; color:#TXT;">小节标题</span>
</section>
```

---

## 5. 汉字印章编号（SVG）

新中式风专用：圆形朱砂印章 + 汉字序号（壹贰叁肆）。

```html
<section style="text-align:center; padding:10px 0;">
  <svg width="46" height="46" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg">
    <circle cx="23" cy="23" r="21" fill="none" stroke="#SUB" stroke-width="2.5"/>
    <text x="23" y="30" text-anchor="middle" font-size="20" fill="#SUB" font-family="STSong, SimSun, serif">壹</text>
  </svg>
</section>
```

---

## 6. 引用卡（CSS 边框 + 引号 SVG）

金句 / 唐诗 / 观点引用。左侧色条 + 大引号。

```html
<section style="margin:14px 0; padding:16px 18px; background:#BG; border-left:4px solid #MAIN; border-radius:6px;">
  <svg width="22" height="22" viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" style="margin-bottom:6px;">
    <text x="0" y="18" font-size="22" fill="#ACC" font-family="Georgia, serif">“</text>
  </svg>
  <p style="margin:0; font-size:15px; line-height:1.9; color:#TXT; font-style:italic;">引用内容放这里，可换行多行展示。</p>
  <p style="margin:8px 0 0; font-size:12px; color:#SUB; text-align:right;">— 出处 / 作者</p>
</section>
```

---

## 7. 双栏对比卡（table 实现）

并排对比（如东市 vs 西市、A 观点 vs B 观点）。用 table 替代 flex/grid。

```html
<table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:separate; border-spacing:10px; margin:14px 0;">
  <tr>
    <td width="50%" valign="top" style="background:#BG; border-radius:10px; padding:14px; border-top:3px solid #MAIN;">
      <p style="margin:0 0 6px; font-size:14px; font-weight:bold; color:#MAIN;">左栏标题</p>
      <p style="margin:0; font-size:13px; line-height:1.8; color:#TXT;">左栏内容描述，可多行。</p>
    </td>
    <td width="50%" valign="top" style="background:#BG; border-radius:10px; padding:14px; border-top:3px solid #SUB;">
      <p style="margin:0 0 6px; font-size:14px; font-weight:bold; color:#SUB;">右栏标题</p>
      <p style="margin:0; font-size:13px; line-height:1.8; color:#TXT;">右栏内容描述，可多行。</p>
    </td>
  </tr>
</table>
```

---

## 8. 虚线互动卡（CSS 虚线边框）

放文末互动 / 提问 / 行动号召。

```html
<section style="margin:16px 0; padding:16px; border:1.5px dashed #MAIN; border-radius:10px; background:#BG; text-align:center;">
  <p style="margin:0 0 6px; font-size:14px; font-weight:bold; color:#MAIN;">今日互动</p>
  <p style="margin:0; font-size:13px; line-height:1.8; color:#TXT;">在评论区聊聊你的看法吧 ✦</p>
</section>
```

---

## 9. 渐变祝福卡（CSS gradient 背景）

文末收尾，柔光渐变 + 居中祝福语。

```html
<section style="margin:16px 0; padding:20px; border-radius:12px; background:linear-gradient(135deg, #MAIN 0%, #SUB 100%); text-align:center;">
  <p style="margin:0; font-size:15px; font-weight:bold; color:#BG; line-height:1.9;">愿你被这世界温柔以待。</p>
</section>
```

> 颜色替换提示：渐变卡里 `#BG` 作文字色需与渐变明度拉开对比，若主辅色都深，文字改用 `#FFFFFF`。

---

## 使用纪律
- 每篇从 1~9 中**至少选 3 种不同类型**（插画类 1/2 算一类，但鼓励跨类组合）。
- 颜色必须全文统一来自本文配色，禁止装饰用一套、文字用一套。
- SVG 内 `xmlns` 必写；所有 `fill`/`stroke` 写在元素上，不写 `<style>` 子标签。
- 复制进微信/秀米前，确认已把 `#MAIN #SUB #ACC #BG #TXT` 全部替换为真实色值。
