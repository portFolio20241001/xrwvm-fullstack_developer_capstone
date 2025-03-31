# 必要なインポートをコメントアウト（必要に応じて有効化する）

# --------------------　不要関数START　------------------------

# Djangoのrender関数をインポート
# from django.shortcuts import render

# Djangoのメッセージ機能をインポート
# from django.contrib import messages

# get_object_or_404、render、redirect関数をインポート
# from django.shortcuts import get_object_or_404, render, redirect

# datetimeモジュールをインポート
# from datetime import datetime

# HttpResponseとHttpResponseRedirectをインポート
# from django.http import HttpResponseRedirect, HttpResponse

# --------------------　不要関数END　------------------------

# Djangoのユーザーモデルをインポート
from django.contrib.auth.models import User

# CarMakeとCarModelをインポート
from .models import CarMake, CarModel

# Djangoのlogout関数をインポート
from django.contrib.auth import logout

# JsonResponseをインポート（APIのレスポンスとしてJSONを返すため）
from django.http import JsonResponse

# login, authenticate関数をインポート（認証処理用）
from django.contrib.auth import login, authenticate

# ロギングモジュールをインポート（ログ出力用）
import logging

# jsonモジュールをインポート（リクエストボディのJSON読み込み用）
import json

# CSRFトークン検証を無効化するデコレーターをインポート
from django.views.decorators.csrf import csrf_exempt

# populateモジュールをインポート（初期データ投入用）
from .populate import initiate

# restapis.py モジュールから関数をインポート
#       get_request: 指定されたエンドポイントからデータを取得する関数
#       analyze_review_sentiments: レビューの感情を分析する関数
#       post_review: レビューをバックエンドに送信する関数
from .restapis import get_request, analyze_review_sentiments, post_review

# ロガーのインスタンスを取得
logger = logging.getLogger(__name__)


# ログイン要求を処理する `login_user` 関数
@csrf_exempt  # CSRFトークンをチェックしない（外部API呼び出し用）
def login_user(request):
    # リクエストのJSONボディからusernameとpasswordを取得
    data = json.loads(request.body)
    username = data['userName']  # ユーザー名を取得
    password = data['password']  # パスワードを取得

    # 入力された認証情報でユーザー認証を試みる
    user = authenticate(username=username, password=password)

    # レスポンス用のデータ初期化
    data = {"userName": username}

    # 認証成功時
    if user is not None:
        # ユーザーをログイン状態にする
        login(request, user)
        # 認証成功のフラグを付加してレスポンスデータにする
        data = {"userName": username, "status": "Authenticated"}

    # JSON形式でレスポンスを返す
    return JsonResponse(data)


# 以下、他の機能の雛形（まだ実装されていない）

# ログアウト要求を処理する `logout_user` 関数
def logout_user(request):
    try:
        logout(request)  # ログアウト処理
        data = {"success": True}  # ログアウト成功を示す
        return JsonResponse(data)
    except Exception as e:
        # エラーが発生した場合、詳細なエラー情報を返す
        return JsonResponse({"error": str(e)}, status=500)


# ユーザー登録を処理する
@csrf_exempt  # CSRF検証を免除（セキュリティリスクがあるので注意）
def registration(request):
    # リクエストボディをJSON形式で読み込み
    data = json.loads(request.body)
    username = data['userName']  # ユーザー名を取得
    password = data['password']  # パスワードを取得
    first_name = data['firstName']  # 名を取得
    last_name = data['lastName']  # 姓を取得
    email = data['email']  # メールアドレスを取得
    username_exist = False  # ユーザー名が既に存在するかどうかのフラグ

    try:
        # ユーザー名がすでに存在するかチェック
        User.objects.get(username=username)  # 同じユーザー名が存在するか確認
        username_exist = True  # 存在する場合、フラグをTrueに設定
    except User.DoesNotExist:
        # ユーザーが存在しない場合、新しいユーザーとしてログを記録
        logger.debug("{} is new user".format(username))  # ユーザー名が新しいことをログに記録

    # もしユーザー名が存在しなければ、新規ユーザーとして登録
    if not username_exist:
        # `auth_user`テーブルに新しいユーザーを作成
        user = User.objects.create_user(
            username=username, first_name=first_name,
            last_name=last_name, password=password, email=email)

        # 新規ユーザーとしてログインし、リストページにリダイレクト
        login(request, user)  # ユーザーをログインさせる

        # 登録成功のレスポンスデータを作成
        data = {"userName": username, "status": "Authenticated"}

        return JsonResponse(data)  # 登録成功のJSONレスポンスを返す
    else:
        # 既に登録されているユーザー名の場合、エラーメッセージを返す
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)  # エラーレスポンスを返す


