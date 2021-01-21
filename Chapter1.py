import cv2
print("Package Imported")
"""
img = cv2.imread("Resources/lena.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)  #0 infinite delay, 1000 -> 1sec

cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

#Web Cam Access
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
