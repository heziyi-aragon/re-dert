'''
必须是训练出RT模型后才能使用，该代码的目的是提高训练完毕的模型的精度
'''
from ultralytics import RTDETR
class Enforce_Training:
    def __init__(self,model_path="runs/train/test_exp/weights/best.pt"):
        print(f"正在加载模型：{model_path}")
        self.model = RTDETR(model_path)
    
    def train(self):
        self.model.train(data="config/data.yaml",
                        epochs=50,
                        imgsz=1024,  # 原先是640，提高分辨率到1024
                        batch=12,     # 分辨率大了，显存占用会变大，需要减小 batch
                        lr0=0.0001,  # 降低学习率进行微调
                        device='0',
                        project="runs/train_finetune",
                        name='enforce_exp')  
    def fina_train(self):
        print("最后突击")
        self.model.train(
            data="config/data.yaml",
            epochs=30,       
            imgsz=1024,
            batch=12,
            optimizer='AdamW',#显式指定优化器，防止系统自动覆盖 lr0
            lr0=0.00001,     # 非常小的学习率 (1e-5)
            lrf=0.01,        # 最终学习率也很小
            cos_lr=True,     # 开启余弦退火，让学习率平滑下降
            device='0',
            project="runs/train_finetune",
            name='enforce_exp_final_boost'
        )