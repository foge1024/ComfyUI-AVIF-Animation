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
    print("📦 开始安装avifenc...")
    
    try:
        url = get_avifenc_url()
        print(f"📥 下载avifenc from: {url}")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = os.path.join(temp_dir, "avifenc.zip")
            
            try:
                urllib.request.urlretrieve(url, zip_path)
                print("✅ 下载完成")
            except Exception as e:
                print(f"❌ 下载失败: {str(e)}")
                print("\n📋 手动下载步骤:")
                print("1. 访问: https://github.com/AOMediaCodec/libavif/releases")
                print("2. 下载最新版本的avifenc (Windows x64)")
                print("3. 解压zip文件")
                print(f"4. 将avifenc.exe复制到: {os.path.join(sys.prefix, 'Scripts')}")
                print("5. 重启ComfyUI")
                return False
            
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
                print("✅ 解压完成")
            except Exception as e:
                print(f"❌ 解压失败: {str(e)}")
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
                    print(f"✅ 复制 {file} 到 {scripts_dir}")
                    avifenc_found = True
            
            if not avifenc_found:
                print(f"❌ 未找到avifenc文件在 {avifenc_dir}")
                print(f"📂 目录内容: {os.listdir(avifenc_dir)}")
                return False
            
            avifenc_path = os.path.join(scripts_dir, "avifenc")
            if os.path.exists(avifenc_path):
                os.chmod(avifenc_path, 0o755)
                print(f"✅ avifenc安装成功！")
                print(f"📁 安装路径: {avifenc_path}")
                print(f"🔧 请确保 {scripts_dir} 在PATH中")
                
                zip_dst = os.path.join(scripts_dir, "avifenc.zip")
                if os.path.exists(zip_dst):
                    os.remove(zip_dst)
                    print(f"✅ 删除临时文件: {zip_dst}")
                
                return True
            else:
                print(f"❌ avifenc未找到在 {avifenc_dir}")
                return False
                
    except Exception as e:
        print(f"❌ 安装失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    install_avifenc()
