from ultralytics import YOLO

model = YOLO("models/trained/dog_detector_v1.pt")

results = model.predict(
    source="data/original_test_images",
    save=True,
    conf=0.25
)

print(f"Processed {len(results)} images")