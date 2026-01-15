# ComfyUI AVIF 动画节点

使用 avifenc 生成带透明通道的 AVIF 动画的 ComfyUI 自定义节点。

## 特性

- ✅ 从图像序列生成 AVIF 动画
- ✅ 完整的透明通道支持
- ✅ 可调节的质量参数
- ✅ 可配置的编码速度
- ✅ 跨平台支持（Windows、macOS、Linux）
- ✅ 无需 Python 依赖
- ✅ **自动安装 avifenc**

## 系统要求

- Python 3.8+
- ComfyUI
- 网络连接（用于自动下载 avifenc）

## 安装

### 自动安装（推荐）

1. 将此仓库克隆或下载到 ComfyUI 的 custom_nodes 目录：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-AVIF-Animation.git
```

2. 重启 ComfyUI

3. 首次启动时，节点会自动检测并安装 avifenc 到 Python 的 Scripts 目录

### 手动安装（如果自动安装失败）

如果自动安装失败，您可以手动安装 avifenc：

1. 访问：https://github.com/AOMediaCodec/libavif/releases
2. 下载适合您平台的最新版本 avifenc：
   - Windows: `libavif-*.windows-x64.zip`
   - macOS: `libavif-*.darwin-arm64.zip` (M1/M2) 或 `libavif-*.darwin-x86_64.zip` (Intel)
   - Linux: `libavif-*.linux-x86_64.zip`
3. 解压 zip 文件
4. 将 `avifenc`（Windows 上是 `avifenc.exe`）复制到以下位置之一：
   - Windows: `C:\Users\[用户名]\Miniconda3\envs\[你的环境]\Scripts\avifenc.exe`
   - macOS/Linux: `/usr/local/bin/avifenc` 或添加到 PATH
5. 重启 ComfyUI

## 使用

1. 打开 ComfyUI
2. 在节点图中右键点击
3. 导航到 `image/animation` 类别
4. 选择 `AVIF Animation (avifenc)` 节点
5. 将图像序列连接到 `images` 输入
6. 调整参数：
   - **FPS**: 每秒帧数（1-120，默认：24）
   - **质量**: 整体质量（0-100，默认：50）
   - **透明质量**: 透明度质量（0-100，默认：60）
   - **速度**: 编码速度（0-10，默认：6）
7. 执行节点生成 AVIF 动画

## 参数说明

### FPS（每秒帧数）
- 范围：1-120
- 默认：24
- 说明：控制动画的播放速度

### 质量
- 范围：0-100
- 默认：50
- 说明：整体图像质量（越高 = 质量越好，文件越大）

### 透明质量
- 范围：0-100
- 默认：60
- 说明：透明通道质量（越高 = 透明度质量越好，文件越大）

### 速度
- 范围：0-10
- 默认：6
- 说明：编码速度（0 = 最慢/最佳质量，10 = 最快/较低质量）

## 输出

节点会输出生成的 AVIF 文件路径，文件保存在 ComfyUI 的输出目录中。

## 示例工作流

```python
# 示例：从图像序列生成 AVIF 动画
1. 使用"Load Image"节点加载图像
2. 连接到"AVIF Animation"节点
3. 设置 FPS 为 24
4. 设置质量为 50
5. 设置透明质量为 60
6. 设置速度为 6
7. 执行以生成 AVIF 动画
```

## 故障排除

### avifenc 未找到
```
错误：❌ avifenc未找到！
```
解决方案：按照上述安装步骤安装 avifenc。

### 导入错误
```
错误：❌ 导入错误: No module named 'torch'
```
解决方案：安装 torch：`pip install torch`

### 透明度不工作
确保输入图像有 4 个通道（RGBA）。如果它们有 3 个通道（RGB），节点会自动添加不透明的 alpha 通道。

## 技术细节

此节点使用：
- **avifenc**: 来自 libavif 的 AVIF 编码命令行工具
- **PIL/Pillow**: 图像处理
- **torch**: ComfyUI 兼容性的张量操作

AVIF 格式提供：
- 比 JPEG、PNG 和 WebP 更好的压缩
- 完整的透明度支持
- 现代设备上的硬件加速解码
- 广泛的浏览器支持（Chrome、Firefox、Safari）

## 许可证

MIT License

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 致谢

- [libavif](https://github.com/AOMediaCodec/libavif) - AVIF 编解码器库
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - UI 框架
