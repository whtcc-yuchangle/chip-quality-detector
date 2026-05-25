# 芯片批量检测程序文档 | Batch Chip Detection Program Documentation

> 本文档面向马来西亚学生培训使用，提供完整的中英文双语说明。
> This document is designed for Malaysian student training, with complete bilingual Chinese-English explanations.

---

## 一、程序概述 | 1. Program Overview

本程序是基于 **YOLO (You Only Look Once)** 目标检测框架的**批量芯片质量检测工具**。与 `detect_test_1.py` 只能检测单张图片不同，本程序能够自动遍历 `datasets/` 文件夹中的**所有图片**，对每张图片分别进行芯片检测，统计每张图片以及所有图片汇总的好芯片（good）和坏芯片（bad）数量，并在控制台生成汇总报告。

This program is a **batch chip quality detection tool** based on the **YOLO (You Only Look Once)** object detection framework. Unlike `detect_test_1.py` which only detects a single image, this program automatically iterates through **all images** in the `datasets/` folder, performs chip detection on each image, counts good and bad chips per image and in total, and generates a summary report in the console.

**与 detect_test_1.py 的区别 | Differences from detect_test_1.py:**

| 对比项 Comparison | detect_test_1.py | detect_test_2.py |
|------------------|------------------|------------------|
| 输入图片 Input | 1 张 Single image | `datasets/` 下所有图片 All images in `datasets/` |
| 结果展示 Display | 等待按键关闭 Wait for key press | 每张显示 1 秒后自动切换 Auto-switch every 1 second |
| 统计范围 Statistics | 仅当前图片 Current image only | 单图 + 全局汇总 Per-image + global summary |
| 输出目录 Output Dir | `out1/` | `out2/` |

---

## 二、功能特性 | 2. Features

| 功能 Feature | 说明 Description |
|-------------|-----------------|
| **批量处理 Batch Processing** | 自动遍历 `datasets` 文件夹中的所有图片文件，无需手动逐个处理 | Automatically iterate through all image files in the `datasets` folder, no manual processing needed |
| **目标检测 Object Detection** | 使用 YOLO 模型检测每张图片中的所有芯片位置 | Detect the positions of all chips in each image using the YOLO model |
| **类别识别 Classification** | 自动区分每张图片中的 good（好芯片）和 bad（坏芯片） | Automatically classify each chip as good or bad in every image |
| **颜色标记 Color Coding** | 好芯片用**蓝色**框标记，坏芯片用**红色**框标记 | Good chips marked with **blue** boxes, bad chips with **red** boxes |
| **单图统计 Per-Image Stats** | 每张图片左上角显示该图片各自的芯片数量 | Each image shows its own chip counts at the top-left corner |
| **汇总统计 Summary Report** | 处理完所有图片后，在控制台输出所有图片的芯片总数统计 | After processing all images, output total chip count summary to the console |
| **自动保存 Auto-Save** | 每张图片的检测结果自动保存到 `out2/` 目录，文件名与原图一致 | Each detection result is automatically saved to the `out2/` directory with the same filename |
| **自动预览 Auto-Preview** | 每张图片检测后弹出窗口显示 1 秒，然后自动切换到下一张 | Each image is displayed in a window for 1 second, then automatically advances to the next |

---

## 三、技术栈 | 3. Tech Stack

| 技术 Technology | 版本要求 Version | 说明 Description |
|----------------|-----------------|-----------------|
| Python | ≥ 3.8 | 编程语言，建议 3.9+ | Programming language, 3.9+ recommended |
| ultralytics | ≥ 8.0 | YOLO 目标检测框架 | YOLO object detection framework |
| OpenCV (cv2) | ≥ 4.0 | 图像处理与窗口显示 | Image processing and window display |
| os | 内置 Built-in | 文件系统操作（遍历目录、路径拼接等） | File system operations (directory traversal, path joining, etc.) |

---

## 四、文件结构 | 4. File Structure

```
chip-quality-detector/
├── chip.pt               # 训练好的 YOLO 模型 (~5.5 MB)
│                         # Trained YOLO model (~5.5 MB)
├── datasets/             # 待检测图片目录（可放入任意数量图片）
│   │                     # Input image folder (can contain any number of images)
│   ├── chip1.png         # 测试图片 1 | Test image 1
│   ├── chip2.png         # 测试图片 2 | Test image 2
│   ├── ...
│   └── chip20.png        # 测试图片 20 | Test image 20
├── detect_test_2.py      # 批量检测程序 | Batch detection program
└── out2/                 # 结果输出目录 (程序自动创建)
    (out2/)               # Output directory (auto-created by the program)
    ├── chip1.png         # 标注后的 chip1 | Annotated chip1
    ├── chip2.png         # 标注后的 chip2 | Annotated chip2
    └── ...               # 与原图一一对应 | One-to-one correspondence with originals
```

