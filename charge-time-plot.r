#!/usr/bin/env Rscript
##-*- coding:utf-8 -*-

## --------------------------------------------------------
## 日経Linux 2015年1月号掲載
## charge-time2.sh で取得した充電時間データを
## スキャッター・チャート（scatter chart）へプロットする。
##
## 使い方：
##    Step 1: charge-time2.sh を実行
##       $ sudo ./charge-time2.sh
##
##    Step 2: スキャッター・チャートの作成
##       $ ./charge-time-plot.r
##
##       ・チャートは "moisture-scatter-char.png" に保存される。
##       ・charge-time2.sh の実行中でもチャートの作成が可能。
## --------------------------------------------------------

## ファイル名
datafile <- "moisture-sensor-readings.csv"
png_file <- "moisture-scatter-chart.png"

## 入力データの取り込み間隔
interval <- 1   # charge-time2.shに合わせて１秒に１回

## データファイルを読み込む
sprintf("データファイル： %s", datafile)
mydata <- read.table(datafile, header=TRUE, sep=",")

## 時系列データ（time series）に変換する
my_time_series <- ts(mydata)

## データ件数などを表示する
data_count  <- length(my_time_series)
total_hours <- data_count / (60 / interval) / 60
sprintf("データ件数：　　 %d",      data_count)
sprintf("対象時間：　　   %f 時間", total_hours)

## png_flie を開き、スキャッター・チャートをプロットする
png(png_file)
print(scatter.smooth(x=1:length(my_time_series), y=my_time_series,
                     xlab="time", ylab="micro-secs", col="#DDDDDD"))
dev.off()
