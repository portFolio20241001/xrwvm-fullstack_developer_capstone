# 必要なインポートをコメントアウト（後で有効化）

# URLパターンを定義するための `path` をインポート
from django.urls import path

# メディアファイル（画像など）の静的ファイル処理のための `static` をインポート
from django.conf.urls.static import static

# Djangoの設定をインポート（settings.pyに格納されている設定値を使用）
from django.conf import settings

# ビュー関数をインポート（アプリケーションの各ビューを参照）
from . import views

# アプリケーション名を定義（URLパターンに名前空間を付与）
app_name = 'djangoapp'

# URLパターンを定義するリスト
urlpatterns = [
    # ユーザー登録用のURLパス（`/register` で registration ビューを呼び出す）
    path('register', views.registration, name='registration'),

    # ログイン用のURLパス（`/login` で login_user ビューを呼び出す）
    path(route='login', view=views.login_user, name='login'),

    # ログアウト用のURLパス（`/logout` で logout_user ビューを呼び出す）
    path(route='logout', view=views.logout_user, name='logout'),

    # Car情報取得用のURLパス（`/get_cars` で get_cars ビューを呼び出す）
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    # ディーラー情報取得用のURLパス（`/get_dealers` で get_dealerships ビューを呼び出す）
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),

    # 特定の州のディーラー情報取得用のURLパス（`/get_dealers/<state>` で get_dealerships ビューを呼び出す）
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),

    # ディーラー詳細情報を取得するURLパス（`/dealer/<dealer_id>` で get_dealer_details ビューを呼び出す）
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),

    # ディーラーのレビューを取得するURLパス（`/reviews/dealer/<dealer_id>` で get_dealer_reviews ビューを呼び出す）
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),

    # ディーラーのレビュー表示用のURLパス（現在コメントアウト中）
    # path('dealer_reviews', views.get_dealer_reviews, name='dealer_reviews'),

    # レビュー追加用のURLパス（現在コメントアウト中）
    # path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # メディアファイルの静的ファイルを処理するための設定
