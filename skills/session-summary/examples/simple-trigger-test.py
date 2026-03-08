#!/usr/bin/env python3
"""
Simple trigger test without Unicode characters
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
    """Check if message triggers the skill."""
    message_lower = message.lower()
    matches = []
    
    for trigger in triggers:
        if trigger.lower() in message_lower:
            matches.append(trigger)
    
    # Check patterns
    patterns = [
        r'(生成|创建|制作|编写).*?(会话|对话|会议|讨论).*?(总结|文档|记录|纪要)',
        r'(总结|整理|记录).*?(会话|对话|会议|讨论)',
        r'(session|conversation|discussion).*?(summary|summarize|document)',
        r'(generate|create).*?(document|summary).*?(session|conversation)',
    ]
    
    for pattern in patterns:
        if re.search(pattern, message_lower):
            matches.append(f"pattern:{pattern}")
    
    return bool(matches), matches[0] if matches else None, matches

def main():
    print("=" * 60)
    print("SESSION SUMMARY SKILL - TRIGGER TEST")
    print("=" * 60)
    
    triggers = load_triggers()
    print(f"\nTriggers: {triggers}")
    
    # Test cases
    test_cases = [
        ("帮我生成会话总结", True),
        ("可以总结一下这个会话吗", True),
        ("创建会话文档", True),
        ("生成技术文档", True),
        ("做会议纪要", True),
        ("generate session summary", True),
        ("session summary please", True),
        ("今天天气怎么样", False),
        ("写一段Python代码", False),
    ]
    
    print("\n" + "=" * 60)
    print("TEST RESULTS")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for message, expected in test_cases:
        triggered, matched, all_matches = check_trigger(message, triggers)
        status = "PASS" if triggered == expected else "FAIL"
        
        if status == "PASS":
            passed += 1
        
        print(f"\n{status}: '{message}'")
        print(f"  Expected: {expected}, Got: {triggered}")
        if triggered:
            print(f"  Matched: {matched}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {passed}/{total} passed ({passed/total*100:.1f}%)")
    print("=" * 60)
    
    # Show examples of automatic triggering
    print("\nEXAMPLES OF AUTOMATIC TRIGGERING:")
    print("-" * 40)
    
    examples = [
        "我们刚才讨论了Python装饰器，生成会话总结吧",
        "这次代码评审很有用，做个会议纪要",
        "generate a summary of our React discussion",
        "把这个技术对话整理成文档"
    ]
    
    for example in examples:
        triggered, matched, all_matches = check_trigger(example, triggers)
        if triggered:
            print(f"✓ '{example}'")
            print(f"  -> Would trigger session-summary skill")
            print(f"  -> Matched: {matched}")
        else:
            print(f"✗ '{example}'")
            print(f"  -> Would NOT trigger")
        print()

if __name__ == "__main__":
    main()