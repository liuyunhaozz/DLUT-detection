import os
from PIL import Image


train_img_dir = os.listdir('datasets/object/images/train')
val_img_dir = os.listdir('datasets/object/images/val')

for index, name in enumerate(train_img_dir):
    path = os.path.join('datasets/object/images/train', name)

    img = Image.open(path)
    if img.size != (640, 480):
        img_deal = img.resize((640,480),Image.ANTIALIAS) # 转化图片
        img_deal = img_deal.convert('RGB') # 保存为.jpg格式才需要
        img_deal.save(path)

for index, name in enumerate(val_img_dir):
    path = os.path.join('datasets/object/images/val', name)

    img = Image.open(path)
    if img.size != (640, 480):
        img_deal = img.resize((640,480),Image.ANTIALIAS) # 转化图片
        img_deal = img_deal.convert('RGB') # 保存为.jpg格式才需要
        img_deal.save(path)

