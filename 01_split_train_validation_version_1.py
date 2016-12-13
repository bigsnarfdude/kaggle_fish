"""
First portion of the baseline set of scripts to get going.
I unzipped all training data into train_all_files variable path.

This script will grab all the files from train_all_file path and put 80% into
train_data_dir path and 20% will be saved for val_data_dir
"""
import os
import numpy as np
import shutil


np.random.seed(2016)

train_data_dir = '/media/datadisk/nature/train_split'
val_data_dir = '/media/datadisk/nature/val_split'
train_all_files = '/media/datadisk/nature/train'
FISHNAMES = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']

nbr_train_samples = 0
nbr_val_samples = 0

# Training proportion
split_proportion = 0.8

for fish in FISHNAMES:
    if fish not in os.listdir(train_all_files):
        os.mkdir(os.path.join(train_all_files, fish))

    total_images = os.listdir(os.path.join(train_all_files, fish))

    nbr_train = int(len(total_images) * split_proportion)

    np.random.shuffle(total_images)

    train_images = total_images[:nbr_train]

    val_images = total_images[nbr_train:]

    for img in train_images:
        source = os.path.join(train_all_files, fish, img)
        target = os.path.join(train_data_dir, fish, img)
        shutil.copy(source, target)
        nbr_train_samples += 1

    if fish not in os.listdir(val_data_dir):
        os.mkdir(os.path.join(val_data_dir, fish))

    for img in val_images:
        source = os.path.join(train_all_files, fish, img)
        target = os.path.join(val_data_dir, fish, img)
        shutil.copy(source, target)
        nbr_val_samples += 1

print('Finish splitting train and val images!')
print('# training samples: {}, # val samples: {}'.format(nbr_train_samples, nbr_val_samples))
