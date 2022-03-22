import tensorflow_decision_forests as tfdf
import pandas as pd
import shutil 
import numpy as np
import pickle
import sys
#read the argument of the test data file name
name_test_data = str(sys.argv[1])

#select test data 
test_data = pd.read_pickle(name_test_data)
test_ds  = tfdf.keras.pd_dataframe_to_tf_dataset(test_data, label='calls_per_hour',task=tfdf.keras.Task.REGRESSION)

# load the model 
model = pickle.load(open('./model.sav', 'rb'))

# test and evaluate the model 
evaluation = model.evaluate(test_ds, verbose=1)