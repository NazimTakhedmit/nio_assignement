# nio_assignement

### Requirements 

please clone this repository in google colab


### Challenge solution

the proposed solution has the following files: 

  - feature_engineering.py: this is where the relevant features for forecast are selected, then they will undergo a series of transformations inlcuding date and time columns split and adding a new column for season using a function generating the season from the available date. Finally, a "group by" operation will be used to caculate the number of calls per hour, and this will serve as a basis to calculate the number of calls per day, week, or month

  - train.py: this file contains the architecture of the used model (boosted decision trees) to perform training, and validation.
  
  - support_functions.py: contains the methods to support the model (get_season) and the unit test is handled by the file test_tools.py
  
  - test.py: this file performs the testing of the model  

  - ML_pipeline.ipynb: this notebook runs all the previous files in the following order: 

  data preprocessing (using feature_engineering.py) => training (using train.py and model.py) => testing (using test.py) => plotting the results
  
  Since the problem is of regression type the metrics that have been used to validate and evaluate the model are: RMSE (root mean squared error) and MAE (mean absolute error).

###### HOW TO RUN THE PIPELINE

- clone the repository into a folder 
- Open google colab -> File -> upload notebook -> choose ML_pipeline.ipynb notebook 
- google colab -> Runtime -> Run all 
- While running the notebook each part will display log messages regarding training, validation, and testing.
- Done! 
