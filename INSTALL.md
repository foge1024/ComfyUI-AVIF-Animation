# Installation Guide

## Quick Start

### 1. Install avifenc (Automatic)

**Run the installer:**
```bash
cd ComfyUI-AVIF-Animation
python install_avifenc.py
```

This will automatically:
- Detect your platform (Windows/macOS/Linux)
- Download avifenc from GitHub releases
- Install it to Python's Scripts directory
- Set executable permissions

**No need to:**
- ❌ Manually download avifenc
- ❌ Modify PATH or system variables
- ❌ Use package managers (winget/brew/apt)

### 2. Install ComfyUI Node

**Option A: Clone from Git**
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-AVIF-Animation.git
```

**Option B: Download ZIP**
1. Download ZIP file from GitHub
2. Extract to `ComfyUI/custom_nodes/ComfyUI-AVIF-Animation/`
3. Restart ComfyUI

### 3. Verify Installation

1. Start ComfyUI
2. Check if "AVIF Animation (avifenc)" node appears in node menu
3. Test with a simple workflow

### 4. Verify avifenc Installation

```bash
python -c "import sys; import os; print(os.path.join(os.path.join(sys.prefix, 'Scripts' if os.name == 'nt' else 'bin'), 'avifenc'))"
```

## Troubleshooting

### avifenc not found

**Symptom:** Node shows "avifenc未安装" error

**Solution:**
1. Run the installer:
   ```bash
   cd ComfyUI-AVIF-Animation
   python install_avifenc.py
   ```
2. Verify avifenc is installed:
   ```bash
   python -c "import sys; import os; print(os.path.join(os.path.join(sys.prefix, 'Scripts' if os.name == 'nt' else 'bin'), 'avifenc'))"
   ```
3. Restart ComfyUI after installing

### Installer fails

**Symptom:** `install_avifenc.py` fails to download

**Solution:**
1. Check internet connection
2. Verify Python installation
3. Try manual download from https://github.com/AOMediaCodec/libavif/releases
4. Check GitHub releases for latest version

### Node not appearing in menu

**Symptom:** "AVIF Animation (avifenc)" node not found

**Solution:**
1. Check file structure:
   ```
   ComfyUI/custom_nodes/ComfyUI-AVIF-Animation/
   ├── __init__.py
   ├── nodes.py
   ├── install_avifenc.py
   ├── README.md
   └── ...
   ```
2. Restart ComfyUI
3. Check ComfyUI console for errors

### Permission denied on Windows

**Symptom:** "Access denied" when saving files

**Solution:**
1. Run ComfyUI as Administrator
2. Or check output directory permissions

### Large file size

**Symptom:** AVIF files are too large

**Solution:**
- Lower `quality` parameter (try 40-60)
- Lower `alpha_quality` parameter (try 40-60)
- Reduce `fps` parameter (try 15-24)

### Slow encoding

**Symptom:** Encoding takes too long

**Solution:**
- Increase `speed` parameter (try 8-10)
- Reduce image resolution
- Reduce number of frames

## System Requirements

### Minimum
- Python 3.8+
- ComfyUI
- avifenc 1.0+ (installed by `install_avifenc.py`)

### Recommended
- Python 3.10+
- ComfyUI latest
- avifenc 1.3+
- NVIDIA GPU (for ComfyUI)

## Compatibility

### Tested Platforms
- ✅ Windows 10/11
- ✅ macOS 12+ (Monterey)
- ✅ Linux (Ubuntu 20.04+, Fedora 35+)

### ComfyUI Versions
- ✅ ComfyUI Stable
- ✅ ComfyUI Daily
- ✅ ComfyUI Portable

## Support

For additional help:
- GitHub Issues: https://github.com/yourusername/ComfyUI-AVIF-Animation/issues
- ComfyUI Discord: https://discord.gg/comfyui
