#import tensorflow
import pandas as pd
import os
import matplotlib as plt
import numpy as np
path_data = "./data/sensors-activity-recognition-dataset-shoaib/DataSet/"

#Create a common dataframe
df = pd.DataFrame()
#Count number of files in directory
for _, _, files in os.walk(path_data):
    for file in files:
        if file.endswith('.csv'):
            print("Gathering data from " + path_data + file)
            df_tmp = pd.read_csv(path_data + file, header=1)
            df = pd.concat([df, df_tmp])

for col in df:
    print("Nombre col: " + col)
    x_axis = np.array([0, len(df)])
    print(x_axis)
    y_axis = df[col].values
    plt.pyplot.plot(x_axis, y_axis)
    plt.show()

