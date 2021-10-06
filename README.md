# agriculture_iot_private

ESP32等からweb_apiを通してログを取るためのプログラムです。
このプログラムは下記で構築しています。

web api
  Django(環境はDockerfileで構築)
 
Data Base
  MySQL(Dockerのイメージを使用)
  
  
・使用方法
　ダウンロード後、"docker-compose up -d"で起動します。
  "docker-compose build"後でも可です。
　※docker、およびdocker-composeが使用できる環境が必要になります。
 　それぞれの環境に合わせてインストールをお願いします。
 
・動作確認
  ローカルであれば"http://127.0.0.1:8000/api_now"で現在時刻が帰ってこれば起動できています。
  こちらは動作確認用、RTC設定用で作成しました。
  ※IPアドレスはアクセス先に合わせて置き換えてください。

･データベース作成(初回・データベースを変更した時のみ)
　起動後、dockerの中に入りデータベースを構築します。
  下記のコマンドでdockerに入ります。もし入れない場合はコンテナ名が違う可能性がありますので docker ps で確認してください
  ※コンテナ名は変わる可能性があります。
　docker exec -it web_api_logger_django_1 bash

  次に下記のコマンドを実行します。
  python3 /project/manage.py migrate

  正常に完了したら exit で抜けてください。

・使い方
  下記のアドレスにアクセスすると、それぞれに応じた値が記録されます。
  http://127.0.0.1:8000/api_log?datetime=2020-01-01 12:00:00&serial_no=0001&voltage=3.00&temp=25.0&humidity=50&atmospheric_pressure=1013.25&moisture_content=30
  ※IPアドレスはアクセス先に合わせて置き換えてください。
  
  農業を前提として製作しましたので、項目がそれ用となっています。
  任意の項目に変更するには下記の二つのファイルを編集してください。
  
  #Data Base構築用のファイル
  /docker/project/project/models.py
  
  #受信したときのデータ書き込み用
  /docker/project/project/views.py

・注意点
  ローカルで使用することを前提に製作しています。
　VPS等で起動すればwebを通してログを取ることも可能ですが、APIキーの設定やNginx、wsgi等、通常のwebサーバのデプロイと同じ手順を踏んでいただけることを推奨します。
 
　このプログラムを使用して発生した事象に対して責任、および保証は一切負いませんので自己責任で使用してください。
