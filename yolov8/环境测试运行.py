from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("weights/yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
#model.train(data="coco128.yaml", epochs=3)  # train the model
#metrics = model.val()  # evaluate model performance on the validation set
results = model.predict(source="ultralytics/assets/bus.jpg",save=True)  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format


