Fssh is based in Vancouver, BC. This is my attempt at the Fish Prediction competition for Kaggle. https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring


# Step 1
Download data from kaggle.

I put all my data unzipped into directory. Then "mkdir train_split"  and mkdir "val_split". 

```
/media/datadisk/nature/

.
├── sample_submission_stg1.csv
├── test_stg1
│   └── test_images
│       ├── img_00005.jpg
│       ├── img_00007.jpg
│       ├── img_00009.jpg
...
│       ├── img_07909.jpg
│       ├── img_07910.jpg
│       └── img_07921.jpg
├── train
│   ├── ALB
│   │   ├── img_00003.jpg
│   │   ├── img_00010.jpg
│   │   ├── img_00012.jpg
...
│   │   ├── img07795.jpg
│   │   ├── img_07804.jpg
│   │   └── img_07825.jpg
│   ├── DOL
│   │   ├── img_00165.jpg
│   │   ├── img_00325.jpg
│   │   ├── img_00348.jpg
...
│   │   ├── img_07693.jpg
│   │   ├── img_07728.jpg
│   │   └── img_07898.jpg
│   ├── LAG
│   │   ├── img_00091.jpg
│   │   ├── img_00176.jpg
│   │   ├── img_00657.jpg
...
│       ├── img_07648.jpg
│       ├── img_07775.jpg
│       └── img_07901.jpg
└── zipped
    ├── sample_submission_stg1.csv.zip
    ├── test_stg1.zip
    └── train.zip
```


# Step 2
Clone directory into working folder like your Desktop or home directory:

```
git clone https://github.com/bigsnarfdude/kaggle_fish.git
```


# Step 3
Run the first script to split your training data. Make sure you edit the file with your directory paths. Script will create new train and validation datasets.

```
python 01_split_train_validation_version_1.py
```


# Step 4
Run the second script to on your training data.  Make sure you edit the file with your directory paths. Script will create HDF5 file of weights named:
weights.h5

```
python 02_train_keras_model_version_1.py
```

# Step 5
Run the third script to on your training data.  Make sure you edit the file with your directory paths. Script will read HDF5 file of weights and create the submit.csv file for your kaggle submission.

```
python 03_predict_version_1.py
```
