## Fitrack - Machine learning

# Overview
This project leverages machine learning to classify barbell exercises and count repetitions based on accelerometer and gyroscope data. Python scripts are utilized to process, visualize, and model the data on plots. 


# Structure
1. Task: Read, process, and merge raw CSV files into a single DataFrame. 


2. Task: Understand sensor data through visuals
- plot various and all combinations per sensor and compare data. 


3. Task: Identify and handle extreme values in dataset
- Use boxplots, IQR, Chauvenet's Criterion, and LOF
- group outliers and replace
Check whether there are any outliers (extreme values) in our data that we want to remove using various methods.

4. Task: create features that enhance model performance
- deal with missing values (imputation)
- Butterworth lowpass filter
- principal component analysis (PCA)
- sum of squares attributes
- Temporal abstraction
- frequency abstraction
- deal with data overlap

5. Task: train and refine machine learning models
- perform feature selection with decision trees
- grid search for hyperparameter tuning


6. Task: implement and evaluate repetition counter
- apply and fine-tune LowPassFilter

# Getting Started
1. clone repo and navigate to project folder
2. create and activate conda environment
```
conda env create-of environment.yml
conda activate tracking-barbell-exercises
```
3. run the following Python scripts to process, data, train models, and visualize results
- make_dataset.py
- visualize.py
- remove_outliers.py
- build_features.py
- train_model.py
- count_repetitions.py