## yolov8的检测算法-python大作业-杨鹏一
## 使用方法如下：在终端中启用命令即可
### 1.yolov8.2检测和训练自己数据集的代码
训练    D盘（我的放在了D盘）
yolo detect train data=D:/yolov8.2/yolov8/ultralytics/cfg/datasets/train2024.yaml   model=D:/yolov8.2/yolov8/weights/yolov8s.pt  epochs=100  imgsz=640 batch=4 workers=2
这里的终端输入的data上传地址和model存储地址以及后面的 epochs都可以更改
### 2.检测
yolo detect predict model=d:/yolov8.2/best.pt       source=d:/yolov8.2/test/
yolo detect predict model=E:/yolov8.2/yolov8s.pt       source=E:/yolov8.2/test/
