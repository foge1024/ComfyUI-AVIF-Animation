# ComfyUI AVIF Animation Node

A ComfyUI custom node for generating AVIF animations with transparency support using avifenc.

## Features

- ✅ Generate AVIF animations from image sequences
- ✅ Full transparency (alpha channel) support
- ✅ Adjustable quality parameters
- ✅ Configurable encoding speed
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ No Python dependencies required

## Requirements

- Python 3.8+
- ComfyUI
- avifenc (libavif command-line tool)

## Installation

### Step 1: Install avifenc

1. Visit: https://github.com/AOMediaCodec/libavif/releases
2. Download the latest version of avifenc for your platform:
   - Windows: `libavif-*.windows-x64.zip`
   - macOS: `libavif-*.darwin-arm64.zip` (M1/M2) or `libavif-*.darwin-x86_64.zip` (Intel)
   - Linux: `libavif-*.linux-x86_64.zip`
3. Extract the zip file
4. Copy `avifenc` (or `avifenc.exe` on Windows) to one of these locations:
   - Windows: `C:\Users\[username]\Miniconda3\envs\[your_env]\Scripts\avifenc.exe`
   - macOS/Linux: `/usr/local/bin/avifenc` or add to PATH

### Step 2: Install the Node

1. Clone or download this repository to your ComfyUI custom_nodes directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-AVIF-Animation.git
```

2. Restart ComfyUI

## Usage

1. Open ComfyUI
2. Right-click in the node graph area
3. Navigate to `image/animation` category
4. Select `AVIF Animation (avifenc)` node
5. Connect your image sequence to `images` input
6. Adjust parameters:
   - **FPS**: Frames per second (1-120, default: 24)
   - **Quality**: Overall quality (0-100, default: 50)
   - **Alpha Quality**: Transparency quality (0-100, default: 60)
   - **Speed**: Encoding speed (0-10, default: 6)
7. Execute the node to generate AVIF animation

## Parameters

### FPS (Frames Per Second)
- Range: 1-120
- Default: 24
- Description: Controls the playback speed of the animation

### Quality
- Range: 0-100
- Default: 50
- Description: Overall image quality (higher = better quality, larger file size)

### Alpha Quality
- Range: 0-100
- Default: 60
- Description: Transparency channel quality (higher = better transparency quality, larger file size)

### Speed
- Range: 0-10
- Default: 6
- Description: Encoding speed (0 = slowest/best quality, 10 = fastest/lower quality)

## Output

The node outputs the path to the generated AVIF file in the ComfyUI output directory.

## Example Workflow

```python
# Example: Generate AVIF animation from image sequence
1. Load images using "Load Image" node
2. Connect to "AVIF Animation" node
3. Set FPS to 24
4. Set Quality to 50
5. Set Alpha Quality to 60
6. Set Speed to 6
7. Execute to generate AVIF animation
```

## Troubleshooting

### avifenc not found
```
Error: ❌ avifenc未找到！
```
Solution: Install avifenc following the installation steps above.

### Import errors
```
Error: ❌ 导入错误: No module named 'torch'
```
Solution: Install torch: `pip install torch`

### Transparency not working
Make sure your input images have 4 channels (RGBA). If they have 3 channels (RGB), the node will automatically add an opaque alpha channel.

## Technical Details

This node uses:
- **avifenc**: Command-line tool from libavif for AVIF encoding
- **PIL/Pillow**: Image processing
- **torch**: Tensor operations for ComfyUI compatibility

The AVIF format provides:
- Better compression than JPEG, PNG, and WebP
- Full transparency support
- Hardware-accelerated decoding on modern devices
- Wide browser support (Chrome, Firefox, Safari)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- [libavif](https://github.com/AOMediaCodec/libavif) - AVIF codec library
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - UI framework
