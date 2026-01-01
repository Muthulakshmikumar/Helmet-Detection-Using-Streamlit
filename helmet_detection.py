from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

def detect_helmet(image):
    results = model(image)
    
    helmet_found = False

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]

        if label == "person":
            helmet_found = True

    result_image = results[0].plot()
    return result_image, helmet_found