def get_cars(request):
    count = CarMake.objects.filter().count()  # CarMakeの数をカウント

    print(count)  # カウント結果をコンソールに出力

    if (count == 0):  # スペースなしで条件を記述
        initiate()  # CarMakeが空の場合、初期データを投入

    # CarModelと関連するCarMakeを取得
    car_models = CarModel.objects.select_related('car_make')
    cars = []  # 車情報を格納するリスト

    for car_model in car_models:  # 各CarModelに対してループ
        # 車種とメーカー名をリストに追加
        cars.append(
            {
                "CarModel": car_model.name,
                "CarMake": car_model.car_make.name
            }
        )

    return JsonResponse({"CarModels": cars})  # 車種とメーカー名のリストをJSON形式で返す


# ディーラー一覧ページの表示を行う `get_dealerships` 関数
def get_dealerships(request, state="All"):  # Stateのデフォルト値は "All"

    if (state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/"+state
    dealerships = get_request(endpoint)  # 指定されたエンドポイントからディーラー情報を取得

    print("dealerships:", dealerships)

    # ディーラー情報をJSON形式で返す
    return JsonResponse({"status": 200, "dealers": dealerships})


# ディーラーのレビュー一覧を表示する `get_dealer_reviews` 関数
def get_dealer_reviews(request, dealer_id):

    print("通過確認1")

    # ディーラーIDが提供されている場合
    if (dealer_id):
        # ディーラーIDに基づいてレビュー情報を取得するエンドポイントを設定
        endpoint = "/fetchReviews/dealer/"+str(dealer_id)

        print("通過確認2")

        # get_request関数を使用して、指定されたエンドポイントからレビュー情報を取得
        reviews = get_request(endpoint)

        print("reviews:", reviews)

        # 取得したレビューごとに処理を行う
        for review_detail in reviews:

            print("通過確認3")
            print("review_detail['review']:", review_detail['review'])

            # レビューの感情分析を行う（レビューのテキストを渡す）
            response = analyze_review_sentiments(review_detail['review'])

            print("response:", response)

            # 感情分析の結果を表示
            print(response)

            # レビューに感情分析結果（sentiment）を追加
            review_detail['sentiment'] = response['sentiment']

            print("通過確認4")

        # レビュー情報をJSON形式で返す
        return JsonResponse({"status": 200, "reviews": reviews})

    # ディーラーIDが提供されていない場合、Bad Requestエラーレスポンスを返す
    return JsonResponse({"status": 400, "message": "Dealer ID not provided"})


# ディーラーの詳細情報を表示する `get_dealer_details` 関数
# `get_dealer_details` 関数の定義（特定のディーラーの詳細情報を取得するためのビュー）
def get_dealer_details(request, dealer_id):
    # `dealer_id` が提供されている場合
    if (dealer_id):
        # ディーラーの詳細情報を取得するためのエンドポイントを設定
        endpoint = "/fetchDealer/"+str(dealer_id)
        # `get_request` を呼び出して指定されたエンドポイントからデータを取得
        dealership = get_request(endpoint)
        # 成功した場合、ディーラー情報を JSON 形式で返す（ステータスコード 200）
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        # `dealer_id` が提供されていない場合、400（Bad Request）エラーメッセージを返す
        return JsonResponse({"status": 400, "message": "Bad Request"})


# ユーザーがレビューを投稿するための関数
def add_review(request):
    # ユーザーがログインしているかどうかを確認
    if not request.user.is_anonymous:
        # リクエストボディをJSON形式で解析（レビュー情報）
        data = json.loads(request.body)

        try:
            # `post_review` 関数を使ってレビューを投稿
            # response = post_review(data)
            post_review(data)

            # 成功した場合、ステータス200を返す
            return JsonResponse({"status": 200})

        except Exception as e:
            # エラーが発生した場合、ステータス401とエラーメッセージを返す
            return JsonResponse(
                {
                    "status": 401, "message": f"Error in posting review: {str(e)}"
                }
            )

    else:
        # ユーザーがログインしていない場合、ステータス403とメッセージを返す（未認証）
        return JsonResponse({"status": 403, "message": "Unauthorized"})
