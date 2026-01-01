'''
必须是训练出RT模型后才能使用，该代码的目的是提高训练完毕的模型的精度
'''
from ultralytics import RTDETR
class Enforce_Training:
    def __init__(self,model="runs/train/test_exp/weights/best.pt"):
        self.model=model
    
    def train(self):
        self.model.train(data='config/data.yaml',
                        imgsz=1024,  # 原先是640，提高分辨率到1024
                        batch=4,     # 分辨率大了，显存占用会变大，需要减小 batch
                        lr0=0.0001,  # 降低学习率进行微调
                        device='0')  