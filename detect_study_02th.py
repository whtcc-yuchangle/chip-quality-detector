
from ultralytics import YOLO  # 导入YOLO目标检测库 | Import YOLO object detection library
import cv2                    # 导入图像处理库 | Import image processing library

model = YOLO("chip.pt")    # 加载训练好的芯片检测模型 | Load trained chip detection model
image_path = "datasets/chip1.png" # 待检测的图片路径 | Path of the image to detect

# 读取图片 | Read image
img = cv2.imread(image_path)

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
        if label == "good":
            color = (255, 0, 0)  # 蓝色 (Blue)
        else:
            color = (0, 0, 255)  # 红色 (Red)
        # 绘制检测框 | Draw bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        # 绘制标签文字 | Draw label text
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# 显示图片（弹出窗口）| Show image (popup window)
cv2.imshow("Chip Detection Result", img)
cv2.waitKey(0)          # 按任意键关闭窗口 | Press any key to close window
cv2.destroyAllWindows() # 释放窗口 | Destroy window
