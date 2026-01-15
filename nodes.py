import os
import sys
import subprocess
import tempfile
import shutil
import numpy as np

try:
    import torch
    from PIL import Image
    import folder_paths
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("📋 Please ensure installed: pip install torch pillow")

def save_image(image, path):
    """Save image to file"""
    try:
        img = image.squeeze().cpu().numpy()
        
        if img.ndim == 3:
            if img.shape[0] == 1:
                img = img[0]
            elif img.shape[0] == 3:
                img = img.transpose(1, 2, 0)
            elif img.shape[0] == 4:
                img = img.transpose(1, 2, 0)
        
        if img.ndim == 2:
            img = Image.fromarray((img * 255).astype('uint8'), mode='L')
        elif img.shape[2] == 3:
            img = Image.fromarray((img * 255).astype('uint8'), mode='RGB')
        elif img.shape[2] == 4:
            rgba_array = (img * 255).astype('uint8')
            img = Image.fromarray(rgba_array, mode='RGBA')
        
        img.save(path)
    except Exception as e:
        print(f"❌ Error saving image {path}: {e}")
        raise

def clear_memory():
    """Clear memory"""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.ipc_collect()

class AVIFAnimationNode:
    """AVIF animation generation node - using avifenc"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "fps": ("INT", {
                    "default": 24,
                    "min": 1,
                    "max": 120,
                    "step": 1,
                    "display": "FPS"
                }),
                "quality": ("INT", {
                    "default": 50,
                    "min": 0,
                    "max": 100,
                    "step": 1,
                    "display": "Quality"
                }),
                "alpha_quality": ("INT", {
                    "default": 60,
                    "min": 0,
                    "max": 100,
                    "step": 1,
                    "display": "Alpha Quality"
                }),
                "speed": ("INT", {
                    "default": 6,
                    "min": 0,
                    "max": 10,
                    "step": 1,
                    "display": "Encoding Speed"
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("avif_path",)
    FUNCTION = "images_to_avif"
    CATEGORY = "image/animation"
    OUTPUT_NODE = True
    
    def find_avifenc(self):
        """Find avifenc executable"""
        avifenc_paths = [
            os.path.join(sys.prefix, "Scripts", "avifenc.exe"),
            os.path.join(sys.prefix, "bin", "avifenc"),
            os.path.join(os.path.dirname(__file__), "avifenc.exe"),
            "avifenc",
        ]
        
        for path in avifenc_paths:
            if os.path.exists(path) or shutil.which(path):
                return path
        
        return None
    
    def images_to_avif(self, images, fps, quality, alpha_quality, speed):
        """Convert image sequence to AVIF animation"""
        try:
            avifenc_path = self.find_avifenc()
            
            if not avifenc_path:
                raise ValueError(
                    "❌ avifenc not found!\n"
                    "📋 Please install avifenc:\n"
                    "1. Visit: https://github.com/AOMediaCodec/libavif/releases\n"
                    "2. Download latest avifenc (Windows x64)\n"
                    "3. Extract zip file\n"
                    "4. Copy avifenc.exe to: " + os.path.join(sys.prefix, "Scripts") + "\n"
                    "5. Restart ComfyUI"
                )
            
            has_transparent_input = any(image.shape[-1] == 4 for image in images)
            
            print(f"\n🔍 Input image analysis:")
            print(f"   Total frames: {len(images)}")
            try:
                output_dir = folder_paths.output_directory
            except ImportError:
                import comfy
                output_dir = os.path.join(comfy.__path__[0], '../output')
            output_dir = os.path.abspath(output_dir)
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            temp_dir = tempfile.mkdtemp()
            
            try:
                count = 0
                frame_files = []
                
                for image in images:
                    temp_image_path = os.path.join(temp_dir, f"frame_{count:09d}.png")
                    frame_files.append(temp_image_path)
                    
                    try:
                        save_image(image, temp_image_path)
                    except Exception as e:
                        print(f"❌ Failed to save frame {count+1}: {e}")
                        raise
                    
                    count += 1
                
                import time
                avif_filename = f"avif_animation_{time.strftime('%Y%m%d%H%M%S')}.avif"
                avif_path = os.path.join(output_dir, avif_filename)
                
                print("\n⚙️  Starting AVIF animation generation:")
                print(f"📁 Output path: {avif_path}")
                print(f"🎨 Frames: {count}")
                print(f"⚡ FPS: {fps}")
                print(f"🎯 Quality: {quality}")
                print(f"🔍 Alpha Quality: {alpha_quality}")
                print(f"🚀 Encoding Speed: {speed}")
                print(f"🔧 avifenc path: {avifenc_path}")
                
                cmd = [
                    avifenc_path,
                    '--fps', str(fps),
                    '-q', str(quality),
                    '--qalpha', str(alpha_quality),
                    '-s', str(speed),
                ]
                cmd.extend(frame_files)
                cmd.append(avif_path)
                
                print(f"\n📋 Executing command: {' '.join(cmd[:5])} ... {len(frame_files)} frames -> {avif_path}")
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    print(f"❌ avifenc execution failed:")
                    print(f"Standard output: {result.stdout}")
                    print(f"Error output: {result.stderr}")
                    raise ValueError(f"avifenc execution failed: {result.stderr}")
                
                print(f"\n✅ AVIF animation generated successfully!")
                
                file_size = os.path.getsize(avif_path) / 1024
                print(f"📊 Output file size: {file_size:.2f} KB")
                
                if has_transparent_input:
                    print("✅ Successfully generated AVIF file with transparency!")
                else:
                    print("ℹ️  Generated AVIF file does not contain transparency")
                
                ui_images = []
                if avif_path and os.path.exists(avif_path):
                    avif_filename = os.path.basename(avif_path)
                    ui_images.append({
                        "filename": avif_filename,
                        "subfolder": "",
                        "type": "output"
                    })
                
                return {
                    "result": (avif_path,),
                    "ui": {
                        "images": ui_images
                    }
                }
                
            finally:
                shutil.rmtree(temp_dir, ignore_errors=True)
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise ValueError(f"Error during processing: {str(e)}")

NODE_CLASS_MAPPINGS = {
    "AVIF Animation (avifenc)": AVIFAnimationNode
}
