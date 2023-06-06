import tensorflow
import pandas as pd
import os
path_data = "data/sensors-activity-recognition-dataset-shoaib/DataSet"

#Count number of files in directory
_, _, files = next(os.walk("/usr/lib"))
num_files = len(files)

#Create a common dataframe
df = pd.DataFrame()
for i in range(num_files):
    print(path_data + files[i])
    df_tmp = pd.read_csv(path_data + files[i], header=1)
    df = pd.concat([df, df_tmp])

# View top 5 rows of dataframe
df.head()