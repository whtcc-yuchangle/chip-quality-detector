# 芯片检测程序文档 | Chip Detection Program Documentation

> 本文档面向马来西亚学生培训使用，提供完整的中英文双语说明。
> This document is designed for Malaysian student training, with complete bilingual Chinese-English explanations.

---

## 一、程序概述 | 1. Program Overview

本程序是一个基于 **YOLO (You Only Look Once)** 目标检测框架的芯片质量检测工具。它可以自动识别图片中的芯片，并根据检测结果将芯片分为 **good（好芯片）** 和 **bad（坏芯片）** 两类，同时用不同颜色的边框标记，方便直观查看检测结果。

This program is a chip quality detection tool based on the **YOLO (You Only Look Once)** object detection framework. It automatically identifies chips in images and classifies them into **good** and **bad** categories. Detection results are highlighted with different colored bounding boxes for easy visual inspection.

**适用场景 | Use Cases:**
- 芯片生产线上快速检测芯片质量 | Quick quality inspection on chip production lines
- 学生学习 YOLO 目标检测的入门示例 | An introductory example for students learning YOLO object detection
- 自动化视觉检测的原型验证 | Prototype validation for automated visual inspection

---

## 二、功能特性 | 2. Features

| 功能 Feature | 说明 Description |
|-------------|-----------------|
| **目标检测 Object Detection** | 使用 YOLO 模型自动检测图片中所有芯片的位置 | Automatically detect the positions of all chips in an image using YOLO model |
| **类别识别 Classification** | 自动区分芯片是 good（好芯片）还是 bad（坏芯片） | Automatically classify each chip as good or bad |
| **颜色区分 Color Coding** | 好芯片用**蓝色**框标记，坏芯片用**红色**框标记，一目了然 | Good chips marked with **blue** boxes, bad chips with **red** boxes for clear visual distinction |
| **数量统计 Counting** | 在图片左上角实时显示好芯片和坏芯片的数量统计 | Display real-time count of good and bad chips at the top-left corner of the image |
| **结果保存 Save Results** | 检测完成后自动将带标注的结果图片保存到 `out1/` 目录 | Automatically save annotated result images to the `out1/` directory |
| **图片预览 Preview** | 弹出 OpenCV 窗口显示检测后的图片，按任意键关闭 | Display detection results in an OpenCV window; press any key to close |

---

## 三、技术栈 | 3. Tech Stack

| 技术 Technology | 版本要求 Version | 说明 Description |
|----------------|-----------------|-----------------|
| Python | ≥ 3.8 | 编程语言，建议使用 3.9+ 以获得更好的性能 | Programming language, 3.9+ recommended for better performance |
| ultralytics | ≥ 8.0 | YOLO 目标检测框架，提供预训练模型和推理接口 | YOLO object detection framework, provides pre-trained models and inference API |
| OpenCV (cv2) | ≥ 4.0 | 图像处理库，用于图片读取、绘制检测框、显示结果 | Image processing library for reading images, drawing bounding boxes, and displaying results |
| os | 内置 Built-in | Python 标准库，用于文件和目录操作 | Python standard library for file and directory operations |

---

## 四、文件结构 | 4. File Structure

```
chip-quality-detector/
├── chip.pt               # 训练好的YOLO模型文件 (~5.5 MB)
│                         # Trained YOLO model file (~5.5 MB), contains 2 classes: good & bad
├── datasets/
│   └── chip1.png         # 待检测的芯片图片 (单张)
│                         # Input chip image to be detected (single image)
├── detect_test_1.py      # 主程序文件 - 单图片检测
│   (detect_test_1.py)    # Main program file - single image detection
└── out1/                 # 结果输出目录 (程序自动创建)
    (out1/)               # Output directory (auto-created by the program)
    └── chip1.png         # 标注后的检测结果图片
                          # Annotated detection result image
```

---

## 五、代码详解 | 5. Code Explanation

