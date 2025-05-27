#!/usr/bin/env python3
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_gemini_api():
    """测试Gemini API是否可用"""
    try:
        # 获取API密钥
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("❌ 错误: 未找到GEMINI_API_KEY环境变量")
            return False
        
        print(f"✓ 找到API密钥: {api_key[:10]}...")
        
        # 配置API
        genai.configure(api_key=api_key)
        
        # 测试模型列表
        print("✓ 正在获取可用模型...")
        models = list(genai.list_models())
        if models:
            print(f"✓ 找到 {len(models)} 个可用模型")
            for model in models[:3]:  # 显示前3个模型
                print(f"  - {model.name}")
        else:
            print("⚠️  未找到可用模型")
        
        # 测试简单的文本生成
        print("\n✓ 测试文本生成...")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Hello, please respond with 'API test successful!'")
        
        if response and response.text:
            print(f"✓ API响应: {response.text.strip()}")
            print("\n🎉 Gemini API测试成功！")
            return True
        else:
            print("❌ API响应为空")
            return False
            
    except Exception as e:
        print(f"❌ API测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 开始测试Gemini API...")
    print("=" * 50)
    
    success = test_gemini_api()
    
    print("=" * 50)
    if success:
        print("✅ 所有测试通过！API可以正常使用。")
    else:
        print("❌ 测试失败！请检查API密钥和网络连接。")
