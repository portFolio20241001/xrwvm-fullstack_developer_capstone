"""
Django settings for djangoproj project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path


# プロジェクト内でのパスの基本ディレクトリを設定
BASE_DIR = Path(__file__).resolve().parent.parent


# 開発用設定 - 本番環境には不適切
# 本番環境にデプロイする際はチェックリストを確認
# https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# セキュリティ警告: 本番環境で使用する秘密鍵は秘密にしておく
SECRET_KEY =\
    'django-insecure-ccow$tz_=9%dxu4(0%^(z%nx32#s@(zt9$ih@)5l54yny)wm-0'

# セキュリティ警告: 本番環境ではDEBUGをONにしない
DEBUG = True

# 許可するホスト名を設定
# 本当はkenkou~のところは分割しない。Lint通すために分割してるだけ。
ALLOWED_HOSTS = [
    'localhost',
    'kenkouishi11-8000.' +
    'theiadockernext-0-labs-prod-theiak8s-4-tor01.' +
    'proxy.cognitiveclass.ai'
]

# CSRF保護を許可するオリジンを設定
# 本当はkenkou~のところは分割しない。Lint通すために分割してるだけ。
CSRF_TRUSTED_ORIGINS = [
    'https://kenkouishi11-8000.' +
    'theiadockernext-0-labs-prod-theiak8s-4-tor01.' +
    'proxy.cognitiveclass.ai'
]

# RESTフレームワークの認証設定
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],  # デフォルトの認証クラスは空
}

# アプリケーション定義

INSTALLED_APPS = [
    'djangoapp.apps.DjangoappConfig',  # 自作のアプリ
    'django.contrib.admin',           # 管理サイト
    'django.contrib.auth',             # ユーザー認証
    'django.contrib.contenttypes',     # コンテンツタイプ
    'django.contrib.sessions',         # セッション
    'django.contrib.messages',         # メッセージ
    'django.contrib.staticfiles',      # 静的ファイル
    'django_extensions',               # ER図作成に必要
]

# ミドルウェア設定

MIDDLEWARE = [
    # セキュリティミドルウェア
    'django.middleware.security.SecurityMiddleware',
    # セッションミドルウェア
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 共通ミドルウェア
    'django.middleware.common.CommonMiddleware',
    # 認証ミドルウェア
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # メッセージミドルウェア
    'django.contrib.messages.middleware.MessageMiddleware',
    # X-Frame-Optionsミドルウェア
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ルートURLの設定

ROOT_URLCONF = 'djangoproj.urls'

# テンプレート設定

TEMPLATES = [
    {
        # Djangoテンプレートエンジン使用
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/static'),
            os.path.join(BASE_DIR, 'frontend/build'),
            os.path.join(BASE_DIR, 'frontend/build/static'),
        ],
        'APP_DIRS': True,  # アプリ内のテンプレートも読み込む
        'OPTIONS': {
            'context_processors': [
                # デバッグ情報をテンプレートに渡す
                'django.template.context_processors.debug',
                # リクエスト情報をテンプレートに渡す
                'django.template.context_processors.request',
                # 認証情報をテンプレートに渡す
                'django.contrib.auth.context_processors.auth',
                # メッセージ情報をテンプレートに渡す
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGIアプリケーション設定

WSGI_APPLICATION = 'djangoproj.wsgi.application'


# データベース設定
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 使用するデータベースエンジン
        'NAME': BASE_DIR / 'db.sqlite3',  # データベースファイルの場所
    }
}

# パスワードバリデータの設定

AUTH_PASSWORD_VALIDATORS = [
    {
        # ユーザー属性の類似性チェック
        'NAME': 'django.contrib.' +
                'auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # 最低文字数チェック
        'NAME': 'django.contrib.' +
                'auth.password_validation.MinimumLengthValidator',
    },
    {
        # 一般的なパスワードチェック
        'NAME': 'django.contrib.' +
                'auth.password_validation.CommonPasswordValidator',
    },
    {
        # 数字のみのパスワードチェック
        'NAME': 'django.contrib.' +
                'auth.password_validation.NumericPasswordValidator',
    },
]


# 国際化設定
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'  # 言語コードを英語に設定

TIME_ZONE = 'UTC'  # タイムゾーンをUTCに設定

USE_I18N = True  # 国際化を有効にする

USE_L10N = True  # ロケールに従ったフォーマットを使用する

USE_TZ = True  # タイムゾーンを有効にする


# 静的ファイル（CSS, JavaScript, 画像）の設定
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'  # 静的ファイルのURL
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 静的ファイルの保存場所
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')  # メディアファイルの保存場所
MEDIA_URL = '/media/'  # メディアファイルのURL

# デフォルトの主キーのフィールドタイプ
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # 主キーをBigAutoFieldに設定

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static'),  # 静的ファイルの追加ディレクトリ
    os.path.join(BASE_DIR, 'frontend/build'),
    os.path.join(BASE_DIR, 'frontend/build/static'),
]
