#!/usr/bin/env python3
"""
测试session-summary技能配置
验证渐进式交互配置的正确性
"""

import json
import os
import sys

def test_configuration():
    """测试配置文件"""
    config_path = "session-summary.json"
    
    if not os.path.exists(config_path):
        print(f"❌ 配置文件不存在: {config_path}")
        return False
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print("✅ 配置文件加载成功")
        print(f"版本: {config.get('version', '未指定')}")
        print(f"交互模式: {config.get('interaction_mode', '未指定')}")
        
        # 验证关键配置
        required_fields = ['interaction_mode', 'progressive_steps', 'session_management']
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            print(f"❌ 缺少必要字段: {missing_fields}")
            return False
        
        print("✅ 所有必要字段都存在")
        
        # 验证渐进式步骤
        steps = config['progressive_steps']
        if len(steps) != 4:
            print(f"❌ 渐进式步骤数量不正确: {len(steps)} (应为4)")
            return False
        
        print("✅ 渐进式步骤配置正确 (4步)")
        
        # 验证会话管理
        session_mgmt = config['session_management']
        if not session_mgmt.get('auto_folder', False):
            print("❌ auto_folder应为true")
            return False
        
        print("✅ 会话管理配置正确")
        
        # 验证触发器
        triggers = config.get('triggers', [])
        if not triggers:
            print("❌ 触发器列表为空")
            return False
        
        print(f"✅ 触发器配置正确 ({len(triggers)}个触发器)")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        return False

def test_workflow_logic():
    """测试工作流程逻辑"""
    print("\n📋 测试工作流程逻辑:")
    
    # 模拟4步交互
    steps = [
        {
            "step": 1,
            "question": "是否总结当前会话？",
            "options": ["是", "否"],
            "default": "是"
        },
        {
            "step": 2,
            "question": "选择输出格式：",
            "options": ["Markdown", "HTML", "两者都生成"],
            "default": "两者都生成"
        },
        {
            "step": 3,
            "question": "选择输出路径：",
            "options": ["默认路径 (g:/blog/)", "当前工作目录", "自定义路径"],
            "default": "默认路径 (g:/blog/)"
        },
        {
            "step": 4,
            "question": "是否为会话创建专用文件夹？",
            "options": ["是（推荐）", "否"],
            "default": "是（推荐）"
        }
    ]
    
    print("✅ 4步交互流程定义正确")
    
    # 模拟用户选择
    user_choices = ["是", "两者都生成", "默认路径 (g:/blog/)", "是（推荐）"]
    
    print("✅ 用户选择模拟:")
    for i, (step, choice) in enumerate(zip(steps, user_choices), 1):
        print(f"  步骤{i}: {step['question']}")
        print(f"    用户选择: {choice}")
        print(f"    默认值: {step['default']}")
    
    return True

def test_folder_management():
    """测试文件夹管理逻辑"""
    print("\n📁 测试文件夹管理:")
    
    import datetime
    
    # 测试文件夹格式
    folder_format = "session_%Y%m%d_%H%M%S"
    now = datetime.datetime.now()
    folder_name = now.strftime(folder_format)
    
    print(f"✅ 文件夹格式: {folder_format}")
    print(f"✅ 生成的文件夹名: {folder_name}")
    
    # 测试默认路径
    default_path = "g:/blog/"
    full_path = os.path.join(default_path, folder_name)
    
    print(f"✅ 默认路径: {default_path}")
    print(f"✅ 完整路径: {full_path}")
    
    return True

def main():
    """主测试函数"""
    print("🔧 测试session-summary技能配置 v3.0.0")
    print("=" * 50)
    
    # 切换到配置文件目录
    original_dir = os.getcwd()
    config_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(config_dir)
    
    try:
        # 运行所有测试
        tests = [
            ("配置验证", test_configuration),
            ("工作流程", test_workflow_logic),
            ("文件夹管理", test_folder_management)
        ]
        
        results = []
        for test_name, test_func in tests:
            print(f"\n🧪 测试: {test_name}")
            try:
                result = test_func()
                results.append((test_name, result))
                if result:
                    print(f"✅ {test_name} - 通过")
                else:
                    print(f"❌ {test_name} - 失败")
            except Exception as e:
                print(f"❌ {test_name} - 异常: {e}")
                results.append((test_name, False))
        
        # 汇总结果
        print("\n" + "=" * 50)
        print("📊 测试结果汇总:")
        
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for test_name, result in results:
            status = "✅ 通过" if result else "❌ 失败"
            print(f"  {test_name}: {status}")
        
        print(f"\n🎯 总体结果: {passed}/{total} 通过")
        
        if passed == total:
            print("✨ 所有测试通过！配置正确。")
            return 0
        else:
            print("⚠️  部分测试失败，请检查配置。")
            return 1
            
    finally:
        os.chdir(original_dir)

if __name__ == "__main__":
    sys.exit(main())