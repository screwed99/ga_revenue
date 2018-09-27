import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import json


def load_to_data_frame(csv_filename):
    JSON_COLUMNS = ["totals"]
    df = pd.read_csv(csv_filename, converters={column: json.loads for column in JSON_COLUMNS},
                     dtype={'fullVisitorId': 'str'})
    for column in JSON_COLUMNS:
        column_as_df = json_normalize(df[column])
        column_as_df.columns = [f"{column}.{sub_column}" for sub_column in column_as_df.columns]
        df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True)
    return df


def print_some_stats(data_frame):
    data_frame["single_revenue"] = data_frame["totals"]["transactionRevenue"]
    data_frame["single_revenue"].hist()
    channel_group_nums = data_frame["channelGrouping"].value_counts()
    print(channel_group_nums)


if __name__ == "__main__":
    df = load_to_data_frame("data/sample_train.csv")
    #print(df.head(10))

    #print_some_stats(df)

    import matplotlib.pyplot as plt
    df["totals.transactionRevenue"] = [float(x) for x in df["totals.transactionRevenue"]]
    df["totals.transactionRevenue"].hist(
        bins=range(0, int(np.nanmax(df["totals.transactionRevenue"])),
                   int(np.nanmax((df["totals.transactionRevenue"]) // 100))))
    print([x for x in df["totals.transactionRevenue"] if not np.isnan(x)])
    plt.show()

