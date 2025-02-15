import cv2
from cv2.typing import map_int_and_double

def recognize_graph():
    # 读取图片
    filepath = "img/2.jpg"
    img = cv2.imread(filepath)
    img = cv2.resize(img, (600, int(img.shape[0] * (600 / img.shape[1])))) #设置分辨率

    # 转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用默认的人脸分类器
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 定义绘制颜色
    color = (0, 255, 255)

    # 调用识别人脸
    faceRects = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 检测到人脸时，绘制矩形框和标记
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # 左眼
            cv2.circle(img, (x + w // 3, y + h // 4 + 30), min(w // 10, h // 10), color)
            # 右眼
            cv2.circle(img, (x + 2 * w // 3, y + h // 4 + 30), min(w // 10, h // 10), color)
            # 嘴巴
            cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8), color)

    # 显示图像
    cv2.imshow("image", img)

    # 等待用户按键
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    recognize_graph()