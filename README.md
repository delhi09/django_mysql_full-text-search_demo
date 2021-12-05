# 「DjangoでMySQLの全文検索機能を使う」のデモアプリ
Django Advent Calendar 2021 の「[DjangoでMySQLの全文検索機能を使う](https://qiita.com/advent-calendar/2021/django)」という記事のデモアプリのリポジトリです。

## 起動方法

### リポジトリを取得する
```shell
$ git clone git@github.com:delhi09/django_mysql_full-text-search_demo.git
$ cd django_mysql_full-text-search_demo
```

### Pythonの仮想環境を作成する
```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### 依存パッケージをインストールする
```
$ pip3 install -r requirements.txt
```

### MySQLを起動する
```shell
$ docker-compose up -d
```

### Djangoのマイグレーションを実行する

```shell
$ python3 demo/manage.py migrate
```

### Django Adminのユーザーを作成する
```shell
$ python3 demo/manage.py createsuperuser
```

### アプリケーションを起動する

```
$ python3 demo/manage.py runserver
```

### 以下にアクセスする
http://localhost:8000/app/

## データ登録方法

### 以下にアクセスする
http://localhost:8000/admin/app/novel/add/

### データを登録する
<img width="966" alt="スクリーンショット 2021-12-18 2 46 42" src="https://user-images.githubusercontent.com/63476957/146586542-e2b88824-5421-482b-ab8c-9783f4479e7b.png">

### ※ 注意
バイグラムインデックスなので、1文字の検索ワードはヒットしません。例えば、「吾輩は猫である」を登録して「猫」で検索してもヒットしません。

## Unit Test実行方法

```
$ python3 demo/manage.py test app
```

## MySQLに接続する
```
$ mysql -u root -p -h 127.0.0.1 -P 3306 demo_app
```
