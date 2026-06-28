# Chip Quality Detector | 芯片质量检测器

基于 YOLO 的芯片好坏检测工具，自动识别图片中的芯片并区分 **good（好芯片）** 和 **bad（坏芯片）**，用蓝色框标记好芯片、红色框标记坏芯片。

A YOLO-based chip quality detection tool. It automatically detects chips in images, classifies them as **good** or **bad**, and marks them with blue boxes (good) and red boxes (bad).

---

## 快速开始 | Quick Start

```bash
# 1. 安装依赖 | Install dependencies
pip install ultralytics opencv-python

# 2. 单图片检测 (输出到 out1/) | Single image detection (outputs to out1/)
python detect_test_1.py

# 3. 批量检测 (输出到 out2/) | Batch detection (outputs to out2/)
python detect_test_2.py

# 4. 摄像头实时检测 (按 q 退出) | Webcam real-time detection (press q to quit)
python detect_test_3.py
```

---

## 项目结构 | Project Structure

```
├── chip.pt                 # 训练好的 YOLO 模型 | Trained YOLO model
├── datasets/               # 测试图片 20 张 | 20 test images
├── detect_test_1.py        # 单图片检测 | Single image detection
├── detect_test_2.py        # 批量图片检测 | Batch image detection
├── detect_test_3.py        # 摄像头实时检测 | Webcam real-time detection
├── detect_study_0*.py      # 单图片学习脚本 4 个 | 4 single-image study scripts
├── detect_study_2_0*.py   # 批量检测学习脚本 5 个 | 5 batch-detection study scripts
├── detect_test_*_doc.md    # 各脚本详细文档 | Detailed docs per script
└── Training/               # 模型训练素材与教程 | Model training materials & tutorial
```

---

## 三个检测脚本对比 | Script Comparison

| | `detect_test_1.py` | `detect_test_2.py` | `detect_test_3.py` |
|---|---|---|---|
| **用途 Purpose** | 单图片检测入门 | 批量图片检测 | 摄像头实时检测 |
| | Single image (beginner) | Batch processing | Real-time webcam |
| **输入 Input** | 1 张图片 (`datasets/chip1.png`) | `datasets/` 下所有图片 | 摄像头实时画面 |
| | | All images in `datasets/` | Live webcam feed |
| **输出 Output** | 弹出窗口 + 保存 1 张 PNG | 逐张弹出窗口 + 全部保存 PNG | 实时视频窗口 |
| | Popup window + 1 saved PNG | Popup per image + save all PNGs | Live video window |
| **输出目录 Output Dir** | `out1/` | `out2/` | 无 None |
| **退出方式 Exit** | 按任意键关闭窗口 | 每张显示 1 秒后自动切换 | 按 `q` 键退出 |
| | Press any key to close | Auto-advance every 1 sec | Press `q` to quit |
| **难度 Difficulty** | ★☆☆ 入门 Beginner | ★★☆ 中级 Intermediate | ★★☆ 中级 Intermediate |

| 功能点 Feature | `detect_test_1.py` | `detect_test_2.py` | `detect_test_3.py` |
|---|---|---|---|
| **循环方式 Loop** | 无（运行一次） No loop | `for` 遍历文件夹 Folder loop | `while True` 无限循环 Infinite |
| **数据保存 Save** | 保存图片 Save image | 保存图片 + 控制台汇总 Save + summary | 不保存 No save |
| **依赖库 Libraries** | `ultralytics`, `cv2`, `os` | `ultralytics`, `cv2`, `os` | `ultralytics`, `cv2` |
| **适用场景 Use Case** | 快速测试单张图片 Quick test | 批量质检大量图片 Batch QA | 产线实时监控 Live monitoring |

---

## 效果说明 | Detection Effects

| 类别 Category | 框颜色 Box Color | 标签 Label | BGR 颜色值 BGR Value |
|---|---|---|---|
| 好芯片 Good Chip | 蓝色 Blue | `good` | `(255, 0, 0)` |
| 坏芯片 Bad Chip | 红色 Red | `bad` | `(0, 0, 255)` |

检测结果会显示在图片/画面上：
- **检测框**：每个芯片周围绘制矩形框
- **标签**：框左上角显示类别名称（good / bad）
- **统计**：画面左上角显示 Good 和 Bad 的实时计数

The detection result is shown on the image/live feed:
- **Bounding box**: A rectangle drawn around each detected chip
- **Label**: Class name (good / bad) displayed above each box
- **Statistics**: Good and Bad counts displayed at the top-left corner

---

