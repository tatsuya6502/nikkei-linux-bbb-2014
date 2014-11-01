#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import Adafruit_BBIO.GPIO as GPIO
import time, os
import datetime as dt

NUM_SAMPLES = 5


def check_user():
    root_uid = 0
    if os.getuid() != root_uid:
        print("GPIOにアクセスするためにroot権限が必要です。sudoで実行してください。")
        exit(8)


def setup(trigger_pin, measure_pin):
    # トリガーピンをGPIO出力に設定
    GPIO.setup(trigger_pin, GPIO.OUT)
    # 測定ピンをGPIO入力に設定
    GPIO.setup(measure_pin, GPIO.IN)
    # トリガーピンをHighにする。トランジスタによるスイッチが入り
    # コンデンサーが放電される
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.5)


def charge_time(trigger_pin, measure_pin):
    timeout = 0
    # 現在時刻を記録
    start = dt.datetime.now()
    # トリガーピンをLowに戻す。充電開始
    GPIO.output(trigger_pin, GPIO.LOW)

    # 測定ピンを読み、Highの間、繰り返す。もしtimeoutカウンターが
    # 10万に達した場合は、測定を打ち切る
    while (GPIO.input(measure_pin) == GPIO.HIGH
           and timeout < 100000):
        timeout += 1

    # 測定ピンがLowになったら現在時刻を記録
    end = dt.datetime.now()
    # トリガーピンをHighにする。トランジスタによるスイッチが入り
    # コンデンサーが放電される
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.1)
    # 所要時間を求める
    return (end - start).microseconds


# メインプログラム
check_user()
setup("P9_11", "P9_13")

while True:
    # charge_time()をNUM_SAMPLES回実行し、平均値を表示する
    charge_time_list = []
    for i in range(NUM_SAMPLES):
        ct = charge_time("P9_11", "P9_13")
        charge_time_list.append(ct)
    average = sum(charge_time_list) / NUM_SAMPLES
    print(average)
    time.sleep(1.0 - 0.1 * NUM_SAMPLES)
