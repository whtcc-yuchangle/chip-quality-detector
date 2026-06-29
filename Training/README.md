# Training — 模型训练素材与教程 | Model Training Materials & Tutorials

本目录包含芯片质量检测和螺丝尺寸检测两个场景的完整模型训练素材、数据集、训练好的模型以及应用脚本。
This directory contains complete model training materials, datasets, trained models, and application scripts for two detection scenarios: chip quality detection and screw size detection.

---

## 📁 目录总览 | Directory Overview

```
Training/
├── 芯片检测模型训练 Chip Detection Model Training.pptx   # 训练教程PPT | Training tutorial slides
├── CHIP_DETECT/                                          # 芯片检测训练素材 | Chip detection training materials
├── SCREW_DETECT/                                         # 螺丝检测训练素材 | Screw detection training materials
└── screw_applicaions/                                    # 螺丝检测应用脚本 | Screw detection application scripts
```

---

## 🎞️ 芯片检测模型训练 Chip Detection Model Training.pptx

全面的模型训练教程幻灯片，以截图方式逐步演示如何使用在线标注和训练平台完成从数据采集、标注、训练到模型导出的完整流程。
A comprehensive training tutorial slide deck that demonstrates, step by step with screenshots, how to complete the full pipeline from data collection, annotation, and training to model export using an online annotation and training platform.

---

## 🔬 CHIP_DETECT/ — 芯片检测训练素材 | Chip Detection Training Materials

芯片质量检测场景的模型训练产物，包含数据集、训练截图和训练好的模型文件。
Training outputs for the chip quality detection scenario, including datasets, training screenshots, and the trained model file.

| 文件 File | 说明 Description |
|-----------|-----------------|
| `芯片检测.zip` | 芯片检测标注数据集（用于 YOLO 训练）\| Annotated dataset for chip detection (used for YOLO training) |
| `采集照片_2026-06-28.zip` | 原始采集照片（2026-06-28）\| Raw collected photos (2026-06-28) |
| `step1.png` | 训练步骤 1 — 数据准备与上传 \| Training step 1 — Data preparation & upload |
| `step2.png` | 训练步骤 2 — 模型配置与训练参数设置 \| Training step 2 — Model config & training parameters |
| `step3.png` | 训练步骤 3 — 训练完成与模型下载 \| Training step 3 — Training completion & model download |
| `original.png` | 训练前的原始图片示例 \| Example original image before training |
| `detect.png` | 训练后模型的检测效果示例 \| Example detection result after training |
| `detect_chip.pt` | 训练好的芯片检测 YOLO 模型（2 分类：good / bad）\| Trained YOLO model for chip detection (2 classes: good / bad) |

---

## 🔩 SCREW_DETECT/ — 螺丝检测训练素材 | Screw Detection Training Materials

螺丝尺寸分类检测场景的模型训练产物，包含数据集、训练截图和训练好的模型文件。
Training outputs for the screw size classification scenario, including datasets, training screenshots, and the trained model file.

| 文件 File | 说明 Description |
|-----------|-----------------|
| `SCREW_SIZE.zip` | 螺丝尺寸标注数据集（用于 YOLO 训练）\| Annotated dataset for screw size detection (used for YOLO training) |
| `screw_20260628.zip` | 螺丝原始采集数据（2026-06-28）\| Raw screw collection data (2026-06-28) |
| `step1.png` | 训练步骤 1 — 数据准备与上传 \| Training step 1 — Data preparation & upload |
| `step2.png` | 训练步骤 2 — 模型配置与训练参数设置 \| Training step 2 — Model config & training parameters |
| `step3.png` | 训练步骤 3 — 训练完成与模型下载 \| Training step 3 — Training completion & model download |
| `original.png` | 训练前的原始图片示例 \| Example original image before training |
| `detect.png` | 训练后模型的检测效果示例 \| Example detection result after training |
| `detect_20260628_101833_812.pt` | 训练好的螺丝尺寸检测 YOLO 模型（3 分类：large / medium / small）\| Trained YOLO model for screw size detection (3 classes: large / medium / small) |

---

## 🖥️ screw_applicaions/ — 螺丝检测应用脚本 | Screw Detection Application Scripts

基于训练好的螺丝检测模型（`screw.pt`）开发的学习和应用脚本，按照逐步深入的方式拆解单图片检测和批量检测流程。该目录结构与项目根目录的芯片检测脚本镜像对应。
Learning and application scripts based on the trained screw detection model (`screw.pt`), progressively breaking down single-image detection and batch detection workflows. The structure mirrors the chip detection scripts in the project root.

### 文件清单 | File List

| 文件 File | 说明 Description |
|-----------|-----------------|
| `screw.pt` | 训练好的螺丝尺寸检测 YOLO 模型 \| Trained YOLO model for screw size detection |
| `datasets/` | 测试图片集（35 张，`0001.png` ~ `0035.png`）\| Test image set (35 images, `0001.png` ~ `0035.png`) |

