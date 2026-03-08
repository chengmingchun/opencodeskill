# Session-Summary 快速参考

## 🎯 触发方式

### 直接命令
```
session-summary
session-summary --path /custom/path
session-summary --current
session-summary --session-id ses_abc123
```

### 自动触发关键词
**说这些话会自动触发**:

#### 中文关键词
- "生成会话总结"
- "总结会话"
- "创建会话文档"
- "做会议纪要"
- "整理对话内容"
- "记录这次讨论"
- "生成技术文档"

#### 英文关键词
- "generate session summary"
- "session summary please"
- "summarize this conversation"
- "create documentation"
- "make meeting notes"

#### 自然表达
- "帮我把这个对话总结一下"
- "刚才的讨论很有用，做个记录"
- "可以生成个总结吗？"
- "把这个整理成文档"

## 📁 输出路径

### 默认路径
`g:/blog` (优先使用)

### 其他选项
- **当前路径**: `--current` 或提到"当前目录"
- **自定义路径**: `--path /your/path` 或指定具体路径
- **集中化路径**: 原配置路径 (兼容性保留)

## 📄 输出文件

### 1. Markdown 文档
`session-summary.md`
- 技术干货内容
- 代码技巧总结
- 最佳实践建议
- 实际代码示例

### 2. HTML 文档
`session-summary.html`
- 前卫灵动设计
- 交互式功能
- 响应式布局
- 多文件支持

## 🎨 HTML 功能

### 交互特性
- ✅ 一键复制代码
- ✅ 折叠/展开内容
- ✅ 目录导航
- ✅ 全文搜索
- ✅ 滚动进度条
- ✅ 响应式设计

### 设计特色
- 紫色(#7c3aed) + 粉色(#f472b6)主题
- Inter + Noto Sans SC 字体
- JetBrains Mono 代码字体
- 毛玻璃效果导航
- 平滑动画过渡

## 🔧 使用示例

### 示例 1: 基本使用
```
用户: 刚才讨论了Python装饰器，生成个总结
AI: 检测到"生成总结"，正在创建文档...
输出: g:/blog/session-summary.{md,html}
```

### 示例 2: 指定路径
```
用户: session-summary --path /projects/docs
AI: 正在生成文档到 /projects/docs...
```

### 示例 3: 当前目录
```
用户: 总结会话 --current
AI: 正在生成文档到当前目录...
```

### 示例 4: 指定会话
```
用户: session-summary --session-id ses_abc123
AI: 正在总结会话 ses_abc123...
```

## ⚡ 快速命令

### 最常用
```bash
# 默认路径生成
session-summary

# 中文触发
总结会话

# 英文触发
generate session summary
```

### 带参数
```bash
# 自定义路径
session-summary --path ~/Documents/summaries

# 当前目录
session-summary --current

# 指定会话
session-summary --session-id ses_xyz789
```

## 🛠️ 故障排除

### 技能不触发？
1. 检查是否包含触发关键词
2. 尝试直接命令 `session-summary`
3. 查看技能配置是否正常

### 文件未生成？
1. 检查路径权限
2. 验证 `g:/blog` 是否存在
3. 尝试使用 `--current` 选项

### HTML 显示问题？
1. 使用现代浏览器 (Chrome/Firefox/Edge)
2. 检查控制台错误
3. 确保网络字体可访问

## 📈 高级技巧

### 批量处理
```bash
# 总结多个会话
for id in ses_abc123 ses_def456 ses_ghi789; do
    session-summary --session-id $id --path /summaries/$id
done
```

### 自定义模板
1. 修改 `templates/session-summary-modern.html`
2. 调整CSS变量 (:root 部分)
3. 保持交互功能完整性

### 集成到工作流
```bash
# 技术讨论后自动总结
discuss --topic "React Hooks" && session-summary --current

# 代码评审后生成文档
code-review --pr 123 && session-summary --path ./review-docs
```

## 🔍 关键词参考表

| 类别 | 关键词示例 | 触发效果 |
|------|-----------|----------|
| 动作词 | 生成、创建、制作、编写 | 高触发率 |
| 目标词 | 会话、文档、总结、纪要 | 高触发率 |
| 组合词 | 生成会话、创建文档、做纪要 | 最高触发率 |
| 英文词 | generate, summary, document | 中英文兼容 |
| 自然表达 | 整理一下、记下来、做个记录 | 上下文感知 |

## 💡 使用建议

### 最佳实践
1. **明确请求**: "生成会话总结" 比 "总结" 更可靠
2. **指定路径**: 需要时明确输出位置
3. **提供上下文**: 技术讨论后立即请求
4. **检查输出**: 确认文件生成位置

### 避免问题
1. 避免在非技术对话中使用触发词
2. 确保输出路径有写入权限
3. 大型会话可能需要更长时间处理
4. 网络字体需要互联网连接

## 🚀 立即尝试

### 测试触发
说这些话试试：
- "帮我生成会话总结"
- "create session documentation"
- "总结刚才的讨论"
- "做会议纪要"

### 验证输出
检查生成的文件：
1. 打开 `g:/blog/session-summary.html`
2. 查看交互功能是否正常
3. 验证内容完整性

---

**提示**: 技能会持续学习优化，使用越多越智能！