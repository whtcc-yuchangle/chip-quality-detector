# Chip Quality Detector | 芯片质量检测器

基于 YOLO 的芯片好坏检测工具，自动识别图片中的芯片并区分 good（好芯片）和 bad（坏芯片）。

A YOLO-based chip quality detection tool that automatically identifies chips in images and classifies them as **good** or **bad**.

---

## 快速开始 | Quick Start

```bash
# 安装依赖 | Install dependencies
pip install ultralytics opencv-python

# 单张图片检测 → 输出至 out1/ | Single image detection → outputs to out1/
python detect_test_1.py

# 批量检测 datasets/ 下所有图片 → 输出至 out2/ | Batch detection → outputs to out2/
python detect_test_2.py

# 实时摄像头检测 → 按 q 退出 | Real-time webcam detection → press q to quit
python detect_test_3.py
```

## 项目结构 | Project Structure

```
├── chip.pt                 # 训练好的 YOLO 模型 | Trained YOLO model
├── datasets/               # 测试图片 (20张) | Test images (20 images)
├── detect_test_1.py        # 单图片检测 | Single image detection
├── detect_test_2.py        # 批量图片检测 | Batch image detection
├── detect_test_3.py        # 实时摄像头检测 | Real-time webcam detection
├── detect_study_01th.py    # 学习脚本 01 | Study script 01
├── detect_study_02th.py    # 学习脚本 02 | Study script 02
├── detect_study_03th.py    # 学习脚本 03 | Study script 03
├── detect_study_04th.py    # 学习脚本 04 | Study script 04
└── detect_test_*_doc.md    # 各脚本详细文档 | Detailed documentation for each script
```

## 效果说明 | Detection Effects

| 类别 Category | 检测框颜色 Bounding Box | 标签 Label |
|---------------|------------------------|------------|
| 好芯片 Good Chip | 蓝色 Blue | good |
| 坏芯片 Bad Chip | 红色 Red | bad |

## 三个检测脚本对比 | Three Detection Scripts Comparison

| 脚本 Script | 输入 Input | 输出 Output | 输出目录 Output Dir |
|-------------|-----------|-------------|-------------------|
| `detect_test_1.py` | 单张图片 (`datasets/chip1.png`) | 图片窗口 + 保存 PNG | `out1/` |
| `detect_test_2.py` | `datasets/` 中所有图片 | 图片窗口 (每张1秒) + 保存 PNG + 控制台汇总 | `out2/` |
| `detect_test_3.py` | 摄像头 (设备 `0`) | 实时视频窗口 | 无 None |

## 学习路径 | Learning Path

建议按以下顺序学习本项目的代码（从简单到复杂）：

Recommended learning order for the code in this project (from simple to complex):

1. `detect_test_1.py` — 单图片检测入门 | Single image detection basics
2. `detect_study_01th.py` ~ `detect_study_04th.py` — 逐步深入的学习脚本 | Step-by-step study scripts
3. `detect_test_2.py` — 批量图片处理 | Batch image processing
4. `detect_test_3.py` — 实时摄像头检测 | Real-time webcam detection
