import pandas as pd

df = pd.read_csv('https://query.data.world/s/plssyzzuum3lzrpxcvzooxkloh4xbv')

df.to_csv('Meteorite_Data_Raw.csv')
