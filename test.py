import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# データフレームの作成
df = pd.DataFrame({
    'name': ['taro', 'sam', 'ken'],
    'score': [50, 20, 30],
    'age': [25, 30, 28],
    'level': [1, 2, 3]
})

# グラフの設定
bar_width = 0.25  # 棒の幅

# 各名前ごとにグラフを描画
for i, name in enumerate(df['name']):
    # 特定の名前のデータを取得
    data = df[df['name'] == name].drop(columns='name').values.flatten()  # スコア、年齢、レベルのデータを取得
    st.dataframe(data)
