import pandas as pd

def convert_uploaded_csv_to_dataframe(files):
    df = pd.read_csv(list(files.to_dict().values())[0])
    print('Successfully converted csv to pandas DataFrame:\n', df.head(),
          '\nDataFrame shape:', df.shape)
    return df
