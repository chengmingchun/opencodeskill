#!/usr/bin/env python3
"""
Session Summary Skill - Path Handling Example

This script demonstrates the path handling logic for the session-summary skill.
The actual implementation will be done by the AI when the skill is invoked.
"""

import os
import sys
from pathlib import Path

def get_output_path(user_path=None, use_current=False):
    """
    Determine the output path based on user input and configuration.
    
    Priority:
    1. If user specifies a custom path, use it
    2. If user requests current path, use workdir
    3. Otherwise, use default path (g:/blog)
    
    Args:
        user_path (str, optional): User-specified custom path
        use_current (bool): Whether to use current working directory
    
    Returns:
        Path: Resolved output directory path
    """
    # Default path (g:/blog)
    DEFAULT_PATH = Path("g:/blog")
    
    # Current working directory (from OpenCode workdir environment)
    CURRENT_PATH = Path(os.getcwd())
    
    # Determine the output path
    if user_path:
        # User specified a custom path
        output_path = Path(user_path)
        print(f"📁 Using custom path: {output_path}")
    elif use_current:
        # User requested current path
        output_path = CURRENT_PATH
        print(f"📁 Using current path: {output_path}")
    else:
        # Use default path
        output_path = DEFAULT_PATH
        print(f"📁 Using default path: {output_path}")
    
    # Create directory if it doesn't exist
    try:
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Directory created/verified: {output_path}")
    except Exception as e:
        print(f"❌ Failed to create directory: {e}")
        # Fallback to current directory
        output_path = CURRENT_PATH
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"⚠️  Falling back to: {output_path}")
    
    return output_path

def save_files(output_path, markdown_content, html_content):
    """
    Save Markdown and HTML files to the output directory.
    
    Args:
        output_path (Path): Directory to save files
        markdown_content (str): Markdown content
        html_content (str): HTML content
    """
    # Define file paths
    md_file = output_path / "session-summary.md"
    html_file = output_path / "session-summary.html"
    
    # Save Markdown file
    try:
        md_file.write_text(markdown_content, encoding='utf-8')
        print(f"📝 Markdown saved: {md_file}")
    except Exception as e:
        print(f"❌ Failed to save Markdown: {e}")
    
    # Save HTML file
    try:
        html_file.write_text(html_content, encoding='utf-8')
        print(f"🌐 HTML saved: {html_file}")
    except Exception as e:
        print(f"❌ Failed to save HTML: {e}")
    
    return md_file, html_file

def generate_sample_content():
    """Generate sample content for demonstration."""
    markdown = """# 🚀 示例会话总结

> 这是一个示例会话总结，展示技能的输出格式

## 📋 会话概述
本次会话讨论了OpenCode技能开发的最佳实践。

## 💡 核心技术点
- 技能模板设计
- 路径处理逻辑
- 交互式HTML生成

### 代码示例
```python
def get_output_path(user_path=None, use_current=False):
    \"\"\"智能路径选择函数\"\"\"
    DEFAULT_PATH = Path("g:/blog")
    
    if user_path:
        return Path(user_path)
    elif use_current:
        return Path(os.getcwd())
    else:
        return DEFAULT_PATH
```

## ✨ 代码技巧总结
| 技巧 | 说明 | 适用场景 |
|------|------|----------|
| 路径优先级 | 默认 > 当前 > 自定义 | 文件输出 |
| 目录创建 | 自动创建不存在的目录 | 路径处理 |
| 错误回退 | 失败时回退到安全路径 | 错误处理 |

> 💭 **总结**: 这是一个完整的技能开发示例

*Generated with ❤️ by OpenCode Session Summary Skill*
"""
    
    html = """<!DOCTYPE html>
<html>
<head>
    <title>示例会话总结</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #7c3aed; }
        .code-block { background: #1a1a1a; color: white; padding: 15px; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>🚀 示例会话总结</h1>
    <p>这是一个示例HTML输出</p>
    <div class="code-block">
        <pre><code>print("Hello, Session Summary!")</code></pre>
    </div>
</body>
</html>"""
    
    return markdown, html

def main():
    """Main demonstration function."""
    print("=" * 60)
    print("Session Summary Skill - Path Handling Demo")
    print("=" * 60)
    
    # Test different path scenarios
    scenarios = [
        ("默认路径 (无参数)", None, False),
        ("当前路径 (--current)", None, True),
        ("自定义路径 (/tmp/test)", "/tmp/test", False),
    ]
    
    for name, user_path, use_current in scenarios:
        print(f"\n🔍 测试场景: {name}")
        print("-" * 40)
        
        # Get output path
        output_path = get_output_path(user_path, use_current)
        
        # Generate sample content
        markdown, html = generate_sample_content()
        
        # Save files (simulated)
        md_file, html_file = save_files(output_path, markdown, html)
        
        print(f"📊 文件位置:")
        print(f"  • Markdown: {md_file}")
        print(f"  • HTML: {html_file}")
    
    print("\n" + "=" * 60)
    print("✅ 演示完成!")
    print("=" * 60)

if __name__ == "__main__":
    main()