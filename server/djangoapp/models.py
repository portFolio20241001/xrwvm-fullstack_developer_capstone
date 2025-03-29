# Djangoのモデルコードを追加する前に、以下のインポートを解除してください

from django.db import models  # Djangoのデータベースモデルをインポート
from django.utils.timezone import now  # 現在の日付と時刻を取得するためにインポート
from django.core.validators import MaxValueValidator, MinValueValidator  # バリデーターをインポート

# 車のメーカーを表すモデル
class CarMake(models.Model):
    # 車のメーカー名を格納するフィールド（最大100文字）
    name = models.CharField(max_length=100)
    # 車のメーカーの説明を格納するフィールド
    description = models.TextField()
    # 必要に応じて他のフィールドを追加

    # オブジェクトを文字列として返すためのメソッド
    def __str__(self):
        return self.name  # 名前を文字列として返す

# 車のモデルを表すモデル
class CarModel(models.Model):
    # CarMakeモデルとの多対一（Many-to-One）関係を定義
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # CarMakeが削除されると、関連するCarModelも削除される
    # 車のモデル名を格納するフィールド（最大100文字）
    name = models.CharField(max_length=100)
    # 車のタイプを選択肢から選ぶためのフィールド
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),  # セダン
        ('SUV', 'SUV'),      # SUV
        ('WAGON', 'Wagon'),  # ワゴン
        # 必要に応じて他の選択肢を追加
    ]
    # 車のタイプを選択肢から選ぶためのフィールド（デフォルトはSUV）
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    # 車の年式を格納するフィールド（2015年から2023年の範囲に制限）
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),  # 最大値は2023年
            MinValueValidator(2015)   # 最小値は2015年
        ])
    # 必要に応じて他のフィールドを追加

    # オブジェクトを文字列として返すためのメソッド
    def __str__(self):
        return self.name  # 名前を文字列として返す

# <ヒント> 車のメーカー（CarMake）モデルを作成 `class CarMake(models.Model)`:
# - name: 車のメーカー名
# - description: 車のメーカーに関する説明
# - 必要に応じて他のフィールドを追加
# - __str__ メソッドで、CarMakeオブジェクトを文字列として表示

# <ヒント> 車のモデル（CarModel）モデルを作成 `class CarModel(models.Model):`:
# - CarMakeモデルとの多対一の関係（1つのCarMakeに多くのCarModelが存在する）
# - name: 車のモデル名
# - type: 車のタイプ（選択肢として、Sedan、SUV、WAGONなど）
# - year: 車の年式（2015年から2023年までの範囲に制限）
# - 必要に応じて他のフィールドを追加
# - __str__ メソッドで、CarModelオブジェクトを文字列として表示
