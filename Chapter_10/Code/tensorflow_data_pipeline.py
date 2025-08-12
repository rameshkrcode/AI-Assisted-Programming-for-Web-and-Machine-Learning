import tensorflow as tf
import pandas as pd
# Load dataset
df = pd.read_csv("products.csv")
# Preprocess data
df['price'] = df['price'].fillna(df['price'].mean())
df['category'] = df['category'].astype('category').cat.codes
# TensorFlow data pipeline
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    df = dataframe.copy()
    labels = df.pop('label')
    ds = tf.data.Dataset.from_tensor_slices((dict(df), labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(df))
    return ds.batch(batch_size)
train_ds = df_to_dataset(df)
