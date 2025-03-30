import os  # OS関連の操作を行うためのモジュール
from dotenv import load_dotenv  # .envファイルから環境変数を読み込むためのモジュール

# .envファイルの環境変数を読み込む
load_dotenv()

# バックエンドのURLを環境変数から取得（デフォルトはローカルホスト）
backend_url = os.getenv('backend_url', default="http://localhost:3030")

# 感情分析サービスのURLを環境変数から取得（デフォルトはローカルホスト）
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# GETリクエストを送信する関数
def get_request(endpoint, **kwargs):
    params = ""  # URLパラメータを格納する変数
    if(kwargs):  # 追加のパラメータが指定されている場合
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"  # キーと値を連結してパラメータを作成

    # リクエストURLを構築
    request_url = backend_url + endpoint + "?" + params
    
    print("GET from {} ".format(request_url))  # 送信するURLを出力
    try:
        # requestsライブラリを使ってGETリクエストを送信
        response = requests.get(request_url)
        return response.json()  # レスポンスをJSON形式で返す
    except:
        # ネットワークエラーが発生した場合の処理
        print("Network exception occurred")

# 以下、未実装の関数（コメントアウト）

# 感情分析を行う関数（未実装）
# def analyze_review_sentiments(text):
#     request_url = sentiment_analyzer_url + "analyze/" + text  # 感情分析APIのURLを構築
#     # ここに感情分析APIを呼び出すコードを追加

# レビューを投稿する関数（未実装）
# def post_review(data_dict):
#     # ここにレビューを投稿するコードを追加
