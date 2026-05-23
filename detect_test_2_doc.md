# 芯片批量检测程序文档 | Batch Chip Detection Program Documentation

## 一、程序概述 | Program Overview

本程序是基于 YOLO 目标检测框架的**批量芯片质量检测工具**，能够自动检测 `datasets` 文件夹中的所有图片，统计每张图片中的好芯片（good）和坏芯片（bad）数量，并生成汇总报告。

This program is a **batch chip quality detection tool** based on the YOLO object detection framework. It automatically detects all images in the `datasets` folder, counts the number of good and bad chips in each image, and generates a summary report.

---

## 二、功能特性 | Features

| 功能 | 说明 |
|------|------|
| **批量处理** | 自动遍历 datasets 文件夹中的所有图片 |
| **目标检测** | 使用 YOLO 模型检测每张图片中的芯片 |
| **类别识别** | 区分 good（好芯片）和 bad（坏芯片） |
| **颜色标记** | 好芯片用蓝色框，坏芯片用红色框 |
| **单图统计** | 每张图片显示各自的芯片数量 |
| **汇总统计** | 统计所有图片的芯片总数 |
| **自动保存** | 每张检测结果自动保存到 out2 目录 |
| **图片预览** | 每张图片检测后显示 1 秒 |

---

## 三、技术栈 | Tech Stack

| 技术 | 版本要求 | 说明 |
|------|---------|------|
| Python | ≥ 3.8 | 编程语言 |
| ultralytics | ≥ 8.0 | YOLO 目标检测库 |
| OpenCV | ≥ 4.0 | 图像处理库 |
| os | 内置库 | 文件系统操作 |

---

## 四、文件结构 | File Structure

```
chip_detect/
├── chip_best.pt          # 训练好的 YOLO 模型 | Trained YOLO model
├── datasets/             # 待检测图片目录 | Image folder to detect
│   ├── chip1.png
│   ├── chip2.png
│   └── ... (其他图片)
├── detect_test_2.py      # 批量检测程序 | Batch detection program
└── out2/                 # 结果输出目录 | Output directory (auto-created)
    ├── chip1.png
    ├── chip2.png
    └── ... (检测后的图片)
```

---

## 五、代码详解 | Code Explanation

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO  # YOLO 目标检测库
import cv2                    # 图像处理库
import os                     # 文件系统操作
```

### 5.2 配置参数 | Configuration

```python
model = YOLO("chip_best.pt")   # 加载模型
input_folder = "datasets"      # 输入图片文件夹
output_dir = "out2"            # 输出结果文件夹
```

### 5.3 创建输出目录 | Create Output Directory

```python
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
```

### 5.4 初始化计数器 | Initialize Counters

```python
total_good = 0   # 所有图片的好芯片总数
total_bad = 0    # 所有图片的坏芯片总数
total_imgs = 0   # 处理的图片总数
```

### 5.5 遍历图片文件夹 | Iterate Through Images

```python
for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    total_imgs += 1
    img = cv2.imread(img_path)
    current_good = 0
    current_bad = 0
```

### 5.6 执行检测并处理结果 | Run Detection & Process Results

```python
results = model(img)
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = model.names[int(box.cls[0])]
        
        if label == "good":
            current_good += 1
            color = (255, 0, 0)  # 蓝色
        else:
            current_bad += 1
            color = (0, 0, 255)  # 红色
        
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

### 5.7 更新统计并保存 | Update Stats & Save

```python
total_good += current_good
total_bad += current_bad
cv2.putText(img, f"Good: {current_good}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.putText(img, f"Bad: {current_bad}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow(f"Result - {filename}", img)
save_path = os.path.join(output_dir, filename)
cv2.imwrite(save_path, img)
cv2.waitKey(1000)  # 显示 1 秒
cv2.destroyAllWindows()
```

### 5.8 输出汇总报告 | Print Summary

```python
print("="*60)
print("批量检测完成！| Batch detection completed!")
print(f"总检测图片数量 | Total images: {total_imgs}")
print(f"所有图片总好芯片数 | Total good chips: {total_good}")
print(f"所有图片总坏芯片数 | Total bad chips: {total_bad}")
print(f"处理后图片已保存至 | Processed images saved to: {output_dir}")
print("="*60)
```

---

## 六、使用方法 | Usage

### 6.1 安装依赖 | Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 6.2 运行程序 | Run Program

```bash
cd /home/uw/桌面/chip_detect
python detect_test_2.py
```

### 6.3 操作说明 | Instructions

1. 确保 `datasets` 文件夹中有待检测的图片
2. 运行程序后会自动处理所有图片
3. 每张图片检测后会显示 1 秒
4. 检测结果保存在 `out2` 目录
5. 最后显示汇总统计报告

---

## 七、输出示例 | Output Example

### 控制台输出 | Console Output

```
============================================================
批量检测完成！| Batch detection completed!
总检测图片数量 | Total images: 20
所有图片总好芯片数 | Total good chips: 156
所有图片总坏芯片数 | Total bad chips: 23
处理后图片已保存至 | Processed images saved to: out2
============================================================
```

---

## 八、注意事项 | Notes

- 图片格式需为常见格式（PNG、JPG、JPEG 等）
- 若 datasets 文件夹为空，程序会处理 0 张图片
- 每张图片显示 1 秒后自动关闭

---

*文档版本：v1.0 | Document Version: v1.0*
*创建日期：2026年5月 | Created: May 2026*