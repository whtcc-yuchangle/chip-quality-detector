
from ultralytics import YOLO  # YOLO 目标检测库 | YOLO object detection library
import cv2                    # OpenCV 图像处理库 | OpenCV image processing library
import os                     # 文件系统操作库 | File system operations library

model = YOLO("chip.pt")       # 加载训练好的 YOLO 模型 | Load the trained YOLO model
input_folder = "datasets"     # 待检测图片所在的文件夹 | Folder containing images to detect

total_good = 0   # 所有图片中好芯片的总数 | Total number of good chips across all images
total_bad = 0    # 所有图片中坏芯片的总数 | Total number of bad chips across all images
total_imgs = 0   # 已处理的图片总数 | Total number of images processed

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)  # 拼接完整图片路径 | Construct full image path
    total_imgs += 1  # 图片计数器 +1 | Increment image counter

    # 5.1 读取图片 | Read Image
    img = cv2.imread(img_path)
    current_good = 0  # 当前图片中好芯片数量 | Good chip count in current image
    current_bad = 0  # 当前图片中坏芯片数量 | Bad chip count in current image

    # 5.2 运行 YOLO 模型进行目标检测 | Run YOLO Model for Object Detection
    results = model(img)

    # 5.3 遍历检测结果，逐个绘制检测框 | Process Detection Results & Draw Bounding Boxes
    for result in results:
        for box in result.boxes:
            # 获取检测框的四个坐标 (左上角 x1,y1, 右下角 x2,y2)
            # Get bounding box coordinates (top-left x1,y1, bottom-right x2,y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # 获取检测目标的类别标签 (good 或 bad)
            # Get the class label of the detected object (good or bad)
            label = model.names[int(box.cls[0])]

            # 根据类别设置颜色并累加计数 | Set color by class and increment counter
            if label == "good":
                current_good += 1
                color = (255, 0, 0)  # 蓝色框标记好芯片 | Blue box for good chips
            else:
                current_bad += 1
                color = (0, 0, 255)  # 红色框标记坏芯片 | Red box for bad chips

            # 在图片上绘制矩形检测框 | Draw rectangle bounding box on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            # 在检测框上方绘制类别标签文字 | Draw class label text above the bounding box
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # 5.4 累加到全局统计 | Add to Global Statistics
    total_good += current_good
    total_bad += current_bad

    # 5.5 在图片左上角绘制当前图片的统计信息 | Draw Per-image Statistics at Top-Left Corner
    cv2.putText(img, f"Good: {current_good}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # 好芯片数量（蓝色）| Good count (blue)
    cv2.putText(img, f"Bad: {current_bad}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # 坏芯片数量（红色）| Bad count (red)

    cv2.imshow(f"Result - {filename}", img)

    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# ---------------------------------------------------------------------------
# 6. 输出汇总报告 | Print Summary Report
# ---------------------------------------------------------------------------
print("=" * 60)
print("批量检测完成！| Batch detection completed!")
print(f"总检测图片数量 | Total images: {total_imgs}")
print(f"所有图片总好芯片数 | Total good chips: {total_good}")
print(f"所有图片总坏芯片数 | Total bad chips: {total_bad}")
print("=" * 60)
