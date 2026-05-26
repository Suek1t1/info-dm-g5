import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("USvideos.csv - Sheet1.csv")

# コメントON
comments_on = df[df["comments_disabled"] == False]

# コメントOFF
comments_off = df[df["comments_disabled"] == True]

# 散布図
plt.scatter(
    comments_on["views"],
    comments_on["likes"],
    label="Comments ON",
    alpha=0.5
)

plt.scatter(
    comments_off["views"],
    comments_off["likes"],
    label="Comments OFF",
    alpha=0.5
)

# ラベル
plt.xlabel("Views")
plt.ylabel("Likes")

plt.title("Views vs Likes")

plt.legend()

plt.show()