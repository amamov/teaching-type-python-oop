# deep-learing-example
# * 해당 파일은 Colab에서 실행해야 합니다.


from google.colab import drive

drive.mount("/content/mai_drive")

import time
import math
from torch import nn, optim, cuda
from torch.utils import data
from torchvision import datasets, transforms
import torch
import torchvision


class VGG(nn.Module):
    """
    VGG model
    """

    def __init__(self, features):
        super().__init__()
        self.features = features
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(512, 512),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(512, 512),
            nn.ReLU(True),
            nn.Linear(512, 10),
        )
        # Initialize weights
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2.0 / n))
                m.bias.data.zero_()

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


class Machine:

    """
    dataset : cifar10
    model : VGG16
    """

    BASE_DIR = "/content/mai_drive/MyDrive/deep_learning"
    DATASETS_DIR = f"{BASE_DIR}/datasets"

    def __init__(self, batch_size: int = 64, epoch_size: int = 1):
        self.batch_size = batch_size
        self.epoch_size = epoch_size
        self.device = "cuda" if cuda.is_available() else "cpu"
        self.get_data()
        self.model = Machine.vgg16()
        self.model.to(self.device)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(self.model.parameters(), lr=0.01, momentum=0.5)

    def get_data(self):
        normalize = transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        )

        self.train_dataset = datasets.CIFAR10(
            root=f"{Machine.DATASETS_DIR}/cifar10_datasets/",
            train=True,
            transform=transforms.Compose(
                [
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomCrop(32, 4),
                    transforms.ToTensor(),
                    normalize,
                ]
            ),
            download=True,
        )

        self.test_dataset = datasets.CIFAR10(
            root=f"{Machine.DATASETS_DIR}/cifar10_datasets/",
            train=False,
            transform=transforms.Compose(
                [
                    transforms.ToTensor(),
                    normalize,
                ]
            ),
        )

        self.train_loader = torch.utils.data.DataLoader(
            dataset=self.train_dataset, batch_size=self.batch_size, shuffle=True
        )

        self.test_loader = torch.utils.data.DataLoader(
            dataset=self.test_dataset, batch_size=self.batch_size, shuffle=False
        )

    @staticmethod
    def vgg16():
        """VGG 16-layer model (configuration)"""

        cfg = [
            64,
            64,
            "M",
            128,
            128,
            "M",
            256,
            256,
            256,
            "M",
            512,
            512,
            512,
            "M",
            512,
            512,
            512,
            "M",
        ]

        def make_layers(cfg, batch_norm=False):
            layers = []
            in_channels = 3
            for v in cfg:
                if v == "M":
                    layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
                else:
                    conv2d = nn.Conv2d(
                        in_channels=in_channels,
                        out_channels=v,
                        kernel_size=3,
                        padding=1,
                    )
                    if batch_norm:
                        layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
                    else:
                        layers += [conv2d, nn.ReLU(inplace=True)]
                    in_channels = v
            return nn.Sequential(*layers)

        return VGG(make_layers(cfg))

    def train(self, epoch):
        self.model.train()
        for batch_idx, (data, target) in enumerate(self.train_loader):
            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

            if batch_idx % 10 == 0:
                print(
                    (
                        f"Train Epoch : {epoch} | Batch Status : {batch_idx*len(data)}/{len(self.train_loader.dataset)}"
                        f"({100. * batch_idx / len(self.train_loader)}%) | Loss : {loss.item()}"
                    )
                )

    def test(self):
        self.model.eval()
        test_loss = 0
        correct = 0
        for data, target in self.test_loader:
            data, target = data.to(self.device), target.to(self.device)
            output = self.model(data)
            test_loss += self.criterion(output, target).item()
            pred = output.data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).cpu().sum()
            test_loss /= len(self.test_loader.dataset)
            print(
                f"\nTest set: Accuracy : {correct}/{len(self.test_loader.dataset)}"
                f"({100. * correct / len(self.test_loader.dataset):.0f}%)"
            )

    def learning(self):
        since = time.time()
        for epoch in range(1, self.epoch_size + 1):
            epoch_start = time.time()
            self.train(epoch)
            m, s = divmod(time.time() - epoch_start, 60)
            print(f"Training time: {m:.0f}m {s:.0f}s")

        self.test()

        m, s = divmod(time.time() - epoch_start, 60)
        print(f"Tesing time: {m:.0f}m {s:.0f}s")

        m, s = divmod(time.time() - epoch_start, 60)
        print(f"Total time : {m:.0f}m {s: .0f}s \nModel was trained on {self.device}!")


class ResNetMachine(Machine):

    """
    [Machine based in ResNet Model]
    """

    def __init__(self, batch_size=64, epoch_size=1):
        super().__init__(batch_size, epoch_size)
        model = torchvision.models.resnet.ResNet(pretrained=True, progress=True)
        self.setup_model(model)


if __name__ == "__main__":
    machine = Machine(batch_size=64, epoch_size=300)
    machine.learning()
