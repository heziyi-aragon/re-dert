from ultralytics.models import RTDETR
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
 
if __name__ == '__main__':
    #model = RTDETR(model='ultralytics/cfg/models/rt-detr/rtdetr-l.yaml')#定义模型路径
    model = RTDETR(model='config/rtdetr-l.yaml')
    # model.load('XXXX.pt')
    model.train(data='config/data.yaml', epochs=2, batch=4, device='0', imgsz=640, workers=2, deterministic=False,
                cache=False,amp=True, mosaic=False, project='runs/train', name='test_exp')#定义训练参数
    # val_status=input("是否进行模型验证：")
    # if val_status:
    #     model = RTDETR(model='./runs/train/exp/weights/best.pt')#训练后的模型路径
    #     model.val(data='config/data.yaml', split='val', batch=1, device='0', project='runs/val', name='exp',
    #             half=False,)