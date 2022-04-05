import pandas as pd

df = pd.read_csv('all_regions.csv')

df = df[(df['RegionName'] == 'England') | (df['RegionName'] == 'Scotland')]

df.to_csv('eng-scot.csv')
