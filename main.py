import cv2
import numpy as np

image_path = "давайте сделаем вид что тут ссылка на фотку.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Ошибка при загрузке изображения.")
    exit()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_img, 50, 150)

output_path = "давайте сделаем вид что тут ссылка на фотку Х2.jpg"
cv2.imwrite(output_path, edges)

cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
