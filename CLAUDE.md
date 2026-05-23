# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Chip quality detection using YOLO (ultralytics) and OpenCV. The trained model (`chip.pt`) classifies chips as **good** or **bad**. Three scripts cover single-image, batch, and real-time webcam detection.

## Commands

```bash
# Install dependencies
pip install ultralytics opencv-python

# Single image detection (outputs to out1/)
python detect_test_1.py

# Batch detection on all images in datasets/ (outputs to out2/)
python detect_test_2.py

# Real-time webcam detection (press 'q' to quit)
python detect_test_3.py
```

## Architecture

Three detection scripts share the same core pattern:

1. **Load model** — `YOLO("chip.pt")`, loaded once at module level
2. **Run inference** — `model(image_path)` or `model(frame)`
3. **Process results** — iterate `result.boxes`, extract `box.xyxy` coordinates and `box.cls` class index, resolve label via `model.names[int(box.cls[0])]`
4. **Render** — draw bounding boxes with OpenCV: blue `(255,0,0)` for good, red `(0,0,255)` for bad; display count text at top-left
5. **Output** — save result image (`detect_test_1.py`, `detect_test_2.py`) or show live feed (`detect_test_3.py`)

| Script | Input | Output | Output Dir |
|--------|-------|--------|------------|
| `detect_test_1.py` | Single image (`datasets/chip1.png`) | Image window + saved PNG | `out1/` |
| `detect_test_2.py` | All images in `datasets/` | Image windows (1s each) + saved PNGs + console summary | `out2/` |
| `detect_test_3.py` | Webcam (device `0`) | Live video window | None |

## Key Files

- `chip.pt` — Trained YOLO model (~5.5 MB) with two classes: `good` and `bad`
- `datasets/` — 20 test images (`chip1.png` through `chip20.png`)
