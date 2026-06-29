
import cv2                    # OpenCV 图像处理库 | OpenCV image processing library
import os                     # 文件系统操作库 | File system operations library

input_folder = "datasets"     # 待检测图片所在的文件夹 | Folder containing images to detect

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)  # 拼接完整图片路径 | Construct full image path

    # 5.1 读取图片 | Read Image
    img = cv2.imread(img_path)

    cv2.imshow(f"Result - {filename}", img)

    cv2.waitKey(1000)
    cv2.destroyAllWindows()
