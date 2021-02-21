# coco数据集提取person，或者其他类别
## 使用步骤：
### 1. 下载yolo版本的coco数据集的labels：[https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip](https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip)
### 2. 下载coco数据集（建议使用迅雷等下载器下载）：
train:[http://images.cocodataset.org/zips/train2017.zip](http://images.cocodataset.org/zips/train2017.zip)
valid:[http://images.cocodataset.org/zips/val2017.zip](http://images.cocodataset.org/zips/val2017.zip)
### 3. 新建代码目录，直接将class_selected.py，以及下载后解压的coco数据集放入第1步下载解压后的coco目录下，然后在coco/images和coco/labels目录下新建train和val目录即可
目录结构如下：  
coco  
├── images  
│   ├── train2017  
│   ├── train  
│   ├── val2017  
│   └── val  
├── labels  
│   ├── train2017  
│   ├── train  
│   ├── val2017  
│   └── val  
└── class_selected.py

### 4. 看情况修改一下class_selected.py代码中的文件夹目录，然后运行即可