# Импортируем библиотеки
import cv2

# Захватываем камеру
cap = cv2.VideoCapture(0)

while not (cv2.waitKey(100) & 0xFF == ord('q')):
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)
    cv2.imwrite('../camera.jpg', frame)

cap.release()
cv2.destroyAllWindows()