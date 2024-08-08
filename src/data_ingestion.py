# version 2

import numpy as np
import pandas as pd

import os


df = pd.read_csv('https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv')



raw_data_path = os.path.join("./data", 'raw')

os.makedirs(raw_data_path, exist_ok=True)

df.to_csv(os.path.join(raw_data_path, "raw.csv"), index = False)


df = df[:]

processed_data_path = os.path.join("./data", 'processed')

os.makedirs(processed_data_path, exist_ok=True)

df.to_csv(os.path.join(processed_data_path, "processed.csv"), index = False)


