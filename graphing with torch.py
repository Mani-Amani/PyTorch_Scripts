import torch
import torchvision
from torchvision import transforms,datasets
train=datasets.MNIST("", train=True, download=True,
                    transform=transforms.Compose([transforms.ToTensor()]))
test=train=datasets.MNIST("", train=False, download=True,
                    transform=transforms.Compose([transforms.ToTensor()]))
trainset= torch.utils.data.DataLoader(train,batch_size=15,shuffle=True)
testset= torch.utils.data.DataLoader(test,batch_size=15,shuffle=True)

    
import matplotlib.pyplot as plt
plt.imshow(data[0][0].view(28,28))
plt.show()