### 脚本分类 | Script Categories

#### 单图片检测学习脚本（4 步递进）\| Single-Image Detection Study Scripts (4 Progressive Steps)

基于根目录 `detect_test_1.py` 的模式，逐步拆解单图片检测流程。
Based on the root-level `detect_test_1.py` pattern, progressively breaking down the single-image detection workflow.

| 脚本 Script | 学习内容 | What You Learn | 输出 Output |
|-------------|---------|----------------|-------------|
| `detect_study_01th.py` | 读取并显示图片 | Read & display an image | 弹出图片窗口 \| Image popup window |
| `detect_study_02th.py` | 运行 YOLO 模型进行检测 | Run YOLO model for detection | 控制台输出检测结果 \| Console detection output |
| `detect_study_03th.py` | 统计检测到的螺丝数量（大/中/小）\| Count detected screws (large/medium/small) | 控制台输出分类计数 \| Console class counts |
| `detect_study_04th.py` | 保存检测结果图片 | Save detection result image | 输出至 `out1/` \| Output to `out1/` |

#### 批量检测学习脚本（5 步递进）\| Batch Detection Study Scripts (5 Progressive Steps)

基于根目录 `detect_test_2.py` 的模式，逐步拆解批量检测流程。
Based on the root-level `detect_test_2.py` pattern, progressively breaking down the batch detection workflow.

| 脚本 Script | 学习内容 | What You Learn | 输出 Output |
|-------------|---------|----------------|-------------|
| `detect_study_2_01th.py` | 读取并显示单张图片 | Read & display a single image | 弹出图片窗口 \| Image popup window |
| `detect_study_2_02th.py` | 对单张图片运行 YOLO 检测 | Run YOLO detection on a single image | 控制台输出检测结果 \| Console detection output |
| `detect_study_2_03th.py` | 统计单张图片的螺丝分类数量 | Count screws per class in one image | 控制台输出单图分类计数 \| Console per-image class counts |
| `detect_study_2_04th.py` | 遍历文件夹批量检测并汇总全局统计 | Iterate folder for batch detection with global summary | 控制台输出全局汇总 \| Console global summary |
| `detect_study_2_05th.py` | 保存每张图片的检测结果 | Save detection result for each image | 输出至 `out2/` \| Output to `out2/` |

### 脚本核心模式 | Core Script Pattern

所有检测脚本共享相同的核心模式，便于学习和扩展：
All detection scripts share the same core pattern, designed for easy learning and extension:

1. **加载模型 \| Load Model** — `YOLO("screw.pt")`，模块级别加载一次 \| loaded once at module level
2. **运行推理 \| Run Inference** — `model(image_path)` 或 `model(frame)` \| or `model(frame)`
3. **处理结果 \| Process Results** — 遍历 `result.boxes`，提取坐标 `box.xyxy` 和类别 `box.cls`，通过 `model.names[int(box.cls[0])]` 解析标签（large / medium / small）\| iterate detection boxes, extract coordinates and class index, resolve labels via model names dictionary
4. **渲染 \| Render** — 使用 OpenCV 绘制检测框和标签 \| draw bounding boxes and labels with OpenCV
5. **输出 \| Output** — 保存结果图片到 `out1/`（单图片）或 `out2/`（批量）\| save result images

### 使用方式 | How to Run

```bash
# 单图片检测学习脚本（逐步深入）| Single-image study scripts (progressive)
python screw_applicaions/detect_study_01th.py
python screw_applicaions/detect_study_02th.py
python screw_applicaions/detect_study_03th.py
python screw_applicaions/detect_study_04th.py

# 批量检测学习脚本（逐步深入）| Batch-detection study scripts (progressive)
python screw_applicaions/detect_study_2_01th.py
python screw_applicaions/detect_study_2_02th.py
python screw_applicaions/detect_study_2_03th.py
python screw_applicaions/detect_study_2_04th.py
python screw_applicaions/detect_study_2_05th.py
```

---

## 🔗 与项目根目录的关系 | Relationship to Project Root

| 项目根目录 Project Root | Training/ 对应内容 Training/ Counterpart |
|--------------------------|------------------------------------------|
| `chip.pt` | `CHIP_DETECT/detect_chip.pt`（训练产物 \| training output） |
| `detect_test_1.py` | `screw_applicaions/detect_study_01th~04th.py`（螺丝场景教学版 \| screw scenario teaching version） |
| `detect_test_2.py` | `screw_applicaions/detect_study_2_01th~05th.py`（螺丝场景教学版 \| screw scenario teaching version） |
| `datasets/`（chip1~chip20.png）| `screw_applicaions/datasets/`（0001~0035.png） |
| — | `SCREW_DETECT/`（螺丝训练全过程记录 \| screw training full process record） |

---

## 📦 依赖 | Dependencies

```bash
pip install ultralytics opencv-python
```
