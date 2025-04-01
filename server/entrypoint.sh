#!/bin/sh

# マイグレーションを作成し、データベースを移行します。
echo "Making migrations and migrating the database. "

# Djangoのマイグレーションを作成。`--noinput` オプションは確認プロンプトなしで実行
python manage.py makemigrations --noinput

# 作成したマイグレーションをデータベースに適用（移行）
python manage.py migrate --noinput

# 静的ファイル（CSS, JavaScript, 画像など）を収集して、指定したディレクトリに保存します
python manage.py collectstatic --noinput

# 指定されたコマンド（引数）を実行する
exec "$@"
