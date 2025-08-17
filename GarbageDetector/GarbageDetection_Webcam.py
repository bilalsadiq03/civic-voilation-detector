import cv2
import math
import cvzone
from ultralytics import YOLO

# Load YOLO model
yolo_model = YOLO("Model/best.pt")

# Define class names
class_labels = ['0', 'c', 'garbage', 'garbage_bag', 'sampah-detection', 'trash']

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)  

while True:
    success, img = cap.read()
    if not success:
        print("⚠️ Could not access webcam")
        break

    # Run YOLO on the frame
    results = yolo_model(img, stream=True)  # stream=True for efficiency

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            if conf > 0.3:  # show only confident predictions
                cvzone.cornerRect(img, (x1, y1, w, h), t=2)
                cvzone.putTextRect(img, f'{class_labels[cls]} {conf}',
                                   (x1, y1 - 10), scale=0.8, thickness=1, colorR=(255, 0, 0))

    # Show webcam feed
    cv2.imshow("Garbage Detection - Webcam", img)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
