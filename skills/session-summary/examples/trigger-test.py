#!/usr/bin/env python3
"""
Session Summary Skill - Trigger Test

This script tests the automatic triggering of the session-summary skill
based on keywords in user messages.
"""

import re
import json
from pathlib import Path

def load_triggers():
    """Load triggers from session-summary.json"""
    config_path = Path(__file__).parent.parent / "session-summary.json"
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    triggers = config.get("triggers", [])
    print(f"Loaded {len(triggers)} triggers from config")
    return triggers

def check_trigger(message, triggers):
    """
    Check if a message triggers the session-summary skill.
    
    Args:
        message (str): User message
        triggers (list): List of trigger keywords/phrases
    
    Returns:
        tuple: (bool triggered, str matched_trigger, list all_matches)
    """
    message_lower = message.lower()
    matches = []
    
    for trigger in triggers:
        # Check for exact phrase match
        if trigger.lower() in message_lower:
            matches.append(trigger)
    
    # Also check for common patterns
    patterns = [
        r'(生成|创建|制作|编写).*?(会话|对话|会议|讨论).*?(总结|文档|记录|纪要)',
        r'(总结|整理|记录).*?(会话|对话|会议|讨论)',
        r'(session|conversation|discussion).*?(summary|summarize|document)',
        r'(generate|create).*?(document|summary).*?(session|conversation)',
    ]
    
    for pattern in patterns:
        if re.search(pattern, message_lower):
            matches.append(f"pattern:{pattern}")
    
    if matches:
        return True, matches[0], matches
    return False, None, []

def test_messages():
    """Test various messages to see if they trigger the skill."""
    test_cases = [
        # Chinese test cases
        ("帮我生成会话总结", True, "生成会话总结"),
        ("可以总结一下这个会话吗", True, "总结会话"),
        ("创建会话文档", True, "创建会话文档"),
        ("生成技术文档", True, "技术文档"),
        ("做会议纪要", True, "会议纪要"),
        ("把这个对话整理一下", True, "pattern"),
        ("记录这次讨论", True, "pattern"),
        
        # English test cases
        ("generate session summary", True, "generate session"),
        ("session summary please", True, "session summary"),
        ("summarize this conversation", True, "summarize conversation"),
        ("create documentation for this session", True, "create documentation"),
        ("can you summarize our discussion", True, "pattern"),
        
        # Negative test cases
        ("今天天气怎么样", False, None),
        ("写一段Python代码", False, None),
        ("帮我调试这个错误", False, None),
        ("什么是OpenAI", False, None),
        
        # Edge cases
        ("会话", True, "会话总结"),  # Partial match
        ("summary", True, "session summary"),  # Partial match
        ("生成", True, "生成会话"),  # Partial match
    ]
    
    triggers = load_triggers()
    
    print("=" * 60)
    print("Session Summary Skill - Trigger Testing")
    print("=" * 60)
    
    results = []
    for message, expected, expected_trigger in test_cases:
        triggered, matched_trigger, all_matches = check_trigger(message, triggers)
        
        status = "✅" if triggered == expected else "❌"
        result = {
            "message": message,
            "expected": expected,
            "actual": triggered,
            "matched": matched_trigger,
            "all_matches": all_matches,
            "status": status
        }
        results.append(result)
        
        print(f"\n{status} 测试: '{message}'")
        print(f"  预期触发: {expected}, 实际触发: {triggered}")
        if triggered:
            print(f"  匹配触发词: {matched_trigger}")
            if len(all_matches) > 1:
                print(f"  所有匹配: {all_matches}")
    
    # Summary
    print("\n" + "=" * 60)
    print("测试结果汇总:")
    print("=" * 60)
    
    passed = sum(1 for r in results if r["status"] == "✅")
    total = len(results)
    
    print(f"通过: {passed}/{total} ({passed/total*100:.1f}%)")
    
    # Show failures
    failures = [r for r in results if r["status"] == "❌"]
    if failures:
        print("\n❌ 失败的测试:")
        for f in failures:
            print(f"  - '{f['message']}': 预期={f['expected']}, 实际={f['actual']}")
    
    return results

def simulate_skill_invocation(message):
    """Simulate what happens when skill is triggered."""
    triggers = load_triggers()
    triggered, matched_trigger, all_matches = check_trigger(message, triggers)
    
    if triggered:
        print(f"\n🎯 技能触发成功!")
        print(f"   用户消息: '{message}'")
        print(f"   匹配触发词: {matched_trigger}")
        print(f"   所有匹配: {all_matches}")
        
        # Simulate skill behavior
        print(f"\n🔧 技能执行:")
        print(f"   1. 分析会话内容")
        print(f"   2. 提取关键技术点和代码技巧")
        print(f"   3. 生成Markdown文档 (session-summary.md)")
        print(f"   4. 生成HTML文档 (session-summary.html)")
        print(f"   5. 保存到默认路径: g:/blog")
        
        return True
    else:
        print(f"\n⏭️  技能未触发")
        print(f"   用户消息: '{message}'")
        print(f"   未匹配任何触发词")
        return False

def main():
    """Main demonstration function."""
    print("=" * 60)
    print("Session Summary Skill - 自动触发功能测试")
    print("=" * 60)
    
    # Run comprehensive tests
    test_messages()
    
    # Interactive simulation
    print("\n" + "=" * 60)
    print("交互式模拟测试")
    print("=" * 60)
    
    simulation_messages = [
        "我们刚才讨论了Python装饰器的用法，可以生成会话总结吗？",
        "这次代码评审有很多有用的建议，做个会议纪要吧",
        "generate a summary of our conversation about React hooks",
        "把这个技术讨论整理成文档",
        "帮我写个总结"
    ]
    
    for msg in simulation_messages:
        simulate_skill_invocation(msg)
        print("-" * 40)
    
    print("\n" + "=" * 60)
    print("✅ 测试完成!")
    print("=" * 60)
    
    # Show trigger list
    triggers = load_triggers()
    print(f"\n📋 当前配置的触发词 ({len(triggers)}个):")
    for i, trigger in enumerate(triggers, 1):
        print(f"  {i:2d}. {trigger}")

if __name__ == "__main__":
    main()