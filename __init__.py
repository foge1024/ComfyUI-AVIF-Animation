import os
import shutil
import sys

def check_and_install_avifenc():
    """Check and automatically install avifenc"""
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
        print("⚠️  avifenc not found, trying to install automatically...")
        try:
            from .install_avifenc import install_avifenc
            install_avifenc()
        except Exception as e:
            print(f"❌ Automatic installation failed: {e}")
            print("📋 Please manually install avifenc:")
            print("1. Visit: https://github.com/AOMediaCodec/libavif/releases")
            print("2. Download latest avifenc (Windows x64)")
            print("3. Extract zip file")
            print(f"4. Copy avifenc.exe to: {os.path.join(sys.prefix, 'Scripts')}")
            print("5. Restart ComfyUI")

check_and_install_avifenc()

from .nodes import AVIFAnimationNode

NODE_CLASS_MAPPINGS = {
    "AVIF Animation": AVIFAnimationNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AVIF Animation": "AVIF Animation (avifenc)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
