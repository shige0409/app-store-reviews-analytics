# はじめに
AWSをほとんど使ったことがなかった私がAWS上でちょっとしたものを作る際に、
`考えていたこと`や`調べたサイト`などをメモ書きとして残します。⚠︎自分用のため読みづらかったらすみません。。

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
- EC2インスタンスはすぐ`削除`(AWSを学習する上では立ち上げ続ける必要はないはず)
- 極力`サーバーレス`を意識(安価になることが多い)


# 学習手順
### 1. AWSにはどういうツールがあって、それぞれ何ができるのか大枠を把握する
- [Udemy これだけでOK！ AWS 認定ソリューションアーキテクト – アソシエイト試験突破講座](https://www.udemy.com/course/aws-associate/)
- [AWSサービス別資料](https://aws.amazon.com/jp/aws-jp-introduction/aws-jp-webinar-service-cut/#ai-wn)

正直ツールが多すぎて結局`何からやれば良いかよく分からない`！！(後で見返すには良さそう)一旦何かを真似するところから始めたい。

### 2. 同期の方が分析基盤構築のアウトプットをQiita記事に
- [Youtube APIデータをBigQueryへロードする作業を自動化する](https://qiita.com/matsu0130/items/4849ebb3681e827274d3)

作りたいものが似ている！AWSではどのように実現できるのか？

### 3. GCPとAWSの対応が把握する
- [GCP と AWS サービス対応表・比較表](https://cloud-ace.jp/column/detail124/)

~~AWS Batch~~ (`labmda 定期実行`と検索したら`Event Bridge`が良いと判明), SNS or SQS, Lambda, S3, Athena or Bigquery, QuickSightを使えば実現できそう => それぞれのツール概要を`手順1`に戻って把握する。

### 4. それぞれのモジュールを少しずつ繋げていく

`Lambda 外部ライブラリ使用方法`, `Lambda S3保存`, `Lambda SNS 連携`, `Lambda S3トリガー`, `Athena QuickSight 連携`などで検索しコードを改良
- [AWS LambdaでPython外部ライブラリのLayerを作る前に](https://qiita.com/polarbear08/items/202752d5ffcb65595bd9)
- [AWS Lambdaを使ったAmazon SNSへのメッセージ送受信](https://business.ntt-east.co.jp/content/cloudsolution/column-try-29.html)
- [QuickSightとAthenaを活用！データ分析入門](https://techblog.nhn-techorus.com/archives/6202)


