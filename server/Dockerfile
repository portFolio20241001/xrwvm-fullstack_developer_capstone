# Pythonのバージョン3.12.0の軽量なイメージを基にする
FROM python:3.12.0-slim-bookworm

# 標準出力のバッファリングを無効化してリアルタイムでログを表示
ENV PYTHONBUFFERED 1

# Pythonのバイトコードをファイルに書き込まないように設定
ENV PYTHONWRITEBYTECODE 1

# アプリケーションの作業ディレクトリを指定
ENV APP=/app

# 作業ディレクトリを変更
WORKDIR $APP

# `requirements.txt` をコンテナ内の作業ディレクトリにコピー
COPY requirements.txt $APP

# `requirements.txt` に記載されたPythonライブラリをインストール
RUN pip3 install -r requirements.txt

# 残りのファイルをコンテナ内の作業ディレクトリにコピー
COPY . $APP

# アプリケーションが使用するポート8000を公開
EXPOSE 8000

# `entrypoint.sh` に実行権限を付与
RUN chmod +x /app/entrypoint.sh

# コンテナ起動時に実行するコマンドを設定
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

# コンテナ起動時のデフォルトコマンドを設定（GunicornでDjangoアプリを起動）
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
