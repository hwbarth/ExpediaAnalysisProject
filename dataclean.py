import os
import pandas as pd

# rawdata.csv file excluded from repository due to size:

f = open(os.getcwd() + "/rawdata.csv", "r")
df = pd.read_csv(f)
clean_df = df.dropna(subset=["comp1_rate"])
clean_df.to_csv(os.getcwd() + "/clean_data.csv")