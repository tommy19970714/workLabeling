# workLabeling
[Value](https://valu.is/)上のユーザーのプロフィールに登録されているSNSアカウントと職業情報をスクレイピングするスクリプトです．

## what is value?
VALUは個人の単位で株のようなものを発行し，資金を集めることができるサービスです．アーティスト，プログラマー，美容師，スポーツ選手など職業を登録し，資金集め活動を行います．

## installation
以下のライブラリが必要です．

```
pymysql
beautifulsoup4

```

スクレイピングしたデータをmysqlに保存する場合は ./config/config.yml にデータベースの情報を以下のように明記します．

``` 
db:
    host: localhost
    user: root
    password: pass
    database: twitter
    user_table: users
    charset: utf8mb4
```

今回使用するデータベースの作成は以下で行うことができます．

```
CREATE DATABASE twitter;
USE twitter;
CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL DEFAULT '',
  `category` varchar(25) NOT NULL,
  `twitter` text,
  `instagram` text,
  `facebook` text,
  `homepage` text,
  `coinprism` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

```


## RUN
以下でスクリプトを実行します．

```
python serachValu.py
```


## 集めたデータ
Valuからスクレイピングしたデータをcsv形式とsql形式で配布しています．集めたユーザ数は19741人です．

csv形式 [download link](https://mega.nz/#!5j5k3SyS!GInfT0kbdsNsOaptkg74TtW5QUCbE3hhJP_K7Q-8EyM)

sql形式 [download link](https://mega.nz/#!FypnFIJR!3y7bJ2k2j68td2UrTucSta9WFgaQOL_k4XQ10MWLahQ)