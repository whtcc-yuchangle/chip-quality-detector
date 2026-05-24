# 芯片实时检测程序文档 | Real-Time Chip Detection Program Documentation

## 一、程序概述 | Program Overview

本程序是基于 YOLO 目标检测框架的**实时芯片质量检测工具**，通过电脑摄像头实时捕获画面，自动识别芯片并统计好芯片（good）和坏芯片（bad）的数量。

This program is a **real-time chip quality detection tool** based on the YOLO object detection framework. It captures video from the computer camera, automatically identifies chips, and counts good and bad chips in real-time.

---

## 二、功能特性 | Features

| 功能 | 说明 |
|------|------|
| **实时检测** | 通过摄像头实时捕获并检测画面 |
| **目标检测** | 使用 YOLO 模型实时识别芯片 |
| **类别识别** | 区分 good（好芯片）和 bad（坏芯片） |
| **颜色标记** | 好芯片用蓝色框，坏芯片用红色框 |
| **实时统计** | 画面左上角实时显示芯片数量 |
| **快捷键退出** | 按 'q' 键退出检测 |

---

## 三、技术栈 | Tech Stack

| 技术 | 版本要求 | 说明 |
|------|---------|------|
| Python | ≥ 3.8 | 编程语言 |
| ultralytics | ≥ 8.0 | YOLO 目标检测库 |
| OpenCV | ≥ 4.0 | 图像处理与视频捕获库 |

---

## 四、文件结构 | File Structure

```
chip-quality-detector/
├── chip.pt               # 训练好的 YOLO 模型 | Trained YOLO model
└── detect_test_3.py      # 实时检测程序 | Real-time detection program
```

---

## 五、代码详解 | Code Explanation

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO  # YOLO 目标检测库
import cv2                    # 图像处理与视频捕获库
```

### 5.2 初始化模型和摄像头 | Initialize Model & Camera

```python
model = YOLO("chip.pt")   # 加载训练好的模型
cap = cv2.VideoCapture(0)      # 打开默认摄像头（0 或 1 可调）
```

**摄像头编号说明：**
- `0`: 通常是外接 USB 摄像头
- `1`: 通常是笔记本内置摄像头

### 5.3 主循环 - 实时检测 | Main Loop - Real-Time Detection

```python
while True:
    ret, frame = cap.read()
    if not ret:
        break  # 读取失败则退出
```

### 5.4 检测并统计 | Detection & Counting

```python
good_count = 0
bad_count = 0
results = model(frame)

for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = model.names[int(box.cls[0])]
        
        if label == "good":
            good_count += 1
            color = (255, 0, 0)  # 蓝色标记好芯片
        else:
            bad_count += 1
            color = (0, 0, 255)  # 红色标记坏芯片
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

### 5.5 显示统计信息 | Display Statistics

```python
cv2.putText(frame, f"Good: {good_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.putText(frame, f"Bad: {bad_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

### 5.6 显示画面并等待退出 | Show Frame & Wait for Exit

```python
cv2.imshow("Chip Real-Time Detection", frame)
if cv2.waitKey(50) & 0xFF == ord('q'):
    break
```

### 5.7 释放资源 | Release Resources

```python
cap.release()           # 释放摄像头
cv2.destroyAllWindows() # 关闭所有窗口
print("检测已结束！| Detection stopped!")
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
python detect_test_3.py
```

### 6.3 操作说明 | Instructions

1. 确保电脑已连接摄像头
2. 运行程序后会自动打开摄像头
3. 将芯片放置在摄像头前
4. 画面会实时显示检测结果
5. 按键盘 `q` 键退出检测

---

## 七、界面说明 | Interface Explanation

### 实时画面元素 | Real-Time Display Elements

- **检测框**：芯片周围的矩形框（蓝色=good，红色=bad）
- **标签文字**：检测框左上角显示类别名称
- **统计信息**：画面左上角显示两行文字
  - `Good: X` - 好芯片数量（蓝色）
  - `Bad: X` - 坏芯片数量（红色）

---

## 八、常见问题 | FAQ

**Q: 摄像头无法打开？**

A: 尝试修改 `cv2.VideoCapture(0)` 中的参数，将 `0` 改为 `1` 或其他数字。

**Q: 检测速度慢？**

A: 实时检测速度取决于电脑性能和模型大小，可尝试使用更轻量的模型。

**Q: 如何退出程序？**

A: 确保检测窗口处于激活状态，然后按键盘 `q` 键退出。

---

## 九、性能优化建议 | Performance Tips

1. **降低分辨率**：在 `cap.read()` 后添加 `frame = cv2.resize(frame, (640, 480))`
2. **使用更小模型**：使用 YOLOv8n（nano）版本
3. **减少检测频率**：增加 `cv2.waitKey()` 的参数值

---

*文档版本：v1.0 | Document Version: v1.0*
*创建日期：2026年5月 | Created: May 2026*