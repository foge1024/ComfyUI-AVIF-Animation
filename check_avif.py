import os
from PIL import Image
import numpy as np

avif_path = r"D:\ai\ComfyUI-aki-v1.6-8180\ComfyUI\output\test_transparency.avif"

print(f"🔍 检查 AVIF 文件: {avif_path}")

try:
    img = Image.open(avif_path)
    print(f"✅ 成功打开 AVIF 文件")
    print(f"   模式: {img.mode}")
    print(f"   大小: {img.size}")
    
    if img.mode == 'RGBA':
        img_array = np.array(img)
        alpha_channel = img_array[:, :, 3]
        
        print(f"   Alpha范围: {alpha_channel.min()} - {alpha_channel.max()}")
        print(f"   透明像素: {(alpha_channel < 128).sum()}/{alpha_channel.size}")
        print(f"   透明像素占比: {(alpha_channel < 128).sum() / alpha_channel.size * 100:.2f}%")
        
        # 检查是否有真正的透明区域
        if (alpha_channel < 128).sum() > 0:
            print("✅ AVIF 文件包含透明区域")
        else:
            print("❌ AVIF 文件没有透明区域")
    else:
        print(f"❌ AVIF 文件不是 RGBA 模式，而是 {img.mode}")
        
except Exception as e:
    print(f"❌ 错误: {e}")
    import traceback
    traceback.print_exc()