本部分逐段解释 `detect_test_1.py` 的每一行代码，帮助初学者理解程序的运行逻辑。
This section explains every part of `detect_test_1.py` line by line, helping beginners understand the program logic.

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO  # 导入 YOLO 目标检测库 | Import YOLO object detection library
import cv2                    # 导入 OpenCV 图像处理库 | Import OpenCV image processing library
import os                     # 导入操作系统接口库 | Import OS interface library
```

**说明 | Explanation:**
- `ultralytics.YOLO`：YOLO 模型的 Python 接口，用于加载模型和执行推理 | Python interface for YOLO models — loading and inference
- `cv2`：OpenCV 库，提供图像读取、绘制、显示等功能 | Provides image reading, drawing, and display functions
- `os`：用于检查目录是否存在、创建目录等文件系统操作 | Used for checking directory existence, creating directories, etc.

### 5.2 核心配置 | Core Configuration

```python
model = YOLO("chip.pt")              # 加载训练好的芯片检测模型 | Load the trained chip detection model
image_path = "datasets/chip1.png"    # 待检测图片的路径 | Path to the image to be detected
output_dir = "out1"                  # 检测结果的保存目录 | Directory for saving detection results
```

**参数说明 | Parameter Details:**

| 参数 Parameter | 含义 Meaning | 可修改 Modifiable |
|---------------|-------------|------------------|
| `"chip.pt"` | 模型文件路径，须与程序在同一目录 | Model file path, must be in the same directory as the script | 可用其他 YOLO 模型替换 |
| `"datasets/chip1.png"` | 输入图片路径 | Input image path | 可改为其他图片路径 |
| `"out1"` | 输出目录名 | Output directory name | 可改为任意目录名 |

### 5.3 目录创建 | Create Output Directory

```python
if not os.path.exists(output_dir):   # 检查输出目录是否存在 | Check if output directory exists
    os.makedirs(output_dir)          # 如果不存在则创建 | Create it if it doesn't exist
```

**为什么要这样做？| Why do this?**
如果输出目录不存在，`cv2.imwrite()` 保存图片时会失败。这段代码确保目录存在，避免程序报错。
If the output directory does not exist, `cv2.imwrite()` will fail when saving images. This code ensures the directory exists to prevent errors.

### 5.4 图片读取与计数器初始化 | Image Reading & Counter Initialization

```python
img = cv2.imread(image_path)    # 读取待检测的图片到内存 | Read the image into memory
good_count = 0                  # 好芯片计数器（初始为0） | Good chip counter (starts at 0)
bad_count = 0                   # 坏芯片计数器（初始为0） | Bad chip counter (starts at 0)
```

**`cv2.imread()` 详解 | About `cv2.imread()`:**
- 将图片文件读取为一个 NumPy 数组（像素矩阵） | Reads an image file into a NumPy array (pixel matrix)
- 返回 `None` 表示文件路径错误或文件损坏 | Returns `None` if the path is wrong or the file is corrupted
- OpenCV 默认以 **BGR** 色彩空间加载（注意：不是 RGB） | Loads in **BGR** color space by default (note: not RGB)

### 5.5 执行 YOLO 检测 | Run YOLO Detection

```python
results = model(image_path)     # 调用 YOLO 模型对图片进行目标检测 | Run YOLO model on the image
```

**内部流程 | Internal Process:**
1. 将图片缩放至模型输入尺寸（通常是 640×640） | Resize the image to the model's input size (typically 640×640)
2. 神经网络前向推理，预测目标位置和类别 | Neural network forward inference to predict object positions and classes
3. 返回包含所有检测结果的列表 | Return a list containing all detection results

### 5.6 遍历检测结果 | Process Detection Results

```python
for result in results:                           # 遍历每张图片的检测结果 | Iterate over detection results for each image
    for box in result.boxes:                     # 遍历该图片中所有检测到的目标框 | Iterate over all detected bounding boxes
        x1, y1, x2, y2 = map(int, box.xyxy[0])   # 获取检测框的四个坐标并转为整数
                                                  # Get bounding box coordinates and convert to integers
        label = model.names[int(box.cls[0])]      # 根据类别索引获取类别名称 (good/bad)
                                                  # Get class name from class index (good/bad)

        if label == "good":                       # 如果是好芯片 | If it's a good chip
            good_count += 1                       # 好芯片计数 +1 | Increment good chip count
            color = (255, 0, 0)                   # 蓝色 (OpenCV 使用 BGR 格式) | Blue color (BGR format)
        else:                                     # 否则是坏芯片 | Otherwise it's a bad chip
            bad_count += 1                        # 坏芯片计数 +1 | Increment bad chip count
            color = (0, 0, 255)                   # 红色 (OpenCV 使用 BGR 格式) | Red color (BGR format)

        # 在图片上绘制矩形检测框，线宽 2 像素
        # Draw rectangle bounding box on the image, 2-pixel line width
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

        # 在检测框上方绘制类别标签文字
        # Draw class label text above the bounding box
        # 参数: 图片, 文字, 位置, 字体, 字号, 颜色, 线宽
        # Parameters: image, text, position, font, font scale, color, line thickness
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

