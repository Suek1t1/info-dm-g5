import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("USvideos.csv - Sheet1.csv")

# コメントON/OFFごとにlikes取得
comments_on = df[df["comments_disabled"] == False]["likes"]
comments_off = df[df["comments_disabled"] == True]["likes"]

# 箱ひげ図
plt.boxplot([comments_on, comments_off])

# ラベル
plt.xticks([1, 2], ["Comments ON", "Comments OFF"])
plt.ylabel("Likes")
plt.title("Comments ON/OFF vs Likes")
plt.show()