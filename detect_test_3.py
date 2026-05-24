# =============================================================================
# 芯片实时摄像头检测程序 | Real-Time Webcam Chip Detection Program
# =============================================================================
# 功能：通过电脑摄像头实时捕获画面，自动识别芯片并区分好芯片(good)和坏芯片(bad)，
#       在画面中实时绘制检测框和统计数量，按 q 键退出。
# Purpose: Capture live video from the webcam, automatically detect chips in
#          real-time, classify them as good or bad, draw bounding boxes and
#          statistics on the live feed. Press 'q' to exit.
# =============================================================================

# ---------------------------------------------------------------------------
# 1. 导入依赖 | Import Dependencies
# ---------------------------------------------------------------------------
from ultralytics import YOLO  # YOLO 目标检测库 | YOLO object detection library
import cv2                    # OpenCV 图像处理与视频捕获库 | OpenCV image processing & video capture library

# ---------------------------------------------------------------------------
# 2. 初始化模型与摄像头 | Initialize Model & Camera
# ---------------------------------------------------------------------------
model = YOLO("chip.pt")        # 加载训练好的芯片检测模型 | Load the trained chip detection model

# 打开默认摄像头 | Open default camera
# 参数说明 | Parameter note:
#   0 = 外接 USB 摄像头 | External USB camera
#   1 = 笔记本内置摄像头 | Built-in laptop camera
#   如果摄像头无法打开，请尝试切换 0 和 1 | If camera fails to open, try switching 0 and 1
cap = cv2.VideoCapture(0)

# ---------------------------------------------------------------------------
# 3. 主循环 - 实时检测 | Main Loop - Real-Time Detection
# ---------------------------------------------------------------------------
while True:
    # 3.1 读取摄像头的一帧画面 | Read one frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break  # 读取失败则退出循环 | Exit loop if frame reading fails

    good_count = 0   # 当前帧中好芯片数量 | Good chip count in current frame
    bad_count = 0    # 当前帧中坏芯片数量 | Bad chip count in current frame

    # 3.2 运行 YOLO 模型进行目标检测 | Run YOLO Model for Object Detection
    results = model(frame)

    # 3.3 遍历检测结果，逐个绘制检测框 | Process Detection Results & Draw Bounding Boxes
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
                good_count += 1
                color = (255, 0, 0)    # 蓝色框标记好芯片 | Blue box for good chips
            else:
                bad_count += 1
                color = (0, 0, 255)    # 红色框标记坏芯片 | Red box for bad chips

            # 在画面上绘制矩形检测框 | Draw rectangle bounding box on the frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            # 在检测框上方绘制类别标签文字 | Draw class label text above the bounding box
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # 3.4 在画面左上角绘制实时统计信息 | Draw Real-Time Statistics at Top-Left Corner
    cv2.putText(frame, f"Good: {good_count}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)   # 好芯片数量（蓝色）| Good count (blue)
    cv2.putText(frame, f"Bad: {bad_count}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)   # 坏芯片数量（红色）| Bad count (red)

    # 3.5 显示实时检测画面 | Display Real-Time Detection Window
    cv2.imshow("Chip Real-Time Detection | 芯片实时检测", frame)

    # 3.6 检测按键：按 'q' 键退出程序 | Check Key Press: press 'q' to quit
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

# ---------------------------------------------------------------------------
# 4. 释放资源 | Release Resources
# ---------------------------------------------------------------------------
cap.release()               # 释放摄像头 | Release the webcam
cv2.destroyAllWindows()     # 关闭所有 OpenCV 窗口 | Close all OpenCV windows
print("检测已结束！| Detection stopped!")
