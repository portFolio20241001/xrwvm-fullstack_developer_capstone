# Flask をインポート（Webアプリケーションの作成に使用）
from flask import Flask

# NLTK の SentimentIntensityAnalyzer をインポート（感情分析を行うため）
from nltk.sentiment import SentimentIntensityAnalyzer

# JSONデータの操作に使用するライブラリをインポート
import json

# Flaskアプリケーションを作成（アプリ名: "Sentiment Analyzer"）
app = Flask("Sentiment Analyzer")

# SentimentIntensityAnalyzer のインスタンスを作成（感情分析エンジンの初期化）
sia = SentimentIntensityAnalyzer()


# ルートエンドポイント ('/') に GET リクエストが来たときに実行される関数
@app.get('/')
def home():
    # サーバーのルートにアクセスしたときの応答メッセージを返す
    return "Welcome to the Sentiment Analyzer. \
    Use /analyze/text to get the sentiment"


# '/analyze/<input_txt>' に GET リクエストが来たときに実行される関数
@app.get('/analyze/<input_txt>')
def analyze_sentiment(input_txt):
    """
    文字列を受け取り、その感情分析の結果を返す
    """

    # 感情分析のスコアを取得（ポジティブ・ネガティブ・ニュートラルの割合）
    scores = sia.polarity_scores(input_txt)

    # スコアをコンソールに表示（デバッグ用）
    print(scores)

    # スコアの個別値を取得（ポジティブ・ネガティブ・ニュートラル）
    pos = float(scores['pos'])  # ポジティブスコア
    neg = float(scores['neg'])  # ネガティブスコア
    neu = float(scores['neu'])  # ニュートラルスコア

    # デフォルトの感情判定を「ポジティブ」とする
    res = "positive"

    # スコアの値をコンソールに表示（デバッグ用）
    print("pos neg neu:", pos, neg, neu)

    # 一番大きいスコアに応じて感情を判定
    if neg > pos and neg > neu:
        res = "negative"  # ネガティブが最大の場合
    elif neu > neg and neu > pos:
        res = "neutral"   # ニュートラルが最大の場合

    # 結果を JSON 形式に変換
    res = json.dumps({"sentiment": res})

    # 結果をコンソールに表示（デバッグ用）
    print(res)

    # クライアントに JSON 形式の結果を返す
    return res


# スクリプトが直接実行された場合に Flask アプリを起動
if __name__ == "__main__":
    app.run(debug=True)  # デバッグモードで起動
