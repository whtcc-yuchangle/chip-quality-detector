
from ultralytics import YOLO # 导入 YOLO 目标检测库 | Import YOLO object detection library
import cv2 # 导入图像处理库 | Import image processing library
import os # 导入文件系统库 | Import file system library

model = YOLO ("chip.pt") # 加载训练好的模型 | Load trained model
input_folder = "datasets" # 待检测的图片文件夹（已修改为 datasets）| Folder with images to detect
output_dir = "out2" # 处理后图片保存文件夹 | Output folder

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

total_good = 0 # 总好芯片数量 | Total good chips
total_bad = 0 # 总坏芯片数量 | Total bad chips
total_imgs = 0 # 总图片数量 | Total images

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    total_imgs += 1  # 图片数量 + 1 | Increment image count

    img = cv2.imread(img_path)
    current_good = 0
    current_bad = 0
    results = model(img)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[int(box.cls[0])]
            if label == "good":
                current_good += 1
                color = (255, 0, 0)  # 蓝色 | Blue
            else:
                current_bad += 1
                color = (0, 0, 255)  # 红色 | Red
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    total_good += current_good
    total_bad += current_bad
    cv2.putText(img, f"Good: {current_good}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, f"Bad: {current_bad}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow(f"Result - {filename}", img)
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

print ("="*60)
print ("批量检测完成！| Batch detection completed!")
print (f"总检测图片数量 | Total images: {total_imgs}")
print (f"所有图片总好芯片数 | Total good chips: {total_good}")
print (f"所有图片总坏芯片数 | Total bad chips: {total_bad}")
print (f"处理后图片已保存至 | Processed images saved to: {output_dir}")
print ("="*60)
