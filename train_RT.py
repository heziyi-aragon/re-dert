from ultralytics.models import RTDETR
from Enforce_Training import Enforce_Training
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
 
if __name__ == '__main__':
    #model = RTDETR(model='ultralytics/cfg/models/rt-detr/rtdetr-l.yaml')#定义模型路径
    val_status=input("你接下来要进行什么操作？ 1：训练模型。\n2：验证模型。3：升级模型。")
    if val_status=="1":
        print("准备训练模型")
        model = RTDETR(model='config/rtdetr-l.yaml')
        # model.load('XXXX.pt')
        model.train(data='config/data.yaml', epochs=2, batch=4, device='0', imgsz=640, workers=2, deterministic=False,
                    cache=False,amp=True, mosaic=False, project='runs/train', name='test_exp')#定义训练参数
    elif val_status=="2":#验证
        print("准备验证模型")
        choose=input(f"接下来是验证模型还是继续增强？1：验证模型。2：TTA增强模型。")
        if choose =="1":
            model = RTDETR(model='./runs/train/test_exp/weights/best.pt')#训练后的模型路径
            model.train(data='config/data.yaml', epochs=100, batch=16, device='0', imgsz=640, workers=2, deterministic=False,
                        cache=False,amp=True, mosaic=False, project='runs/train', name='test_exp')#定义训练参数
        elif choose =="2":#TTA (测试时增强)
            model = RTDETR(model="./runs/train_finetune/enforce_exp3/weights/best.pt")
            metrics = model.val(data='config/data.yaml',split='test',imgsz=1024, batch=1,augment=True)
            print(f"TTA mAP50: {metrics.box.map50}")
    elif val_status=="3":#增强训练
        print("准备增强模型")
        choose=input("接下来是衔接上一轮继续还是选择最好的继续？1：衔接上一轮继续。2：从最好的开始。3：如果运行2之后还不满意")
        if choose=="1":
            url="runs/train/test_exp/weights/last.pt" #衔接继续学：如果根据日志,100轮前损失函数（Loss）还在下降，说明模型还能学
            model = RTDETR(model='./runs/train/test_exp/weights/last.pt')#训练后的模型路径
            model.train(resume=True)
        elif choose=="2":
            #url="runs/train/test_exp/weights/best.pt"#增强学习
            url="runs/train_finetune/enforce_exp2/weights/best.pt"#增强学习
            Train=Enforce_Training(url)
            Train.train()
        elif choose=="3":
            url="runs/train_finetune/enforce_exp3/weights/best.pt"#增强学习
            Train=Enforce_Training(url)
            Train.fina_train()