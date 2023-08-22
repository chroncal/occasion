import torch
import torchvision
from torchvision import datasets,transforms
from torch.autograd import Variable
import torch.utils.data.dataloader as Data
import torch.nn as nn
from torchvision import models
import numpy as np
import cv2
# 导入相应的库之后定义函数

def show_image_diff(original_img,original_label,adversarial_img,adversarial_label):
    # 对比展示原始图片和对抗样本图片
    import matplotlib.pyplot as plt
    plt.figure()
    
    if original_img.any()>1.0:
        original_img=original_img/255.0# 归一化
    if adversarial_img.any()>1.0:
        adversarial_img=adversarial_img/255.0
        
    plt.subplot(131)
    plt.title('Original')
    plt.imshow(original_img)
    plt.axis('off')
    plt.subplot(132)
    plt.title('Adversarial')
    plt.imshow(adversarial_img)
    plt.axis('off')
 
    plt.subplot(133)
    plt.title('Adversarial-Original')
    difference=adversarial_img-original_img
    # (-1,1)->(0,1)
    difference=difference/abs(difference).max()/2.0+0.5
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(difference)
    plt.show()


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
image_path=r"C:\\Users\\Meow_Sakura\\Desktop\\test\\02923.jpg"
orig=cv2.imread(image_path)[...,::-1]
orig=cv2.resize(orig,(224,224))
img=orig.copy().astype(np.float32)
 
mean=[.485,.456, 0.406]
std=[.229,.224,.225]
img/=255.0
img=(img-mean)/std
img=img.transpose(2,0,1)# 将hwc转成chw
 
img=np.expand_dims(img,axis=0)
img=Variable(torch.from_numpy(img).to(device).float())
print(img.shape)# should be torch.Size([1,3,224,224])
# 使用模型预测
model=models.alexnet(pretrained=True).to(device).eval()
label=np.argmax(model(img).data.cpu().numpy())
print("label{}".format(label))# should be 345

# 设置梯度可获取
img.requires_grad=True
 
# model的参数不用改变，因此设置梯度为false
for param in model.parameters():
    param.requires_grad = False
 
optimizer = torch.optim.Adam([img])
loss_func = torch.nn.CrossEntropyLoss()
 
# 超参数设置
epochs=100
e=0.001
target=266
target = Variable(torch.Tensor([float(target)]).to(device).long()) 
for epoch in range(epochs):
    output=model(img)
    loss = loss_func(output,target)
    label=np.argmax(output.data.cpu().numpy())
    print("epoch={} loss={} label={}".format(epoch,loss,label))
    
    # 如果定向攻击成功
    if label == target:
        print("")
        break
    
    # 梯度清零
    optimizer.zero_grad()
    # 反向传递梯度信息
    loss.backward()
    img.data=img.data-e*torch.sign(img.grad.data)# 利用梯度信息更新输入图像x，e对应论文中的namida

adv=img.data.cpu().numpy()[0]
print(adv.shape)# should be (3,224,224)
adv =adv.transpose(1,2,0)# chw->hwc
adv=(adv*std)+mean
adv=adv*255.0
adv=np.clip(adv,0,255).astype(np.uint8)# np.clip()函数，将数值限定在一个范围内，此处，限制为0~255，同torch.clamp()
# 展示图像和不同
show_image_diff(orig,388,adv,target.data.cpu().numpy()[0])