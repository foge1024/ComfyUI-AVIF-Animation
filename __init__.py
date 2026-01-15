import os
import shutil
import sys

def check_and_install_avifenc():
    """检查并自动安装avifenc"""
    avifenc_paths = [
        os.path.join(sys.prefix, "Scripts", "avifenc.exe"),
        os.path.join(sys.prefix, "bin", "avifenc"),
        os.path.join(os.path.dirname(__file__), "avifenc.exe"),
    ]
    
    avifenc_exists = False
    for path in avifenc_paths:
        if os.path.exists(path) or shutil.which("avifenc"):
            avifenc_exists = True
            break
    
    if not avifenc_exists:
        print("⚠️  avifenc未找到，尝试自动安装...")
        try:
            from .install_avifenc import install_avifenc
            install_avifenc()
        except Exception as e:
            print(f"❌ 自动安装失败: {e}")
            print("📋 请手动安装avifenc:")
            print("1. 访问: https://github.com/AOMediaCodec/libavif/releases")
            print("2. 下载最新版本的avifenc (Windows x64)")
            print("3. 解压zip文件")
            print(f"4. 将avifenc.exe复制到: {os.path.join(sys.prefix, 'Scripts')}")
            print("5. 重启ComfyUI")

check_and_install_avifenc()

from .nodes import AVIFAnimationNode

NODE_CLASS_MAPPINGS = {
    "AVIF Animation": AVIFAnimationNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AVIF Animation": "AVIF Animation (avifenc)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
