import os
import shutil
import sys
import urllib.request
import zipfile
import tempfile
import platform

def get_avifenc_url():
    system = platform.system()
    if system == "Windows":
           return "https://github.com/AOMediaCodec/libavif/releases/download/v1.3.0/windows-artifacts.zip"
    elif system == "Darwin":
          return "https://github.com/AOMediaCodec/libavif/releases/download/v1.3.0/macOS-artifacts.zip"
    elif system == "Linux":
         return "https://github.com/AOMediaCodec/libavif/releases/download/v1.3.0/linux-artifacts.zip"
    else:
        raise ValueError(f"Unsupported system: {system}")

def install_avifenc():
    print("📦 Starting avifenc installation...")
    
    try:
        url = get_avifenc_url()
        print(f"📥 Downloading avifenc from: {url}")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = os.path.join(temp_dir, "avifenc.zip")
            
            try:
                urllib.request.urlretrieve(url, zip_path)
                print("✅ Download completed")
            except Exception as e:
                print(f"❌ Download failed: {str(e)}")
                print("\n📋 Manual download steps:")
                print("1. Visit: https://github.com/AOMediaCodec/libavif/releases")
                print("2. Download latest avifenc (Windows x64)")
                print("3. Extract zip file")
                print(f"4. Copy avifenc.exe to: {os.path.join(sys.prefix, 'Scripts')}")
                print("5. Restart ComfyUI")
                return False
            
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                print("✅ Extraction completed")
            except Exception as e:
                print(f"❌ Extraction failed: {str(e)}")
                return False
            
            avifenc_dir = os.path.join(temp_dir, "bin")
            if not os.path.exists(avifenc_dir):
                avifenc_dir = temp_dir
            
            scripts_dir = os.path.join(sys.prefix, "Scripts")
            if not os.path.exists(scripts_dir):
                scripts_dir = os.path.join(sys.prefix, "bin")
            
            os.makedirs(scripts_dir, exist_ok=True)
            
            avifenc_found = False
            for file in os.listdir(avifenc_dir):
                if file.startswith("avifenc"):
                    src = os.path.join(avifenc_dir, file)
                    dst = os.path.join(scripts_dir, file)
                    shutil.copy2(src, dst)
                    print(f"✅ Copied {file} to {scripts_dir}")
                    avifenc_found = True
            
            if not avifenc_found:
                print(f"❌ avifenc file not found in {avifenc_dir}")
                print(f"📂 Directory contents: {os.listdir(avifenc_dir)}")
                return False
            
            avifenc_path = os.path.join(scripts_dir, "avifenc")
            if os.path.exists(avifenc_path):
                os.chmod(avifenc_path, 0o755)
                print(f"✅ avifenc installed successfully!")
                print(f"📁 Installation path: {avifenc_path}")
                print(f"🔧 Please ensure {scripts_dir} is in PATH")
                
                zip_dst = os.path.join(scripts_dir, "avifenc.zip")
                if os.path.exists(zip_dst):
                    os.remove(zip_dst)
                    print(f"✅ Deleted temporary file: {zip_dst}")
                
                return True
            else:
                print(f"❌ avifenc not found in {avifenc_dir}")
                return False
                
    except Exception as e:
        print(f"❌ Installation failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    install_avifenc()
