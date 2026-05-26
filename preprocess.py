import pandas as pd

def preprocess(df):

    # 特徴量作成
    df["title_len"] = df["title"].str.len()
    df["tag_count"] = df["tags"].str.count(r"\|") + 1
    df["publish_time"] = pd.to_datetime(df["publish_time"])
    df["publish_hour"] = df["publish_time"].dt.hour

    return df