---

## 五、代码详解 | 5. Code Explanation

本部分逐段解释 `detect_test_2.py` 的代码逻辑，帮助初学者理解批量检测与单张检测的核心差异。
This section explains the code logic of `detect_test_2.py` in detail, helping beginners understand the key differences between batch and single-image detection.

### 5.1 导入依赖 | Import Dependencies

```python
from ultralytics import YOLO   # YOLO 目标检测库 | YOLO object detection library
import cv2                     # OpenCV 图像处理库 | OpenCV image processing library
import os                      # 文件系统操作库 | File system operations library
```

与 `detect_test_1.py` 完全相同的三个依赖，其中 `os` 在本程序中尤为重要，因为需要遍历目录中的所有文件。
Same three dependencies as `detect_test_1.py`. The `os` module is especially important here for iterating through all files in a directory.

### 5.2 核心配置 | Core Configuration

```python
model = YOLO("chip.pt")        # 加载训练好的 YOLO 模型 | Load the trained YOLO model
input_folder = "datasets"      # 输入图片文件夹路径 | Path to the input image folder
output_dir = "out2"            # 输出结果文件夹路径 | Path to the output folder
```

**配置对比 | Configuration Comparison:**

| 配置项 Config | detect_test_1.py | detect_test_2.py | 说明 Note |
|--------------|------------------|------------------|----------|
| 输入 Input | `image_path` (单个文件) | `input_folder` (整个文件夹) | 批量处理需要指向文件夹 |
| 输出 Output | `out1/` | `out2/` | 使用不同目录避免结果混淆 |

### 5.3 创建输出目录 | Create Output Directory

```python
if not os.path.exists(output_dir):   # 检查 out2/ 目录是否存在 | Check if out2/ exists
    os.makedirs(output_dir)          # 如果不存在则自动创建 | Auto-create it if not
```

必须放在循环**之前**执行，否则每张图片保存时都会重复检查。只需创建一次即可。
This must execute **before** the loop, otherwise the check would repeat for every image. Creating once is sufficient.

### 5.4 全局计数器初始化 | Initialize Global Counters

```python
total_good = 0     # 所有图片的好芯片总数 | Running total of good chips across all images
total_bad = 0      # 所有图片的坏芯片总数 | Running total of bad chips across all images
total_imgs = 0     # 已处理的图片总数 | Total number of images processed
```

**计数器层级说明 | Counter Hierarchy:**
- **全局计数器 Global Counters** (`total_good`, `total_bad`, `total_imgs`)：累加所有图片的结果 | Accumulate results from all images
- **局部计数器 Local Counters** (`current_good`, `current_bad`)：每张图片独立计数，每轮循环重置为 0 | Reset to 0 for each image

### 5.5 主循环 - 遍历图片文件夹 | Main Loop - Iterate Through Images

```python
for filename in os.listdir(input_folder):    # 遍历 datasets/ 目录下的所有文件
                                             # Iterate all files in the datasets/ directory
    img_path = os.path.join(input_folder, filename)  # 拼接完整路径 (datasets/chip1.png)
                                                     # Join folder path + filename
    total_imgs += 1                          # 图片计数 +1 | Increment image counter

    img = cv2.imread(img_path)               # 读取当前图片 | Read the current image
    current_good = 0   # 当前图片好芯片计数 (每张图重置为0) | Reset for each image
    current_bad = 0    # 当前图片坏芯片计数 (每张图重置为0) | Reset for each image
```

**关键函数说明 | Key Function Details:**

| 函数 Function | 作用 Purpose | 示例 Example |
|--------------|-------------|-------------|
| `os.listdir(folder)` | 列出文件夹中所有文件和子文件夹的名称 | `['chip1.png', 'chip2.png', ...]` |
| `os.path.join(a, b)` | 用系统分隔符拼接路径 | `"datasets/chip1.png"` (Linux/Mac) 或 `"datasets\\chip1.png"` (Windows) |

