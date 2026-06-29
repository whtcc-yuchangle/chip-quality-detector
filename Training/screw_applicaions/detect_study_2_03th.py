
from ultralytics import YOLO  # YOLO 目标检测库 | YOLO object detection library
import cv2                    # OpenCV 图像处理库 | OpenCV image processing library
import os                     # 文件系统操作库 | File system operations library

model = YOLO("screw.pt")       # 加载训练好的 YOLO 模型 | Load the trained YOLO model
input_folder = "datasets"     # 待检测图片所在的文件夹 | Folder containing images to detect

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)  # 拼接完整图片路径 | Construct full image path

    # 5.1 读取图片 | Read Image
    img = cv2.imread(img_path)
    current_large = 0  # 当前图片中大螺丝数量 | Large screw count in current image
    current_medium = 0  # 当前图片中中螺丝数量 | Medium small screw count in current image
    current_small = 0  # 当前图片中小螺丝数量 | Small screw count in current image

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
            if label == "large":
                current_large += 1
                color = (255, 0, 0)  # 蓝色框标记大螺丝 | Blue box for large screws
            elif label == "medium":
                current_medium += 1
                color = (0, 255, 0)  # 绿色框标记中螺丝 | Green box for medium screws
            else:
                current_small += 1
                color = (0, 0, 255)  # 红色框标记小螺丝 | Red box for small screws

            # 在图片上绘制矩形检测框 | Draw rectangle bounding box on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            # 在检测框上方绘制类别标签文字 | Draw class label text above the bounding box
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # 5.5 在图片左上角绘制当前图片的统计信息 | Draw Per-image Statistics at Top-Left Corner
    cv2.putText(img, f"Large: {current_large}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # 大螺丝数量（蓝色）| Large count (blue)
    cv2.putText(img, f"Medium: {current_medium}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # 中螺丝数量（绿色）| Medium count (green)
    cv2.putText(img, f"Small: {current_small}", (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  # 小螺丝数量（红色）| Small count (red)

    cv2.imshow(f"Result - {filename}", img)

    cv2.waitKey(1000)
    cv2.destroyAllWindows()
