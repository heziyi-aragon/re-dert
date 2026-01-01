from ultralytics.models import RTDETR
from Enforce_Training import Enforce_Training
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
 
if __name__ == '__main__':
    #model = RTDETR(model='ultralytics/cfg/models/rt-detr/rtdetr-l.yaml')#定义模型路径
    val_status=input("你接下来要进行什么操作？ 1：训练模型。\n2：验证模型。3：升级模型。")
    if val_status==1:
        model = RTDETR(model='config/rtdetr-l.yaml')
        # model.load('XXXX.pt')
        model.train(data='config/data.yaml', epochs=2, batch=4, device='0', imgsz=640, workers=2, deterministic=False,
                    cache=False,amp=True, mosaic=False, project='runs/train', name='test_exp')#定义训练参数
    elif val_status==2:
        model = RTDETR(model='./runs/train/test_exp2/weights/best.pt')#训练后的模型路径
        model.val(data='config/data.yaml', split='val', batch=1, device='0', project='runs/val', name='exp',
                half=False)
    elif val_status==3:
        url="runs/train/test_exp/weights/best.pt"
        Train=Enforce_Training(url)
        Train.train()