## 模型训练 | Model Training

`Training/` 目录包含模型训练与适配的完整素材，涵盖芯片检测和螺丝检测两个场景，展示如何从数据采集到模型训练、再到部署推理的全流程。

The `Training/` directory contains complete model training and adaptation materials covering both chip detection and screw detection scenarios, demonstrating the full pipeline from data collection to model training and deployment inference.

### 目录结构 | Directory Structure

```
Training/
├── 芯片检测模型训练 Chip Detection Model Training.pptx   # 训练教程PPT | Training tutorial slides
├── CHIP_DETECT/                                          # 芯片检测训练素材
│   ├── detect_chip.pt              # 训练产出模型 | Trained model output
│   ├── 芯片检测.zip                 # 训练数据集 | Training dataset
│   ├── 采集照片_2026-06-28.zip      # 采集的原始照片 | Raw collected photos
│   ├── original.png                # 原始图片示例 | Original image sample
│   ├── step1.png ~ step3.png       # 训练过程截图 | Training process screenshots
│   └── detect.png                  # 检测效果图 | Detection result
├── SCREW_DETECT/                                          # 螺丝检测训练素材
│   ├── detect_20260628_101833_812.pt  # 训练产出模型 | Trained model output
│   ├── SCREW_SIZE.zip                 # 螺丝尺寸数据集 | Screw size dataset
│   ├── screw_20260628.zip             # 螺丝原始数据集 | Raw screw dataset
│   ├── original.png                   # 原始图片示例 | Original image sample
│   ├── step1.png ~ step3.png          # 训练过程截图 | Training process screenshots
│   └── detect.png                     # 检测效果图 | Detection result
```

### 训练流程概览 | Training Pipeline Overview

| 步骤 Step | 内容 Content | 产出 Output |
|---|---|---|
| 1. 数据采集 Collection | 拍摄芯片/螺丝照片，打包为数据集 | `.zip` 原始数据集 |
| 2. 数据标注 Annotation | 标注目标区域与类别（good/bad 或尺寸类别） | 标注后的数据集 `.zip` |
| 3. 模型训练 Training | 使用标注数据集训练 YOLO 模型 | `.pt` 模型文件 |
| 4. 推理验证 Inference | 使用训练好的模型进行检测验证 | `detect.png` 检测结果图 |

### 两种检测场景对比 | Two Detection Scenarios

| | CHIP_DETECT | SCREW_DETECT |
|---|---|---|
| **检测对象 Target** | 芯片好坏 | 螺丝尺寸 |
| | Chip quality (good/bad) | Screw size classification |
| **模型文件 Model** | `detect_chip.pt` | `detect_20260628_101833_812.pt` |
| **数据集 Dataset** | `芯片检测.zip` | `SCREW_SIZE.zip` |
| **原始照片 Raw Photos** | `采集照片_2026-06-28.zip` | `screw_20260628.zip` |

> 💡 **学习建议**：先阅读 `芯片检测模型训练 Chip Detection Model Training.pptx` 了解完整训练流程，再对照 `CHIP_DETECT/` 和 `SCREW_DETECT/` 中的素材理解两个场景的模型适配方法。

---

## 学习路径 | Learning Path

建议按以下顺序学习（从简单到复杂）：

Recommended learning order (from simple to complex):

1. **`detect_test_1.py`** — 单图片检测入门，理解 YOLO 推理和 OpenCV 绘图的核心流程 | Learn the basic YOLO inference + OpenCV drawing pipeline
2. **`detect_study_01th.py` ~ `detect_study_04th.py`** — 单图片检测逐步深入的学习脚本 | Step-by-step single-image detection study scripts
3. **`detect_test_2.py`** — 批量处理，学习文件遍历和全局/局部计数器模式 | Learn file iteration and accumulator patterns
4. **`detect_study_2_01th.py` ~ `detect_study_2_05th.py`** — 批量检测逐步深入的学习脚本 | Step-by-step batch detection study scripts
5. **`detect_test_3.py`** — 实时摄像头检测，学习视频流处理和无限循环控制 | Learn video stream processing and infinite loop control
6. **`Training/` 模型训练** — 学习从数据采集、标注到 YOLO 模型训练的完整流程，掌握芯片检测和螺丝尺寸检测两个场景的模型适配方法 | Learn the full pipeline from data collection & annotation to YOLO model training, covering model adaptation for both chip detection and screw size detection

详细文档请查看各脚本对应的 `detect_test_*_doc.md` 文件。
For detailed documentation, see the corresponding `detect_test_*_doc.md` files.
