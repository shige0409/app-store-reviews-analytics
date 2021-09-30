# はじめに
AWSをほとんど使ったことがなかった私がAWS上でちょっとしたものを作る際に、
`考えていたこと`や`調べたサイト`などをメモ書きとして残します。⚠︎自分用のため読みづらかったらすみません。。

[ソースコード Github](https://github.com/shige0409/app-store-reviews-analytics/tree/master/src)
# 作りたいもの
定期的に特定のアプリのAppStoreレビューをスクレイピング => 整形 => データ格納 => 集計 => 可視化をAWS上でできるように構築したい

# 作る前注意点
`AWS 高額請求`や`GCP 高額請求`で検索するとやらかした話が思った以上に出てくる。。

- [10日間 で AWS Lambda 関数を 28億回 実行した話](https://blog.mmmcorp.co.jp/blog/2019/12/25/lambda-cloud-bankruptcy/)
- [BigQueryで150万円溶かした人の顔](https://qiita.com/itkr/items/745d54c781badc148bb9)
- [AWS 高額請求 |クラウド利用の注意点！高額請求事例と対策方法](https://www.3sss.co.jp/tis/media/aws-high-billing/)

そのため下記は必ず
- `AWS 高額請求 対策`などで検索して認証や予算、請求アラートなどの設定
- 各ツールの`料金設定`を確認
- EC2などのインスタンスはすぐ`削除`(AWSを学ぶ上では立ち上げ続ける必要はないはず)
- 極力`サーバーレス`を意識(安価になることが多い)


# 学習手順
### 1. どこから学べば良いか分からん。とりあえずUdemyで学んでみる
- [Udemy これだけでOK！ AWS 認定ソリューションアーキテクト – アソシエイト試験突破講座](https://www.udemy.com/course/aws-associate/)
- [~~Udemy AWS Certified Data Analytics Specialty 2021 - Hands On!~~](https://www.udemy.com/course/aws-data-analytics/) => 英語動画かつ基礎知識が無さすぎて無理でした。。

`AWS初期設定`と`分析基盤`に関係ありそうな動画だけ視聴しながらハンズオンし`AWSに慣れる`

ただ`どんなツールが必要か？どのように連携させるか？`がまだ掴めない-> 似たようなものを作ってる記事を見つけて真似することから始めた方が良いかも。

### 2. 同期の方が分析基盤構築のアウトプットをQiita記事に
- [Youtube APIデータをBigQueryへロードする作業を自動化する](https://qiita.com/matsu0130/items/4849ebb3681e827274d3)

今回APIは使わないが作りたいものは似ているかも！AWSではどのように実現できるのか？

### 3. GCPとAWSの対応が把握する
- [GCP と AWS サービス対応表・比較表](https://cloud-ace.jp/column/detail124/)

~~AWS Batch~~ (`labmda 定期実行`と検索したら`Event Bridge`が良いと判明), SNS or SQS, Lambda, S3, Athena or Bigquery, QuickSightを使えば実現できるのでは？

それぞれのツール概要を[AWSサービス別資料](https://aws.amazon.com/jp/aws-jp-introduction/aws-jp-webinar-service-cut/#ai-wn)で把握する。


### 4. それぞれのモジュールを少しずつ繋げていく

`AWS Lambda スクレイピング`, `Lambda 外部ライブラリ使用方法`, `Lambda S3保存`, `Lambda SNS 連携`, `Lambda S3トリガー`, `Athena QuickSight 連携`などで検索しコードを改修&繋げていく
- [AWS LambdaでPython外部ライブラリのLayerを作る前に](https://qiita.com/polarbear08/items/202752d5ffcb65595bd9)
- [AWS Lambdaを使ったAmazon SNSへのメッセージ送受信](https://business.ntt-east.co.jp/content/cloudsolution/column-try-29.html)
- [QuickSightとAthenaを活用！データ分析入門](https://techblog.nhn-techorus.com/archives/6202)


# 実際に作ったもの
![AWS-ARC.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/225073/1aa85dbd-8920-7837-fd81-72f6088c4ac9.png)

詳細は後日追記予定