**关键数据结构说明 | Key Data Structures:**

| 属性 Attribute | 含义 Meaning | 示例 Example |
|---------------|-------------|-------------|
| `box.xyxy[0]` | 检测框的四个坐标 `[x1, y1, x2, y2]` | `[100.5, 200.3, 300.7, 400.1]` |
| `box.cls[0]` | 检测目标的类别索引 (0=good, 1=bad) | `0.0` 或 `1.0` |
| `model.names` | 类别索引到名称的映射字典 | `{0: 'good', 1: 'bad'}` |

**OpenCV 颜色值参考 | OpenCV Color Values Reference:**

| 颜色 Color | BGR 值 BGR Value | 用途 Usage |
|-----------|-----------------|-----------|
| 蓝色 Blue | `(255, 0, 0)` | 好芯片 Good chips |
| 红色 Red | `(0, 0, 255)` | 坏芯片 Bad chips |
| 绿色 Green | `(0, 255, 0)` | 可用于其他标记 Other uses |

### 5.7 绘制统计信息 | Draw Statistics

```python
# 在图片左上角 (10, 40) 位置显示好芯片数量（蓝色文字）
# Display good chip count at top-left corner (10, 40) in blue text
cv2.putText(img, f"Good: {good_count}", (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# 在图片左上角 (10, 80) 位置显示坏芯片数量（红色文字）
# Display bad chip count at top-left corner (10, 80) in red text
cv2.putText(img, f"Bad: {bad_count}", (10, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
```

**文字参数说明 | Text Parameter Details:**
- 第一行：`Good: X` — 好芯片数量，蓝色显示 | Good chip count in blue
- 第二行：`Bad: X` — 坏芯片数量，红色显示 | Bad chip count in red
- `cv2.FONT_HERSHEY_SIMPLEX`：无衬线字体，适合屏幕显示 | Sans-serif font, ideal for screen display
- `1`：字体缩放比例，数值越大文字越大 | Font scale factor, larger value = larger text
- `2`：文字线宽（像素） | Text line thickness in pixels

### 5.8 保存与显示结果 | Save & Display Result

```python
# 将标注后的图片保存到 out1/ 目录
# Save the annotated image to the out1/ directory
cv2.imwrite(f"{output_dir}/{filename}", img)

# 弹出窗口显示检测结果，窗口标题为 "Chip Detection Result"
# Display result in a popup window titled "Chip Detection Result"
cv2.imshow("Chip Detection Result | 芯片检测结果", img)

cv2.waitKey(0)             # 等待用户按下键盘任意键 | Wait for any key press
cv2.destroyAllWindows()    # 关闭所有 OpenCV 窗口 | Close all OpenCV windows
```

**`cv2.waitKey(0)` 说明 | About `cv2.waitKey(0)`:**
- 参数 `0` 表示无限等待，直到用户按下任意键 | Parameter `0` means wait indefinitely until any key is pressed
- 如果改成 `1000`，则窗口显示 1 秒后自动关闭 | If changed to `1000`, the window closes automatically after 1 second
- 这是 OpenCV 显示窗口的必需调用，否则窗口不会显示 | This call is required for OpenCV windows to display properly

### 5.9 打印控制台结果 | Print Console Results

```python
print("检测完成！| Detection completed!")
print(f"好芯片：{good_count} | Good chips: {good_count}")
print(f"坏芯片：{bad_count} | Bad chips: {bad_count}")
print(f"结果已保存至 out1/ | Result saved to out1/")
```

### 5.10 完整代码流程图 | Complete Code Flow

