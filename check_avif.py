import os
from PIL import Image
import numpy as np

avif_path = r"D:\ai\ComfyUI-aki-v1.6-8180\ComfyUI\output\test_transparency.avif"

print(f"🔍 Checking AVIF file: {avif_path}")

try:
    img = Image.open(avif_path)
    print(f"✅ Successfully opened AVIF file")
    print(f"   Mode: {img.mode}")
    print(f"   Size: {img.size}")
    
    if img.mode == 'RGBA':
        img_array = np.array(img)
        alpha_channel = img_array[:, :, 3]
        
        print(f"   Alpha range: {alpha_channel.min()} - {alpha_channel.max()}")
        print(f"   Transparent pixels: {(alpha_channel < 128).sum()}/{alpha_channel.size}")
        print(f"   Transparent pixel ratio: {(alpha_channel < 128).sum() / alpha_channel.size * 100:.2f}%")
        
        if (alpha_channel < 128).sum() > 0:
            print("✅ AVIF file contains transparent areas")
        else:
            print("❌ AVIF file does not contain transparent areas")
    else:
        print(f"❌ AVIF file is not in RGBA mode, but {img.mode}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
