import pandas as pd
path = "path to file" # path to file
df = pd.read_csv(path) # reading file

low = 0 # Initial Lower Limit
high = 1000 # Initial Higher Limit
while(high < len(df)):
    df_new = df[low:high] # subsetting DataFrame based on index
    low = high #changing lower limit
    high = high + 1000 # givig uper limit with increment of 1000
    df_new.to_csv("Path to output file") # output file 