# Project Structure

```
ComfyUI-AVIF-Animation/
├── __init__.py              # Node registration and initialization
├── nodes.py                 # Main node implementation
├── README.md                # Full documentation (English)
├── README_CN.md             # Quick start (Chinese)
├── INSTALL.md               # Installation guide
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT License
├── requirements.txt          # Python dependencies (none required)
├── .gitignore             # Git ignore rules
└── example_workflow.json    # Example ComfyUI workflow
```

## File Descriptions

### Core Files

**__init__.py**
- Registers the AVIFAnimationNode with ComfyUI
- Maps node class to display name
- Required for ComfyUI to recognize the custom node

**nodes.py**
- Main implementation of AVIFAnimationNode class
- Handles image processing and avifenc execution
- Includes helper functions for image saving and memory management
- Comprehensive error handling and user feedback

### Documentation Files

**README.md**
- Complete documentation in English
- Features, requirements, usage examples
- Format comparison table
- Troubleshooting guide

**README_CN.md**
- Quick start guide in Chinese
- Basic installation and usage
- Links to full documentation

**INSTALL.md**
- Detailed installation instructions
- Platform-specific commands
- Troubleshooting common issues
- System requirements

**CHANGELOG.md**
- Version history and release notes
- Feature additions and changes
- Planned features for future releases

### Configuration Files

**requirements.txt**
- Python dependencies (none required)
- Notes about system dependencies (avifenc)

**.gitignore**
- Git ignore patterns
- Excludes Python cache, IDE files, OS files

**LICENSE**
- MIT License text
- Allows free use, modification, and distribution

**example_workflow.json**
- Sample ComfyUI workflow
- Demonstrates node usage
- Can be imported directly into ComfyUI

## Installation

Copy the entire `ComfyUI-AVIF-Animation/` folder to:
```
ComfyUI/custom_nodes/
```

## Development

To modify or extend this node:

1. Edit `nodes.py` for node logic
2. Edit `__init__.py` for node registration
3. Test changes in ComfyUI
4. Update documentation as needed
5. Update CHANGELOG.md for version changes

## Dependencies

### System (Required)
- avifenc (libavif tools)
  - Windows: winget install jark006.jarkViewer
  - macOS: brew install libavif
  - Linux: sudo apt-get install libavif-bin

### Python (No additional dependencies)
- torch (already required by ComfyUI)
- pillow (already required by ComfyUI)
- Standard library modules:
  - os, subprocess, tempfile
  - concurrent.futures, gc

## Versioning

This project follows Semantic Versioning (SemVer):
- MAJOR.MINOR.PATCH
- Example: 1.0.0

## Contributing

When contributing:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Update documentation
5. Submit a pull request

## Support

For issues and questions:
- GitHub Issues
- ComfyUI Discord community
