# coding:utf-8
from ultralytics import YOLO

# 模型配置文件
model_yaml_path = "ultralytics/cfg/models/v8/yolov8n.yaml"
# 数据集配置文件
data_yaml_path = 'ultralytics/cfg/datasets/train2024.yaml'
# 预训练模型
pre_model_name = 'yolov8n.pt'

if __name__ == '__main__':
    # 加载预训练模型
    model = YOLO("ultralytics/cfg/models/v8/yolov8.yaml").load('yolov8s.pt')
    # 训练模型
    results = model.train(data=data_yaml_path, epochs=10, batch=4, name='train_v8')