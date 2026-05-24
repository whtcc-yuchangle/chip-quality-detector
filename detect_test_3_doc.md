# 芯片实时检测程序文档 | Real-Time Chip Detection Program Documentation

> 本文档面向马来西亚学生培训使用，提供完整的中英文双语说明。
> This document is designed for Malaysian student training, with complete bilingual Chinese-English explanations.

---

## 一、程序概述 | 1. Program Overview

本程序是基于 **YOLO (You Only Look Once)** 目标检测框架的**实时芯片质量检测工具**。它通过电脑摄像头（Webcam）实时捕获画面，对每一帧画面进行芯片目标检测，自动识别芯片并在实时画面中绘制检测框，区分好芯片（good）和坏芯片（bad），同时在画面中实时更新统计数量。用户按键盘上的 **`q`** 键即可退出检测。

This program is a **real-time chip quality detection tool** based on the **YOLO (You Only Look Once)** object detection framework. It captures live video from the computer's webcam, performs chip detection on every frame, automatically identifies chips and draws bounding boxes in the live feed, classifies them as good or bad, and updates the count statistics on screen in real-time. Press the **`q`** key to exit.

**与前两个脚本的关系 | Relationship with the previous two scripts:**

| 脚本 Script | 输入 Input | 输出 Output | 核心差异 Key Difference |
|------------|-----------|-------------|----------------------|
| `detect_test_1.py` | 1 张静态图片 1 static image | 1 张结果图片 1 result image | 最基本的检测流程 Basic detection flow |
| `detect_test_2.py` | 文件夹中所有图片 All images in folder | 批量结果图片 Batch result images | 批量处理 + 汇总报告 Batch processing + summary |
| `detect_test_3.py` | 摄像头实时视频流 Live webcam feed | 实时画面 + 无文件保存 Real-time display, no file saved | 实时视频流 + 无限循环 + 按键退出 Real-time + infinite loop + key-to-exit |

---

## 二、功能特性 | 2. Features

| 功能 Feature | 说明 Description |
|-------------|-----------------|
| **实时检测 Real-Time Detection** | 通过摄像头实时捕获并检测每一帧画面，延迟通常在 100-300ms | Capture and detect every frame from the webcam in real-time, typical latency 100-300ms |
| **目标检测 Object Detection** | 使用 YOLO 模型在每一帧中实时识别所有芯片的位置 | Use the YOLO model to identify all chip positions in every frame |
| **类别识别 Classification** | 自动区分画面中的 good（好芯片）和 bad（坏芯片） | Automatically classify each chip as good or bad in the live feed |
| **颜色标记 Color Coding** | 好芯片用**蓝色**框标记，坏芯片用**红色**框标记 | Good chips marked with **blue** boxes, bad chips with **red** boxes |
| **实时统计 Live Statistics** | 画面左上角实时更新当前帧中的好/坏芯片数量 | Live-updating good/bad chip counts displayed at the top-left corner |
| **快捷键退出 Quick Exit** | 按下键盘 **`q`** 键即可安全退出检测程序 | Press the **`q`** key on the keyboard to safely exit the detection program |

---

## 三、技术栈 | 3. Tech Stack

| 技术 Technology | 版本要求 Version | 说明 Description |
|----------------|-----------------|-----------------|
| Python | ≥ 3.8 | 编程语言，建议 3.9+ | Programming language, 3.9+ recommended |
| ultralytics | ≥ 8.0 | YOLO 目标检测框架，提供推理接口 | YOLO object detection framework, provides inference API |
| OpenCV (cv2) | ≥ 4.0 | 图像处理 + 视频捕获 + 窗口显示，核心依赖 | Image processing + video capture + window display, core dependency |

注意：本程序不需要 `os` 库，因为没有文件读写操作。所有检测都在内存中进行。
Note: This script does not need the `os` library because there are no file read/write operations. All detection happens in memory.

---

## 四、文件结构 | 4. File Structure

```
chip-quality-detector/
├── chip.pt               # 训练好的 YOLO 模型 (~5.5 MB)
│                         # Trained YOLO model (~5.5 MB)
└── detect_test_3.py      # 实时摄像头检测程序
    (detect_test_3.py)    # Real-time webcam detection program
```

本程序**不需要** `datasets/` 目录（没有输入图片）和输出目录（不保存任何文件）。所有数据来自摄像头实时流，结果仅显示在屏幕上。
This script does **not** need the `datasets/` directory (no input images) or an output directory (no files are saved). All data comes from the live webcam stream, and results are displayed on screen only.

