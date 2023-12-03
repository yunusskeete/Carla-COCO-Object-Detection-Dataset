# Carla-COCO-Object-Detection-Dataset-No-Images

**Hugging Face COCO-Style Labelled Dataset for Object Detection in Carla Simulator**

This dataset contains 1028 images, each 640x380 pixels, with corresponding publically accessible URLs.
The dataset is split into 249 test and 779 training examples.
The dataset was collected in Carla Simulator, driving around in autopilot mode in various environments (Town01, Town02, Town03, Town04, Town05) and saving every i-th frame.
The labels where then automatically generated using the semantic segmentation information.

**Available classes are:**

* Automobile (Car, Truck)
* Bike
* Motorbike
* Traffic light
* Traffic sign

**Example image:**

![example image](https://github.com/yunusskeete/Carla-COCO-Object-Detection-Dataset/raw/master/images/train/Town01_011940.png)

**Example annotated image:**

![example image with annotations](https://github.com/yunusskeete/Carla-COCO-Object-Detection-Dataset/raw/master/Town01_011940_annotated.png)

## Dataset Structure
### Data Instances
A data point comprises an image, its file name, its publically accessible URL, and its object annotations.
```json
{
    "image_id": 14,
    "width": 640,
    "height": 380,
    "file_name": "Town01_001860.png",
    "url": "https: //github.com/yunusskeete/Carla-COCO-Object-Detection-Dataset/blob/master/images/train/Town01_001860.png",
    "objects": {
        "id": [1, 2],
        "area": [41650, 150],
        "bbox": [
            [201, 205, 238, 175],
            [363, 159, 6, 25]
        ],
        "category": [1, 4]
    }
}
```

### Data Fields
* **image_id**: the image id
* **width**: the image width
* **height**: the image height
* **objects**: a dictionary containing bounding box metadata for the objects present on the image
* **id**: the annotation id
* **area**: the area of the bounding box
* **bbox**: the object's bounding box (in the coco format)
* **category**: the object's category, with possible values including automobile (1), bike (2), motorbike (3), traffic_light (4) and traffic_sign (5)

## Contributions
This repo is a fork from [Carla-Object-Detection-Dataset](https://github.com/DanielHfnr/Carla-Object-Detection-Dataset).
Acknowledgements are made to [DanielHfnr](https://github.com/DanielHfnr) for the original data collection and dataset preparation.