# 必要なインポートをコメントアウト（必要に応じて有効化する）

# Djangoのrender関数をインポート
from django.shortcuts import render

# HttpResponseとHttpResponseRedirectをインポート
from django.http import HttpResponseRedirect, HttpResponse

# Djangoのユーザーモデルをインポート
from django.contrib.auth.models import User

# CarMakeとCarModelをインポート
from .models import CarMake, CarModel

# get_object_or_404、render、redirect関数をインポート
from django.shortcuts import get_object_or_404, render, redirect

# Djangoのlogout関数をインポート
from django.contrib.auth import logout

# Djangoのメッセージ機能をインポート
from django.contrib import messages

# datetimeモジュールをインポート
from datetime import datetime

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

# populateモジュールをインポート（コメントアウト中、初期データ投入用？）
# from .populate import initiate


# ロガーのインスタンスを取得
logger = logging.getLogger(__name__)

# ここからビュー関数を定義

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
    context = {}  # 空のコンテキストを作成（後で使う場合がある）

    # リクエストボディをJSON形式で読み込み
    data = json.loads(request.body)
    username = data['userName']  # ユーザー名を取得
    password = data['password']  # パスワードを取得
    first_name = data['firstName']  # 名を取得
    last_name = data['lastName']  # 姓を取得
    email = data['email']  # メールアドレスを取得
    username_exist = False  # ユーザー名が既に存在するかどうかのフラグ
    email_exist = False  # メールアドレスが既に存在するかどうかのフラグ（現在は未使用）

    try:
        # ユーザー名がすでに存在するかチェック
        User.objects.get(username=username)  # 同じユーザー名が存在するか確認
        username_exist = True  # 存在する場合、フラグをTrueに設定
    except:
        # ユーザーが存在しない場合、新しいユーザーとしてログを記録
        logger.debug("{} is new user".format(username))  # ユーザー名が新しいことをログに記録

    # もしユーザー名が存在しなければ、新規ユーザーとして登録
    if not username_exist:
        # `auth_user`テーブルに新しいユーザーを作成
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        # 新規ユーザーとしてログインし、リストページにリダイレクト
        login(request, user)  # ユーザーをログインさせる
        data = {"userName": username, "status": "Authenticated"}  # 登録成功のレスポンスデータを作成
        return JsonResponse(data)  # 登録成功のJSONレスポンスを返す
    else:
        # 既に登録されているユーザー名の場合、エラーメッセージを返す
        data = {"userName": username, "error": "Already Registered"}  # 既存ユーザーエラーメッセージ
        return JsonResponse(data)  # エラーレスポンスを返す


def get_cars(request):
    count = CarMake.objects.filter().count()  # CarMakeの数をカウント
    print(count)  # カウント結果をコンソールに出力
    if(count == 0):
        initiate()  # CarMakeが空の場合、初期データを投入
    car_models = CarModel.objects.select_related('car_make')  # CarModelと関連するCarMakeを取得
    cars = []  # 車情報を格納するリスト
    for car_model in car_models:  # 各CarModelに対してループ
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})  # 車種とメーカー名をリストに追加
    return JsonResponse({"CarModels":cars})  # 車種とメーカー名のリストをJSON形式で返す
    

# ディーラー一覧ページの表示を行う `get_dealerships` 関数
# def get_dealerships(request):
#     ...

# ディーラーのレビュー一覧を表示する `get_dealer_reviews` 関数
# def get_dealer_reviews(request, dealer_id):
#     ...

# ディーラーの詳細情報を表示する `get_dealer_details` 関数
# def get_dealer_details(request, dealer_id):
#     ...

# レビュー投稿を処理する `add_review` 関数
# def add_review(request):
#     ...
