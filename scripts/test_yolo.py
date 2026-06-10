from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True
)

print("YOLO test complete.")