```
开始 Start
  │
  ├── 1. 导入库 Import libraries
  │
  ├── 2. 加载模型 Load YOLO model ("chip.pt")
  │
  ├── 3. 设置路径 Set image path & output directory
  │
  ├── 4. 创建输出目录 Create output directory (if not exists)
  │
  ├── 5. 读取图片 Read image (cv2.imread)
  │
  ├── 6. 初始化计数器 Initialize counters (good=0, bad=0)
  │
  ├── 7. 运行 YOLO 推理 Run YOLO inference
  │
  ├── 8. 遍历检测结果 For each detection:
  │   ├── 获取坐标 Get coordinates (x1,y1,x2,y2)
  │   ├── 获取类别 Get class label (good/bad)
  │   ├── 累加计数 Increment counter
  │   ├── 选择颜色 Choose color (blue/red)
  │   ├── 绘制矩形框 Draw rectangle
  │   └── 绘制标签文字 Draw label text
  │
  ├── 9. 绘制统计信息 Draw statistics (Good/Bad count)
  │
  ├── 10. 保存结果图片 Save result image
  │
  ├── 11. 显示结果窗口 Display result window
  │
  └── 12. 打印控制台输出 Print console output

结束 End
```

---

## 六、使用方法 | 6. Usage

### 6.1 环境准备 | Environment Setup

**第一步：确认 Python 已安装 | Step 1: Verify Python is installed**
```bash
python --version    # 应显示 Python 3.8 或更高版本 | Should show Python 3.8+
```

**第二步：安装依赖库 | Step 2: Install dependencies**
```bash
pip install ultralytics opencv-python
```

这一步会安装以下库 | This installs the following libraries:
- `ultralytics` — YOLO 目标检测框架 | YOLO object detection framework
- `opencv-python` — OpenCV 图像处理库 | OpenCV image processing library
- 相关依赖会自动安装 | Related dependencies are installed automatically

**第三步：确认文件齐全 | Step 3: Verify required files**
```bash
ls               # 确认 chip.pt 和 detect_test_1.py 在项目目录下
ls datasets/     # 确认 datasets/ 目录中有待检测的图片
```

### 6.2 运行程序 | Run Program

```bash
cd chip-quality-detector      # 进入项目目录 | Enter project directory
python detect_test_1.py       # 运行单图片检测程序 | Run the single-image detection program
```

### 6.3 操作说明 | Operation Instructions

| 步骤 Step | 操作 Action | 预期结果 Expected Result |
|----------|------------|------------------------|
| 1 | 运行程序 | 程序自动加载模型（~5.5 MB），可能需要几秒钟 |
| | Run the program | The program loads the model (~5.5 MB), may take a few seconds |
| 2 | 等待推理完成 | 模型对图片进行检测，通常在 1-3 秒内完成 |
| | Wait for inference | Model detects objects in the image, usually within 1-3 seconds |
| 3 | 查看弹出窗口 | 弹出窗口显示标注了检测框和统计信息的图片 |
| | View the popup window | A window shows the image with bounding boxes and statistics |
| 4 | 按任意键关闭窗口 | 窗口关闭，程序退出 |
| | Press any key to close | Window closes, program exits |
| 5 | 检查输出 | 查看 `out1/` 目录中保存的结果图片 |
| | Check output | View the saved result image in the `out1/` directory |

---

## 七、输出说明 | 7. Output Explanation

### 7.1 图片输出 | Image Output

检测后的图片包含以下视觉元素：
The annotated result image contains the following visual elements:

| 元素 Element | 说明 Description | 示例 Example |
|-------------|-----------------|-------------|
| **检测框 Bounding Box** | 每个芯片周围的矩形框 | 蓝色框 = good（好芯片），红色框 = bad（坏芯片） |
| | Rectangle around each detected chip | Blue box = good chip, Red box = bad chip |
| **类别标签 Class Label** | 检测框左上角的文字标识 | "good" 或 "bad" |
| | Text label at the top-left of each bounding box | "good" or "bad" |
| **统计信息 Statistics** | 图片左上角两行文字 | `Good: 5` (蓝色), `Bad: 2` (红色) |
| | Two lines of text at the image's top-left corner | `Good: 5` (blue), `Bad: 2` (red) |

### 7.2 控制台输出 | Console Output