---

## 五、代码详解 | 5. Code Explanation

本部分逐段解释 `detect_test_3.py` 的代码，重点说明实时检测与静态图片检测的核心差异。
This section explains the code of `detect_test_3.py` in detail, focusing on the key differences between real-time and static image detection.

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO  # YOLO 目标检测库 | YOLO object detection library
import cv2                    # OpenCV - 同时用于视频捕获和图像处理
                              # OpenCV - used for both video capture and image processing
```

本程序只需两个依赖库：
This script only needs two dependencies:
- `ultralytics`：加载 YOLO 模型并执行推理 | Load YOLO model and run inference
- `cv2`：**既用于视频捕获（`VideoCapture`），又用于图像处理和窗口显示** | **Used for both video capture (`VideoCapture`) and image processing/display**

### 5.2 初始化模型和摄像头 | Initialize Model & Camera

```python
model = YOLO("chip.pt")       # 加载训练好的芯片检测模型 | Load the trained chip detection model

cap = cv2.VideoCapture(0)     # 打开摄像头设备 | Open the webcam device
                              # 参数 0 = 第一个摄像头 (通常是外接 USB 摄像头)
                              # Parameter 0 = first camera (usually external USB webcam)
                              # 参数 1 = 第二个摄像头 (通常是笔记本内置摄像头)
                              # Parameter 1 = second camera (usually built-in laptop camera)
```

**摄像头编号详解 | Camera Index Details:**

| 参数 Parameter | 通常对应 Typically Maps To | 说明 Note |
|---------------|--------------------------|----------|
| `0` | 外接 USB 摄像头 External USB webcam | 大多数台式机的默认摄像头 |
| `1` | 笔记本内置摄像头 Built-in laptop camera | 笔记本用户可能需要使用此参数 |
| `-1` | 让 OpenCV 自动选择 | 部分系统支持，效果不稳定 |
| 视频文件路径 | 读取视频文件 | 如 `cv2.VideoCapture("video.mp4")` |

**如果摄像头无法打开怎么办？| What if the camera fails to open?**
- 首先尝试将 `0` 改为 `1` | First try changing `0` to `1`
- 检查是否有其他程序占用了摄像头 | Check if another program is using the camera
- 确认摄像头驱动已正确安装 | Verify the camera driver is properly installed
- 运行 `cap.isOpened()` 检查摄像头是否成功打开 | Run `cap.isOpened()` to check if the camera opened successfully

### 5.3 主循环 - 实时检测 | Main Loop - Real-Time Detection

```python
while True:                        # 无限循环，持续检测每一帧 | Infinite loop, continuously detect every frame
    ret, frame = cap.read()        # 从摄像头读取一帧画面 | Read one frame from the webcam
                                   # ret: bool - 是否成功读取 | True if frame read successfully
                                   # frame: 图像数据 (NumPy 数组) | Image data (NumPy array)
    if not ret:
        break                      # 读取失败则退出循环 (如摄像头被拔出) | Exit if read fails (e.g., camera unplugged)
