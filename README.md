# Chip Quality Detector

基于 YOLO 的芯片好坏检测工具，自动识别图片中的芯片并区分 good（好芯片）和 bad（坏芯片）。

## 快速开始

```bash
# 安装依赖
pip install ultralytics opencv-python

# 单张图片检测 → 输出至 out1/
python detect_test_1.py

# 批量检测 datasets/ 下所有图片 → 输出至 out2/
python detect_test_2.py

# 实时摄像头检测 → 按 q 退出
python detect_test_3.py
```

## 项目结构

```
├── chip.pt               # 训练好的 YOLO 模型
├── datasets/             # 测试图片 (20张)
├── detect_test_1.py      # 单图片检测
├── detect_test_2.py      # 批量图片检测
├── detect_test_3.py      # 实时摄像头检测
└── detect_test_*_doc.md  # 各脚本详细文档
```

## 效果说明

| 类别 | 检测框颜色 | 标签 |
|------|-----------|------|
| 好芯片 | 蓝色 | good |
| 坏芯片 | 红色 | bad |
