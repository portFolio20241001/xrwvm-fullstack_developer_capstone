# 必要なライブラリをインポート
import requests  # HTTPリクエストを送信するためのライブラリ
import os  # 環境変数を取得するためのライブラリ
from dotenv import load_dotenv  # .envファイルの環境変数を読み込むライブラリ

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数からバックエンドのURLを取得（デフォルトはローカルサーバー）
backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")

# 環境変数から感情分析APIのURLを取得（デフォルトはローカルサーバー）
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# GETリクエストを送信する関数
def get_request(endpoint, **kwargs):
    """
    指定されたエンドポイントにGETリクエストを送信する。

    引数:
        endpoint (str): リクエストを送信するエンドポイント
        **kwargs: クエリパラメータ（例: key=value）

    戻り値:
        dict: APIレスポンスのJSONデータ（エラー時はNone）
    """
    params = ""  # クエリパラメータの初期化
    if(kwargs):
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"

    print("GETリクエストを送信: {}".format(request_url))
    try:
        # requestsライブラリを使ってGETリクエストを送信
        response = requests.get(request_url)
        return response.json()  # JSONレスポンスを返す
    except Exception as e:
        # ネットワークエラーが発生した場合
        print(f"ネットワークエラー: {e}")
        return None

# 感情分析を実行する関数（未実装）
# def analyze_review_sentiments(text):
#     """
#     感情分析APIにテキストを送信し、感情スコアを取得する関数（未実装）。
#     """
#     request_url = f"{sentiment_analyzer_url}analyze/{text}"
#     # ここにコードを追加

# レビューを投稿する関数（未実装）
# def post_review(data_dict):
#     """
#     APIにレビューを投稿する関数（未実装）。
#     """
#     # ここにコードを追加
