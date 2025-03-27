"""djangoproj URL設定

`urlpatterns`リストは、URLをビューにルーティングします。詳細については、以下を参照してください:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

例:
関数ベースのビュー
    1. インポートを追加:  from my_app import views
    2. `urlpatterns`にURLを追加:  path('', views.home, name='home')

クラスベースのビュー
    1. インポートを追加:  from other_app.views import Home
    2. `urlpatterns`にURLを追加:  path('', Home.as_view(), name='home')

他のURLconfのインクルード
    1. `include()`関数をインポート: from django.urls import include, path
    2. `urlpatterns`にURLを追加:  path('blog/', include('blog.urls'))
"""

# 必要なモジュールのインポート
from django.contrib import admin  # Django管理サイトのインポート
from django.urls import path, include  # URLパターンを定義するためのインポート
from django.views.generic import TemplateView  # テンプレートビューを表示するためのインポート
from django.conf.urls.static import static  # 静的ファイル用のインポート
from django.conf import settings  # 設定をインポート

# URLパターンのリストを定義
urlpatterns = [
    # 管理サイトのURL設定
    path('admin/', admin.site.urls),  # Django管理サイトへのパス

    # djangoappアプリケーションのURL設定をインクルード
    path('djangoapp/', include('djangoapp.urls')),  # djangoappアプリケーションのURL設定をインクルード

    # ホームページのテンプレートビュー設定
    path('', TemplateView.as_view(template_name="Home.html")),  # ホームページ用のテンプレートビュー

    # アバウトページのテンプレートビュー設定
    path('about/', TemplateView.as_view(template_name="About.html")),  # アバウトページ用のテンプレートビュー

    # お問い合わせページのテンプレートビュー設定
    path('contact/', TemplateView.as_view(template_name="Contact.html")),  # お問い合わせページ用のテンプレートビュー
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 静的ファイルのルーティング設定
