---
name: session-summary
description: |
  将OpenCode会话内容总结为有趣的Markdown和HTML文档。自动提取代码技巧、干货内容，生成交互式文档。
  支持默认路径(g:/blog)和自定义路径。
  
  触发条件：
  - 用户提到"生成会话"、"总结会话"、"创建会话文档"等关键词
  - 用户请求生成技术文档或会议纪要
  - 用户需要将对话内容整理成结构化文档
  - 用户提到"session-summary"、"总结"、"文档"等关键词
  
  使用场景：
  - 技术讨论后需要整理成文档
  - 代码评审后需要总结最佳实践
  - 问题解决后需要记录解决方案
  - 学习交流后需要整理知识点
---


# Session Summary Skill

## 概述
将OpenCode会话内容总结为有趣的Markdown和HTML文档。自动提取代码技巧、干货内容，生成交互式文档。支持默认路径(g:/blog)和自定义路径。

## 功能特性
- **智能总结**: 自动提取会话中的关键技术点、代码技巧和解决方案
- **双格式输出**: 同时生成Markdown和HTML文档
- **前卫设计**: 现代、灵动、可交互的HTML界面
- **路径灵活**: 支持默认路径(g:/blog)、当前路径和自定义路径
- **多文件支持**: HTML支持加载和切换多个Markdown文件

## 触发条件

### 主要触发词
- `session-summary`: 直接命令
- `总结会话`: 中文命令
- `生成会话总结`: 明确请求
- `创建会话文档`: 文档生成请求

### 关键词自动触发
当用户消息包含以下关键词时，技能会自动触发：

**中文关键词**:
- 生成会话
- 总结会话
- 会话总结
- 创建文档
- 技术文档
- 会议纪要
- 整理对话
- 记录会话
- 文档生成
- 总结内容

**英文关键词**:
- generate session
- session summary
- summarize conversation
- create documentation
- technical document
- meeting notes
- organize discussion
- record session
- document generation
- summarize content

### 上下文触发
在以下上下文中会自动触发：
1. 技术讨论结束后用户说"帮我把这个整理一下"
2. 代码评审后用户说"记录一下这些最佳实践"
3. 问题解决后用户说"把这个解决方案记下来"
4. 学习交流后用户说"整理成文档方便以后查看"
## 使用示例

### 基本用法
```
session-summary
```
默认输出到 `g:/blog` 文件夹

### 指定输出路径
```
session-summary --path /custom/path
```
输出到自定义路径

### 指定会话ID
```
session-summary --session-id ses_abc123
```
总结指定会话

### 使用当前路径
```
session-summary --current
```
输出到OpenCode当前工作目录

## 输出文件

### 1. Markdown文档 (session-summary.md)
- 有趣且吸引人的标题
- 技术干货内容
- 代码技巧总结
- 最佳实践建议
- 包含实际代码片段

### 2. HTML文档 (session-summary.html)
- 前卫灵动的浅色主题
- 紫色(#7c3aed)和粉色(#f472b6)为主色调
- 现代字体系统：Inter、Noto Sans SC、JetBrains Mono
- 交互功能：
  - 一键复制代码
  - 折叠/展开内容
  - 平滑滚动导航
  - 全文搜索
  - 滚动进度条
  - 响应式目录
- 响应式设计，支持移动端
- 多文件切换支持

## 路径配置

### 默认路径
`g:/blog` - 优先使用此路径

### 当前路径
OpenCode当前工作目录（workdir环境变量）

### 自定义路径
用户指定的任意路径

## 设计系统

### 颜色方案
- 主色: `#7c3aed` (紫色)
- 辅色: `#f472b6` (粉色)
- 强调色: `#f59e0b` (橙色)
- 成功色: `#10b981` (绿色)
- 危险色: `#ef4444` (红色)
- 信息色: `#3b82f6` (蓝色)

### 字体系统
- 正文字体: Inter, Noto Sans SC
- 标题字体: Fredoka, Inter
- 代码字体: JetBrains Mono

### 间距系统
- 基础间距: 1rem (16px)
- 圆角: 8px, 12px, 16px, 24px
- 阴影: 多级阴影系统

## 模板文件

### HTML模板
`templates/session-summary-modern.html`
- 现代设计，交互性强
- 内联CSS和JS，单文件使用
- 支持多文件切换

### Markdown模板
`templates/session-summary-md.md`
- 技术文档结构
- 代码块支持
- 格式化内容

## 配置选项

### session-summary.json
```json
{
  "name": "session-summary",
  "description": "将OpenCode会话内容总结为有趣的Markdown和HTML文档...",
  "category": "writing",
  "version": "2.0.0",
  "features": {
    "markdown": {
      "template": "templates/session-summary-md.md"
    },
    "html": {
      "template": "templates/session-summary-modern.html",
      "multiFileSupport": true
    }
  }
}
```

## 开发说明

### 模板变量
- `{{title}}`: 文档标题
- `{{content}}`: Markdown内容
- `{{files}}`: 文件列表（JSON数组）
- `{{defaultFile}}`: 默认文件

### 扩展HTML功能
HTML模板支持以下扩展语法：
- `:::collapsible 标题\n内容\n:::` - 可折叠区域
- `:::tag::: 标签文本` - 标签样式
- `:::tag.warning::: 警告标签` - 警告标签
- `:::tag.success::: 成功标签` - 成功标签

### 代码高亮
HTML模板内置语法高亮：
- `.keyword`: 关键字
- `.string`: 字符串
- `.number`: 数字
- `.comment`: 注释
- `.function`: 函数
- `.variable`: 变量
- `.property`: 属性
- `.operator`: 操作符

## 最佳实践

### 内容组织
1. 从会话中提取关键技术点
2. 使用实际代码展示技巧
3. 总结解决方案和最佳实践
4. 保持技术深度同时生动有趣

### 路径处理
1. 优先使用默认路径 `g:/blog`
2. 检查路径是否存在，不存在则创建
3. 支持相对路径和绝对路径
4. 验证写入权限

### 错误处理
1. 会话不存在时提供友好提示
2. 路径不可写时建议替代方案
3. 模板文件缺失时使用默认模板
4. 网络字体加载失败时使用备用字体

## 更新日志

### v2.0.0 (当前)
- 重新设计HTML模板，前卫灵动风格
- 添加默认路径 `g:/blog` 支持
- 改进代码块配色和交互
- 增强响应式设计
- 更新字体系统

### v1.0.0
- 初始版本
- 基础Markdown和HTML输出
- 简单交互功能
- 多路径支持

## 未来计划
- 添加更多主题选项
- 支持导出为PDF
- 添加统计分析
- 集成更多数据源
- 支持自定义模板