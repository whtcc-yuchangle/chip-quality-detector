# 芯片检测程序文档 | Chip Detection Program Documentation

## 一、程序概述 | Program Overview

本程序是一个基于 YOLO 目标检测框架的芯片质量检测工具，用于自动识别图片中的芯片并统计好芯片（good）和坏芯片（bad）的数量。

This program is a chip quality detection tool based on the YOLO object detection framework. It automatically identifies chips in images and counts the number of good chips and bad chips.

---

## 二、功能特性 | Features

| 功能 | 说明 |
|------|------|
| **目标检测** | 使用YOLO模型检测图片中的芯片位置 |
| **类别识别** | 区分芯片是 good（好芯片）还是 bad（坏芯片） |
| **颜色区分** | 好芯片用蓝色框标记，坏芯片用红色框标记 |
| **数量统计** | 统计并显示好芯片和坏芯片的数量 |
| **结果保存** | 自动保存检测结果到指定目录 |
| **图片预览** | 弹出窗口显示检测后的图片 |

---

## 三、技术栈 | Tech Stack

| 技术 | 版本要求 | 说明 |
|------|---------|------|
| Python | ≥ 3.8 | 编程语言 |
| ultralytics | ≥ 8.0 | YOLO目标检测库 |
| OpenCV | ≥ 4.0 | 图像处理库 |
| os | 内置库 | 文件系统操作 |

---

## 四、文件结构 | File Structure

```
chip-quality-detector/
├── chip.pt               # 训练好的YOLO模型文件 | Trained YOLO model
├── datasets/
│   └── chip1.png         # 待检测的芯片图片 | Image to detect
├── detect_test_1.py      # 主程序文件 | Main program file
└── out1/                 # 结果输出目录 | Output directory (auto-created)
    └── chip1.png         # 检测结果图片 | Detection result
```

---

## 五、代码详解 | Code Explanation

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO  # YOLO目标检测库
import cv2                    # 图像处理库
import os                     # 文件系统操作
```

### 5.2 核心配置 | Core Configuration

```python
model = YOLO("chip.pt")    # 加载训练好的芯片检测模型
image_path = "datasets/chip1.png" # 待检测图片路径
output_dir = "out1"             # 结果保存目录
```

### 5.3 目录创建 | Create Output Directory

```python
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
```

自动创建输出目录，避免文件保存失败。

### 5.4 图片读取与初始化 | Image Reading & Initialization

```python
img = cv2.imread(image_path)    # 读取图片
good_count = 0                  # 好芯片计数器
bad_count = 0                   # 坏芯片计数器
```

### 5.5 执行检测 | Run Detection

```python
results = model(image_path)
```

调用YOLO模型执行目标检测。

### 5.6 遍历检测结果 | Process Detection Results

```python
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # 获取检测框坐标
        label = model.names[int(box.cls[0])]     # 获取类别标签
        
        if label == "good":
            good_count += 1
            color = (255, 0, 0)  # 蓝色标记好芯片
        else:
            bad_count += 1
            color = (0, 0, 255)  # 红色标记坏芯片
        
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)  # 绘制检测框
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)  # 绘制标签
```

**关键逻辑说明：**
- `box.xyxy[0]`: 获取检测框的四个坐标 (x1, y1, x2, y2)
- `box.cls[0]`: 获取检测目标的类别索引
- `model.names[]`: 根据索引获取类别名称（good/bad）
- 颜色区分：好芯片使用蓝色，坏芯片使用红色

### 5.7 绘制统计信息 | Draw Statistics

```python
cv2.putText(img, f"Good: {good_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.putText(img, f"Bad: {bad_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

在图片左上角显示两行统计文字：
- 第一行：Good 数量（蓝色）
- 第二行：Bad 数量（红色）

### 5.8 保存与显示结果 | Save & Display Result

```python
cv2.imwrite(f"{output_dir}/{filename}", img)  # 保存结果图片
cv2.imshow("Chip Detection Result", img)      # 显示图片窗口
cv2.waitKey(0)                                # 等待按键关闭
cv2.destroyAllWindows()                       # 关闭窗口
```

### 5.9 打印结果 | Print Results

```python
print("检测完成！| Detection completed!")
print(f"好芯片：{good_count} | Good chips: {good_count}")
print(f"坏芯片：{bad_count} | Bad chips: {bad_count}")
print(f"结果已保存至 out1/ | Result saved to out1/")
```

---

## 六、使用方法 | Usage

### 6.1 安装依赖 | Install Dependencies

```bash
pip install ultralytics opencv-python
```

### 6.2 运行程序 | Run Program

```bash
cd chip-quality-detector
python detect_test_1.py
```

### 6.3 操作说明 | Instructions

1. 程序运行后会自动加载模型并检测图片
2. 检测完成后会弹出显示窗口，显示检测结果
3. 按键盘任意键关闭显示窗口
4. 检测结果图片保存在 `out1/` 目录 | Result image saved in `out1/` directory

---

## 七、输出说明 | Output Explanation

### 7.1 图片输出 | Image Output

检测后的图片包含以下元素：
- **检测框**：每个芯片周围的矩形框（蓝色=good，红色=bad）
- **标签文字**：每个检测框左上角显示类别名称（good/bad）
- **统计信息**：图片左上角显示两行统计文字

### 7.2 控制台输出 | Console Output

```
检测完成！| Detection completed!
好芯片：5 | Good chips: 5
坏芯片：2 | Bad chips: 2
结果已保存至 out1/ | Result saved to out1/
```

---

## 八、扩展建议 | Extension Suggestions

1. **批量检测**：可修改代码支持批量检测多个图片
2. **视频检测**：扩展支持视频流实时检测
3. **结果报表**：生成检测报告文档
4. **Web界面**：开发网页版检测工具

---

## 九、常见问题 | FAQ

**Q: 运行时提示模型文件找不到？**

A: 确保 `chip.pt` 文件位于程序运行目录下。

**Q: 检测结果不准确？**

A: 可能需要重新训练模型，增加训练数据量或调整训练参数。

**Q: 显示窗口无法关闭？**

A: 确保图片窗口处于激活状态，然后按任意键关闭。

---

*文档版本：v1.0 | Document Version: v1.0*
*创建日期：2026年5月 | Created: May 2026*