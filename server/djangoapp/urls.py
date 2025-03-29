# 必要なインポートをコメントアウト（後で有効化）

# URLパターンを定義するための `path` をインポート
from django.urls import path

# メディアファイル（画像など）の静的ファイル処理のための `static` をインポート
from django.conf.urls.static import static

# Djangoの設定をインポート（settings.pyに格納されている設定値を使用）
from django.conf import settings

# ビュー関数をインポート
from . import views

# アプリケーション名を定義（URLパターンに名前空間を付与）
app_name = 'djangoapp'

# URLパターンを定義するリスト
urlpatterns = [
    # ユーザー登録用のURLパス
    path('register', views.registration, name='registration'),

    # ログイン用のURLパス
    path(route='login', view=views.login_user, name='login'),

    # ログアウト用のURLパス
    path(route='logout', view=views.logout_user, name='logout'),

    # Car情報取得用のURLパス
    path(route='get_cars', view=views.get_cars, name ='getcars'),

    # ディーラーのレビュー表示用のURLパス（現在コメントアウト中）
    # path('dealer_reviews', views.get_dealer_reviews, name='dealer_reviews'),

    # レビュー追加用のURLパス（現在コメントアウト中）
    # path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
