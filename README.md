Fssh is based in Vancouver, BC. This is my attempt at the Fish Prediction competition for Kaggle. https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring


# Step 1
Download data from kaggle.

I put all my data unzipped into directory

```
/media/datadisk/nature/


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
