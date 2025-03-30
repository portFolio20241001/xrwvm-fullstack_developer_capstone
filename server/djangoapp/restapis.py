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
    if(kwargs):  # kwargsが存在する場合
        for key, value in kwargs.items():  # 各クエリパラメータを処理
            params += f"{key}={value}&"  # パラメータをURLエンコードして追加

    # 完成したリクエストURL
    request_url = f"{backend_url}{endpoint}?{params}"

    print("GETリクエストを送信: {}".format(request_url))  # リクエストURLの出力
    try:
        # requestsライブラリを使ってGETリクエストを送信
        response = requests.get(request_url)
        return response.json()  # JSONレスポンスを返す
    except Exception as e:
        # ネットワークエラーが発生した場合
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
    request_url = sentiment_analyzer_url+"analyze/"+text  # 感情分析APIのURLを作成
    try:
        # requestsライブラリを使ってGETリクエストを送信
        response = requests.get(request_url)
        return response.json()  # JSONレスポンスを返す
    except Exception as err:
        # エラー発生時の処理
        print(f"予期しないエラー: {err=}, {type(err)=}")
        print("ネットワークエラーが発生しました")
        return None


# ディーラーのレビューを投稿する関数
def post_review(data_dict):
    # レビューを送信するためのURLを設定（バックエンドのエンドポイント）
    request_url = backend_url + "/insert_review"
    
    try:
        # POSTリクエストを送信（`data_dict`をJSON形式で送信）
        response = requests.post(request_url, json=data_dict)
        
        # レスポンスとして返されたJSONデータを表示
        print(response.json())
        
        # レスポンスを返す
        return response.json()
    
    except:
        # ネットワーク例外が発生した場合のエラーメッセージ
        print("Network exception occurred")
