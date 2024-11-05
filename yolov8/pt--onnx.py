from ultralytics import YOLO

model = YOLO(model="runs/detect/train2/weights/best.pt")

model.export(format="onnx")
