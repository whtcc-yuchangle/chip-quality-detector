
import cv2                    # 导入图像处理库 | Import image processing library

image_path = "datasets/chip1.png" # 待检测的图片路径 | Path of the image to detect

# 读取图片 | Read image
img = cv2.imread(image_path)

# 显示图片（弹出窗口）| Show image (popup window)
cv2.imshow("Chip Detection Result", img)
cv2.waitKey(0)          # 按任意键关闭窗口 | Press any key to close window
cv2.destroyAllWindows() # 释放窗口 | Destroy window
