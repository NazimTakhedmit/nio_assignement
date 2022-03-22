import tensorflow_decision_forests as tfdf
import pandas as pd
import shutil 
import numpy as np
import pickle
import sys 

#read the argument of the train data file name
name_train_data = str(sys.argv[1])


# select train data 
#train_data = dataset[dataset.year.isin([2017, 2018, 2019, 2020, 2021])].reset_index()
train_data = pd.read_pickle(name_train_data)
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_data, label="calls_per_hour",task=tfdf.keras.Task.REGRESSION)

#build model 
model = tfdf.keras.GradientBoostedTreesModel(task=tfdf.keras.Task.REGRESSION,loss = 'SQUARED_ERROR',max_depth = 3, num_trees=500)

model.compile( metrics = ["MAE"])

model.fit(train_ds, verbose = 2 )

#show the training log 
print(model.summary())

#save the model 
pickle.dump(model, open('model.sav', 'wb'))