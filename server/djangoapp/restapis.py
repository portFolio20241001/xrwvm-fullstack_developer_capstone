import requests  # HTTPリクエストを送信するためのライブラリ
import os  # 環境変数を取得するためのライブラリ
from dotenv import load_dotenv  # .envファイルの環境変数を読み込むライブラリ

# .envファイルの内容を読み込む
load_dotenv()

# 環境変数からバックエンドのURLを取得（デフォルトはローカルサーバー）
backend_url = os.getenv("backend_url", default="http://localhost:3030")

# 環境変数から感情分析APIのURLを取得（デフォルトはローカルサーバー）
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


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
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GETリクエストを送信: {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"ネットワークエラー: {e}")
        return None


# 感情分析を実行する関数
def analyze_review_sentiments(text):
    """
    与えられたテキストに基づいて感情分析を実行し、結果を返す。

    引数:
        text (str): 感情分析を行いたいテキスト

    戻り値:
        dict: 感情分析結果のJSONデータ
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"予期しないエラー: {err=}, {type(err)=}")
        print("ネットワークエラーが発生しました")
        return None


# ディーラーのレビューを投稿する関数
def post_review(data_dict):
    """
    ディーラーのレビューを投稿する。

    引数:
        data_dict (dict): レビュー情報を含む辞書

    戻り値:
        dict: APIレスポンスのJSONデータ
    """
    request_url = f"{backend_url}/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None