运行程序后，终端会输出以下信息：
After running, the terminal will display the following information:

```
检测完成！| Detection completed!
好芯片：5 | Good chips: 5
坏芯片：2 | Bad chips: 2
结果已保存至 out1/ | Result saved to out1/
```

### 7.3 输出文件 | Output Files

| 文件 File | 路径 Path | 说明 Description |
|----------|----------|-----------------|
| 结果图片 Result Image | `out1/chip1.png` | 与原图同名，包含所有标注信息 Same name as original, with all annotations |

---

## 八、扩展建议 | 8. Extension Suggestions

以下是一些可以在本项目基础上扩展的方向，适合学生动手实践：
Below are some directions for extending this project, suitable for student hands-on practice:

| 扩展方向 Extension | 难度 Difficulty | 说明 Description |
|-------------------|----------------|-----------------|
| **批量检测 Batch Detection** | ★☆☆ | 修改代码循环遍历 `datasets/` 文件夹中的所有图片 | Loop through all images in the `datasets/` folder (see `detect_test_2.py`) |
| **视频文件检测 Video Detection** | ★★☆ | 使用 `cv2.VideoCapture("video.mp4")` 代替图片读取，逐帧检测 | Replace image reading with `cv2.VideoCapture("video.mp4")` for frame-by-frame detection |
| **摄像头实时检测 Webcam Detection** | ★★☆ | 使用摄像头实时捕获画面并进行检测 | Use webcam for real-time capture and detection (see `detect_test_3.py`) |
| **结果报表 Report Generation** | ★★★ | 将检测结果导出为 CSV/Excel 文件，包含每张图的统计信息 | Export detection results to CSV/Excel with per-image statistics |
| **Web 界面 Web Interface** | ★★★ | 使用 Flask 或 Streamlit 开发网页版检测工具，支持上传图片查看结果 | Build a web-based detection tool using Flask or Streamlit with image upload |

---

## 九、常见问题 | 9. FAQ

**Q1: 运行时提示 "No module named 'ultralytics'"？**
> 原因：未安装 ultralytics 库。| Cause: The ultralytics library is not installed.
> 解决：运行 `pip install ultralytics` 安装依赖。| Solution: Run `pip install ultralytics` to install.

**Q2: 提示模型文件找不到 "chip.pt not found"？**
> 原因：模型文件不在程序运行目录下。| Cause: The model file is not in the script's working directory.
> 解决：确保 `chip.pt` 文件与 `detect_test_1.py` 在同一目录。| Solution: Make sure `chip.pt` is in the same directory as `detect_test_1.py`.

**Q3: 检测结果不准确，漏检或误检？**
> 原因：模型训练数据可能不够充分，或图片与训练数据差异较大。| Cause: The model may not have been trained on enough data, or the test images differ significantly from training data.
> 解决：收集更多芯片图片，重新训练模型；或调整模型参数。| Solution: Collect more chip images to retrain the model; or adjust model parameters.

**Q4: 显示窗口无法关闭？**
> 原因：窗口可能未处于激活状态。| Cause: The window may not be in focus (active state).
> 解决：点击图片窗口使其激活，然后按键盘任意键关闭。| Solution: Click on the image window to activate it, then press any key.

**Q5: 如何更换检测其他图片？**
> 原因/解决：修改 `image_path = "datasets/chip1.png"` 为你的图片路径即可。| Cause/Solution: Change `image_path = "datasets/chip1.png"` to the path of your image.

**Q6: OpenCV 显示的颜色不对？**
> 原因：OpenCV 使用 BGR 色彩空间，而不是常见的 RGB。| Cause: OpenCV uses the BGR color space, not the more common RGB.
> 解决：蓝色 `(255,0,0)` 对应 RGB 的红色；红色 `(0,0,255)` 对应 RGB 的蓝色。使用时按 BGR 格式指定颜色即可。| Solution: `(255,0,0)` in BGR = Blue; `(0,0,255)` in BGR = Red. Always specify colors in BGR format when using OpenCV.

---

*文档版本 | Document Version: v2.0*
*更新日期 | Last Updated: 2026年5月 | May 2026*
*适用对象 | Target Audience: 马来西亚学生培训 | Malaysian Student Training*
