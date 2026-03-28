from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# COCO classes for vehicles
VEHICLE_CLASSES = [2, 3, 5, 7]  # car, bike, bus, truck

def detect_vehicles(frame):
    results = model(frame)[0]
    count = 0

    for box in results.boxes:
        cls = int(box.cls[0])
        if cls in VEHICLE_CLASSES:
            count += 1

    return count