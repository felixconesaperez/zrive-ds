import boto3
import pandas as pd


def data_download():
    s3 = boto3.client('s3')

    bucket_name = 'zrive-ds-data'
    key_i = ['groceries/sampled-datasets/', 'groceries/box_builder_dataset/']
    data_i = [['abandoned_carts.parquet','inventory.parquet','orders.parquet','regulars.parquet','users.parquet',], ['feature_frame.csv']]

    for key,data, in zip(key_i,data_i):
        for file in data:
            print(bucket_name, key+file, file)
            s3.download_file(bucket_name, key+file, file)

def main ():
    data_download()


if __name__ == "__main__":
    main()