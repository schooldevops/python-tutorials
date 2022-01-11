import pandas as pd 
from scdev_pd_column import example as ex

def do_example():
  data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}  
  df = pd.DataFrame(data)
  
  print(df)
  
  colVal = ex.getColumn(df, 'Age')
  print(colVal)
  
do_example()
  