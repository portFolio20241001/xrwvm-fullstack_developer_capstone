# Djangoの管理サイトのために必要なモジュールをインポート
from django.contrib import admin
# 作成したCarMakeモデルとCarModelモデルをインポート
from .models import CarMake, CarModel


# モデルを管理サイトに登録するための準備

# CarModelInlineクラス
# CarMakeモデルに関連するCarModelの情報をインラインで表示するために使用

# CarModelAdminクラス
# CarModelモデルを管理サイトでどのように表示するかを定義するクラス

# CarMakeAdminクラス
# CarMakeモデルの管理サイト用設定を行い、CarModelInlineを使ってCarModelも表示するクラス

# モデルを管理サイトに登録
# CarMakeモデルを管理サイトに登録
admin.site.register(CarMake)

# CarModelモデルを管理サイトに登録
admin.site.register(CarModel)
