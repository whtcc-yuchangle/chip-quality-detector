
from ultralytics import YOLO # 导入 YOLO 目标检测库 | Import YOLO object detection library
import cv2 # 导入图像处理库 | Import image processing library

model = YOLO ("chip.pt") # 加载训练好的芯片检测模型 | Load trained chip detection model
cap = cv2.VideoCapture (0) # 打开默认摄像头（1 为内置摄像头，可调 0/1）| Open default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break  # 读取失败则退出 | Exit if failed to read frame
    good_count = 0
    bad_count = 0
    results = model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[int(box.cls[0])]
            if label == "good":
                good_count += 1
                color = (255, 0, 0)  # 蓝色 | Blue
            else:
                bad_count += 1
                color = (0, 0, 255)  # 红色 | Red
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    cv2.putText(frame, f"Good: {good_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f"Bad: {bad_count}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Chip Real-Time Detection", frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release () # 释放摄像头 | Release camera
cv2.destroyAllWindows () # 关闭所有窗口 | Close all windows
print ("检测已结束！| Detection stopped!")
