日経Linux PCボード「Beagle Bone」で家庭菜園の水分や温度を監視 付録プログラム
==================================================================

作成者：河野 達也 / Tatsuya Kawano

最終更新：2014年11月16日

目次
----

1. はじめに
2. ディレクトリ構成
3. プログラムの内容について
4. 問い合わせ先について
5. ソフトウェアライセンスについて


1. はじめに
-----------

- 本書および関連するプログラムは、日経Linux 2014年12月号から2015年2月号に掲載予定の短期連載『PCボード「Beagle Bone」で家庭菜園の水分や温度を監視』の付録です。

- ウェブブラウザで以下のURLを開くと読みやすく整形された本書が表示されます。
  * https://github.com/tatsuya6502/nikkei-linux-fp/blob/master/README.md


2. ディレクトリ構成
-------------------

このリポジトリにはBeagleBone Blackで実行するPythonプログラムが収められています。ディレクトリ構成は以下の通りです。


```shell
nikkei-linux-bbb-2014/
    README.md            # このファイル
    LICENSE              # オープンソースソフトウェアライセンス（英語）
    LICENSE_ja           # オープンソースソフトウェアライセンス（日本語）
    charge-time-plot.r   # 2015年1月号で使用するRスクリプト
    charge-time1.py      # 2014年12月号で使用するPythonプログラム
    charge-time2.py      # 2015年1月号で使用するPythonプログラム
```

3. プログラムの内容について
-----------------------

プログラムの内容については、プログラムファイル内の日本語コメントをお読みください。必要なライブラリーなどのインストール手順や、測定に使う回路については、日経Linux 2014年12月号から2015年2月号掲載の『PCボード「Beagle Bone」で家庭菜園の水分や温度を監視』を参照してください。


4. お問い合わせについて
-----------------------

- プログラムの不具合を見つけられた場合には、issueトラッカーでご報告ください。日本語でかまいません。
  * https://github.com/tatsuya6502/nikkei-linux-bbb-2014/issues

- 日経Linux掲載記事についてのご意見やお問い合わせは、日経Linux編集部までお願いします。


5. ソフトウェアライセンスについて
------------------------------

Copyright (c) 2014 Tatsuya Kawano
Released under the MIT license / MITライセンスのもとで配布されています。

https://github.com/tatsuya6502/nikkei-linux-bbb-2014/blob/master/LICENSE
https://github.com/tatsuya6502/nikkei-linux-bbb/2014/blob/master/LICENSE_ja

##