**潜在问题提醒 | Potential Issues:**
- `os.listdir()` 会列出文件夹中**所有**文件，包括非图片文件（如 `.txt`、`.json` 等）。如果文件夹中有非图片文件，`cv2.imread()` 会返回 `None`，可能导致后续代码报错。建议只放图片文件在 `datasets/` 目录中。
- `os.listdir()` lists **all** files in the folder, including non-image files (like `.txt`, `.json`). If non-image files exist, `cv2.imread()` returns `None`, which may cause errors. It's recommended to only place image files in `datasets/`.

### 5.6 执行检测并处理结果 | Run Detection & Process Results

```python
    results = model(img)                     # 对当前图片运行 YOLO 推理 | Run YOLO inference on current image

    for result in results:                   # 遍历推理结果 | Iterate over inference results
        for box in result.boxes:             # 遍历所有检测到的目标框 | Iterate all detected boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])   # 获取坐标并转整数 | Get coordinates as ints
            label = model.names[int(box.cls[0])]      # 获取类别标签 | Get class label

            if label == "good":                       # 好芯片分支 | Good chip branch
                current_good += 1                     # 当前计数 +1 | Increment current count
                color = (255, 0, 0)                   # 蓝色 BGR | Blue in BGR
            else:                                     # 坏芯片分支 | Bad chip branch
                current_bad += 1
                color = (0, 0, 255)                   # 红色 BGR | Red in BGR

            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)    # 绘制检测框 | Draw bounding box
            cv2.putText(img, label, (x1, y1 - 10),              # 绘制标签 | Draw label
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

**核心检测逻辑与 detect_test_1.py 完全一致**，唯一区别是使用 `current_good`/`current_bad` 作为局部变量（每张图片独立计数），而非全局变量。
The core detection logic is **identical to detect_test_1.py**. The only difference is using `current_good`/`current_bad` as local variables (per-image counters) instead of global ones.

### 5.7 更新统计并保存 | Update Statistics & Save

```python
    total_good += current_good               # 将当前图片的好芯片数累加到全局 | Add to global good total
    total_bad += current_bad                 # 将当前图片的坏芯片数累加到全局 | Add to global bad total

    # 在图片左上角绘制统计文字 | Draw statistics text at top-left corner
    cv2.putText(img, f"Good: {current_good}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)   # Good 数量 (蓝色) | Good count (blue)
    cv2.putText(img, f"Bad: {current_bad}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)   # Bad 数量 (红色) | Bad count (red)

    # 弹出窗口显示结果 | Display result in a window
    cv2.imshow(f"Result - {filename}", img)

    # 保存标注后的图片到 out2/ 目录 | Save annotated image to out2/ directory
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, img)

    cv2.waitKey(1000)            # 窗口显示 1000 毫秒 (1秒) | Display window for 1000ms (1 second)
    cv2.destroyAllWindows()      # 关闭当前窗口 | Close current window
```

**`cv2.waitKey(1000)` vs `cv2.waitKey(0)` 对比:**

| 参数 Parameter | 行为 Behavior | 使用场景 Use Case |
|---------------|-------------|-----------------|
| `0` | 无限等待，直到用户按键 | 单张图片检测（需要人工确认每张） |
| | Wait indefinitely until key press | Single image detection (manual confirmation) |
| `1000` | 显示 1 秒后自动关闭 | 批量检测（自动化处理，无需手动干预） |
| | Auto-close after 1 second | Batch detection (fully automated, no manual intervention) |

### 5.8 输出汇总报告 | Print Summary Report

```python
print("=" * 60)                              # 输出 60 个等号的分隔线 | Print separator line
print("批量检测完成！| Batch detection completed!")
print(f"总检测图片数量 | Total images: {total_imgs}")      # 总共处理了多少张图片
print(f"所有图片总好芯片数 | Total good chips: {total_good}")  # 所有图片的好芯片之和
print(f"所有图片总坏芯片数 | Total bad chips: {total_bad}")   # 所有图片的坏芯片之和
print(f"处理后图片已保存至 | Processed images saved to: {output_dir}")
print("=" * 60)
```

汇总报告在**所有图片处理完毕后**才输出，给用户一个整体统计概览。注意这些 `print` 语句不在 `for` 循环内部。
The summary report is printed **after all images have been processed**, giving the user an overall statistical overview. Note that these `print` statements are **outside** the `for` loop.

### 5.9 完整代码流程图 | Complete Code Flow

```
开始 Start
  │
  ├── 1. 导入依赖库 Import libraries
  │
  ├── 2. 加载 YOLO 模型 Load YOLO model
  │
  ├── 3. 设置输入/输出路径 Set input/output paths
  │
  ├── 4. 创建输出目录 Create output directory
  │
  ├── 5. 初始化全局计数器 Init global counters (total_good=0, total_bad=0)
  │
  ├── 6. 遍历 datasets/ 下每个文件 For each file in datasets/:
  │   │
  │   ├── 6.1 拼接路径并读取图片 Join path & read image
  │   ├── 6.2 初始化当前图片计数器 Init per-image counters (current_good=0, current_bad=0)
  │   ├── 6.3 运行 YOLO 推理 Run YOLO inference
  │   ├── 6.4 遍历检测框 For each detection:
  │   │   ├── 获取坐标 Get coordinates
  │   │   ├── 获取类别 Get label
  │   │   ├── 累加局部计数 Increment local counter
  │   │   ├── 绘制矩形框 Draw rectangle
  │   │   └── 绘制标签 Draw label text
  │   ├── 6.5 累加到全局计数器 Add to global counters
  │   ├── 6.6 绘制局部统计文字 Draw per-image statistics
  │   ├── 6.7 显示窗口 Display window
  │   ├── 6.8 保存结果 Save result
  │   ├── 6.9 等待 1 秒 Wait 1 second
  │   └── 6.10 关闭窗口 Close window
  │
  ├── 7. 输出全局汇总报告 Print global summary report
  │
  └── 结束 End
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

**第三步：准备图片 | Step 3: Prepare images**
将待检测的芯片图片放入 `datasets/` 文件夹中。支持的图片格式：PNG、JPG、JPEG、BMP 等常见格式。
Place chip images to be detected into the `datasets/` folder. Supported image formats: PNG, JPG, JPEG, BMP, and other common formats.

### 6.2 运行程序 | Run Program

```bash
cd chip-quality-detector      # 进入项目目录 | Enter project directory
python detect_test_2.py       # 运行批量检测 | Run batch detection
```

### 6.3 操作说明 | Operation Instructions

| 步骤 Step | 操作 Action | 预期结果 Expected Result |
|----------|------------|------------------------|
| 1 | 准备图片到 `datasets/` | 确保至少有 1 张图片 | Ensure at least 1 image exists in `datasets/` |
| 2 | 运行程序 Run program | 程序自动加载模型并开始处理 | Program loads model and starts processing |
| 3 | 观察检测窗口 Observe windows | 每张图片显示 1 秒后自动切换下一张 | Each image shown for 1 second, then auto-advance |
| 4 | 等待程序结束 Wait for completion | 所有图片处理完毕后，窗口不再弹出 | When done, no more windows will pop up |
| 5 | 查看控制台汇总 View summary | 终端显示总图片数、总好/坏芯片数等统计信息 | Terminal shows total images, total good/bad chips, etc. |
| 6 | 检查输出文件 Check output | 打开 `out2/` 目录查看所有标注后的图片 | Open the `out2/` directory to view all annotated images |

---

## 七、输出示例 | 7. Output Example

### 7.1 控制台输出 | Console Output

运行程序处理 `datasets/` 中 20 张测试图片后的典型输出：
Typical console output after processing 20 test images in `datasets/`:

```
============================================================
批量检测完成！| Batch detection completed!
总检测图片数量 | Total images: 20
所有图片总好芯片数 | Total good chips: 156
所有图片总坏芯片数 | Total bad chips: 23
处理后图片已保存至 | Processed images saved to: out2
============================================================
```

### 7.2 输出文件 | Output Files

| 输入 Input | 输出 Output | 说明 Description |
|-----------|------------|-----------------|
| `datasets/chip1.png` | `out2/chip1.png` | 标注后的图片，与原图同名 | Annotated image, same name as original |
| `datasets/chip2.png` | `out2/chip2.png` | 同上 Same as above |
| ... | ... | 一一对应 One-to-one correspondence |

---

## 八、注意事项 | 8. Notes

| 注意事项 Note | 详细说明 Detail |
|-------------|---------------|
| **图片格式 Image Format** | 仅支持常见图片格式（PNG、JPG、JPEG、BMP 等）。不支持 PDF、视频等非图片文件 | Only common image formats are supported (PNG, JPG, JPEG, BMP, etc.). PDFs and videos are not supported |
| **空文件夹 Empty Folder** | 如果 `datasets/` 为空，程序不会报错，但会处理 0 张图片，汇总结果全为 0 | If `datasets/` is empty, the program won't crash but will process 0 images with all counts being 0 |
| **非图片文件 Non-Image Files** | `datasets/` 文件夹中不要放置非图片文件（如 .txt、.json），否则可能导致 `cv2.imread()` 返回 None 引发错误 | Do not place non-image files (e.g., .txt, .json) in the `datasets/` folder, as `cv2.imread()` may return None and cause errors |
| **自动关闭窗口 Auto-Close** | 每张图片窗口仅显示 1 秒（`cv2.waitKey(1000)`），如需更长时间观察，可将 `1000` 改为更大的值（单位：毫秒） | Each image window displays for 1 second only. To view longer, change `1000` to a larger value (unit: milliseconds) |
| **输出目录覆盖 Overwriting** | 每次运行程序会用新结果**覆盖** `out2/` 中的同名文件，不会删除旧文件 | Each run **overwrites** files with the same name in `out2/`, but does not delete old files |
| **内存占用 Memory** | 程序一次性只处理一张图片，内存占用较低，适合处理大量图片 | The program processes one image at a time with low memory usage, suitable for large batches |

---

## 九、与 detect_test_1.py 的对比 | 9. Comparison with detect_test_1.py

| 维度 Aspect | detect_test_1.py | detect_test_2.py |
|------------|------------------|------------------|
| 输入方式 Input | 单张图片 Single image | 整个文件夹 All images in folder |
| 文件遍历 File iteration | 无 No | `os.listdir()` + `for` 循环 |
| 计数器 Counters | 全局 2 个 Global × 2 | 全局 3 个 + 局部 2 个 Global × 3 + Local × 2 |
| 窗口关闭方式 Window close | 按任意键手动关闭 Manual key press | 1 秒自动关闭 Auto-close after 1s |
| 控制台输出 Console | 简短 Brief | 分隔线 + 汇总统计 Separator + summary |
| 输出目录 Output dir | `out1/` | `out2/` |
| 适用场景 Use case | 快速测试单张图片 Quick single test | 批量检测大量图片 Batch processing |

---

## 十、配套学习脚本 | 10. Companion Study Scripts

本程序对应一组逐步深入的学习脚本，每一版在前一版基础上新增一个功能点：
This program has a companion set of progressive study scripts, each adding one feature on top of the previous:

| 脚本 Script | 新增功能 New Feature | 说明 Description |
|------------|---------------------|-----------------|
| `detect_study_2_01th.py` | 批量图片读取与显示 | 遍历 `datasets/` 所有图片并逐一显示 | Read and display all images from `datasets/` |
| `detect_study_2_02th.py` | + YOLO 目标检测 | 加入模型推理、绘制检测框和类别标签 | Add YOLO inference, bounding boxes, and class labels |
| `detect_study_2_03th.py` | + 单图统计 | 加入每张图片的 good/bad 计数器及左上角统计显示 | Add per-image good/bad counters and on-screen statistics |
| `detect_study_2_04th.py` | + 全局汇总 | 加入全局计数器及控制台汇总报告 | Add global counters and console summary report |
| `detect_study_2_05th.py` | + 结果保存 | 加入输出目录创建及图片保存，功能与 `detect_test_2.py` 完全一致 | Add output directory creation and image saving, feature-complete with `detect_test_2.py` |

建议学习顺序：从 `detect_study_2_01th.py` 开始，逐版运行对比变化，最后阅读 `detect_test_2.py` 完整版代码。
Recommended learning order: start from `detect_study_2_01th.py`, run each version to compare changes, then read the complete `detect_test_2.py` code.

---

## 十一、学习要点 | 11. Key Learning Points

对于马来西亚学生，建议重点理解以下编程概念：
For Malaysian students, we recommend focusing on the following programming concepts:

| 概念 Concept | 代码体现 Code Example | 学习价值 Learning Value |
|-------------|---------------------|------------------------|
| **循环遍历 Loop** | `for filename in os.listdir(...)` | 理解如何批量处理文件 | Understanding batch file processing |
| **路径拼接 Path Join** | `os.path.join(folder, filename)` | 跨平台兼容的路径操作 | Cross-platform path operations |
| **累加器模式 Accumulator** | `total_good += current_good` | 经典的"局部+全局"双层统计模式 | Classic two-tier local+global statistics pattern |
| **自动化处理 Automation** | `cv2.waitKey(1000)` 自动关闭 | 无需人工干预的自动化流程设计 | Designing automated workflows without human intervention |

---

*文档版本 | Document Version: v2.0*
*更新日期 | Last Updated: 2026年5月 | May 2026*
*适用对象 | Target Audience: 马来西亚学生培训 | Malaysian Student Training*
