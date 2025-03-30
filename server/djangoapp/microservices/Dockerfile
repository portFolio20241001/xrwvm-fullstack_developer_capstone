# Python 3.9.18 の軽量バージョン (slim-bookworm) の公式イメージを使用
FROM python:3.9.18-slim-bookworm

# コンテナ内の作業ディレクトリを /python-docker に設定
WORKDIR /python-docker

# requirements.txt をコンテナにコピー（パッケージの依存関係を管理するため）
COPY requirements.txt requirements.txt

# 依存パッケージをインストール
RUN pip3 install -r requirements.txt

# カレントディレクトリ（ローカルの全ファイル）をコンテナ内にコピー
COPY . .

# コンテナ内のファイル・ディレクトリをリスト表示（デバッグ用）
RUN ls

# コンテナ起動時に Flask アプリを実行
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