```

**`cap.read()` 返回值详解 | Return Values of `cap.read()`:**

| 返回值 Return Value | 类型 Type | 含义 Meaning |
|-------------------|---------|-------------|
| `ret` | `bool` | `True` = 成功读取帧 | Frame read successfully; `False` = 失败（摄像头断连等）|
| `frame` | `numpy.ndarray` | 图像数据矩阵，shape 为 `(高度, 宽度, 3)` 的 BGR 图像 | Image data as a BGR image with shape `(height, width, 3)` |

### 5.4 检测并统计 | Detection & Counting

```python
    good_count = 0                   # 当前帧中好芯片计数 (每帧重置) | Good count for current frame (reset each frame)
    bad_count = 0                    # 当前帧中坏芯片计数 | Bad count for current frame

    results = model(frame)           # 对当前帧运行 YOLO 推理 | Run YOLO inference on current frame

    for result in results:           # 遍历推理结果 | Iterate over inference results
        for box in result.boxes:     # 遍历所有检测框 | Iterate all detected boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])    # 获取坐标 | Get coordinates
            label = model.names[int(box.cls[0])]       # 获取类别 | Get class label

            if label == "good":                       # 好芯片 | Good chip
                good_count += 1
                color = (255, 0, 0)                   # 蓝色 BGR | Blue in BGR
            else:                                     # 坏芯片 | Bad chip
                bad_count += 1
                color = (0, 0, 255)                   # 红色 BGR | Red in BGR

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)    # 绘制矩形框 | Draw rectangle
            cv2.putText(frame, label, (x1, y1 - 10),              # 绘制标签 | Draw label
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

**核心检测逻辑与静态检测完全相同**。关键差异是计数器每帧重置为 0（而非整个程序运行期间累加），因为每帧画面独立统计。
The core detection logic is **identical to static image detection**. The key difference is that counters reset to 0 every frame (rather than accumulating over the entire program run), because each frame's statistics are independent.

### 5.5 显示实时统计信息 | Display Real-Time Statistics

```python
    # 在画面左上角显示好芯片数量 (蓝色)
    # Display good chip count at top-left corner (blue)
    cv2.putText(frame, f"Good: {good_count}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # 在画面左上角显示坏芯片数量 (红色)
    # Display bad chip count at top-left corner (red)
    cv2.putText(frame, f"Bad: {bad_count}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

**实时统计的特点 | Characteristics of Live Statistics:**
- 每帧都会重新计算并更新显示，因此当摄像头前的芯片变化时，数字会相应变化 | Recalculated and updated every frame, so numbers change as chips in front of the camera change
- 统计数据是当前帧的瞬时结果，不是历史累计值 | Statistics reflect the current frame only, not a historical accumulation

### 5.6 显示画面并检测按键 | Display Frame & Check Key Press

```python
    cv2.imshow("Chip Real-Time Detection | 芯片实时检测", frame)  # 显示实时画面 | Show live feed

    if cv2.waitKey(50) & 0xFF == ord('q'):    # 检测是否按下 'q' 键 | Check if 'q' key is pressed
        break                                   # 按下 'q' 则退出循环 | Exit the loop if pressed
```

**`cv2.waitKey(50)` 详解 | About `cv2.waitKey(50)`:**

| 参数 Parameter | 含义 Meaning | 为什么是 50 Why 50 |
|---------------|-------------|-------------------|
| `50` | 等待 50 毫秒 | 约 20 FPS 的刷新率（1000ms ÷ 50ms = 20 帧/秒） |
| | Wait for 50 milliseconds | Approx. 20 FPS refresh rate (1000ms ÷ 50ms = 20 frames/sec) |
| `& 0xFF` | 按位与操作，取低 8 位 | 兼容不同操作系统的按键码处理 |
| | Bitwise AND, takes lower 8 bits | Cross-platform keycode compatibility |
| `ord('q')` | 获取字符 'q' 的 ASCII 码 | 用于判断用户是否按下了 'q' 键 |
| | Get ASCII code of character 'q' | Used to determine if the user pressed 'q' |

**`cv2.waitKey()` 在实时检测中的双重作用 | Dual Role of `cv2.waitKey()`:**
1. 控制帧率（延迟越长，FPS 越低）| Control frame rate (longer delay = lower FPS)
2. 检测键盘输入 | Detect keyboard input

### 5.7 释放资源 | Release Resources

```python
cap.release()                # 释放摄像头资源 | Release the webcam resource
                             # 重要：如果不释放，摄像头可能一直被占用
                             # Important: if not released, the camera may remain occupied

cv2.destroyAllWindows()      # 关闭所有 OpenCV 创建的窗口 | Close all windows created by OpenCV
                             # 如果不关闭，某些系统上窗口可能残留
                             # If not closed, windows may remain on some systems

print("检测已结束！| Detection stopped!")
```

**为什么必须释放资源？| Why must resources be released?**
- 摄像头是硬件设备，不释放会导致其他程序无法使用摄像头 | The camera is a hardware device; not releasing it prevents other programs from using it
- OpenCV 窗口不关闭可能在某些系统上成为"僵尸窗口" | Unclosed OpenCV windows may become "zombie windows" on some systems

### 5.8 完整代码流程图 | Complete Code Flow

```
开始 Start
  │
  ├── 1. 导入依赖 Import libraries (ultralytics, cv2)
  │
  ├── 2. 加载 YOLO 模型 Load YOLO model ("chip.pt")
  │
  ├── 3. 打开摄像头 Open webcam (cv2.VideoCapture(0))
  │
  ├── 4. 进入主循环 Enter main loop (while True):
  │   │
  │   ├── 4.1 读取一帧 Read one frame (cap.read())
  │   ├── 4.2 检查读取是否成功 Check if read succeeded
  │   │     └── 失败 → break 退出循环
  │   ├── 4.3 重置当前帧计数器 Reset frame counters (good=0, bad=0)
  │   ├── 4.4 运行 YOLO 推理 Run YOLO inference
  │   ├── 4.5 遍历检测框 For each detection:
  │   │   ├── 获取坐标 Get coordinates
  │   │   ├── 获取类别 Get label
  │   │   ├── 累加计数 Increment counter
  │   │   ├── 绘制矩形框 Draw rectangle
  │   │   └── 绘制标签 Draw label text
  │   ├── 4.6 绘制统计文字 Draw statistics text
  │   ├── 4.7 显示实时画面 Display live frame
  │   └── 4.8 检测 'q' 键 → 按下则 break
  │
  ├── 5. 释放摄像头 Release webcam (cap.release())
  │
  ├── 6. 关闭所有窗口 Close all windows (cv2.destroyAllWindows())
  │
  └── 7. 打印结束信息 Print exit message

结束 End
```

---

## 六、使用方法 | 6. Usage

### 6.1 环境准备 | Environment Setup

**第一步：确认 Python 已安装 | Step 1: Verify Python is installed**
```bash
python --version    # 应显示 Python 3.8+ | Should show Python 3.8+
```

**第二步：安装依赖 | Step 2: Install dependencies**
```bash
pip install ultralytics opencv-python
```

**第三步：确认摄像头可用 | Step 3: Verify webcam is available**
- Windows：打开"相机"应用测试摄像头是否正常 | Open the "Camera" app to test
- Mac：打开 Photo Booth 测试 | Open Photo Booth to test
- Linux：运行 `ls /dev/video*` 检查摄像头设备 | Run `ls /dev/video*` to check camera devices

### 6.2 运行程序 | Run Program

```bash
cd chip-quality-detector      # 进入项目目录 | Enter project directory
python detect_test_3.py       # 运行实时检测 | Run real-time detection
```

### 6.3 操作说明 | Operation Instructions

| 步骤 Step | 操作 Action | 预期结果 Expected Result |
|----------|------------|------------------------|
| 1 | 确保摄像头已正确连接 | 如果使用外接摄像头，确认 USB 已插入 | Make sure the webcam is properly connected or built-in camera is working |
| 2 | 运行程序 Run program | 程序加载模型后自动打开摄像头，弹出实时检测窗口 | After loading the model, the webcam opens and a live detection window appears |
| 3 | 将芯片放在摄像头前 Place chips in front of camera | 画面上出现蓝色（good）和红色（bad）检测框 | Blue (good) and red (bad) bounding boxes appear on screen |
| 4 | 移动芯片测试 Move chips to test | 检测框和统计数字随画面实时更新 | Bounding boxes and statistics update in real-time |
| 5 | 按 `q` 键退出 Press `q` to exit | 确保检测窗口处于激活状态（点击窗口），然后按 `q` | Make sure the detection window is active (click on it), then press `q` |
| 6 | 查看控制台 Check console | 终端输出 "检测已结束！\| Detection stopped!" | Terminal outputs "检测已结束！\| Detection stopped!" |

---

## 七、界面说明 | 7. Interface Explanation

### 7.1 实时画面元素 | Real-Time Display Elements

| 元素 Element | 位置 Position | 说明 Description |
|-------------|-------------|-----------------|
| **检测框 Bounding Box** | 芯片周围 Around each chip | 蓝色 = good（好芯片），红色 = bad（坏芯片） | Blue = good chip, Red = bad chip |
| **类别标签 Class Label** | 检测框左上角 Top-left of each box | 显示 "good" 或 "bad" | Displays "good" or "bad" |
| **好芯片计数 Good Count** | 画面左上角第1行 Top-left, line 1 | `Good: X` — 当前帧好芯片数量（蓝色） | Good chip count in current frame (blue) |
| **坏芯片计数 Bad Count** | 画面左上角第2行 Top-left, line 2 | `Bad: X` — 当前帧坏芯片数量（红色） | Bad chip count in current frame (red) |
| **窗口标题 Window Title** | 窗口标题栏 Title bar | "Chip Real-Time Detection \| 芯片实时检测" |

### 7.2 画面示意图 | Display Layout Diagram

```
┌──────────────────────────────────────────────┐
│ Chip Real-Time Detection | 芯片实时检测       │ ← 窗口标题 Window Title
│                                              │
│ Good: 3              ← 蓝色文字 Blue text    │
│ Bad: 1               ← 红色文字 Red text     │
│                                              │
│   ┌──────────┐      ┌──────────┐             │
│   │  good    │      │  good    │             │ ← 蓝色框 Blue box
│   │  蓝色框  │      │  蓝色框  │             │
│   └──────────┘      └──────────┘             │
│                                              │
│             ┌──────────┐                     │
│             │   bad    │                     │ ← 红色框 Red box
│             │  红色框  │                     │
│             └──────────┘                     │
│                                              │
│   ┌──────────┐                               │
│   │  good    │                               │ ← 蓝色框 Blue box
│   │  蓝色框  │                               │
│   └──────────┘                               │
└──────────────────────────────────────────────┘
```

---

## 八、常见问题 | 8. FAQ

**Q1: 运行后摄像头无法打开，窗口一片空白或直接退出？**
> **The camera fails to open — the window is blank or the program exits immediately.**
>
> 原因 Cause：摄像头编号不正确或摄像头被其他程序占用。The camera index is wrong, or the camera is occupied by another app.
>
> 解决方法 Solution:
> 1. 尝试将 `cv2.VideoCapture(0)` 中的 `0` 改为 `1`（笔记本常用）或 `-1` Try changing `0` to `1` (common for laptops) or `-1`
> 2. 关闭其他正在使用摄像头的程序（如 Zoom、Teams、微信等） Close other apps using the camera (Zoom, Teams, WeChat, etc.)
> 3. 添加错误检查代码：在 `cap = cv2.VideoCapture(0)` 后添加 `if not cap.isOpened(): print("摄像头无法打开 Cannot open camera"); exit()`

**Q2: 检测速度很慢，画面卡顿？**
> **Detection is slow and the video is choppy.**
>
> 原因 Cause：YOLO 模型推理消耗大量计算资源，尤其在没有 GPU 的电脑上。YOLO model inference consumes significant computing power, especially on computers without a GPU.
>
> 解决方法 Solution:
> 1. 降低摄像头分辨率：在 `cap.read()` 后添加 `frame = cv2.resize(frame, (320, 240))` | Reduce resolution: add `frame = cv2.resize(frame, (320, 240))` after `cap.read()`
> 2. 使用更轻量的模型（如 YOLOv8n） | Use a lighter model (e.g., YOLOv8n)
> 3. 增大 `cv2.waitKey()` 的参数值（如从 50 改为 100） | Increase the `cv2.waitKey()` value (e.g., from 50 to 100)

**Q3: 如何退出程序？**
> **How do I exit the program?**
>
> 解决方法 Solution:
> 1. 首先**点击**检测窗口使其处于激活状态 | First **click** on the detection window to activate it
> 2. 然后按键盘上的 **`q`** 键 | Then press the **`q`** key on your keyboard
> 3. 如果窗口无响应，在终端按 `Ctrl+C` 强制终止 | If the window is unresponsive, press `Ctrl+C` in the terminal to force quit

**Q4: 检测框位置不准或漏检？**
> **Detection boxes are inaccurate or chips are missed.**
>
> 原因 Cause：摄像头拍摄角度、光线条件、芯片与训练数据差异等因素。Factors include camera angle, lighting conditions, differences from training data.
>
> 解决方法 Solution:
> 1. 调整摄像头角度和距离，使芯片清晰可见 | Adjust camera angle and distance so chips are clearly visible
> 2. 确保光线充足，避免阴影遮挡芯片 | Ensure good lighting, avoid shadows covering chips
> 3. 芯片放置于纯色背景上，减少干扰 | Place chips on a solid-colored background to reduce interference

**Q5: 为什么没有保存检测结果的图片/视频？**
> **Why aren't detection results saved as images/video?**
>
> 原因 Cause：实时检测的设计目标是实时查看，不保存任何文件。若需保存，需自行添加代码。Real-time detection is designed for live viewing only; no files are saved. You need to add code if you want to save results.
>
> 解决方法（如需保存） Solution (if you need to save):
> ```python
> # 在 cv2.imshow() 之后添加以下代码保存每一帧 | Add after cv2.imshow() to save each frame
> cv2.imwrite(f"output/frame_{frame_count}.png", frame)
> ```

---

## 九、性能优化建议 | 9. Performance Tips

| 优化方法 Optimization | 代码修改 Code Change | 效果 Effect | 副作用 Side Effect |
|----------------------|---------------------|------------|-------------------|
| **降低分辨率 Reduce Resolution** | 添加 `frame = cv2.resize(frame, (320, 240))` | 显著提升 FPS | 画面变模糊 Blurrier image |
| **使用更小模型 Lighter Model** | 替换为 YOLOv8n（nano 版） | 速度大幅提升，精度略降 | 可能增加误检 More false detections |
| **跳帧检测 Frame Skipping** | 添加帧计数器，每 N 帧检测一次 | 显著降低计算量 | 检测框更新不连贯 |
| | Add frame counter, detect every N frames | Significant computation reduction | Detection boxes update less smoothly |
| **增大 waitKey 值 Increase waitKey** | `cv2.waitKey(100)` 代替 `50` | 降低 CPU 占用 | 显示更卡顿 |
| | Use `cv2.waitKey(100)` instead of `50` | Lower CPU usage | Choppier display |
| **使用 GPU 加速 GPU Acceleration** | 安装 CUDA 版 PyTorch | 推理速度提升 5-10 倍 | 需要 NVIDIA GPU |
| | Install CUDA version of PyTorch | 5-10x inference speedup | Requires NVIDIA GPU |

**建议顺序 Recommended Order：**
1. 先尝试增大 `waitKey` 值（最简单）
2. 再尝试降低分辨率（效果最明显）
3. 最后考虑更换模型或使用 GPU（需要额外安装）

1. First try increasing the `waitKey` value (easiest)
2. Then try reducing resolution (most noticeable effect)
3. Finally consider switching models or using GPU (requires additional installation)

---

## 十、与静态检测的对比 | 10. Comparison with Static Detection

| 维度 Aspect | detect_test_1.py (静态) | detect_test_3.py (实时) |
|------------|------------------------|------------------------|
| 输入 Input | 图片文件 Image file | 摄像头视频流 Webcam stream |
| 循环方式 Loop | 无循环（检测一次） No loop (detects once) | 无限循环 `while True` Infinite loop |
| 退出方式 Exit | 程序自然结束 Natural completion | 按 `q` 键手动退出 Press `q` to exit |
| 计数器 Counter | 全程累加 Accumulates globally | 每帧重置 Resets every frame |
| 文件操作 File I/O | 读取图片 + 保存结果 Read image + save result | 无文件操作 No file operations |
| 窗口关闭 Window | 按任意键关闭 Any key to close | 按特定键 `q` 退出 Specific key (`q`) to exit |
| 适用场景 Use Case | 分析单张图片 Analyze one image | 实时产线监控 Live production line monitoring |

---

## 十一、学习要点 | 11. Key Learning Points

对于马来西亚学生，建议重点理解以下编程概念：
For Malaysian students, we recommend focusing on the following programming concepts:

| 概念 Concept | 代码体现 Code Example | 学习价值 Learning Value |
|-------------|---------------------|------------------------|
| **无限循环 Infinite Loop** | `while True:` | 理解持续运行的后台程序如何设计 | Understanding how to design continuously running programs |
| **视频捕获 Video Capture** | `cv2.VideoCapture(0)` | 学习如何从摄像头获取数据流 | Learning how to capture data streams from cameras |
| **实时处理 Real-Time Processing** | 每帧独立检测 Detect each frame independently | 理解实时数据处理的核心模式 | Understanding core patterns of real-time data processing |
| **资源管理 Resource Management** | `cap.release()` + `destroyAllWindows()` | 学习如何正确地申请和释放硬件资源 | Learning proper hardware resource acquisition and release |
| **按键交互 Keyboard Interaction** | `cv2.waitKey() & 0xFF == ord('q')` | 学习如何在持续运行的程序中响应用户输入 | Learning how to respond to user input in continuously running programs |
| **帧率控制 Frame Rate Control** | `cv2.waitKey(50)` | 理解延迟参数如何影响画面流畅度和 CPU 占用 | Understanding how delay parameters affect smoothness and CPU usage |

---

*文档版本 | Document Version: v2.0*
*更新日期 | Last Updated: 2026年5月 | May 2026*
*适用对象 | Target Audience: 马来西亚学生培训 | Malaysian Student Training*
