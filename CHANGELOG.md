# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-01-15

### Added
- Initial release of AVIF Animation node for ComfyUI
- Full transparency (alpha channel) support
- Adjustable FPS, quality, alpha quality, and encoding speed
- Automatic transparency channel detection and addition
- Multi-threaded image processing
- Memory optimization with automatic cleanup
- Comprehensive error handling and user feedback
- Support for infinite loop playback

### Features
- Uses libavif's avifenc for optimal AVIF encoding
- YUV444 color format support
- Non-premultiplied alpha channel
- Automatic avifenc installation check
- Detailed console output for debugging
- File size reporting after encoding
- Transparency verification after encoding

### Documentation
- Comprehensive README with usage examples
- Installation guide for Windows, macOS, and Linux
- Format comparison table
- Troubleshooting section
- Example workflow JSON
- MIT License

### Compatibility
- ComfyUI Stable and Daily versions
- Windows 10/11
- macOS 12+ (Monterey)
- Linux (Ubuntu 20.04+, Fedora 35+)
- iOS 16+ and macOS Ventura+ for AVIF playback

## [Unreleased]

### Planned
- GPU acceleration support (if available in future avifenc versions)
- Batch processing for multiple animations
- Custom output directory option
- Preview functionality within ComfyUI
- Additional AVIF encoding parameters
