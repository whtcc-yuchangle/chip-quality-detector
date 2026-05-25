# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
此文件为 Claude Code 提供代码仓库的操作指引。

## Project Overview | 项目概述

Chip quality detection using YOLO (ultralytics) and OpenCV. The trained model (`chip.pt`) classifies chips as **good** or **bad**. Three scripts cover single-image, batch, and real-time webcam detection.

使用 YOLO (ultralytics) 和 OpenCV 进行芯片质量检测。训练好的模型 (`chip.pt`) 将芯片分类为 **good**（好芯片）或 **bad**（坏芯片）。三个脚本分别覆盖单图片检测、批量检测和实时摄像头检测。

## Commands | 常用命令

```bash
# 安装依赖 | Install dependencies
pip install ultralytics opencv-python

# 单图片检测 (输出至 out1/) | Single image detection (outputs to out1/)
python detect_test_1.py

# 批量检测 datasets/ 下所有图片 (输出至 out2/) | Batch detection (outputs to out2/)
python detect_test_2.py

# 实时摄像头检测 (按 q 退出) | Real-time webcam detection (press 'q' to quit)
python detect_test_3.py

# 单图片检测学习脚本 (逐步深入) | Single-image study scripts (progressive)
python detect_study_01th.py
python detect_study_02th.py
python detect_study_03th.py
python detect_study_04th.py

# 批量检测学习脚本 (逐步深入) | Batch-detection study scripts (progressive)
python detect_study_2_01th.py
python detect_study_2_02th.py
python detect_study_2_03th.py
python detect_study_2_04th.py
python detect_study_2_05th.py
```

## Architecture | 架构

Three detection scripts share the same core pattern:
三个检测脚本共享相同的核心模式：

1. **Load model | 加载模型** — `YOLO("chip.pt")`, loaded once at module level (模块级别加载一次)
2. **Run inference | 运行推理** — `model(image_path)` or `model(frame)`
3. **Process results | 处理结果** — iterate `result.boxes`, extract `box.xyxy` coordinates and `box.cls` class index, resolve label via `model.names[int(box.cls[0])]` (遍历检测框，提取坐标和类别索引，通过字典解析标签)
4. **Render | 渲染** — draw bounding boxes with OpenCV: blue `(255,0,0)` for good, red `(0,0,255)` for bad; display count text at top-left (用 OpenCV 绘制检测框：好芯片蓝色，坏芯片红色；左上角显示统计数量)
5. **Output | 输出** — save result image (`detect_test_1.py`, `detect_test_2.py`) or show live feed (`detect_test_3.py`) — 保存结果图片或显示实时视频流

Two series of progressive study scripts break down single-image and batch detection step by step:
两组逐步深入的学习脚本，分别拆解单图片检测和批量检测：

| Series | Scripts | Based On | Description |
|--------|---------|----------|-------------|
| Single-image | `detect_study_01th.py` ~ `detect_study_04th.py` | `detect_test_1.py` | 4 steps: read/display → detection → counters → save | 4 步：读取显示 → 检测 → 计数 → 保存 |
| Batch | `detect_study_2_01th.py` ~ `detect_study_2_05th.py` | `detect_test_2.py` | 5 steps: read/display → detection → per-image stats → global summary → save | 5 步：读取显示 → 检测 → 单图统计 → 全局汇总 → 保存 |

| Script | Input | Output | Output Dir |
|--------|-------|--------|------------|
| `detect_test_1.py` | Single image (`datasets/chip1.png`) | Image window + saved PNG | `out1/` |
| `detect_test_2.py` | All images in `datasets/` | Image windows (1s each) + saved PNGs + console summary | `out2/` |
| `detect_test_3.py` | Webcam (device `0`) | Live video window | None |

## Key Files | 关键文件

- `chip.pt` — Trained YOLO model (~5.5 MB) with two classes: `good` and `bad` | 训练好的 YOLO 模型 (~5.5 MB)，包含两个类别：good 和 bad
- `datasets/` — 20 test images (`chip1.png` through `chip20.png`) | 20 张测试图片
- `detect_study_01th.py` ~ `detect_study_04th.py` — Progressive single-image study scripts | 单图片检测逐步学习脚本
- `detect_study_2_01th.py` ~ `detect_study_2_05th.py` — Progressive batch-detection study scripts | 批量检测逐步学习脚本
