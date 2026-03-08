# 📖 Session Summary Skill 使用指南

## 🎯 功能概述

这个自定义Skill可以将OpenCode会话内容自动转化为：
1. **Markdown文档** - 充满干货、技术深度、有趣生动
2. **炫酷HTML文档** - 交互性强、支持多文件、响应式设计

## 📁 文件结构

```
C:\Users\Administrator\.config\opencode\
└── skills\
    ├── session-summary.json          # Skill配置文件
    └── templates\
        ├── session-summary-md.md     # Markdown模板
        └── session-summary-html.html # HTML模板
```

## 🚀 使用方法

### 1. 在OpenCode中使用

在OpenCode会话中，直接调用此skill：

```
请使用 session-summary skill 总结这个会话内容
```

### 2. 手动使用

#### 生成Markdown：
1. 使用 `session_read` 获取会话内容
2. 使用 `session_summary` prompt生成Markdown
3. 保存为 `.md` 文件

#### 生成HTML：
1. 获取Markdown内容
2. 使用HTML模板渲染
3. 保存为 `.html` 文件

## ✨ HTML特性

### 炫酷视觉效果
- 🌙 暗色主题
- 🎨 渐变背景和色彩
- ✨ 流畅动画

### 交互功能
- 📋 一键复制代码
- 📂 折叠/展开长内容
- 🔍 实时搜索
- 📑 目录导航
- 📊 滚动进度条

### 响应式设计
- 🖥️ 桌面端优化
- 📱 移动端适配

### 多文件支持
在HTML中可轻松扩展多个md文件：

```javascript
// 在script中配置
const CONFIG = {
    files: [
        'session-01.md',
        'session-02.md', 
        'session-03.md'
    ],
    defaultFile: 'session-01.md'
};

// 添加文件内容
const fileContents = {
    'session-01.md': '内容1',
    'session-02.md': '内容2',
    'session-03.md': '内容3'
};
```

## 🎨 自定义模板

### 修改颜色主题
在CSS变量中修改：

```css
:root {
    --primary: #00d9ff;      /* 主色调 */
    --secondary: #7b2cbf;     /* 副色调 */
    --accent: #ff6b6b;        /* 强调色 */
    --bg-dark: #0a0e17;       /* 背景色 */
}
```

### 添加新文件
1. 在 `CONFIG.files` 数组中添加文件名
2. 在 `fileContents` 对象中添加对应内容
3. 文件会自动出现在顶部标签栏

## 📝 Markdown语法支持

- 标题 (# ## ### ####)
- 代码块 (```语言)
- 行内代码 (`code`)
- 表格 (|---|)
- 列表 (- item)
- 引用 (> quote)
- 链接 ([text](url))
- 粗体/斜体 (**bold** *italic*)

### 扩展语法

```markdown
:::collapsible 点击展开:::
这里是隐藏内容
:::

:::tag::: 标签1
:::tag.warning::: 警告标签
:::tag.success::: 成功标签
```

## 🔧 技术亮点

1. **零依赖** - 纯原生HTML/CSS/JS
2. **单文件** - 所有CSS/JS内联
3. **TreeWalker** - 高效文本搜索
4. **CSS变量** - 轻松定制主题
5. **模块化** - 配置驱动扩展

## 📄 输出示例

生成的文档包含：
- 会话概述和目标
- 核心技术点（代码展示）
- 解决方案
- 代码技巧总结
- 最佳实践
- 相关资源

---
*Generated with ❤️ by OpenCode*
