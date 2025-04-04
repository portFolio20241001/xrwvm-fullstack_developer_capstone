# Django 5.1.7 によって生成されたマイグレーションファイル（作成日時：2025-03-30 06:35）

# バリデーション用のモジュールをインポート
import django.core.validators
# 外部キー削除時の挙動を制御するモジュールをインポート
import django.db.models.deletion
# Djangoのマイグレーションに必要な基本モジュールをインポート
from django.db import migrations, models


# マイグレーションを定義するクラス
class Migration(migrations.Migration):

    # このマイグレーションが最初であることを示す
    initial = True

    # 依存関係がないため空のリスト
    dependencies = [
    ]

    # 実行されるマイグレーション操作のリスト
    operations = [
        # CarMakeモデルの作成
        migrations.CreateModel(
            name='CarMake',  # モデル名：CarMake
            fields=[
                # 主キーのidフィールド、自動生成されるBigAutoField型
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                # メーカー名のフィールド、最大100文字の文字列
                ('name', models.CharField(max_length=100)),
                # メーカーの説明文を格納するTextField型
                ('description', models.TextField()),
            ],
        ),
        # CarModelモデルの作成
        migrations.CreateModel(
            name='CarModel',  # モデル名：CarModel
            fields=[
                # 主キーのidフィールド、自動生成されるBigAutoField型
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                # 車種名を格納するフィールド、最大100文字
                ('name', models.CharField(max_length=100)),
                # 車の種類（タイプ）を選択式で定義、デフォルトは'SUV'
                ('type', models.CharField(
                    choices=[
                        ('SEDAN', 'Sedan'),  # セダン
                        ('SUV', 'SUV'),      # SUV
                        ('WAGON', 'Wagon')   # ワゴン
                    ],
                    default='SUV',
                    max_length=10
                )),
                # 製造年を格納するフィールド、バリデーション付き
                ('year', models.IntegerField(
                    default=2023,  # デフォルトは2023年
                    validators=[
                        # 最大値は2023年まで
                        django.core.validators.MaxValueValidator(2023),
                        # 最小値は2015年から
                        django.core.validators.MinValueValidator(2015)
                    ]
                )),
                # CarMakeモデルとの外部キーリレーション、CarMakeが削除されるとCarModelも削除される
                ('car_make', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='djangoapp.carmake')),
            ],
        ),
    ]
