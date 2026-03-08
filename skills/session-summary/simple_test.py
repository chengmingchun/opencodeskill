#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单测试session-summary技能配置
"""

import json
import os

def main():
    print("测试session-summary技能配置 v3.0.0")
    print("=" * 50)
    
    config_path = "session-summary.json"
    
    if not os.path.exists(config_path):
        print("错误: 配置文件不存在")
        return
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print("1. 基本信息:")
        print(f"   名称: {config.get('name')}")
        print(f"   版本: {config.get('version')}")
        print(f"   交互模式: {config.get('interaction_mode')}")
        
        print("\n2. 渐进式步骤:")
        steps = config.get('progressive_steps', [])
        for step in steps:
            print(f"   步骤{step.get('step')}: {step.get('question')}")
            print(f"     选项: {', '.join(step.get('options', []))}")
            print(f"     默认: {step.get('default')}")
        
        print("\n3. 会话管理:")
        session_mgmt = config.get('session_management', {})
        print(f"   自动创建文件夹: {session_mgmt.get('auto_folder')}")
        print(f"   文件夹格式: {session_mgmt.get('folder_format')}")
        print(f"   默认路径: {session_mgmt.get('default_path')}")
        
        print("\n4. 触发器:")
        triggers = config.get('triggers', [])
        print(f"   数量: {len(triggers)}")
        print(f"   列表: {', '.join(triggers)}")
        
        print("\n" + "=" * 50)
        print("配置验证完成!")
        
        # 验证关键配置
        if config.get('interaction_mode') != 'progressive':
            print("警告: interaction_mode应为'progressive'")
        
        if len(steps) != 4:
            print(f"警告: progressive_steps应有4步，实际{len(steps)}步")
        
        if not session_mgmt.get('auto_folder'):
            print("警告: auto_folder应为true")
            
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()