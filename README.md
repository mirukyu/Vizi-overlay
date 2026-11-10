# VIZI Overlay

A Python tool that adds screenshot metadata overlays to VRChat screenshots. It extracts player count, world name, author, and date information from VRCX metadata embedded in PNG images and displays it as an overlay.

## Features

- Extracts VRCX metadata from PNG images
- Displays world name, photographer, player count, and screenshot date
- Automatic date extraction from filename (VRChat_YYYY-MM-DD format)
- Text shadow effect for better readability
- Supports images of any resolution

## Requirements

- Python 3.7+
- Pillow (PIL)

Install dependencies:
```bash
pip install Pillow
```

## Usage

```bash
python vmaker-run.py input.png output.png
```

**Arguments:**
- `input.png` - Path to the VRChat screenshot with VRCX metadata
- `output.png` - Path where the overlayed image will be saved

### Example

```bash
python vmaker-run.py "VRChat_2026-01-23_08-46-35.052_7680x4320.png" "output.png"
```

## Before and After

<p align="left">
  <img src="VRChat_2026-01-23_08-46-35.052_7680x4320_wrld_6364fa61-1ba6-4333-b8a3-566ca813d12d.png" alt="Before overlay" width="420" />
  <img src="final.png" alt="After overlay" width="420" />
</p>

## Overlay Format

The overlay displays in the bottom-left corner:
```
VIZI.SH
[World Name]
by [photographer]
[Player Count] players
[Date]
```