# 元素定位
定位器是 Playwright 自动等待和重试能力的核心部分。

## Dom结构示例
```html
<h3>Sign up</h3>
<label for="username">Username</label>
<input id="username" type="text" />
<label for="password">Password</label>
<input id="password" type="password" />

<!--点击 "Email:" 或输入框本身，都会激活输入框。-->
<label>
    Subscribe
    <input type="email" name="email" />
</label>
<input type="email" placeholder="name@example.com" />
<br>
<button type="submit">Sign up</button>

<span>Hello World</span>
<img src="https://playwright.dev/img/playwright-logo.svg" alt="Playwright Logo" />

<span title='span-title'>title test</span>
```
## 1、按角色定位
按显式和隐式可访问性属性进行定位语法：page.get_by_role（） 

语法：page.get_by_role(role, name=None, exact=False)

- role‌：必填参数，指定元素的 ARIA 角色类型（如 button、checkbox、heading 等）‌12。
- ‌name‌：可选参数，通过元素的显式名称（如按钮文本）或隐式可访问性属性（如 aria-label）进行过滤，支持字符串或正则表达式‌13。
- ‌exact‌：默认为 False，控制 name 的匹配方式（精确或模糊）‌

```python
# 检查名称为“Sign up”的标题是否可见
expect(page.get_by_role("heading", name="Sign up")).to_be_visible()
#勾选名称为 “Subscribe” 的复选框：
page.get_by_role("checkbox", name="Subscribe").check()
#使用正则表达式匹配名称（忽略大小写）
page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
#精准匹配
page.get_by_role("button", name="Sign in").click()

#定位导航栏中的链接（a 标签）
page.get_by_role("link", name="首页")
```

## 按标签定位
通过关联标签的文本查找表单控件，适用于输入框、复选框、单选按钮等元素的高效定位‌

语法：page.get_by_label(label_text‌)
- label_text‌：必填参数，指定与表单控件关联的 <label> 标签的显示文本（支持字符串或正则表达式）‌

 输入框操作
示例代码：
```python
page.get_by_label("Password").fill("hz123456")
#定位标签为“Birth date”的输入框并填写日期  
page.get_by_label("Birth date").fill("1999-12-31")
#‌复选框/单选框操作
示例代码：勾选或取消勾选关联标签的控件
# 勾选标签为“I agree to the terms above”的复选框  
page.get_by_label('I agree to the terms above').check()
 
#验证标签为“Subscribe to newsletter”的复选框是否已选中  
assert page.get_by_label('Subscribe to newsletter').is_checked() is True
#复杂表单交互, 处理带有嵌套标签或动态生成的表单
#使用正则表达式匹配部分标签文本（如“数字输入专用”）  
page.get_by_label(re.compile("数字输入")).fill("1.1234567890")

```
按标签定位特点
1. 标签唯一性‌：确保 label_text 在页面中唯一，否则可能定位到多个元素导致操作失败‌
2. 复合组件定位‌：对于复杂组件（如带图标的标签），可能需要结合其他定位方法（如 get_by_role() 或 CSS 选择器）‌

## 按占位符定位
语法：page.get_by_placeholder(placeholder)

```python
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```


## 通过文本定位
语法：page.get_by_text()
```python
# 可以通过元素包含的文本找到该元素
page.get_by_text("Welcome, John")
# 设置完全匹配
page.get_by_text("Welcome, John", exact=True)
# 正则表达式匹配
page.get_by_text(re.compile("welcome, john", re.IGNORECASE))
```
说明：
1. 按文本匹配始终会规范化空格，即使完全匹配也是如此。例如，它将多个空格转换为一个空格，将换行符转换为空格，并忽略前导和尾随空格。
2. 建议使用文本定位器来查找非交互式元素，如 div、span、p 等。对于button、a、input等交互式元素，请使用角色定位器。

## 通过替代文本定位
通过其文本替代来定位元素（通常是图像），所有图片都应具有描述图像的 alt 属性。可以使用page.get_by_alt_text() 根据替代文本查找图片。
语法：page.get_by_alt_text()
说明：当元素支持替代文本（如 img 和 area 元素）时，建议使用此定位器

## 按标题定位
按元素的 title 属性查找元素语法：page.get_by_title()
```python
expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

## 按测试 ID 查找根据元素data-testid 属性来定位元素（可以配置其他属性）
语法：page.get_by_title()
```python
page.get_by_test_id("directions").click()
```

## 通过 CSS 或 XPath 定位
```python
page.locator("css=button").click()
page.locator("xpath=//button").click()
 
#如果省略 css= 或 xpath= 前缀，则会自动检测它们
page.locator("button").click()
page.locator("//button").click()
```
不建议使用 CSS 和 XPath，因为 DOM 经常会更改，从而导致无法复原的测试。相反，请尝试提供一个接近用户感知页面的定位器，例如角色定位器，或者使用测试 ID 定义显式测试协定。

# 在 Shadow DOM 中定位
Shadow DOM 是 Web Components 技术的一部分，它提供了一种将 HTML 结构、样式和行为封装在一个独立的、封闭的 DOM 中的机制。
```html
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Shadow DOM Example</title>  
    <style>  
        /* 外部样式，不会影响 Shadow DOM 内部 */  
        .container {  
            font-size: 20px;  
            color: red;  
        }  
    </style>  
</head>  
<body>  
    <div id="hostElement" class="container">Shadow Host (这里不会显示 Shadow DOM 的内容)</div>  
  
    <script>  
        // 自定义元素定义及 Shadow DOM 创建  
        class MyCustomElement extends HTMLElement {  
            constructor() {  
                super();  
                // 创建 Shadow Root  
                const shadowRoot = this.attachShadow({ mode: 'open' });  
  
                // Shadow DOM 内部样式和内容  
                shadowRoot.innerHTML = `  
                    <style>  
                        .shadow-content {  
                            font-size: 16px;  
                            color: blue;  
                        }  
                    </style>  
                    <div class="shadow-content">This is inside the Shadow DOM.</div>  
                `;  
            }  
        }  
  
        // 注册自定义元素  
        customElements.define('my-custom-element', MyCustomElement);  
  
        // 将自定义元素添加到文档中  
        const customElement = document.createElement('my-custom-element');  
        document.body.appendChild(customElement);  
  
        // 注意：在实际应用中，你可能会将自定义元素直接写在 HTML 中，如：<my-custom-element></my-custom-element>  
        // 而不是通过 JavaScript 动态创建和添加。  
    </script>  
</body>  
</html>
```
