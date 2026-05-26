from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(X, y):

    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=0
    )

    # モデル作成
    model = LinearRegression()

    # 学習
    model.fit(X_train, y_train)

    # 予測
    y_pred = model.predict(X_test)

    return model, X_test, y_test, y_pred