from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import glob
import cv2
import pandas as pd
import os


np.random.seed(2016)
img_width = 299
img_height = 299
FISHNAMES = ['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
project_directory = '/home/ubuntu/kaggle_fish/'
weights_path = os.path.join(project_directory, 'weights.h5')
test_data_dir = "/media/datadisk/nature/test_stg1"


def get_im_cv2(path):
    img = cv2.imread(path)
    # I'm not sure what is width and height inputs to resize function ???
    resized = cv2.resize(img, (299,299), interpolation=cv2.INTER_LINEAR)

    return resized


def load_test():
    path = os.path.join(test_data_dir, '*.jpg')
    files = sorted(glob.glob(path))

    X_test = []
    X_test_id = []
    for fh in files:
        fhbase = os.path.basename(fh)
        img = get_im_cv2(fh)
        X_test.append(img)
        X_test_id.append(fhbase)

    return X_test, X_test_id


print('Loading model and weights from training process ...')
InceptionV3_model = load_model(weights_path)

print('Predicting where da fish are using testing data ...')
test_data, test_id = load_test()
X_test = np.array(test_data, dtype=np.uint8)

# I'm not sure about what is happening on this transpose function
X_test = X_test.transpose((0, 1, 2, 3))
X_test = X_test.astype('float32')
X_test /= 255
print(X_test.shape[0], 'test samples')

predictions = InceptionV3_model.predict(X_test)

image = test_id

submission_df = pd.DataFrame(image,columns=["image"])
submission_df[FISHNAMES] = pd.DataFrame(predictions)
submission_df.to_csv('submission.csv',index=False)

print('Submission file successfully generated')
