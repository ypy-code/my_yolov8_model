## yolov8的检测算法-python大作业-杨鹏一
## 使用方法如下：在终端中启用命令即可
### 1.yolov8.2检测和训练自己数据集的代码
训练    D盘（我的放在了D盘）

yolo detect train data=D:/yolov8.2/yolov8/ultralytics/cfg/datasets/train2024.yaml   model=D:/yolov8.2/yolov8/weights/yolov8s.pt  epochs=100  imgsz=640 batch=4 workers=2

这里的终端输入的data上传地址和model存储地址以及后面的 epochs都可以更改
### 2.检测
yolo detect predict model=d:/yolov8.2/best.pt       source=d:/yolov8.2/test/

yolo detect predict model=E:/yolov8.2/yolov8s.pt       source=E:/yolov8.2/test/

同理，这里的source也是根据自己的文件目录去更改
## 代码仓库文件说明
 1.train_lable 训练图像的标签图片（含格式要求）
 
 2.train_image 要求训练的图片 （图片的标注工作是在LabelMe上进行的）

 3.train_code 训练的源代码和一些我训练的图片结果，其中train4是最终的训练结果

 4.如果大家使用百度网盘中的zip文件，直接下载代码即可，就不用再下载数据了

 5.如果大家想要使用源代码，并且放入自己的数据集，直接下载本代码仓库就可以，并且将自己的数据集放到相应的文件夹下  train2024

## train_code内容说明
 1.runs/detect/train4目录是最终的8000多张标记的图片的训练结果

 2.runs/detect/train4/weights/best.pt这是训练结果最终的最佳结果和已经训练好的模型，可以向外导出应用在同等情况下

 3.yolov8/ultralytics/cfg/datasets/train2024.yaml这是标记的类的说明，我一共标记了4个类，大家可以参考yolov8/ultralytics/cfg/datasets/coco8.yaml目录下的80余个类来进行自己训练的类的选择
