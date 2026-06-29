
from ultralytics import YOLO  # 导入YOLO目标检测库 | Import YOLO object detection library
import cv2                    # 导入图像处理库 | Import image processing library
import os                     # 导入文件系统库 | Import file system library

model = YOLO("screw.pt")    # 加载训练好的螺丝检测模型 | Load trained screw detection model
image_path = "datasets/0001.png" # 待检测的图片路径 | Path of the image to detect
output_dir = "out1"              # 结果保存文件夹 | Result save folder

# 自动创建输出文件夹 | Auto create output folder
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取图片 | Read image
img = cv2.imread(image_path)

# 初始化计数器 | Initialize counters
large_count = 0
medium_count = 0
small_count = 0

# 执行检测 | Run detection
results = model(image_path)

# 遍历检测结果 | Traverse detection results
for result in results:
    for box in result.boxes:
        # 获取坐标 | Get box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        # 获取类别 | Get class label
        label = model.names[int(box.cls[0])]
        # 统计数量 | Count chips
        if label == "large":
            large_count += 1
            color = (255, 0, 0)  # 蓝色 (Blue)
        elif label == "medium":
            medium_count += 1
            color = (0, 255, 0)  # 绿色 (Green)
        else:
            small_count += 1
            color = (0, 0, 255)  # 红色 (Red)
        # 绘制检测框 | Draw bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        # 绘制标签文字 | Draw label text
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# 绘制左上角统计文字 | Draw count text on top-left
cv2.putText(img, f"Large: {large_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.putText(img, f"Medium: {medium_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.putText(img, f"Small: {small_count}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# 保存结果图片 | Save result image
cv2.imwrite(f"{output_dir}/result.png", img)

# 显示图片（弹出窗口）| Show image (popup window)
cv2.imshow("Screw Study Detection Result", img)
cv2.waitKey(0)          # 按任意键关闭窗口 | Press any key to close window
cv2.destroyAllWindows() # 释放窗口 | Destroy window
