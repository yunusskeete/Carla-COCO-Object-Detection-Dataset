# coding=utf-8
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Carla-COCO-Object-Detection-Dataset"""

import collections
import json
import os

import datasets


logger = datasets.logging.get_logger(__name__)

_DESCRIPTION = """\
This dataset contains 1028 images each 640x380 pixels.
The dataset is split into 249 test and 779 training examples.
Every image comes with MS COCO format annotations.
The dataset was collected in Carla Simulator, driving around in autopilot mode in various environments
(Town01, Town02, Town03, Town04, Town05) and saving every i-th frame.
The labels where then automatically generated using the semantic segmentation information.
"""

_HOMEPAGE = "https://github.com/yunusskeete/Carla-COCO-Object-Detection-Dataset"

_LICENSE = "MIT"

_URL = "https://github.com/yunusskeete/Carla-COCO-Object-Detection-Dataset/raw/master/Carla-COCO-Object-Detection-Dataset-No-Images/"
_URLS = {
    "train": _URL + "train/train.tar.gz",
    "test": _URL + "test/test.tar.gz",
}

_CATEGORIES = ["automobile", "bike", "motorbike", "traffic_light", "traffic_sign"]

class CARLA_COCO(datasets.GeneratorBasedBuilder):
    """Carla-COCO-Object-Detection-Dataset"""

    VERSION = datasets.Version("1.1.0")

    def _info(self):
        """This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset"""

        features = datasets.Features(
            {
                "image_id": datasets.Value("int64"),
                # "image": datasets.Image(),
                "width": datasets.Value("int32"),
                "height": datasets.Value("int32"),
                "file_name": datasets.Value("string"),
                "url": datasets.Value("string"),
                "objects": datasets.Sequence(
                    {
                        "id": datasets.Value("int64"),
                        "area": datasets.Value("int64"),
                        "bbox": datasets.Sequence(datasets.Value("float32"), length=4),
                        "category": datasets.ClassLabel(names=_CATEGORIES),
                    }
                ),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
        )

    def _split_generators(self, dl_manager):
        """This method is tasked with downloading/extracting the data and defining the splits depending on the configuration"""

        downloaded_files = dl_manager.download_and_extract(_URLS)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(downloaded_files["train"], "train.jsonl"),
                    "split": "train"
                }
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(downloaded_files["test"], "test.jsonl"),
                    "split": "test"
                }
            ),
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath, split):
        """
        This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        The `key` is for legacy reasons (tfds) and is not important in itself, but must be unique for each example.
        """

        logger.info("generating examples from = %s", filepath)

        with open(filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                yield key, {
                    "image_id": data["image_id"],
                    # "image": data["image"],
                    "width": data["width"],
                    "height": data["height"],
                    "file_name": data["file_name"],
                    "url": data["url"],
                    "objects": {
                        "id": data["objects"]["id"],
                        "area": data["objects"]["area"],
                        "bbox": data["objects"]["bbox"],
                        "category": [c-1 for c in data["objects"]["category"]]
                    },
                }